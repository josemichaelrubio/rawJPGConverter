import os
import shutil
import glob

# Set the source directory containing JPG files
src_dir = "/path/to/source/directory"

# Set the destination directory where you want to move the JPG files
dst_dir = "/path/to/destination/directory"

# Create the destination directory if it doesn't exist
os.makedirs(dst_dir, exist_ok=True)

# Find all JPG files in the source directory
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    # Move each JPG file to the destination directory
    shutil.move(jpgfile, dst_dir)

print(f"All JPG files from {src_dir} have been moved to {dst_dir}.")
