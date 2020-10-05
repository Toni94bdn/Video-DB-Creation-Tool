
import json
import os
import sys
import VideoRecorder

try:

    json_file=  open(os.path.join(os.path.dirname(__file__),"Settings/settings.json"))
    config = json.load(json_file)['config']
    
    print("S1: Configuration loaded successfully")    
    input("Press Enter to continue...")

except Exception as e:
    print("Error: "+str(e))