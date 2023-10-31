# check if the desktop has any images
# display them
# and delete them if not opened for the last 4 days
# confirmation message fo them being moved to the trash bin
import os
import curses
import time
import shutil

# Function to list image files on the desktop


def list_images_on_desktop(desktop_path):
    image_extensions = ['.jpg', '.jpeg',
                        '.png', '.gif', '.bmp', '.svg']
    image_files = []

    for filename in os.listdir(desktop_path):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            image_files.append(os.path.join(desktop_path, filename))

    return image_files

# Function to check if an image hasn't been opened for the last 4 days


def is_image_unused(image_path, days=4):
    current_time = time.time()
    last_access_time = os.path.getmtime(image_path)

    return current_time - last_access_time >= days * 24 * 60 * 60

# Function to move images to the trash bin


def move_to_trash(images):
    trash_dir = os.path.expanduser("~/.Trash")  # macOS trash bin

    for image in images:
        image_name = os.path.basename(image)
        trash_path = os.path.join(trash_dir, image_name)
        shutil.move(image, trash_path)
        print(f"\nMoved '{image_name}' to the trash bin.")

# Function to clean unused images on the desktop


def CleanScs():
    desktop_path = os.path.expanduser("~/Desktop")
    image_files = list_images_on_desktop(desktop_path)

    unused_images = [img for img in image_files if is_image_unused(img)]

    if not unused_images:
        print("\nNo unused images found on the desktop.")
        return

    print("\nList of unused images on the desktop:")
    for i, image in enumerate(unused_images, start=1):
        print(f"{i}. {os.path.basename(image)}")

    choice = input(
        "Enter the numbers of images to delete (comma-separated)[ 0 for all]: ")
    if choice == "0":
        images_to_delete = unused_images
    else:
        to_delete = [int(x.strip()) for x in choice.split(
            ",") if x.strip().isdigit() and 1 <= int(x) <= len(unused_images)]
        images_to_delete = [unused_images[i - 1] for i in to_delete]

    if not images_to_delete:
        print("No images selected for deletion.")
        return

    print("Deleting selected images...")
    move_to_trash(images_to_delete)

    # print("Cleanup complete. Deleted the selected images.")


CleanScs()
