import cv2
import numpy as np
import os
import datetime

def StartVideoCapture(config):
    int_waitTime = config['waitTime']
    int_width = config['width']
    int_height = config['height']
    str_nameprefix = config['nameprefix']
    str_outputdir = config['outputdir']
    str_fileformat = config['fileformat']
    str_codec = config['codec']
    int_framerate = config['framerate']
    
    
    int_count = 0
    str_currentFileName = os.path.join(str_outputdir,str_nameprefix+"-"+str(int_count)+str_fileformat)
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter(str_currentFileName, cv2.VideoWriter_fourcc(*str_codec), int_framerate, (int_width,int_height))
    ts_StartTime = datetime.datetime.now
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)
            # write the flipped frame
            cv2.imshow('frame',frame)
            b_timeout, str_seconds  =waitTimer(ts_StartTime,int_waitTime)
            if (b_timeout) :
                out.write(frame)
                ts_StartTime = datetime.datetime.now
            else :
                cv2.putText(frame, str_seconds,(round(int_height/2), round(int_width/2)), font, 1,(0,0,255),2,cv2.LINE_AA)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def waitTimer(in_tsStart ,in_waitTime):
    ts_now = datetime.datetime.now - in_tsStart
    return ts_now.total_seconds()> in_waitTime , str(round(ts_now.total_seconds()))
