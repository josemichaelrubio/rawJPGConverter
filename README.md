*raw-jpg-converter.py

This script checks for files with RAW extensions like .cr2, .nef, .arw, and .dng in the specified directory and converts them to JPEG format. You can add or remove file extensions based on the RAW formats you’re working with. Make sure to replace '/path/to/your/raw/files' with the actual path to your directory containing RAW images.

First:
-pip install fastapi (You don't really need this)
-pip install Pillow

Second:
In main.py, Update the directory address where the raw files are located

---------------------------------------
*jpg-migration.py

To move all JPG files from a source directory to a destination directory.

Replace "/path/to/source/directory" and "/path/to/destination/directory" with the actual paths to your source and destination directories. This script will recursively search for JPG files in the source directory and move them to the specified destination directory. If any files with the same names already exist in the destination directory, they will be overwritten.