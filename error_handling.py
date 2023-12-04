
import csv
import requests
from requests.exceptions import RequestException
import os

def Error_handling():
    while True:

        # Check file permissions
        if not os.access('.', os.W_OK):
            print("Sorry, you do not have write permission.")
        if not os.access('.', os.R_OK):
            print("Sorry, you do not have read permission.")

        # Calculate available disk space
        disk_space = os.statvfs('.')
        available_space = disk_space.f_bavail * disk_space.f_frsize

        # Check available disk space
        if available_space < 1024 * 1024:  # 1MB
            print("Insufficient disk space to save the CSV file.")
            break
        else:
            print("Sufficient disk space available.")

        break  # Terminate the loop if all checks pass

Error_handling()