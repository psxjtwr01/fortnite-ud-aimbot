import os
import json
import shutil
import zipfile
import subprocess
import urllib.request

try:
    
    file_paths = [
        "./library.py",
        "./yolo.cfg",
        "./yolo.weights",
        "./req.txt",
        "./LICENSE",
        "./README.md",
        "./current_version.txt",
    ]

    localv_path = "localv.json"

    if not os.path.exists(localv_path) or not os.path.exists(file_paths[1]):
        local_version = "0.0.0"
        

    if os.path.exists("library.py"):
        subprocess.run(["python", "library.py"])
    else:
        print("Failed to update, please delete localv.json and launch this again.")
        exit()

except KeyboardInterrupt:
    exit()
