# this fucntion will display a list of apps that have not been used in the last 4 months,
# in the order of least used to most used.
# allowing user to choose which apps to delete
# and move that app to the trash bin
import os
import shutil
import time

# Function to list unused apps based on last access time


def list_unused_apps(directory, months=4):
    unused_apps = []
    current_time = time.time()

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            last_access_time = os.path.getatime(file_path)
            if current_time - last_access_time >= months * 30 * 24 * 60 * 60:
                unused_apps.append(file_path)

    return unused_apps

# Function to delete and move apps to the trash bin


def delete_apps(apps):
    trash_dir = os.path.expanduser("~/.Trash")  # macOS trash bin
    for app in apps:
        app_name = os.path.basename(app)
        trash_path = os.path.join(trash_dir, app_name)
        shutil.move(app, trash_path)
        print(f"Moved '{app_name}' to the trash bin.")

# Function to clean unused apps


def CleanApps():
    print("Cleaning Apps - Finding unused apps...")
    user_home = os.path.expanduser("~")
    unused_apps = list_unused_apps(user_home)

    if len(unused_apps) == 0:
        print("No unused apps found.")
        return

    print("List of unused apps:")
    for i, app in enumerate(unused_apps, start=1):
        print(f"{i}. {os.path.basename(app)}")

    choice = input("Enter the numbers of apps to delete (comma-separated): ")
    to_delete = [int(x.strip()) for x in choice.split(
        ",") if x.strip().isdigit() and 1 <= int(x) <= len(unused_apps)]

    apps_to_delete = [unused_apps[i - 1] for i in to_delete]

    if not apps_to_delete:
        print("No apps selected for deletion.")
        return

    print("Deleting selected apps...")
    delete_apps(apps_to_delete)

    print("Cleanup complete. Deleted the selected apps.")
