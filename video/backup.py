import os
import shutil
from datetime import datetime


def backup_download_folder():
    download_folder = "downloads"
    backup_folder = "backup"

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    if os.path.exists(download_folder):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        new_folder_name = os.path.join(
            os.path.dirname(download_folder), current_datetime
        )
        os.rename(download_folder, new_folder_name)

        shutil.move(new_folder_name, backup_folder)
