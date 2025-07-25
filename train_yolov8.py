from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")  # or yolov8s.pt etc.
    model.train(
        data="data/groceries-roboflow/data.yaml", 
        epochs=50, 
        imgsz=640, 
        device=0
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # <-- Important on Windows!
    main()
