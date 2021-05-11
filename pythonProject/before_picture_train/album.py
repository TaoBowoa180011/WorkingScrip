import albumentations as A
from PIL import Image
import cv2 as cv
import numpy as np

trans =  A.Compose(
    [
        A.HorizontalFlip(p = 0.5),
        # A.Transpose(),
        A.OneOf([
            A.IAAAdditiveGaussianNoise(),
            A.GaussNoise(),
        ], p=0.3),
        A.OneOf([
            A.MotionBlur(p=0.2),
            A.MedianBlur(blur_limit=3, p=0.1),
            A.Blur(blur_limit=3, p=0.1),
        ], p=0.5),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
        A.OneOf([
            A.OpticalDistortion(p=0.3),
            A.GridDistortion(p=0.1),
            A.IAAPiecewiseAffine(p=0.3),
        ], p=0.5),
        A.OneOf([
            A.CLAHE(clip_limit=2),
            A.IAASharpen(),
            A.IAAEmboss(),
            A.RandomBrightnessContrast(),
        ], p=0.5),
        A.HueSaturationValue(p=0.3),
    ])

image = cv.imread("valid2/task_c90842521_valid_1-2020_11_24_08_56_57-yolo/frame_000660.PNG")
cv.imshow('da',image)
cv.waitKey()