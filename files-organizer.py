import os
import shutil

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Audios": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
}


def main():
    files = os.listdir()
    for file_name in files:
        file_path = os.path.join(os.getcwd(), file_name)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(file_name)[1].lower()

        moved = False

        for folder, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                dest_folder = os.path.join(os.getcwd(), "sorted", folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.copy2(file_path, os.path.join(dest_folder, file_name))
                moved = True
                print(f"Moved: {file_name} → {folder}")
                break

        if not moved:
            dest_folder = os.path.join(os.getcwd(), "sorted", "Others")
            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy2(file_path, os.path.join(dest_folder, file_name))
            print(f"Moved: {file_name} → Others")


if __name__ == "__main__":
    main()
    print("✅ File organization complete!")
