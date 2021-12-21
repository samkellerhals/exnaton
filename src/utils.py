import os
import pandas as pd
import logging
from typing import Optional
from src.constants import LOGGER_NAME
from dotenv import load_dotenv

logger = logging.getLogger(LOGGER_NAME)


def load_dotenv_credentials() -> None:
    """Loads credentials from .env file."""
    load_dotenv()
    if os.getenv("EMAIL") is None:
        raise SystemExit("Credentials not available in .env file.")


def pandas_to_parquet(df: pd.DataFrame, path: str, engine: Optional[str] = "pyarrow") -> None:
    """Writes pandas dataframe to parquet.
    
    Args:
        df: Pandas dataframe
        path: Path to save file to.
        engine: Parquet engine to use.

    """
    df.to_parquet(path, engine=engine)
    logger.info(f"Wrote pandas dataframe to {path}")


def json_to_pandas(json_data: dict) -> pd.DataFrame:
    """Serializes JSON data to pandas.
    
    Args:
        json_data: A dictionary containing json data.

    Returns:
        A dataframe of representing the JSON data.

    """
    try:
        df = pd.json_normalize(json_data, sep="_")
        df["timestamp"] = df["timestamp"].str.replace(r"\D", "")
        df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y%m%d%H%M%S%f")
        logger.info("Succesfully serialised JSON to Pandas.")
    except Exception as e:
        logger.error(e)
        raise SystemExit
    return df
