import cv2
import cvlib as cv 
from cvlib.object_detection import draw_bbox 

video = cv2.VideoCapture(0)
labels = []

while(True):
    ret,frame = video.read()
    bbox,label,config = cv.detect_common_objects(frame)

    output = draw_bbox(frame,bbox,label,config)

    cv2.imshow("Vision",output)

    for stuff in label:
        if stuff not in labels:
            labels.append(stuff)

    if (cv2.waitKey(1) & 0xFF) == ord("q"):
        break


i = 0
newSentence = []
for stuff in labels:
    if i == 0:
        newSentence.append(f'found {stuff}')
    else:
        newSentence.append(", ",stuff)
    
    i += 1
        
print('stuff')
print(" ".join(newSentence))