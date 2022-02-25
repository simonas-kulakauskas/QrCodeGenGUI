# Importing Packages
# Update Requirements with 'pipreqs'
import qrcode, tkinter, sys, subprocess, os, time
from tkinter import *
import tkinter.filedialog
from PIL import ImageTk, Image


loc = "/" # Base Directory Variable

class logoLoc(object): # Locations of all logos put into a class - Easier to Call Globally
    iconjpg = "src/icons/icon.jpg"
    iconico = "src/icons/icon.ico"
    empty = "src/icons/empty.jpg"


def askUser(): 
    uIn = content.get() # Grabs Input
    if uIn == "" : # Checks if input is empty
        return
    else:
        filename = tkinter.filedialog.asksaveasfile(defaultextension=".jpg") # Tkinter's built in 'save as' popup
        try:
            uOut = filename.name #Seperates whole filename to just have directory e.g. /user/..../image.jpg
        except:
            print("Error! Error! Error!\nSave File Canceled!, Restarting!\nError! Error! Error!")
            return
        else:
            genImage(uIn, uOut) 

def genImage(a, b) :
    global loc # Grabs the temp directory
    img = qrcode.make(a) 
    img.save(b)
    loc = b
    image=Image.open(b)
    img=image.resize((120, 120))

    window.my_img=ImageTk.PhotoImage(img)
    my_label.configure(image=window.my_img)

    lbl=Label(window,text="Saved to: ", fg='black', font=("Helvetica", 12))
    lbl.place(x=210, y=230)
    lbl=Label(window,text=b, fg='black', font=("Helvetica", 12))
    lbl.place(x=210, y=250)

def closeProgram() :
    popup = tkinter.Tk()
    popup.wm_title("Close Program")
    label = tkinter.Label(popup, text="Do you want to close the program?")
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="YES", command=sys.exit)
    B2 = tkinter.Button(popup, text="CANCEL", command=popup.destroy)
    B1.pack()
    B2.pack()
    popup.mainloop()

def openFile() :
    global loc
    show = loc
    if show == "/":
        popup = tkinter.Tk()
        popup.wm_title("Open File")
        label = tkinter.Label(popup, text=("Nothing to Open"))
        label.pack(side="top", fill="x", pady=10)
        B1 = tkinter.Button(popup, text="OK", command=popup.destroy)
        B1.pack()
        popup.mainloop()
    else:
        try:
            subprocess.call(["open", "-R", show])
        except:
            popup.destroy()
        

def deleteFile() :
    global loc
    def finalDel():
        global loc
        try:
            os.remove(loc)
            lbl=Label(window,text="                                                                                                                                        ", fg='black', font=("Helvetica", 12))
            lbl.place(x=210, y=250)

            image=Image.open(logoLoc.empty)
            img=image.resize((120, 120))
            window.my_img=ImageTk.PhotoImage(img)
            my_label.configure(image=window.my_img)
            loc = "/"
            popup.destroy()
        except:
            loc = "/"
            popup.destroy()
            
    if loc == "/":
        popup = tkinter.Tk()
        popup.wm_title("Delete File")
        label = tkinter.Label(popup, text=("Cannot Delete '/'"))
        label.pack(side="top", fill="x", pady=10)
        B1 = tkinter.Button(popup, text="OK", command=popup.destroy)
        B1.pack()
        popup.mainloop()
    else:
        show = loc
        popup = tkinter.Tk()
        popup.wm_title("Delete File")
        label = tkinter.Label(popup, text=("Are you sure you want to delete the file : " + show))
        label.pack(side="top", fill="x", pady=10)
        B1 = tkinter.Button(popup, text="YES", command=finalDel)
        B1.pack()
        popup.mainloop()

def exit_function():
    print("Program shutting down")
    sys.exit()
    

window = tkinter.Tk()
window.protocol('WM_DELETE_WINDOW', exit_function)

lbl=Label(window, text="QR Code Generator by Simonas Kulakauskas", fg='black', font=("Helvetica", 24))
lbl.place(x=55, y=45)

btn=Button(window, text="Generate QR Code", fg='black', command=askUser)
btn.place(x=75, y=350)

btn=Button(window, text="Close Program", fg='black', command=closeProgram)
btn.place(x=225, y=350)

btn=Button(window, text="Open File", fg='green', command=openFile)
btn.place(x=209, y=275)

btn=Button(window, text="Delete File", fg='red', command=deleteFile)
btn.place(x=300, y=275)

lbl=Label(window, text="Input your website or message to be made into a QR Code", fg='black', font=("Helvetica", 12))
lbl.place(x=80, y=116)

lbl=Label(window, text="For the webpage, Please put in format 'https://www.website.com/'", fg='black', font=("Helvetica", 12))
lbl.place(x=80, y=135)

content=Entry(window, bd=1,)
content.place(x=80, y=160)

image=Image.open(logoLoc.empty)
img=image.resize((120, 120))
window.my_img=ImageTk.PhotoImage(img)
my_label = Label(image=window.my_img)
my_label.place(x=80, y=210)


window.title("QR Code Generator by Simonas Kulakauskas")
window.geometry("600x400+10+20")
window.minsize(600,400)
window.maxsize(600,400)

img = tkinter.Image("photo", file=logoLoc.iconjpg)
window.tk.call("wm", "iconphoto", window._w, img)
window.iconbitmap("src/icons/icon.ico")

window.mainloop()

askUser()