import os
import csv
from tabulate import tabulate  # Keep this as module import
from ultralytics import YOLO
from count_utils import count_objects
from PIL import Image

print("🚀 Batch Detection Script Started")

# Load YOLOv8 model
print("📦 Loading model...")
model = YOLO("models/yolov8s.pt")

# Input and output folders
input_folder = "C:\\Users\\DELL\\Desktop\\2343053\\GroceryDetector\\data\\groceries-roboflow\\test\\images"
output_folder = "C:\\Users\\DELL\\Desktop\\2343053\\GroceryDetector\\outputs\\detected_images"
csv_output_path = "C:\\Users\\DELL\\Desktop\\2343053\\GroceryDetector\\outputs\\detection_counts.csv"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Prepare CSV file
csv_file = open(csv_output_path, mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Image Name", "Label", "Count"])

# Process each image
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

if not image_files:
    print("❌ No images found in the input folder.")
else:
    for image_name in image_files:
        image_path = os.path.join(input_folder, image_name)
        print(f"🖼️ Processing {image_name}...")

        # Run model
        results = model(image_path)
        output_path = os.path.join(output_folder, f"detected_{image_name}")
        results[0].save(filename=output_path)

        # Count objects
        counts = count_objects(results, model)

        if counts:
            print(tabulate([[k, v] for k, v in counts.items()], headers=["Label", "Count"]))
        else:
            print("No objects detected.")

        # Save to CSV
        for label, count in counts.items():
            csv_writer.writerow([image_name, label, count])

    print(f"✅ Detection complete. Saved results in '{output_folder}' and counts in '{csv_output_path}'.")

csv_file.close()
