import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.simpledialog as tksd
import tkinter.messagebox as tkms
from webbrowser import open_new


def displayImage():
    global window, canvas, photo, present
    w = present.width
    h = present.height
    window.geometry(str(w) + "x" + str(h))
    if not canvas:
        canvas = tk.Canvas(window, bg="#626262", bd=0, highlightthickness=0)
    canvas.delete("all")
    canvas.config(width=w, height=h)
    photo = tk.PhotoImage()  # you should initialize photo
    photo.put(present.make_blob())  # no need to get RGB!!!!!
    canvas.create_image((w / 2, h / 2), image=photo, state="normal")
    canvas.pack()


def func_open():
    global origin, present
    readFp = tkfd.askopenfilename(
        filetypes=[("All image file", ".jpg .jpeg .bmp .png .tif .gif")],
    )  # PhotoImage widget supports the GIF, PGM, PPM, and PNG file formats as of Tkinter 8.6
    if not readFp:
        return
    origin = wd.Image(filename=readFp, format="png")
    present = wd.Image(filename=readFp, format="png")
    displayImage()
    pass


def func_save():
    global window, present
    if present == None:
        return
    saveFp = tkfd.asksaveasfile(
        defaultextension=".png",
        filetypes=(("PNG file", ".png"), ("All", "*.*")),
    )
    if not saveFp:
        return
    savePhoto = present.convert("png")
    savePhoto.save(filename=saveFp.name)
    pass


def func_exit():
    global window
    window.quit()
    window.destroy()
    pass


def func_scale():
    global present
    if present == None:
        return
    scale = tksd.askfloat("scale", "Enter scale(0~5))", minvalue=0, maxvalue=5)
    if scale != None:
        present.resize(int(present.width * scale), int(present.height * scale))
        displayImage()
    pass


def func_rotate():
    global present
    if present == None:
        return
    degree = tksd.askfloat("degree", "Enter degree(0~360))", minvalue=0, maxvalue=360)
    if degree != None:
        present.rotate(degree)
        displayImage()
    pass

preserve = {"resize, "}

def config(func, **kwargs):
    eval("")

def preservetest(funcname: str, state1, state2=None):
    if preserve[]


window, canvas, origin, temp, present = (None,) * 5
window = tk.Tk()
window.geometry("250x250")
window.title("photoshop")

try:
    import wand.image as wd
except ModuleNotFoundError:
    tkms.showerror(
        "ModuleNotFoundError",
        "wand is not installed. To install, type 'pip install wand` in cmd",
    )
    func_exit()
except ImportError:
    yesorno = tkms.askyesnocancel(
        "ImportError", "ImageMagick is not installed. Do you want to install?"
    )
    if yesorno:
        open_new(
            r"https://download.imagemagick.org/ImageMagick/download/binaries/ImageMagick-7.1.0-13-Q16-HDRI-x64-dll.exe"
        )
    else:
        tkms.showerror("ImportError", "Install ImageMagick")
    func_exit()

mainMenu = tk.Menu(window)
window["menu"] = mainMenu

fileMenu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(label="open file", command=func_open)
fileMenu.add_command(label="save file", command=func_save)
fileMenu.add_command(label="exit")

tool1Menu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="tool1", menu=tool1Menu)
tool1Menu.add_command(label="scale", command=func_scale)
tool1Menu.add_command(
    label="flip",
    command=lambda: present.flip() and displayImage() if present else None,
)
tool1Menu.add_command(
    label="flop",
    command=lambda: present.flop() and displayImage() if present else None,
)
tool2Menu = tk.Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="tool2", menu=tool2Menu)
tool2Menu.add_command(label="rotate", command=func_rotate)
tool2Menu.add_command(label="zoom")
tool2Menu.add_command(label="zoom")


window.mainloop()
