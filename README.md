# GitHub Demo Repository

This repository demonstrates how to use common GitHub features through a
simple Python project.

## Getting Started

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # (requirements are minimal for demo)
   ```
3. Run tests with `pytest`.

## GitHub Features Demonstrated

- **Branching and Pull Requests**: Work on new features in branches and open
  pull requests for review.
- **GitHub Actions**: Automated tests run via the workflow in
  `.github/workflows/ci.yml`.
- **Issue and PR Templates**: Standardize contributions using templates
  located in the `.github` directory.
- **Documentation**: Additional docs in `docs/` explain GitHub basics.

See [docs/github_guide.md](docs/github_guide.md) for more details.

## Обучение детекции людей на базе YOLO

Ниже приведена базовая инструкция по запуску обучения и последующего детектирования людей c использованием библиотеки [Ultralytics](https://github.com/ultralytics/ultralytics). Предполагается, что используется актуальная версия YOLO (в примерах – `yolov8n`).

### Подготовка окружения

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Подготовьте датасет в формате YOLO. В репозитории предпололагается наличие YAML-файла с путями до изображений и разметок.

### Запуск обучения

```
python -m yolo.train_yolo path/to/dataset.yaml --model yolov8n.pt --epochs 50
```

После завершения обучения лучшая модель будет расположена в каталоге `runs/train/exp/weights/best.pt`.

### Запуск детекции

```
python -m yolo.detect runs/train/exp/weights/best.pt --source path/to/images
```

Результаты будут сохранены в подкаталог `runs/detect/`.
