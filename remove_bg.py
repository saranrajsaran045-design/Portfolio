from rembg import remove
from PIL import Image
import io, sys

input_path  = r"d:\smartworkz Projects\Brochuree\public\images\saranraj_1.jpg"
output_path = r"d:\smartworkz Projects\Brochuree\public\images\saranraj_nobg.png"

print("Reading image...", flush=True)
with open(input_path, "rb") as f:
    input_data = f.read()

print("Removing background (downloading AI model on first run — may take 1-2 min)...", flush=True)
output_data = remove(input_data)

print("Saving PNG with transparent background...", flush=True)
with open(output_path, "wb") as f:
    f.write(output_data)

img = Image.open(output_path)
print(f"SUCCESS! Output: {img.size}, mode: {img.mode}", flush=True)
print(f"Saved to: {output_path}", flush=True)
