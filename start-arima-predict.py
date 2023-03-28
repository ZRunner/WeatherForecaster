from arima_methods import load_model, get_sensors_dataset, predict


def forecast(hours: int):
    n_periods = 4 * hours
    model = load_model()
    data = get_sensors_dataset().resample('15min').mean()[-n_periods:]
    data["hour"] = data.index.hour
    predictions = predict(model, data, n_periods=n_periods)
    print(predictions)

if __name__ == "__main__":
    forecast(hours=2)
