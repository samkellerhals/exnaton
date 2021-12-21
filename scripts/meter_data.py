import argparse
import logging.config
from src.request import authenticate, get_measurement_data
from src.utils import load_dotenv_credentials, pandas_to_parquet, json_to_pandas

def main(start: str, end: str, meter_id: str, measurement: str, parquet_path: str) -> None:
    """Executes main program."""
    load_dotenv_credentials()
    auth_token = authenticate()
    measurement_json = get_measurement_data(meter_id, auth_token, start, end, measurement)
    df = json_to_pandas(measurement_json)
    pandas_to_parquet(df, parquet_path)

if __name__ == "__main__":
    logging.config.fileConfig(fname="logging.ini")
    parser = argparse.ArgumentParser(description="A utility for requesting meter data and saving it as parquet.")

    parser.add_argument(
        "start", type=str, help="Start date to retrieve data from."
        )
    
    parser.add_argument(
        "end", type=str, help="End date to retrieve data until."
        )
    
    parser.add_argument(
        "--meter-id", 
        type=str, 
        help="Unique identifier of the smart meter.", 
        default="C-2caa1954-b3c8-466c-9722-c1b72dabe32b"
        )
    
    parser.add_argument(
        "--measurement", 
        type=str, 
        help="Measurement type ot retrieve",
        default="energy"
        )

    parser.add_argument(
        "--parquet-path",
        type=str,
        help="Path to save data to.",
        default="assets/smart_meter.parquet"
    )
    
    args = vars(parser.parse_args())

    main(**args)
