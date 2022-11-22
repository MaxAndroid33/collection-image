import cv2
import uuid
import os
import time
import shutil


# 2. Define Images to Collect

labels = ['Left', 'Right', 'Up', 'Down']
number_imgs = 5

# 3. Setup Folders 
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
if not os.path.exists(IMAGES_PATH):
    os.makedirs(IMAGES_PATH)
    
         

for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path)



# 4. Capture Images
for label in labels:
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))    
        while(1):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        cv2.imwrite(imgname, frame)        
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


# 5. Image Labelling
LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')
if not os.path.exists(LABELIMG_PATH):
    shutil.copytree(r"F:\Design_Programs\Season5_LABs\5th_First_Semster_LABs\AI_Labs\OurProject\labelimg",r"F:\Design_Programs\Season5_LABs\5th_First_Semster_LABs\AI_Labs\OurProject\main\Tensorflow\labelimg")    

import subprocess
subprocess.call(f"cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc", shell=True) 
subprocess.call(f"cd {LABELIMG_PATH} && python labelImg.py", shell=True) 

# 6. Move them into a Training and Testing Partition

TRAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'train')
TEST_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'test')


