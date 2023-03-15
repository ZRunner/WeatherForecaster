#!/usr/bin/bash

GRAFANA_DATA_FILE=/usr/share/grafana/public/weather-forecast/data.csv
GRAFANA_CONDITIONS_FILE=/usr/share/grafana/public/weather-forecast/conditions.csv


# data file
if [ -f "$GRAFANA_DATA_FILE" ]
then
    rm "$GRAFANA_DATA_FILE"
fi
ln "$(pwd)/data.csv" "$GRAFANA_DATA_FILE"

# conditions file
if [ -f "$GRAFANA_CONDITIONS_FILE" ]
then
    rm "$GRAFANA_CONDITIONS_FILE"
fi
ln "$(pwd)/conditions.csv" "$GRAFANA_CONDITIONS_FILE"