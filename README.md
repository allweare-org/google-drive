# Purpose
- This repo is meant to be a toolkit / starting point for interacting with Google Drive API (both personal and Shared Drives)
- This contains essential files for setting up environment on local machine or for use in Google Cloud Functions


# Setup

1. These routines all use Service Account Authentication
   1. Go to Google console and create a service account key
   2. Download and save as "credentials.json" in parent directory (./credentials.json)
2. Create a .env file in your root directory (./env)
   1. Add your environment variables according to the scripts below
3. Local Python virtual environment creation instructions:
   1. python3 -m venv .venv
   2. source .venv/bin/activate
   3. pip install -r requirements.txt

# Callable Scripts

- **move_all_files.py** - script to move all files from one Google drive folder location to another
  - Required environment variables:
    1. OLD_FOLDER_ID - *Target folder containing files (no quotes needed)*
    2. NEW_FOLDER_ID - *Source folder where you want to move files (no quotes needed)*

# Custom Libraries

- **drive_service.py** - contains all methods for interacting with Google Drive API
- **log.py** - uses python 'logging' library to format errors and save to 'out.log' and 'err.txt' files

# References

Big props to https://github.com/m3ldis/GoogleMove
