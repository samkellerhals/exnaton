import requests as req
import os
import json
import warnings
import pandas as pd
import logging
from src.constants import AUTH_URL, MEASUREMENT_ENDPOINT, API_LIMIT, LOGGER_NAME

warnings.simplefilter(action='ignore', category=FutureWarning)

logger = logging.getLogger(LOGGER_NAME)

def authenticate() -> str:
    """Authenticate to the Exnaton API.
    
    Returns:
        Database session token.
    """
    try:
        credentials= {"email": os.getenv("EMAIL"), "password": os.getenv("PASSWORD")}
        r = req.post(AUTH_URL, data=credentials)
        cookies = r.cookies.get_dict()
        db_token = cookies["_db_sess"]
        logger.info("Succesfully authenticated with Exnaton API.")
    except Exception as e:
        logger.error(e)
        raise SystemExit
    return db_token

def get_measurement_data(smart_meter_id: str, auth_token: str, start: str, end: str, measurement: str) -> dict:
    """Makes a GET request to get measurement data from the Exnaton API.
    
    Args:
        smart_meter_id: Identifier of the smart meter.
        auth_token: Authentication token.
        start: Start date to retrieve data for with format Y-m-d
        end: Start date to retrieve data for with format Y-m-d
        measurement: Measurement type to retrieve.

    Returns:
        Dictionary containing JSON response.
    """
    try:
        get_params = {"muid": smart_meter_id, "start": start, "end": end, "measurement": measurement, "limit": API_LIMIT}
        r = req.get(url=MEASUREMENT_ENDPOINT, params=get_params, cookies={"_db_sess": auth_token})
        json_content = json.loads(r.text)
        logger.info(f"Succesfully made GET request to {MEASUREMENT_ENDPOINT}")
    except Exception as e:
        logger.error(e)
        raise SystemExit
    return json_content["data"]
    