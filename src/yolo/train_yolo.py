"""Simple training script for YOLO models using the Ultralytics library."""

from pathlib import Path
from ultralytics import YOLO


def train(data: str, model: str = "yolov8n.pt", epochs: int = 50) -> None:
    """Train a YOLO model on the provided dataset."""
    yolo = YOLO(model)
    yolo.train(data=data, epochs=epochs)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train YOLO model")
    parser.add_argument("data", help="Path to dataset YAML describing training data")
    parser.add_argument("--model", default="yolov8n.pt", help="Base model checkpoint")
    parser.add_argument("--epochs", type=int, default=50, help="Number of training epochs")
    args = parser.parse_args()

    train(args.data, model=args.model, epochs=args.epochs)
