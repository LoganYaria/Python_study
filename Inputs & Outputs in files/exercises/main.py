import pathlib
import shutil

new_folder = pathlib.Path.cwd()/'myfolder'
new_folder.mkdir(exist_ok=True)

path_files = [
    new_folder/'file1.txt',
    new_folder / 'file2.txt',
    new_folder / 'image1.png',
]
for every_object in path_files:
    every_object.touch()


images = new_folder/'images'/'image1.png'
images.parent.mkdir(exist_ok=True)
(new_folder/'image1.png').replace(images)

(new_folder/'file1.txt').unlink(missing_ok=True)

shutil.rmtree(new_folder)