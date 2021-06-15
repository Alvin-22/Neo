import cv2

from desktopmagic.screengrab_win32 import getDisplayRects, getRectAsImage
from PIL import Image


def image(image_type, monitor):
  if image_type:
    screenshot = getRectAsImage(getDisplayRects()[monitor])

    return {'message': 'Screenshot successfully captured', 'screenshot': screenshot, 'text_mode': 'success'}
  elif not image_type:
    cam = cv2.VideoCapture(monitor)
    
    check, frame = cam.read()
    if not check:
      raise Exception('Cam unavailable')

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)

    cam.release()

    return {'message': 'Cam screenshot successfully captured', 'screenshot': frame, 'text_mode': 'success'}
  else:
    raise Exception('Error message')