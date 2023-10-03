import numpy as np
import cv2

def center_image(img, output_width=100, output_height=100, padding=10):
  # Determine the dimensions of the original image
  height = img.shape[0]
  width = img.shape[1]
  #height, width, channels = img.shape

  # Calculate the scaling factor needed to fit the image within a 100x100 frame with 10px padding
  max_size = output_width - 2*padding
  scale = min(max_size / height, max_size / width)

  # Calculate the new dimensions of the image
  new_height = int(scale * height)
  new_width = int(scale * width)

  # Resize the image while maintaining aspect ratio
  resized_img = cv2.resize(img, (new_width, new_height))

  # Create a new image with 10px padding on all sides and center the resized image within it
  if len(img.shape) > 2:
    padded_img = np.zeros((output_height, output_width, img.shape[2]), dtype=np.uint8)
  else:
    padded_img = np.zeros((output_height, output_width), dtype=np.uint8)
  padding_top = (output_height - new_height) // 2
  padding_left = (output_width - new_width) // 2
  padded_img[padding_top:padding_top+new_height, padding_left:padding_left+new_width] = resized_img
  return padded_img
