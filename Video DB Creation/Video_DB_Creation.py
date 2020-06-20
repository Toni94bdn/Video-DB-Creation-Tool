
import cv2
import json
import os
import sys


try:

    with open(os.path.join(os.path.dirname(__file__),"Settings\settings.json")) as json_file:
        config = json.load(json_file)['config']

       


    
except Exception as e:
    print("Error: "+str(e))