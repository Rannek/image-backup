# Image Resizer Script

This Python script helps reduce the disk space used by images. It scans all directories and subdirectories starting from the current directory, finds image files (.png, .jpg, .jpeg, .bmp), and resizes them, saving the smaller versions in a backup directory. The original images are not altered.

## Features

- Scans all directories and subdirectories from the current directory.
- Resizes images (PNG, JPG, JPEG, BMP) to save disk space.
- Creates a backup directory that mirrors the existing directory structure.
- Skips images that are already small (width <= 1024px, height <= 768px, file size <= 50KB).
- Handles errors gracefully, ensuring the script continues running even if some images cannot be processed.

## Usage

1. Clone this repository or download the `IMGbackup.py` script.
2. Place the script in the directory where you want to start the scan.
3. Run the script using Python: `python IMGbackup.py`.

## Requirements

This script requires Python 3 and the following Python packages:

- `Pillow` for handling image operations.
- `tqdm` for displaying progress information.

You can install these packages using pip:
```bash
pip install pillow tqdm
