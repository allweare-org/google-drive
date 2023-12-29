import os.path
import sys

from dotenv import dotenv_values
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

file_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(file_dir))

from drive_service import DriveClient

# If modifying these scopes, delete the file token.json
SCOPES = ["https://www.googleapis.com/auth/drive"]


ENV = dotenv_values(".env")

# TODO: update the .env file with the folder where you would like move files to and from
OLD_FOLDER_ID = ENV.get("OLD_FOLDER_ID")  # Source folder
NEW_FOLDER_ID = ENV.get("NEW_FOLDER_ID")  # Target folder


def move_files(old_folder_id, new_folder_id):
    try:
        dc = DriveClient()
        dc.move_all_content_location(old_folder_id, new_folder_id)

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    move_files(OLD_FOLDER_ID, NEW_FOLDER_ID)
