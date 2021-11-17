from PIL import Image
import numpy as np
import cv2

def main():
    img = np.array(Image.open('images/input.jpg'))
    dst = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
    Image.fromarray(dst).save('images/result.jpg')

if __name__ == '__main__':
    main()