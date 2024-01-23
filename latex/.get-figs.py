import os, shutil

EXTENSIONS = [".pdf", ".png"] # Use PDFs first, then PNGs.

ROOT = "/Your/workspace/directory/"
FIGURE_DIRECTORY = f"{ROOT}paper/figs/"

for f in os.listdir(FIGURE_DIRECTORY):
    for extension in EXTENSIONS:
        if f.endswith(extension):
            # DANGER this removes all files in the figure directory that end with an extension given in EXTENSIONS. Remove this code if you don't want to do that.
            os.remove(f"FIGURE_DIRECTORY{f}")
            break

with open(ROOT + f"{FIGURE_DIRECTORY}.fig-sources.txt", 'r') as f:
    for line in f.readlines():
        if line == '':
            continue
        if line.startswith('#'):
            continue
        if line.endswith("\n"):
            line = line[:-1]
        args = line.split(' ')
        if len(args) != 2:
            continue
        name, path = args
        success = False
        for extension in EXTENSIONS: # Accept PDF first, then PNG
            if not os.path.isfile(ROOT + path + extension):
                continue
            shutil.copyfile(ROOT+path+extension, ROOT + FIGURE_DIRECTORY+name+extension)
            if extension == ".png":
                print(f"File {name} was a png")
            success = True
            break
        if not success:
            print("Could not find " + path)
