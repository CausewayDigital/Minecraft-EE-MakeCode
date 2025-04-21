"""
Generate the next version of release for github action
"""
import os
import logging
import json

current_release_data = os.getenv("prior_release_data")
if not current_release_data:
    logging.error("No data found in env `fetch-api-data`")
    exit(1)

current_release_data = json.loads(current_release_data)
version: str = current_release_data[0]["name"]
split_version = version.split(".")
new_version = f"{split_version[0]}.{split_version[1]}.{int(split_version[2]) + 1}"
logging.info(f"new version: {new_version}")
print(new_version)