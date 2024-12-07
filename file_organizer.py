import os
import pathlib
import shutil

fileCategories = {
    "Web": [".html5", ".html", ".htm", ".xhtml"],
    "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "Video": [".avi", ".mkv", ".flv", ".wav", ".mov", ".mp4", ".webm", ".vob", ".mng", ".at", ".mpg", ".mpeg", ".3gp"],
    "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".doce", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "Python": [".py"]
}

categoryNames = list(fileCategories.keys())
categoryExtensions = list(fileCategories.values())

# Remove duplicates from the extension lists
categoryExtensions = [list(set(exts)) for exts in categoryExtensions]

downloadFolder = r"C:\Users\Hp\Downloads"
destinationFolder = r"C:\Users\Hp\Downloads\Organized"

# Ensure the destination folder exists
if not os.path.exists(destinationFolder):
    os.makedirs(destinationFolder)

Z_otherFolder = os.path.join(destinationFolder, "Z_other")  # Define the Z_other folder path
unmatchedFilesFound = False  # Track if unmatched files are found

for file in os.scandir(downloadFolder):
    if file.is_file():
        filePath = pathlib.Path(file.name)
        fileExtension = filePath.suffix.lower()

        sourcePath = file.path
        targetFolder = destinationFolder

        if fileExtension == "":
            print(f"{sourcePath} has no file format.")
        else:
            moved = False
            for extensions in categoryExtensions:
                if fileExtension in extensions:
                    category = categoryNames[categoryExtensions.index(extensions)]
                    categoryFolder = os.path.join(destinationFolder, category)

                    if not os.path.exists(categoryFolder):
                        os.makedirs(categoryFolder)
                    targetFolder = categoryFolder
                    moved = True
                    break

            if not moved:
                print(f"{sourcePath} doesn't match any category, moving to 'Z_other' folder.")
                unmatchedFilesFound = True  # Mark that unmatched files exist
                if not os.path.exists(Z_otherFolder):  # Create Z_other only if it doesn't exist
                    os.makedirs(Z_otherFolder)
                targetFolder = Z_otherFolder

        # Move the file to the determined folder
        print(f"{sourcePath} moved to {targetFolder}!")
        shutil.move(sourcePath, targetFolder)


print("File organization is complete!")
