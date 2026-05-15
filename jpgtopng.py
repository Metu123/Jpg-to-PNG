from PIL import Image
from pathlib import Path

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".webp", ".bmp"}


def convert_image(input_path: Path, output_dir: Path = None, overwrite=False):
    if not input_path.exists():
        print(f"File does not exist: {input_path}")
        return

    if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        print(f"Unsupported file type: {input_path.name}")
        return

    output_dir = output_dir or input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{input_path.stem}.png"

    if output_path.exists() and not overwrite:
        print(f"Skipped (already exists): {output_path}")
        return

    try:
        with Image.open(input_path) as img:

            # Handle transparency
            if img.mode in ("RGBA", "LA", "P"):
                background = Image.new("RGB", img.size, (255, 255, 255))

                if img.mode == "P":
                    img = img.convert("RGBA")

                background.paste(img, mask=img.split()[-1])
                img = background
            else:
                img = img.convert("RGB")

            img.save(output_path, "PNG")
            print(f"Converted: {output_path}")

    except Exception as e:
        print(f"Failed: {input_path} -> {e}")


def convert_batch(folder_path: Path, output_dir: Path = None, overwrite=False):
    if not folder_path.exists() or not folder_path.is_dir():
        print("Invalid folder path.")
        return

    image_files = [
        file for file in folder_path.iterdir()
        if file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not image_files:
        print("No supported image files found.")
        return

    for file in image_files:
        convert_image(file, output_dir, overwrite)

    print("Batch conversion completed.")


def main():
    print("PNG Image Converter")
    print("1. Convert single image")
    print("2. Convert folder")

    choice = input("Select option: ").strip()

    overwrite_choice = input("Overwrite existing PNG files? (y/n): ").strip().lower()
    overwrite = overwrite_choice == "y"

    if choice == "1":
        path = Path(input("Enter image path: ").strip())
        convert_image(path, overwrite=overwrite)

    elif choice == "2":
        folder = Path(input("Enter folder path: ").strip())
        convert_batch(folder, overwrite=overwrite)

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
