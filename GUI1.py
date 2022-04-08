from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import os

window = Tk()

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

label_bg_color = "#e6b49b"

# Login and Register window
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


# Labels of Amounts and Options
amount_lable_1 = Label(window, text="Số lượng", fg="black", bg=label_bg_color, font=("Arial", 10, "bold")).place(x=231,y=130)
amount_lable_2 = Label(window, text="Số lượng", fg="black", bg=label_bg_color, font=("Arial", 10, "bold")).place(x=482,y=130)
lable_loai_1 = Label(window, text="Loại", fg="black", bg=label_bg_color, font=("Arial", 10, "bold")).place(x=159, y=130)
lable_loai_2 = Label(window, text="Loại", fg="black", bg=label_bg_color,font=("Arial", 10, "bold")).place(x=409, y=130)


# Calculation units
kg_unit = "đvt: kg"
box_unit = "đvt: hộp"
pack_unit = "đvt: vỉ"

# Unit Label
pork_unit_label = Label(window, text=kg_unit, bg=label_bg_color)
fish_unit_label = Label(window, text=kg_unit, bg=label_bg_color)
milk_unit_label = Label(window, text=box_unit, bg=label_bg_color)
cow_unit_label = Label(window, text=kg_unit, bg=label_bg_color)
egg_unit_label = Label(window, text=pack_unit, bg=label_bg_color)
vegetable_unit_label = Label(window, text=kg_unit, bg=label_bg_color)

pork_unit_label.place(x=233, y=185)
fish_unit_label.place(x=233, y=235)
milk_unit_label.place(x=233, y=285)
cow_unit_label.place(x=483, y=185)
egg_unit_label.place(x=483, y=235)
vegetable_unit_label.place(x=483, y=285)

# Options
pork_options = ['Thịt thăn', "Thịt cốt lết", "Thịt chân giò", "Móng giò", "Thịt ba chỉ", "Thịt nạc vai", "Thịt mông", "Sườn heo"]
fish_options = ("Cá rô", "Cá lóc", "Cá diêu hồng", "Cá tra", "Cá nục", "Cá bớp")
milk_options = ("Vinamilk", "TH True Milk", "Milo", "Cô gái Hà Lan", "Kun", "Long Thành")
cow_options = ("Vai bò", "Gầu bò", "Bắp bò", "Sườn bò", "Thăn vai bò", "Thịt mông", "Thịt hông")
egg_options = ("Trứng gà", "Trứng vịt", "Trứng cút", "Trứng vịt lộn")
vegetable_options = ("Rau muống", "Rau cải", "Súp lơ", "Cà rốt", "Rau răm", "Bắp sú")
option_list = [pork_options, fish_options, milk_options, cow_options, egg_options, vegetable_options]

a = [0] * 6
pork_option_prices = [1000, 2000, 3000, 2500, 5000, 7000, 2400, 8600]
fish_option_prices = [1000, 2000, 3000, 2500, 5000, 7000]
milk_option_prices = [1000, 2000, 3000, 2500, 5000, 7000]
cow_option_prices = [1000, 2000, 3000, 2500, 5000, 7000, 2400]
egg_option_prices = [1000, 2000, 3000, 2500]
vegetable_option_prices = [1000, 2000, 3000, 2500, 5000, 7000]
price_option_list = [pork_option_prices, fish_option_prices, milk_option_prices, cow_option_prices, egg_option_prices, vegetable_option_prices]

# Combobox Variables
cbb1 = StringVar()
cbb2 = StringVar()
cbb3 = StringVar()
cbb4 = StringVar()
cbb5 = StringVar()
cbb6 = StringVar()
Combobox_var_list = [cbb1, cbb2, cbb3, cbb4, cbb5, cbb6]

# Comboboxs for Options
pork_Combobox = Combobox(window, width=10, values=pork_options,state='disabled', textvariable=cbb1)
fish_Combobox = Combobox(window, width=10, values=fish_options,state='disabled', textvariable=cbb2)
milk_Combobox = Combobox(window, width=10, values=milk_options,state='disabled', textvariable=cbb3)
cow_Combobox = Combobox(window, width=10, values=cow_options,state='disabled', textvariable=cbb4)
egg_Combobox = Combobox(window, width=10, values=egg_options,state='disabled', textvariable=cbb5)
vegetable_Combobox = Combobox(window, width=10, values=vegetable_options,state='disabled', textvariable=cbb6)
Combobox_list = [pork_Combobox, fish_Combobox, milk_Combobox, cow_Combobox, egg_Combobox, vegetable_Combobox]

pork_Combobox.place(x=130,y=160)
fish_Combobox.place(x=130, y=210)
milk_Combobox.place(x=130, y=260)
cow_Combobox.place(x=380, y=160)
egg_Combobox.place(x=380, y=210)
vegetable_Combobox.place(x=380, y=260)

# Func to change state of Cbb and Ent when check and uncheck
def checkbox_clicked(i):
    if var_list[i].get() == 1:
         Combobox_list[i].config(state='normal')
         Entry_list[i].config(state='normal')
    else:
         Combobox_list[i].config(state='disable')
         Entry_list[i].config(state='disable')

# Checkbutton's Variables
var = StringVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
var_list = [v1, v2, v3, v4, v5, v6]

# Checkbuttons
pork_Checkbutton = Checkbutton(window, text="Thịt heo", bg=label_bg_color, font=("Arial", 10, "bold"), variable=v1, command=lambda: checkbox_clicked(0))
fish_Checkbutton = Checkbutton(window, text="Cá", bg=label_bg_color, font=("Arial", 10, "bold"), variable=v2, command=lambda: checkbox_clicked(1))
milk_Checkbutton = Checkbutton(window, text="Sữa", bg=label_bg_color, font=("Arial", 10, "bold"), variable=v3, command=lambda: checkbox_clicked(2))
cow_Checkbutton = Checkbutton(window, text="Thịt bò", bg=label_bg_color, font=("Arial", 10, "bold"), variable=v4, command=lambda: checkbox_clicked(3))
egg_Checkbutton = Checkbutton(window, text="Trứng", bg=label_bg_color, font=("Arial", 10, "bold"), variable=v5, command=lambda: checkbox_clicked(4))
vegetable_Checkbutton = Checkbutton(window, text="Rau", bg=label_bg_color, font=("Arial", 10, "bold"), variable=v6, command=lambda: checkbox_clicked(5))

pork_Checkbutton.place(x=50, y=158)
fish_Checkbutton.place(x=50, y=208)
milk_Checkbutton.place(x=50, y=258)
cow_Checkbutton.place(x=310, y=158)
egg_Checkbutton.place(x=310, y=208)
vegetable_Checkbutton.place(x=310, y=258)

# Price for each goods
def each_type_price(i):
    x = price_option_list[i][option_list[i].index(Combobox_var_list[i].get())]
    y = entry_var_list[i].get()
    sum = x*y
    price_label[i].config(text=f'giá là {sum}')
    a[i] = sum

# Event Function for Price labels
def price_type_pork(event):
    each_type_price(0)

def price_type_fish(event):
    each_type_price(1)

def price_type_milk(event):
    each_type_price(2)

def price_type_cow(event):
    each_type_price(3)

def price_type_egg(event):
    each_type_price(4)

def price_type_vegetable(event):
    each_type_price(5)

# Price Lables
pork_price_label = Label(window, bg =label_bg_color)
cow_price_label = Label(window,bg =label_bg_color)
fish_price_label = Label(window,bg =label_bg_color)
milk_price_label = Label(window,bg =label_bg_color)
egg_price_label = Label(window,bg =label_bg_color)
vegetable_price_label = Label(window,bg =label_bg_color)
price_label = [pork_price_label, fish_price_label, milk_price_label, cow_price_label, egg_price_label, vegetable_price_label]

pork_price_label.place(x=130, y=185)
fish_price_label.place(x=130, y=235)
milk_price_label.place(x=130, y=285)
cow_price_label.place(x=380, y=185)
egg_price_label.place(x=380, y=235)
vegetable_price_label.place(x=380, y=285)

# Entry's Variables
entrytext1 = IntVar()
entrytext2 = IntVar()
entrytext3 = IntVar()
entrytext4 = IntVar()
entrytext5 = IntVar()
entrytext6 = IntVar()
entry_var_list = [entrytext1, entrytext2, entrytext3, entrytext4, entrytext5, entrytext6]

# Entries for Amount
pork_Entry = Entry(window, width =10,state='disabled', textvariable=entrytext1)
fish_Entry = Entry(window, width =10,state='disabled', textvariable=entrytext2)
milk_Entry = Entry(window, width =10,state='disabled', textvariable=entrytext3)
cow_Entry = Entry(window, width =10,state='disabled', textvariable=entrytext4)
egg_Entry = Entry(window, width =10,state='disabled', textvariable=entrytext5)
vegetable_Entry = Entry(window, width =10,state='disabled', textvariable=entrytext6)
Entry_list = [pork_Entry, fish_Entry, milk_Entry, cow_Entry, egg_Entry, vegetable_Entry]

pork_Entry.place(x=230, y=160)
fish_Entry.place(x=230, y=210)
milk_Entry.place(x=230, y=260)
cow_Entry.place(x=480, y=160)
egg_Entry.place(x=480, y=210)
vegetable_Entry.place(x=480, y=260)

# Binding Event 'Enter' key
pork_Entry.bind('<Return>', price_type_pork)
fish_Entry.bind('<Return>', price_type_fish)
milk_Entry.bind('<Return>', price_type_milk)
cow_Entry.bind('<Return>', price_type_cow)
egg_Entry.bind('<Return>', price_type_egg)
vegetable_Entry.bind('<Return>', price_type_vegetable)

# Sum button
def Sum_button_clicked():
    s = 0
    for i in range(len(a)):
        s += a[i]
    messagebox.showinfo("Hóa đơn", f"""Cảm ơn quý khách đã mua hàng!
Tổng tiền của quý khách là {s} """)

btnsum = Button(window, text="Tính tiền", command=Sum_button_clicked, pady=5, padx=20)
img1 = PhotoImage(file="Button.png")
Sum_button = Button(
     image=img1,
     borderwidth=0,
     bg=label_bg_color,
     highlightthickness=0,
     command=Sum_button_clicked,
     relief="flat")

Sum_button.place(
     x=220, y=320,
     width=160,
     height=65)

window.mainloop()

