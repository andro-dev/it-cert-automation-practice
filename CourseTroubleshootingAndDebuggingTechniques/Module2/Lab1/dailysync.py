#!/usr/bin/env python3

import subprocess, os
from multiprocessing import Pool


home = os.path.expanduser("~")
backup_src = os.path.join(home, "Downloads", "Pictures")
backup_dest = os.path.join(home, "backup")
if not os.path.exists(backup_dest):
    os.mkdir(backup_dest)

def get_folders(root):
    folders = []
    for item in os.listdir(root):
        if os.path.isdir(os.path.join(root, item)):
        # if not item.startswith(".") and os.path.isdir(os.path.join(root, item)):
            folders.append(os.path.join(root,item))
    return folders

def run(folder):
  # Do something with task here
  print("Handling {}".format(folder))
  subprocess.call(["rsync", "-ar", folder, backup_dest])

if __name__ == "__main__":
    folders = get_folders(backup_src)
#   # Create a pool of specific number of CPUs
    p = Pool(len(folders))
#   # Start each task within the pool
    p.map(run, folders)
