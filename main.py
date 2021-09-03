"""
PyARFishe by Lachrymogenic

CREDITS 
Thanks to: Stackoverflow.
And ofcourse: Sascha_T for giving the image change idea

'If you're so smart, why don't you do it?'

"""

import time
import cv2
import mss
import numpy

from tkinter import *
import pyautogui
from pynput.keyboard import Key, KeyCode, Listener
quitloop = 0
def show(key):

    if key == KeyCode(char='q'):
        cv2.destroyAllWindows()
        global quitloop
        quitloop = 1
        return False
  
#mon = {'top': 480, 'left': 900, 'width': 100, 'height': 80}
mon = {'top': 470, 'left': 930, 'width': 50, 'height': 50}
with mss.mss() as sct:
    root = Tk()
    root.title("PyARfishe")
    root.geometry('350x270')
    root.resizable(0,0)
    frame = Frame(root)
    frame.pack()
    frame2 = Frame(root)
    frame2.pack()
    frame3 = Frame(root)
    frame3.pack(pady=20)
    lbl = Label(root, text = "Lachrymogenic's Python AR Autofishing Utility")
    lbl.pack()
 
    
    def startfishe():
        global quitloop
        quitloop = 0
        scrtime = entry.get()
        detection = var1.get()
        topvar = var2.get()
        cv2imshow = var3.get()
        rodslot = str(entry2.get())
        print(float(scrtime))
        print(detection)
        print(topvar)
        
        if topvar == 1:
            root.attributes("-topmost", True)
            root.lift()
        else:
            root.attributes("-topmost", False)
            
        Listener(on_press = show).start()
        while quitloop == 0:
            im = numpy.asarray(sct.grab(mon))
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            im = cv2.addWeighted(im, 0.7, im, 0.7, 0.0)
            hist = cv2.calcHist([im], [0],None, [256], [0, 256])
            #im = cv2.Canny(im, 150, 250)
            #im = cv2.threshold(im, 150, 255, cv2.THRESH_OTSU)
            #text = pytesseract.image_to_string(im, lang='eng',config='--psm 7')
        
            #print(text)
            #hint = numpy.array(hist, dtype='int')
            def click():
                start = time.time()
                while time.time() < start + 4:
                    print("Click!")
                    pyautogui.click(700,500)
                    time.sleep(0.1)
                time.sleep(0.5)
                pyautogui.press(rodslot)
                time.sleep(0.5)
                pyautogui.press(rodslot)
                time.sleep(0.8)
                pyautogui.click(700,500)
            print(any(i > 1100 for i in hist))
            if any(i > 1100 for i in hist) == True:
                if detection == 1:
                    click()
            #print(hist)q
            if cv2imshow == 1:
                cv2.imshow('Image', im)
                cv2.moveWindow('Image', 100, 100)

            # Press "q" to quit
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            # Screenshot time
            time.sleep(float(scrtime))
        else:
            cv2.destroyAllWindows()
            
    btn = Button(root, text = "Start", command=startfishe)
    btn.pack()
    
    def DSave(top,left,width,height):
        global mon
        mon = {'top': top, 'left': left, 'width': width, 'height': height}
        print(mon)
    
    def DField():
        window = Toplevel()
        window.geometry('350x120')
        window.resizable(0,0)
        newlabel = Label(window, text = "Detection Field Configuration")
        newlabel.pack()
        newframe = Frame(window)
        newframe.pack()
        newframe2 = Frame(window)
        newframe2.pack()
        newframe3 = Frame(window)
        newframe3.pack()
        
        nentry = Entry(newframe, width = 10)
        nentry.pack(side=LEFT)
        nentry2 = Entry(newframe, width = 10)
        nentry2.pack(side=LEFT)
        nentry3 = Entry(newframe, width = 10)
        nentry3.pack(side=LEFT)
        nentry4 = Entry(newframe, width = 10)
        nentry4.pack(side=LEFT)
        
        nentry.insert(0,'470')
        nentry2.insert(0,'930')
        nentry3.insert(0,'50')
        nentry4.insert(0,'50')
        
        newlbl = Label(newframe2, text = "top, left, width, height")
        newlbl.pack(side=LEFT)
        newbtn = Button(newframe3, text = "Preview", command=startfishe)
        newbtn.pack(side=LEFT)
        newbtn2 = Button(newframe3, text = "Save", command=lambda: DSave(int(nentry.get()),int(nentry2.get()),int(nentry3.get()),int(nentry4.get())))
        newbtn2.pack(side=LEFT)
        
    btn2 = Button(frame, text = "Detection Field", command=DField)
    btn2.pack(side=LEFT)
    lbl2 = Label(frame3, text = "Screenshots per second")
    lbl2.pack(side=LEFT)
    entry = Entry(frame3, width = 10)
    entry.insert(0,'0.5')
    entry.pack(side=LEFT, padx=10)
    lbl3 = Label(frame2, text = "Fishing Rod Slot")
    lbl3.pack(side=LEFT, padx=28)
    entry2 = Entry(frame2, width = 10)
    entry2.insert(0,'3')
    entry2.pack(side=LEFT, padx=10, pady=10)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar(value=1)
    checkbox = Checkbutton(frame, text="Trigger?", variable=var1).pack(side=LEFT)
    checkbox2 = Checkbutton(frame, text="Stay on top", variable=var2).pack(side=BOTTOM)
    checkbox3 = Checkbutton(frame, text="Show Image", variable=var3).pack(side=LEFT) 
    
    rodslot = str(entry2.get())
    scrtime = entry.get()
    detection = var1.get()
    topvar = var2.get()
    cv2imshow = var3.get()
    print(detection)
    print(topvar)
    print(float(scrtime))
    #btn.place(relx=0.01, rely=0.15, anchor=NW)
    root.mainloop()
