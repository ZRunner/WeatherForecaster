from requests import post

from arima_methods import (get_sensors_dataset, load_model, predict, save_model,
                           update_model)

URL = "https://wf.zrunner.me/data"

def forecast(hours: int):
    n_periods = 4 * hours
    model = load_model()
    data = get_sensors_dataset().resample('15min').mean()[-n_periods:]
    update_model(model, hours)
    save_model(model)
    data["hour"] = data.index.hour
    predictions = predict(model, data, n_periods=n_periods)
    json_obj = {}
    for index, row in predictions.iterrows():
        json_obj[index.isoformat(timespec='seconds')] = max(0, row["Prediction"])
    post(URL, json=json_obj).raise_for_status()

if __name__ == "__main__":
    forecast(hours=2)
