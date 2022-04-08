
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import os
window = Tk()
imgA = ImageTk.PhotoImage(Image.open("D:\laptrinhcungdin\HK2\TH5\TKINTER\Source code\logo1.png"))
window.iconphoto(False, imgA)
window.title('Cửa hàng bách hóa')
window.geometry("600x400")
imE = PhotoImage(file='Frame1.png')
window.configure(bg="#FFFFFF")
canvas = Canvas(
     window,
     bg="#FFFFFF",
     height=600,
     width=1000,
     bd=0,
     highlightthickness=0,
     relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"Frame1.png")
background = canvas.create_image(
     300, 200,
     image=background_img)
def get_color(element):
    # Returns HEX form of element RGB color (str)
    el_r = element["fills"][0]["color"]['r'] * 255
    el_g = element["fills"][0]["color"]['g'] * 255
    el_b = element["fills"][0]["color"]['b'] * 255

    hex_code = ('#%02x%02x%02x' % (round(el_r), round(el_g), round(el_b)))
    return hex_code


def get_coordinates(element):
    # Returns element coordinates as x (int) and y (int)
    x = int(element["absoluteBoundingBox"]["x"])
    y = int(element["absoluteBoundingBox"]["y"])

    return x, y


def get_dimensions(element):
    # Return element dimensions as width (int) and height (int)
    height = int(element["absoluteBoundingBox"]["height"])
    width = int(element["absoluteBoundingBox"]["width"])

    return width, height
def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(window)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=delete2).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(window)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(window)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(window)
    screen1.title("Đăng kí tài khoản ở đây nè")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Đăng kí tài khỏan ở đây nhé!", ).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(window)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Ở đây để đăng nhập tài khoản").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()

b0 = Button(text = "Register", command=register,fg="black", bg ="#e6b49b", font=("Arial", 10, "bold")).place(x=10, y=120,width=60,height=20)
b1 = Button(text = "Login", command=login,fg="black", bg ="#e6b49b", font=("Arial", 10, "bold")).place(x=80, y=120,width=60,height=20)

lable2 = Label(window, text = "Số lượng", fg="black", bg ="#e6b49b", font=("Arial", 10, "bold")).place(x=231,y=130)
lable3 = Label(window, text = "Số lượng", fg="black",bg ="#e6b49b", font=("Arial", 10, "bold")).place(x=482,y=130)
lable_loai_1 = Label(window, text = "Loại", fg="black",bg ="#e6b49b", font=("Arial", 10, "bold")).place(x=159, y=130)
lable_loai_2 = Label(window, text = "Loại", fg="black",bg ="#e6b49b",font=("Arial", 10, "bold")).place(x=409, y=130)

#đvt
dvt_heo = Label(window, text = "đvt: kg ",bg ="#e6b49b")
dvt_ca = Label(window, text = "đvt: kg ",bg ="#e6b49b")
dvt_sua= Label(window, text = "đvt: hộp ",bg ="#e6b49b")
dvt_bo = Label(window, text = "đvt: kg ",bg ="#e6b49b")
dvt_trung = Label(window, text = "đvt: vỉ ",bg ="#e6b49b")
dvt_rau = Label(window, text = "đvt: kg ",bg ="#e6b49b")

dvt_heo.place(x=233, y=185)
dvt_ca.place(x=233, y=235 )
dvt_sua.place(x=233, y=285)
dvt_bo.place(x=483, y=185)
dvt_trung.place(x=483, y=235)
dvt_rau.place(x=483, y=285)

def clicked1():
 if v1.get()==0:
     loai_heo.config(state="disabled")
     e1.config(state="disabled")
 if v1.get()==1:
     loai_heo.config(state="normal")
     e1.config(state="normal")
def clicked2():
 if v2.get()==0:
     loai_bo.config(state="disabled")
     e2.config(state="disabled")
 if v2.get()==1:
     loai_bo.config(state="normal")
     e2.config(state="normal")
def clicked3():
 if v3.get()==0:
     loai_ca.config(state="disabled")
     e3.config(state="disabled")
 if v3.get()==1:
     loai_ca.config(state="normal")
     e3.config(state="normal")
def clicked4():
 if v4.get()==0:
     loai_trung.config(state="disabled")
     e4.config(state="disabled")
 if v4.get()==1:
     loai_trung.config(state="normal")
     e4.config(state="normal")
def clicked5():
 if v5.get()==0:
     loai_sua.config(state="disabled")
     e5.config(state="disabled")
 if v5.get()==1:
     loai_sua.config(state="normal")
     e5.config(state="normal")
def clicked6():
 if v6.get()==0:
     loai_rau.config(state="disabled")
     e6.config(state="disabled")
 if v6.get()==1:
     loai_rau.config(state="normal")
     e6.config(state="normal")


data_1=("Thịt thăn","Thịt cốt lết","Thịt chân giò","Móng giò","Thịt ba chỉ","Thịt nạc vai"
    ,"Thịt mông","Sườn heo")
data_2=("Vai bò", "Gầu bò", "Bắp bò", "Sườn bò", "Thăn vai bò", "Thịt mông","Thịt hông")
data_3=("Cá rô","Cá lóc","Cá diêu hồng","Cá tra", "Cá nục", "Cá bớp")
data_4=("Vinamilk","TH True Milk", "Milo", "Cô gái Hà Lan", "Kun", "Long Thành")
data_5=("Trứng gà", "Trứng vịt", "Trứng cút", "Trứng vịt lộn")
data_6=("Rau muống", "Rau cải", "Súp lơ", "Cà rốt", "Rau răm", "Bắp sú")

loai_heo = Combobox(window, width=10, values=data_1,state='disabled')
loai_bo= Combobox(window, width=10, values=data_2,state='disabled')
loai_ca= Combobox(window, width=10, values=data_3,state='disabled')
loai_sua=Combobox(window, width=10, values=data_4,state='disabled')
loai_trung=Combobox(window, width=10, values=data_5,state='disabled')
loai_rau=Combobox(window, width=10, values=data_6,state='disabled')

loai_rau.place(x=380, y=260)
loai_heo.place(x=130,y=160)
loai_bo.place(x=380, y=160)
loai_ca.place(x=130, y=210)
loai_sua.place(x=130, y=260)
loai_trung.place(x=380, y=210)

var = StringVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
C1 = Checkbutton(window, text="Thịt heo",bg ="#e6b49b",font=("Arial", 10, "bold"),variable=v1,command=clicked1)
C2 = Checkbutton(window, text="Thịt bò",bg ="#e6b49b",font=("Arial", 10, "bold"),variable=v2,command=clicked2)
C3 = Checkbutton(window, text="Cá",bg ="#e6b49b",font=("Arial", 10, "bold"), variable=v3,command=clicked3)
C4 = Checkbutton(window, text="Trứng",bg ="#e6b49b",font=("Arial", 10, "bold"), variable=v4,command=clicked4)
C5 = Checkbutton(window, text="Sữa",bg ="#e6b49b", font=("Arial", 10, "bold"),variable=v5,command=clicked5)
C6 = Checkbutton(window, text="Rau",bg ="#e6b49b",font=("Arial", 10, "bold"), variable=v6,command=clicked6)

C1.place(x=50, y=158)
C2.place(x=310, y=158)
C3.place(x=50, y=208)
C4.place(x=310, y=208)
C5.place(x=50, y=258)
C6.place(x=310, y=258)


entrytext1 = IntVar()
entrytext2 = IntVar()
entrytext3 = IntVar()
entrytext4 = IntVar()
entrytext5 = IntVar()
entrytext6 = IntVar()
e1 = Entry(window, width =10,state='disabled', textvariable=entrytext1)
e3 = Entry(window, width =10,state='disabled', textvariable=entrytext2)
e5 = Entry(window, width =10,state='disabled', textvariable=entrytext3)
e2 = Entry(window, width =10,state='disabled', textvariable=entrytext4)
e4 = Entry(window, width =10,state='disabled', textvariable=entrytext5)
e6 = Entry(window, width =10,state='disabled', textvariable=entrytext6)


e1.place(x=230, y=160)
e3.place(x=230, y=210)
e5.place(x=230, y=260)
e2.place(x=480, y=160)
e4.place(x=480, y=210)
e6.place(x=480, y=260)

a = [0] * 6
data_heo = [1000, 2000, 3000, 2500, 5000, 7000, 2400, 8600]
data_bo = [1000, 2000, 3000, 2500, 5000, 7000, 2400]
data_ca = [1000, 2000, 3000, 2500, 5000, 7000]
data_sua = [1000, 2000, 3000, 2500, 5000, 7000]
data_rau = [1000, 2000, 3000, 2500, 5000, 7000]
data_trung = [1000, 2000, 3000, 2500]
def price_tong(price, data, data_1, entryy):
    for i in range(0, len(data)):
        if price.get() == data[i]:
            price1 = (entryy.get() * data_1[i])
            return price1

def price_heo(event):
    if loai_heo.get():
        label33.config(text=f'giá là {price_tong(loai_heo, data_1, data_heo, entrytext1)}')
        a[0] = (price_tong(loai_heo, data_1, data_heo, entrytext1))
label33 = Label(window, bg ="#e6b49b")
label33.place(x=130, y=185)

def price_bo(event):
    if loai_bo.get():
        label44.config(text=f'giá là {price_tong(loai_bo, data_2, data_bo, entrytext4)}')
        a[1] = (price_tong(loai_bo, data_2, data_bo, entrytext4))
label44 = Label(window,bg ="#e6b49b")
label44.place(x=380, y=185)


def price_ca(event):
    if loai_ca.get():
        label55.config(text=f'giá là {price_tong(loai_ca, data_3, data_ca, entrytext2)}')
        a[2] = (price_tong(loai_ca, data_3, data_ca, entrytext2))
label55 = Label(window,bg ="#e6b49b")
label55.place(x=130, y=235)



def price_sua(event):
    if loai_sua.get():
        label66.config(text=f'giá là {price_tong(loai_sua, data_4, data_sua, entrytext3)}')
        a[3] = (price_tong(loai_sua, data_4, data_sua, entrytext3))
label66 = Label(window,bg ="#e6b49b")
label66.place(x=130, y=285)


def price_trung(event):
    if loai_trung.get():
        label77.config(text=f'giá là {price_tong(loai_trung, data_5, data_trung, entrytext5)}')
        a[4] = (price_tong(loai_trung, data_5, data_trung, entrytext5))
label77 = Label(window,bg ="#e6b49b")
label77.place(x=380, y=235)


def price_rau(event):
    if loai_rau.get():
        label88.config(text=f'giá là {price_tong(loai_rau, data_6, data_rau, entrytext6)}')
        a[5] = (price_tong(loai_rau, data_6, data_rau, entrytext6))
label88 = Label(window,bg ="#e6b49b")
label88.place(x=380, y=285)

window.bind('<Return>', price_heo)
window.bind('<Return>', price_bo, add='+')
window.bind('<Return>', price_ca, add='+')
window.bind('<Return>', price_sua, add='+')
window.bind('<Return>', price_trung, add='+')
window.bind('<Return>', price_rau, add='+')


def sum(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s


def clickSumButton():
    sum(a)
    messagebox.showinfo("Hóa đơn", f"""Cảm ơn quý khách đã mua hàng!
    Tổng tiền của quý khách là {sum(a)} """)

window.bind('<Return>', price_heo, add='+')
window.bind('<Return>', price_bo, add='+')
window.bind('<Return>', price_ca, add='+')
window.bind('<Return>', price_sua, add='+')
window.bind('<Return>', price_trung, add='+')
window.bind('<Return>', price_rau, add='+')


def sum(a):
   s = 0
   for i in range(len(a)):
       s += a[i]
   return s


def clickSumButton():
   sum(a)
   messagebox.showinfo("Hóa đơn", f"""Cảm ơn quý khách đã mua hàng!
Tổng tiền của quý khách là {sum(a)} """)

btnsum = Button(window, text = "Tính tiền", command = clickSumButton, pady = 5, padx = 20)
img1 = PhotoImage(file="Button.png")
b1 = Button(
     image=img1,
     borderwidth=0,
     bg = "#e6b49b",
     highlightthickness=0,
     command=clickSumButton,
     relief="flat")

b1.place(
     x=220, y=320,
     width=160,
     height=65)

window.mainloop()
