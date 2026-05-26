import cv2
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.camera import get_camera,release_camera
from src.utils import detect_defects,draw_results
def run():
 cap=get_camera(0)
 ok_count=0
 defect_count=0
 print("Running/Press q to quit")
 while True:
  ret,frame=cap.read()
  if not ret:
   break
  defects = detect_defects(frame)
  result, status = draw_results(frame, defects)
  if status == "ok":
   ok_count += 1
  else:
   defect_count += 1
  total = ok_count + defect_count
  rate = (defect_count / total * 100) if total else 0.0
  cv2.putText(result,f"OK: {ok_count // 10}", (20, 80),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
  cv2.putText(result,f"Defects: {defect_count // 10}", (20, 110),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
  cv2.putText(result,f"Rate: {rate:.1f}%",(20, 140), cv2.FONT_HERSHEY_SIMPLEX,0.65,(200, 200, 0), 2)
  cv2.imshow("Industrial Defect Detection", result)
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break
 release_camera(cap)
if __name__ == "__main__":
 run() 
