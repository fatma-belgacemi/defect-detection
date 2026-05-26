import cv2
def preprocess(frame):
 gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 blurred=cv2.GaussianBlur(gray,(5,5),0)
 kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
 closed = cv2.morphologyEx(blurred, cv2.MORPH_CLOSE, kernel)
 return closed
def detect_defects(frame,min_area=500):
 processed=preprocess(frame)
 edges=cv2.Canny(processed,50,150)
 kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
 edges=cv2.dilate(edges,kernel,iterations=1)
 contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
 defects=[c for c in contours if cv2.contourArea(c)>min_area]
 return defects
def draw_results(frame,defects):
 result=frame.copy()
 status="ok"
 color=(0,255,0)
 if defects:
  status="defect detected"
  color=(0,0,255)
  for cnt in defects:
   x,y,w,h=cv2.boundingRect(cnt)
   cv2.rectangle(result,(x,y),(x+w,y+h),color,2)
   cv2.putText(result,status,(20,40),cv2.FONT_HERSHEY_SIMPLEX,1.2,color,3)
  return result,status
