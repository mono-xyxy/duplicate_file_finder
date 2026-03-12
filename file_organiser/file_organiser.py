import os
import shutil

folder = "files"
for file in os.listdir(folder):
    if file.endswith(".txt"):
        shutil.move(folder+"/"+file,folder+"/text/"+file)