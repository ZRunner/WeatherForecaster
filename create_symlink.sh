#!/usr/bin/bash

GRAFANA_FILE=/usr/share/grafana/public/weather-forecast/data.csv

if [ -f "$GRAFANA_FILE" ]
then
    rm "$GRAFANA_FILE"
fi

ln "$(pwd)/data.csv" "$GRAFANA_FILE"