import argparse
import numpy as np
import cv2
from FractalDimension import fractal_dimension

parser = argparse.ArgumentParser()
parser.add_argument("--img", help="Choose a 2D img", required=True)
args = parser.parse_args()

img_path = str(args.img)

image = cv2.imread(img_path, 0)

fd = fractal_dimension(image)
print(f"Fractal dimension of the image: {fd}")
