Real-time surface defect detection using Python and OpenCV.  
Simulates a visual quality control system used in industrial automation.
1. Captures live webcam feed
2. Applies Gaussian blur + Canny edge detection
3. Detects abnormal contours above a minimum area threshold
4. Classifies each frame as OK or DEFECT DETECTED
- Python 3.x
- OpenCV
- NumPy
pip install -r requirements.txt
python src/detector.py