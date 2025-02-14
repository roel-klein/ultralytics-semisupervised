from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model
# results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
results = model.train(data="african-wildlife.yaml", epochs=100, imgsz=640)