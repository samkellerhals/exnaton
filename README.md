# Exnaton Smart Meter Utility

A simple command-line utility to interact with Exnaton's development API.

## Usage

```
usage: meter_data.py [-h] [--meter-id METER_ID] [--measurement MEASUREMENT] [--parquet-path PARQUET_PATH] start end

A utility for requesting meter data and saving it as parquet.

positional arguments:
  start                 Start date to retrieve data from.
  end                   End date to retrieve data until.

optional arguments:
  -h, --help            show this help message and exit
  --meter-id METER_ID   Unique identifier of the smart meter.
  --measurement MEASUREMENT
                        Measurement type ot retrieve
  --parquet-path PARQUET_PATH
                        Path to save data to.
```

## Docker

Build a container: `docker build . --tag exnaton`

Run the script: `docker run -it -v /home/pop/Development/exnaton/assets:/app/assets exnaton "2021-09-10" "2021-10-01"`

**Note:** You need to mount a local folder to the `/app/assets` folder which is where the data is downloaded to. You also need a `.env` file where you have defined a `EMAIL` and `PASSWORD` to use to authenticate to the API.
