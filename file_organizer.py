import os
import shutil

folder = input("Enter the folder path: ")

if not os.path.exists(folder):
    print("Folder does not exist.")
else:
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Music": [".mp3", ".wav"]
    }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in file_types.items():
                if extension in extensions:
                    category_folder = os.path.join(folder, category)

                    if not os.path.exists(category_folder):
                        os.mkdir(category_folder)

                    shutil.move(file_path, os.path.join(category_folder, file))
                    print(f"Moved {file} → {category}")
                    moved = True
                    break

            if not moved:
                print(f"Skipped: {file}")

    print("File organization completed!")