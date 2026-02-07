import os, sys
import subprocess


def startApp():
    x=1
    y=2
    z=3
    if x==1:
        if y==2:
            if z==3:
                if x+y+z==6:
                    print("Deep nesting")

    subprocess.call("ls -la", shell=True)


startApp()
