import os
import logging


def get_recent_folders(dir_path, num_years=5):
    all_entries = os.listdir(dir_path)

    # Filter out only the folders after the year 2000
    # "0000320193-98-000105" -> not a valid year
    # "0000320193-21-000105" -> valid year
    all_folders = [entry for entry in all_entries if
                   os.path.isdir(os.path.join(dir_path, entry)) and int(entry.split('-')[1]) < 25]

    # Extract years and sort them, assuming the folder format includes the year as shown
    # Folder format example: "0000320193-21-000105"
    # Extracts the '21' part as the year
    sorted_folders = sorted(all_folders, key=lambda x: int('20' + x.split('-')[1]), reverse=True)

    # Get the most recent 'num_years' folders
    recent_folders = sorted_folders[:num_years]
    return recent_folders
