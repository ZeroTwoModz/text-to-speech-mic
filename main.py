import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # >.> https://github.com/pygame/pygame/blob/main/src_py/__init__.py#L387-L393

import pyttsx3
import time
from pygame import mixer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
cc=0
for a in voices:
    adfjhadfh = a.id.split("\\")[-1]
    if "Natia" in adfjhadfh:
        voice = len(adfjhadfh)
    else:
        cc=cc+1
        if cc == len(voices):
            print("Natiis xma ar moizebna")
            os.system("start \"\" http://blindaid.ge/files/sapi/RHVoice-voice-Georgian-Natia-v4.0.5-setup.exe")
            exit()
engine.setProperty('voice', voices[voice].id)
engine.setProperty('rate',180)
def a():
 g = input("Daweret rac gindat ro mikrofonshi gadaeces:\n")
 engine.save_to_file(g, "audio.mp3")
 engine.runAndWait()
 mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
 sound = mixer.Sound("audio.mp3")
 sound.play()
 while (mixer.get_busy()):
    time.sleep(00.1)
 a()

if __name__ == "__main__":
    a()