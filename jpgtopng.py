from PIL import Image
import os

def jpg_to_png():
    jpg_path = input("Enter the path to the JPG file: ").strip()

    if not os.path.exists(jpg_path) or not jpg_path.lower().endswith(".jpg"):
        print("Invalid JPG file path.")
        return

    try:
        img = Image.open(jpg_path)
        img = img.convert("RGB")  # Ensure it's in RGB mode

        directory = os.path.dirname(jpg_path)
        base_name = os.path.splitext(os.path.basename(jpg_path))[0]
        png_path = os.path.join(directory, base_name + ".png")

        img.save(png_path, "PNG")
        print(f"Converted image saved as: {png_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    jpg_to_png()