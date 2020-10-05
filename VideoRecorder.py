import cv2
import numpy as np
import os

def StartVideoCapture(config):
    int_waitTime = config['waitTime']
    int_width = config['width']
    int_height = config['height']
    str_nameprefix = config['nameprefix']
    str_outputdir = config['utputdir']
    str_fileformat = config['fileformat']
    str_codec = config['codec']
    int_framerate = config['framerate']
    
    
    int_count = 0
    str_currentFileName = os.path.join(str_outputdir,str_nameprefix+"-"+str(int_count)+"."+str_fileformat)

    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter(str_currentFileName, cv2.cv.CV_FOURCC(*str_codec), int_framerate, (int_width,int_height))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()



    
