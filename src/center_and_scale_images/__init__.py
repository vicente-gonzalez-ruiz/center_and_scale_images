import numpy as np
import cv2

def center_and_scale_image_in_canvas(img, canvast_width=160, canvas_height=120, image_padding_in_canvas=10):
  # Determine the dimensions of the original image
  original_image_height = img.shape[0]
  original_image_width = img.shape[1]
  #height, width, channels = img.shape

  # Calculate the scaling factor needed to fit the image within a
  # 100x100 frame with 10px padding
  max_size = canvas_width - 2*image_padding_in_canvas
  scale = min(max_size / original_image_height, max_size / original_image_width)

  # Calculate the new dimensions of the image
  resized_image_height = int(scale * original_image_height)
  resized_image_width = int(scale * original_image_width)

  # Resize the image while maintaining aspect ratio
  resized_img = cv2.resize(img, (resized_image_width, resized_image_height))

  # Create a new image with 10px padding on all sides and center the
  # resized image within it
  if len(img.shape) > 2:
    padded_img = np.zeros((canvas_height, canvas_width, img.shape[2]), dtype=img.dtype)
  else:
    padded_img = np.zeros((canvas_height, canvas_width), dtype=img.dtype)
  y_coordinate_resized_image_in_canvas = (canvas_height - resized_image_height) // 2
  x_coordinate_resized_image_in_canvas = (canvas_width - resized_image_width) // 2
  yy_coordinate_resized_image_in_canvas = y_coordinate_image + resized_image_height
  xx_coordinate_resized_image_in_canvas = x_coordinate_image + resized_image_width
  padded_img[y_coordinate_resized_image_in_canvas:yy_coordinate_resized_image_in_canvas,
             x_coordinate_resized_image_in_canvas:xx_coordinate_resized_image_in_canvas] = resized_img

  info2 = "\"center_and_scale_image_in_canvas\" "
  info  = f"{original_image_width}\t"
  info2  += "original_image_width "
  info += f"{original_image_height}\t"
  info2  += "original_image_height "
  info += f"{canvas_width}\t"
  info2  += "canvas_width "
  info += f"{canvas_height}\t"
  info2  += "canvas_height "
  info += f"{image_padding_in_canvas}\t"
  info2  += "image_padding_in_canvas "
  info += f"{scale}\t"
  info2  += "scale "
  info += f"{resized_image_width}\t"
  info2  += "resized_image_width "
  info += f"{resized_image_height}\t"
  info2  += "resized_image_height "
  info += f"{x_coordinate_resized_image_in_canvas}\t"
  info2  += "x_coordinate_resized_image_in_canvas "
  info += f"{y_coordinate_resized_image_in_canvas}\t"
  info2  += "y_coordinate_resized_image_in_canvas "
  info += info2
  
  return padded_img, info

def move_and_scale_image_in_canvas(
    img,
    x_coordinate_image,
    y_coordinate_image,
    scale,
    canvas_width=160,
    canvas_height=120):

    # Create a black canvas
    canvas = np.zeros((output_canvas_height, output_canvas_width), dtype=np.uint8)

    # Get the dimensions of the input image
    input_height, input_width = image.shape[:2]

    # Calculate the new dimensions for the resized image
    new_width = int(input_width * scale)
    new_height = int(input_height * scale)

    # Resize the image to the new dimensions
    resized_img = cv2.resize(image, (new_width, new_height))

    # Create a region of interest on the canvas and place the resized image in it
    roi = canvas[y_coordinate_image:y_coordinate_image+new_height,
                 x_coordinate_image:x_coordinate_image+new_width]
    roi[:new_height, :new_width] = resized_img

    return canvas
