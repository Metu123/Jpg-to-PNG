JPG/JPEG to PNG Converter (Python Script)

Overview

This script is a command-line utility that converts JPG/JPEG images into PNG format using the Python Imaging Library (Pillow). It supports both single-image conversion and batch conversion for all supported images in a folder.

It also handles transparency conversion safely by adding a white background when necessary.


---

Features

Convert a single JPG/JPEG image to PNG

Convert all JPG/JPEG images in a folder

Supports .jpg and .jpeg file extensions

Handles images with transparency (RGBA / LA modes)

Option to control output directory

Option to prevent overwriting existing files

Safe error handling per file

Automatic directory creation for output



---

Requirements

Python 3.7+

Pillow library


Install dependency:

pip install pillow


---

Supported Formats

Input formats supported:

.jpg

.jpeg


Output format:

.png



---

How It Works

1. File Validation

Each input file is validated before processing:

The file must exist

The file must have a supported extension (.jpg, .jpeg)


If validation fails, a ValueError is raised.


---

2. Output Directory Handling

If no output directory is provided:

The image is saved in the same folder as the input file


If provided:

The directory is created automatically if it does not exist




---

3. Conversion Process

Each image is processed as follows:

Opening the Image

The image is opened using Pillow:

with Image.open(input_path)


---

Transparency Handling

Some images may contain alpha transparency (RGBA or LA mode). Since PNG supports transparency, the script handles it safely:

If image has transparency:

A white background is created

The image is pasted on top using the alpha channel


Otherwise:

The image is converted directly to RGB




---

Saving Output

The image is saved as PNG:

Output filename: same name as input, but .png

Format: PNG


Example:

image.jpg → image.png


---

4. Batch Processing

The batch function:

convert_batch(folder_path)

Behavior:

Scans all files in a directory

Filters only .jpg and .jpeg

Converts each valid file using convert_image()



---

5. Overwrite Protection

If overwrite=False (default):

Existing PNG files will not be replaced

The script prints:


Skipped (already exists): file.png

If overwrite=True:

Existing files will be replaced



---

Usage

Run the script:

python script.py


---

Menu Options

When executed, the script asks:

Convert (1) single image or (2) folder?


---

Option 1: Single Image

Example:

Enter image path: /home/user/photo.jpg

Result:

Converted: /home/user/photo.png


---

Option 2: Folder Conversion

Example:

Enter folder path: /home/user/images

All JPG/JPEG images in the folder are converted.


---

Example Output

Converted: /home/user/images/img1.png
Converted: /home/user/images/img2.png
Skipped (already exists): /home/user/images/img3.png
Failed: /home/user/images/corrupt.jpg -> cannot identify image file


---

Code Structure

Main Conversion Function

convert_image(input_path: Path, output_dir: Path = None, overwrite=False)

Handles:

Single image conversion

Transparency handling

Saving output PNG



---

Batch Conversion Function

convert_batch(folder_path: Path, output_dir: Path = None, overwrite=False)

Handles:

Folder scanning

Filtering supported files

Iterative conversion



---

Entry Point

if __name__ == "__main__":
    main()

Handles:

User interaction

Mode selection (single or batch)



---

Design Decisions

1. Strict file validation

Only .jpg and .jpeg are allowed to avoid processing unsupported formats.


---

2. Safe overwrite handling

Prevents accidental data loss by skipping existing files unless explicitly allowed.


---

3. Transparency-safe conversion

Ensures PNG output remains visually consistent by flattening transparency onto a white background when needed.


---

4. Lightweight batch processing

Uses simple directory iteration (iterdir) for fast and minimal overhead processing.


---

Limitations

Does not recurse into subdirectories

No parallel processing for large batches

No CLI arguments (uses interactive input only)

Transparency is flattened (not preserved as alpha blending in all cases)



---

Possible Improvements

Add argparse CLI support

Add recursive folder scanning (rglob)

Add multiprocessing for faster batch conversion

Allow custom background color for transparency

Add logging system instead of print statements

Support additional formats (WEBP, BMP, TIFF)



---

License

This script is free to use, modify, and distribute for both personal and commercial projects.
