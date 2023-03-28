from arima_methods import apply_time_offset, get_dataset, save_model, train_arima


def train_and_save():
    data = get_dataset()
    data = apply_time_offset(data, hours=2)
    model = train_arima(data)
    save_model(model)

if __name__ == "__main__":
    train_and_save()
    print("Model trained and saved!")
