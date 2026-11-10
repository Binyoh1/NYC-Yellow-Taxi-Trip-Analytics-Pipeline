# NYC Yellow Taxi Trip Analytics Pipeline
This project implements an end-to-end New York City Yellow Taxi trip analytics data pipeline using medallion architecture on Databricks.

## About the Data
This pipeline processes New York City (NYC) Yellow Taxi trip record data for the years **2018 - 2025** obtained from the [NYC Taxi and Limousine Commission (TLC) website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

Trip records include fields capturing pickups and drop-offs dates/times, pickup and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. Consult the [data dictionary](docs/data_dictionary_trip_records_yellow.pdf) for more information about the dataset columns.


## Architecture & System Design
### Folder Structure
```text
.
├── config/
├── docs/
├── notebooks/
├── schemas/
├── src/
│   ├── extract/            # Contains python script with source data extraction logic
│   └── nyc_yt_trips/
└── tests/
```