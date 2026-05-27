import logging
import shutil
from pathlib import Path
from datetime import datetime

import pandas as pd


INPUT_DIRECTORY = Path("data/input")
PROCESSED_DIRECTORY = Path("data/processed")
TEMP_DIRECTORY = Path("data/temp")

INPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
PROCESSED_DIRECTORY.mkdir(parents=True, exist_ok=True)
TEMP_DIRECTORY.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename="logs/email_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_latest_file():

    files = [f for f in INPUT_DIRECTORY.iterdir() if f.is_file()]

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def prepare_file():

    latest_file = get_latest_file()

    if not latest_file:
        logging.warning("No files found.")
        print("No files found.")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    temp_file = TEMP_DIRECTORY / f"report_{timestamp}{latest_file.suffix}"

    shutil.copy2(latest_file, temp_file)

    logging.info(f"Temporary file created: {temp_file.name}")
    print(f"Temporary file created: {temp_file.name}")

    return temp_file


def archive_file(file_path):

    destination = PROCESSED_DIRECTORY / file_path.name

    shutil.move(str(file_path), str(destination))

    logging.info(f"File archived: {file_path.name}")
    print(f"File archived: {file_path.name}")