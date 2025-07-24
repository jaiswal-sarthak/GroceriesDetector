import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os

class DetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv8 Grocery Detector")
        self.root.geometry("600x400")
        self.folder_path = ""

        self.label = tk.Label(root, text="Select Image Folder:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.select_button.pack()

        self.run_button = tk.Button(root, text="Start Detection", command=self.run_detection, bg="green", fg="white")
        self.run_button.pack(pady=20)

        self.log_box = scrolledtext.ScrolledText(root, width=70, height=15)
        self.log_box.pack()

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path = folder_selected
            self.log(f"Selected folder: {self.folder_path}")

    def run_detection(self):
        if not self.folder_path:
            messagebox.showwarning("No Folder", "Please select a folder first.")
            return

        self.log("Running detection...")

        # Run detect.py using subprocess and pass folder as argument
        try:
            result = subprocess.run(
                ["python", "src/detect.py", "--input", self.folder_path],
                capture_output=True, text=True, check=True
            )
            self.log(result.stdout)
        except subprocess.CalledProcessError as e:
            self.log(e.output)
            messagebox.showerror("Error", "Detection failed.")

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DetectionApp(root)
    root.mainloop()
