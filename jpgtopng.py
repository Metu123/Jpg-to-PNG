from PIL import Image
from pathlib import Path


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg"}


def convert_image(input_path: Path, output_dir: Path = None, overwrite=False):
    if not input_path.exists() or input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Invalid image file: {input_path}")

    output_dir = output_dir or input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{input_path.stem}.png"

    if output_path.exists() and not overwrite:
        print(f"Skipped (already exists): {output_path}")
        return

    try:
        with Image.open(input_path) as img:
            
            if img.mode in ("RGBA", "LA"):
                background = Image.new("RGB", img.size, (255, 255, 255))
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
        raise ValueError("Invalid folder path")

    files = list(folder_path.iterdir())
    if not files:
        print("this don't exist.")
        return

    for file in files:
        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            convert_image(file, output_dir, overwrite)


def main():
    choice = input("Convert (1) single image or (2) folder? ").strip()

    if choice == "1":
        path = Path(input("Enter image path: ").strip())
        convert_image(path)

    elif choice == "2":
        folder = Path(input("Enter folder path: ").strip())
        convert_batch(folder)

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
