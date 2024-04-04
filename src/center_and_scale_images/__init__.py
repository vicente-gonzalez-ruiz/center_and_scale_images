import numpy as np
import cv2

def center_and_scale_image_in_canvas(
    image,
    canvas_width=160, canvas_height=120,
    image_padding_in_canvas_y=20,
    image_padding_in_canvas_x=30):
  '''Create a new image with 10px padding on all sides and center the
  resized image within it.

  '''

  # Determine the dimensions of the original image
  image_height = image.shape[0]
  image_width = image.shape[1]
  #height, width, channels = img.shape

  # Calculate the scaling factor needed to fit the image within a
  # 100x100 frame with 10px padding
  max_size_width = canvas_width - 2*image_padding_in_canvas_x
  max_size_height = canvas_height - 2*image_padding_in_canvas_y
  scale = min(max_size_height / image_height, max_size_width / image_width)

  # Calculate the new dimensions of the image
  resized_image_height = int(scale * image_height)
  resized_image_width = int(scale * image_width)

  # Resize the image while maintaining aspect ratio
  resized_img = cv2.resize(image, (resized_image_width, resized_image_height))

  # Canvas allocation
  if len(image.shape) > 2:
    canvas = np.zeros((canvas_height, canvas_width, image.shape[2]), dtype=image.dtype)
  else:
    canvas = np.zeros((canvas_height, canvas_width), dtype=image.dtype)
  y_coordinate_resized_image_in_canvas = (canvas_height - resized_image_height) // 2
  x_coordinate_resized_image_in_canvas = (canvas_width - resized_image_width) // 2
  yy_coordinate_resized_image_in_canvas = y_coordinate_resized_image_in_canvas + resized_image_height
  xx_coordinate_resized_image_in_canvas = x_coordinate_resized_image_in_canvas + resized_image_width
  roi = canvas[y_coordinate_resized_image_in_canvas:yy_coordinate_resized_image_in_canvas,
               x_coordinate_resized_image_in_canvas:xx_coordinate_resized_image_in_canvas] = resized_img
  #roi[:resized_image_height, :resized_image_width] = resized_img

  info = "center_and_scale_image_in_canvas\t"
  info += f"original_image_width={image_width}\t"
  info += f"original_image_height={image_height}\t"
  info += f"canvas_width={canvas_width}\t"
  info += f"canvas_height={canvas_height}\t"
  info += f"image_padding_in_canvas_x={image_padding_in_canvas_x}\t"
  info += f"image_padding_in_canvas_y={image_padding_in_canvas_y}\t"
  info += f"scale={scale}\t"
  info += f"resized_image_width={resized_image_width}\t"
  info += f"resized_image_height={resized_image_height}\t"
  info += f"x_coordinate_resized_image_in_canvas={x_coordinate_resized_image_in_canvas}\t"
  info += f"y_coordinate_resized_image_in_canvas={y_coordinate_resized_image_in_canvas}"
  
  return canvas, info

def extract_WOI(
    image,
    WOI_x_coordinate=0, WOI_y_coordinate=0,
    WOI_xx_coordinate=140, WOI_yy_coordinate=110):

  WOI = image[WOI_y_coordinate:WOI_yy_coordinate,
              WOI_x_coordinate:WOI_xx_coordinate]

  info = "extract_WOI\t"
  info += f"WOI_x_coordinate={WOI_x_coordinate}\t"
  info += f"WOI_y_coordinate={WOI_y_coordinate}\t"
  info += f"WOI_xx_coordinate={WOI_xx_coordinate}\t"
  info += f"WOI_yy_coordinate={WOI_yy_coordinate}"

  return WOI, info

def insert_WOI_in_canvas(
    WOI, canvas,
    WOI_x_coordinate=0, WOI_y_coordinate=0,
    WOI_xx_coordinate=140, WOI_yy_coordinate=110):

  canvas[WOI_y_coordinate:WOI_yy_coordinate,
         WOI_x_coordinate:WOI_xx_coordinate] += WOI

  info = "insert_WOI_in_canvas\t"
  info += f"WOI_x_coordinate={WOI_x_coordinate}\t"
  info += f"WOI_y_coordinate={WOI_y_coordinate}\t"
  info += f"WOI_xx_coordinate={WOI_xx_coordinate}\t"
  info += f"WOI_yy_coordinate={WOI_yy_coordinate}"
  
  return canvas, info

def scale_image(
    image,
    scale=1.0):

  image_height = image.shape[0]
  image_width = image.shape[1]
  resized_image_width = int(image_width * scale)
  resized_image_height = int(image_height * scale)
  scaled_image = cv2.resize(image, (resized_image_width, resized_image_height))

  info = "scale_image\t"
  info += f"scale={scale}\t"
  info += f"resized_image_width={resized_image_width}\t"
  info += f"resized_image_height={resized_image_height}"

  return scaled_image, info

'''
def place_window_in_canvas(
    window,
    WOI_x_offset=10, WOI_y_offset=10,
    WOI_x_width=140, WOI_y_width=105,
    WOI_x_coordinate_in_image=0, WOI_y_coordinate_in_image=0,
    window_xx_coordinate_in_image=140, window_yy_coordinate_in_image=110):
    canvas_width=160, canvas_height=120):

  

def place_WOI_in_canvas(
    image_with_WOI, 

    
    image_with_WOI,
    scale,
    ROI_x_offset=10, ROI_y_offset=10,
    ROI_x_width=140, ROI_y_width=105,
    x_coordinate_of_resized_=0, place_y_coordinate=0,
    canvas_width=160, canvas_height=120):

  # Canvas allocation
  if len(image.shape) > 2:
    canvas = np.zeros((canvas_height, canvas_width, image.shape[2]), dtype=image.dtype)
  else:
    canvas = np.zeros((canvas_height, canvas_width), dtype=image.dtype)

  # Extract the image (remover the margins)
  ROI = image[image_y_offset:image_y_offset + image_y_width,
              image_x_offset:image_x_offset + image_x_width, ...]

  # Get the dimensions of the input image
  ROI_height, ROI_width = ROI.shape[0], ROI.shape[1]
  print(ROI_height, ROI_width)
  
  # Calculate the new dimensions for the resized image
  resized_ROI_width = int(ROI_width * scale)
  resized_ROI_height = int(ROI_height * scale)
  if resized_ROI_width >= canvas_width:
    resized_ROI_width = canvas_width - 1
  if resized_ROI_height >= canvas_height:
    resized_image_height = canvas_height - 1
  
  # Resize the image to the new dimensions
  resized_ROI = cv2.resize(ROI, (resized_ROI_width, resized_ROI_height))

  canvas[place_y_coordinate:place_y_coordinate + resized_ROI_height,
         place_x_coordinate:place_x_coordinate + resized_ROI_width] = resized_ROI
  
  # Create a region of interest on the canvas and place the resized image in it

  place_yy_coordinate = place_y_coordinate + resized_ROI_height
  place_xx_coordinate = place_x_coordinate + resized_ROI_width
  if place_yy_coordinate >= canvas_height:
    place_yy_coordinate = canvas_height - 1
  if place_xx_coordinate >= canvas_width:
    place_xx_coordinate = canvas_width - 1
  print(place_yy_coordinate, place_xx_coordinate)
  roi = canvas[place_y_coordinate:place_yy_coordinate, place_x_coordinate:place_xx_coordinate]
  roi[:resized_image_height, :resized_image_width] = resized_img
  
  info = "\"place_image_in_canvas\" "
  info += f"canvas_width={canvas_width}\t"
  info += f"canvas_height={canvas_height}\t"
  info += f"scale={scale}\t"
  info += f"resized_ROI_width={resized_ROI_width}\t"
  info += f"resized_ROI_height={resized_ROI_height}\t"
  info += f"place_x_coordinate={place_x_coordinate}\t"
  info += f"place_y_coordinate={place_y_coordinate}\t"
  
  return canvas, info
'''
