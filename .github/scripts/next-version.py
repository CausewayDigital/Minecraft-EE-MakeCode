"""
Generate the next version of release for github action
"""
import logging
import json
import urllib.request

request = urllib.request.Request("https://api.github.com/repos/CausewayDigital/Minecraft-EE-MakeCode/releases?per_page=1&page=1",
                       headers={"accept": "application/vnd.github+json", "X-GitHub-Api-Version":"2022-11-28"})

try:
    with urllib.request.urlopen(request) as response:
        body = response.read()
        json_body = json.loads(body)
except:
    logging.error("Unable to make request for release data to Github")
    print("ERROR")

try:
    version: str = json_body[0]["name"]
    split_version = version.split(".")
    new_version = f"{split_version[0]}.{split_version[1]}.{int(split_version[2]) + 1}"
    logging.info(f"new version: {new_version}")
    print(new_version)
except:
    logging.error("Unable to calculate next release")
    print("ERROR")