import os
import pickle

import pandas as pd
import pmdarima as pm

DATA_FILE_NAME = os.path.dirname(__file__) + "/data.csv"
CONDITIONS_FILE_NAME = os.path.dirname(__file__) + "/conditions.csv"
MODEL_FILE_NAME = os.path.dirname(__file__) + "/arima_model.pkl"

def get_sensors_dataset():
    sensors = pd.read_csv(DATA_FILE_NAME).fillna(method='ffill')
    sensors["date"] = pd.to_datetime(sensors["datetime"])
    sensors = sensors.set_index("date")
    return sensors

def get_dataset():
    sensors = get_sensors_dataset()
    conditions = pd.read_csv(CONDITIONS_FILE_NAME)

    # remove duplicated condition rows and rows with no precipitation value
    conditions = conditions.dropna().drop_duplicates(subset="datetime", keep="last")
    conditions["date"] = pd.to_datetime(conditions["datetime"])

    # resample data (group by minute and apply mean)
    sensors = sensors.resample('15min').mean(numeric_only=False)

    # apply neighbor humidity value to missing data
    sensors["humidity"] = sensors["humidity"].fillna(method='ffill')

    # merge both datasets based on the "date" column
    data = pd.merge_asof(sensors, conditions, on="date", direction="backward")
    # remove rows containing NaNs
    data = data.dropna()

    # change sensors["datetime"] and conditions["datetime"] column name
    data = data.rename(columns={
        "datetime_x": "datetime",
        "datetime_y": "api_collection",
        "condition-text": "condition_label",
        "condition-code": "condition_code",
        })
    # convert humidity and condition-code types
    data["humidity"] = data["humidity"].astype(int)
    data["condition_code"] = data["condition_code"].astype(int).astype("category")

    # set date as the dataset index
    data = data.set_index("date")

    # add day, hour and minute columns
    data["hour"] = data.index.hour

    rolling_avg = data['precipitations'].rolling(window=10, min_periods=1).mean()

    # Find rows with 0 precipitation and at least one non-zero neighbor
    mask = (data['precipitations'] == 0) & \
        (rolling_avg.shift(1).ne(0) & rolling_avg.shift(-1).ne(0))

    # Fill 0 values with rolling average of non-zero neighbors
    data.loc[mask, 'precipitations'] = rolling_avg[mask]

    data["is_raining"] = data["precipitations"] > 0
    return data

def apply_time_offset(data: pd.DataFrame, hours: int):
    date_offset = pd.DateOffset(hours=hours)
    prediction_data = data[["pressure", "humidity", "temperature", "hour"]]
    predicted_data = data[["precipitations", "is_raining"]]
    prediction_data.index += date_offset
    return prediction_data.join(predicted_data).dropna()

def train_arima(data: pd.DataFrame, debug_trace: bool=False):
    model: pm.ARIMA = pm.auto_arima(
        data["precipitations"], # the column to predict
        X=data[["pressure", "humidity", "temperature", "hour"]],
        stationary=False,
        start_p=1, # starting value of p, aka number of past observations to use in prediction
        max_p=4*12,
        start_q=5, # starting value of q, aka order of the moving-average model
        max_q=4*8,
        trace=2 if debug_trace else 0, # print some info while testing
        test='adf',
    )
    model.fit(data["precipitations"], X=data[["pressure", "humidity", "temperature", "hour"]])
    return model

def save_model(model: pm.ARIMA):
    with open(MODEL_FILE_NAME, 'wb') as raw:
        pickle.dump(model, raw)

def load_model():
    with open(MODEL_FILE_NAME, 'rb') as raw:
        model = pickle.load(raw)
    return model

def predict(model: pm.ARIMA, data: pd.DataFrame, n_periods: int):
    forecast, _ = model.predict(
        X=data[["pressure", "humidity", "temperature", "hour"]],
        n_periods=n_periods,
        return_conf_int=True
    )
    return pd.DataFrame(forecast, columns=['Prediction']).round()
