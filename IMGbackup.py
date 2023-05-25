import os
import shutil
from PIL import Image, ImageFile
from tqdm import tqdm

ImageFile.LOAD_TRUNCATED_IMAGES = True

def resize_image(input_image_path, output_image_path, size, quality):
    try:
        original_image = Image.open(input_image_path)
        original_size = os.path.getsize(input_image_path)
        width, height = original_image.size

        resized_image = original_image.resize(size)
        if resized_image.mode in ("RGBA", "P"):
            resized_image = resized_image.convert("RGB")
        resized_image.save(output_image_path, "JPEG", quality=quality)

        return original_size - os.path.getsize(output_image_path)  # Returns the space saved
    except Exception as e:
        print(f"Failed to process file {input_image_path}. Error: {e}")
        return 0

def scan_directory(path, resize_percentage, quality):
    total_files = sum(len(files) for _, _, files in os.walk(path))  # Get total number of files in directory
    processed_files = 0
    total_saved = 0
    progress_bar = tqdm(total=total_files, unit="files")  # Create a progress bar

    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                original_path = os.path.join(foldername, filename)
                backup_path = original_path.replace(path, 'backup', 1)
                backup_dir = os.path.dirname(backup_path)

                if os.path.exists(backup_path):
                    continue

                os.makedirs(backup_dir, exist_ok=True)

                try:
                    with Image.open(original_path) as img:
                        width, height = img.size
                        if width > 1024 or height > 768 or os.path.getsize(original_path) > 50 * 1024:
                            width = int(width * resize_percentage / 100)
                            height = int(height * resize_percentage / 100)
                            total_saved += resize_image(original_path, backup_path, (width, height), quality)
                        else:
                            shutil.copy2(original_path, backup_path)

                    processed_files += 1
                    progress_bar.set_description(f"Processed: {processed_files}, Saved: {total_saved / (1024 * 1024):.2f}MB")
                    progress_bar.update()
                except Exception as e:
                    print(f"Failed to open or process file {original_path}. Error: {e}")

    progress_bar.close()

def start_backup():
    resize_percentage = int(input("Enter the resizing percentage (e.g., 50 for 50%): "))
    quality = int(input("Enter the JPEG quality (e.g., 85 for 85%): "))
    print("Press Enter to start the backup process...")
    input()
    scan_directory(os.getcwd(), resize_percentage, quality)

start_backup()
