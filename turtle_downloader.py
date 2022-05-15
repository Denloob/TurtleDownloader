import random
import urllib.request
from tqdm import tqdm
import sys
import time
import json

with open('turtles.json', 'r') as f:
    TURTLE_IMAGE_URLS = json.load(f)


def download_file(url, file_name):
    """
    Download a file from a url.
    """
    if os.path.exists(file_name):
        print(f"File {file_name} already exists")
        return

    print(f"Downloading {url}")
    urllib.request.urlretrieve(url, file_name)


def download_random_turtle_image(file_name):
    """
    Download a random turtle image.
    """
    url = random.choice(TURTLE_IMAGE_URLS)
    download_file(url, file_name)


def download_all_turtle_images(show_download_progress=True):
    """
    Download all turtle images.
    """
    pbar = tqdm(total=len(TURTLE_IMAGE_URLS),
                unit="images", unit_scale=True, leave=False)
    for i, url in enumerate(TURTLE_IMAGE_URLS):
        __show_menu(force_select=3)
        download_file(url, f"turtle_{i}.png")
        pbar.update()


def download_turtle_by_index(index, file_name):
    if index > len(TURTLE_IMAGE_URLS):
        print("Index out of range")
        return
    download_file(TURTLE_IMAGE_URLS[index], file_name)


__selected = 1


def __clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def __show_menu(force_select=False):
    global __selected
    if force_select:
        __selected = force_select
    __clear_console()
    tprint("Turtle Downloader", font="modular")
    print('\n')
    print("Choose an option: (press right arrow to select)")
    for i, action in enumerate(["download turtle by index", "download random turtle", "download all turtles"], start=1):
        print("{1} {0}. {3} {2}".format(i, ">" if __selected ==
              i else " ", "<" if __selected == i else " ", action))


def __up():
    global __selected
    if __selected == 1:
        return
    __selected -= 1
    __show_menu()


def __down():
    global __selected
    if __selected == 3:
        return
    __selected += 1
    __show_menu()


def __execute_selected():
    global __selected
    if __selected == 1:
        index = int(input("Enter index: "))
        file_name = input("Enter file name (ex: my_file.png): ")
        print()
        download_turtle_by_index(index, file_name)
    elif __selected == 2:
        file_name = input("Enter file name (ex: my_file.png): ")
        print()
        download_random_turtle_image(file_name)
    elif __selected == 3:
        print("Starting download...")
        download_all_turtle_images()

    print("\nDone!")
    time.sleep(2)
    __show_menu()


if __name__ == "__main__":
    from art import tprint
    import keyboard
    import platform
    import os

    __show_menu()
    keyboard.add_hotkey('up', __up)
    keyboard.add_hotkey('down', __down)
    keyboard.add_hotkey('right', __execute_selected)
    keyboard.wait()
