import streamlit as st 

from PIL import Image
import numpy as np


def load_image(img):
 im = Image.open(img)
 image = np.array(im)
 return image