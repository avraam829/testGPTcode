from importlib import import_module


def test_import_train():
    assert import_module('yolo.train_yolo')


def test_import_detect():
    assert import_module('yolo.detect')
