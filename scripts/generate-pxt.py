import json
import os
from pathlib import Path
from typing import List

script_path = Path(__file__).parent
save_path = script_path.parent/"pxt.json"
tutorial_files: List[str] = []


# Load base PXT JSON file
with open(script_path/"config"/"base-pxt.json", "r") as base_file:
    pxt = json.load(base_file)

# Load ignored file
with open(script_path/"config"/"ignore.json", "r") as base_file:
    ignored_files = json.load(base_file)

for root, dirs, files in os.walk(script_path.parent/"tutorials"):
    for file in files:
        if file.endswith(".md"):
            tutorial_files.append(str(Path(root).relative_to(script_path.parent)/file))

tutorial_files.sort()
tutorial_files = [t for t in tutorial_files if t not in ignored_files["ignoredFiles"]]
pxt["files"] = pxt["files"] + tutorial_files

with open(save_path, "w+", encoding="utf-8") as save_file:
    json.dump(pxt, save_file, indent=4)
