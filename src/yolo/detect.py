"""Run inference using a trained YOLO model."""

from pathlib import Path
from ultralytics import YOLO


def detect(model_path: str, source: str = "images", save: bool = True) -> None:
    """Run detection on images or video using a trained model."""
    model = YOLO(model_path)
    model.predict(source, save=save)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run YOLO detection")
    parser.add_argument("model", help="Path to trained model (e.g., runs/train/exp/weights/best.pt)")
    parser.add_argument("--source", default="images", help="Path to input images or video")
    parser.add_argument("--nosave", action="store_true", help="Do not save output images")
    args = parser.parse_args()

    detect(args.model, source=args.source, save=not args.nosave)
