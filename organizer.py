import os
import shutil

folder = "./Downloads"

categories = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".py": "Code"
}

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isdir(path):
        continue

    name, ext = os.path.splitext(file)

    if ext in categories:
        category_folder = os.path.join(folder, categories[ext])

        if not os.path.exists(category_folder):
            os.mkdir(category_folder)

        shutil.move(path, os.path.join(category_folder, file))
        print("Moved:", file)
