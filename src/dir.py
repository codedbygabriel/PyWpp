import os
import subprocess
from pathlib import Path

user_home = os.getenv('HOME')
path = Path(f'{user_home}/Wallpapers')


def list_dirs():
    files = set()
    if path.is_dir():
        for file in path.iterdir():
            files.add(file)
        return files
    else:
        create_dir(path)


def create_dir(path):
    res = os.makedirs(path)
    if res == 0:
        return True
    else:
        return False


def change_wallpaper(wallpaper_path):
    monitors = get_monitors()
    os.system(f"hyprctl hyprpaper preload {wallpaper_path}")
    for monitor in monitors:
        os.system(f"hyprctl hyprpaper wallpaper {monitor}, {wallpaper_path}")


def get_monitors():
    res = str(subprocess.check_output(
        "hyprctl monitors all", shell=True, ))
    # print(res.split("\\n")[0].split(" "))
    monitor_list = set()

    for i in res.split("\\n"):
        if "monitor" in i.lower():
            monitor_list.add(i.split(" ")[1])

    return monitor_list
