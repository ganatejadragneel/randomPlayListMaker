import os
import random
from mutagen.mp4 import MP4
import subprocess
import time
x=os.listdir("C:\\Users\\hp\\Desktop\\utube")
a=[]
for i in range(len(x)):
    a.append(x[i])
l=len(a)
playlist=[]
playlist_index=[]
for i in range(0,5):
    s=random.randrange(0,l)
    playlist_index.append(s)
for i in range(5):
    s=a[playlist_index[i]]
    playlist.append(s)
for i in range(5):
    audio =MP4("C:\\Users\\hp\\Desktop\\utube\\"+playlist[i])
    #print(audio)
    t=audio.info.length
    callString="explorer C:\\Users\\hp\\Desktop\\utube\\"+playlist[i];
    subprocess.call(callString, shell=True)
    time.sleep(t)