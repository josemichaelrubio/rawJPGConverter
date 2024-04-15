import os
from PIL import Image

# Set the directory containing your RAW files
directory = '/Users/josemichaelrubio/Pictures/Ashley-Jake-Engagement-2024/Raw'

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.lower().endswith(('.cr2', '.nef', '.arw', '.dng')):  # Add or remove file extensions as needed
        raw_image_path = os.path.join(directory, filename)
        try:
            with Image.open(raw_image_path) as img:
                rgb_image = img.convert('RGB')
                # Save the converted image as JPEG
                rgb_image.save(os.path.splitext(raw_image_path)[0] + '.jpg', 'JPEG')
                print(f'Converted {filename} to JPEG')
        except IOError:
            print(f'Cannot convert {filename}. Unsupported file format or corrupt file.')

print('Conversion process completed.')