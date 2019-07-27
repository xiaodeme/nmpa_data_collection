

import platform

def UsePlatform():
    sysstr = platform.system()
    if(sysstr =="Windows"):
        print ("Call Windows tasks")
    elif(sysstr == "Linux"):
        print ("Call Linux tasks")
    else:
        print ("Other System tasks")

UsePlatform()