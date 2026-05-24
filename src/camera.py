import cv2
def get_camera(index=0):
 cap=cv2.VideoCapture(index)
 if not cap.isOpened():
  raise RuntimeError("camera not open")
 return cap
def release_camera(cap):
 cap.release()
 cv2.destroyAllWindows()