import tkinter
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import math

master = Tk()
master.geometry('400x300')
filename = 'silownia.csv'
master.title("Siłownia")
tabControl = ttk.Notebook(master)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Wejścia i Wyjścia')
tabControl.add(tab2, text='Kupno Karnetu')
tabControl.add(tab3, text='Dodawanie osob')
tabControl.pack(expand=1, fill="both")

def timestamp():
    ts = time.time()
    ts = round(ts)/60
    return int(round(ts))

def f_wejscie():
    i = 0
    for x in rows:
        if variable_in.get()==rows[i][0]:
            rows[i][3]=1
            rows[i][4]=timestamp()

        i+=1
    i=0
    for x in nazwy_wejscie:
        if variable_in.get() == x:
            nazwy_wyjscie.append(nazwy_wejscie[i])
            nazwy_wejscie.pop(i)
        i += 1
    wejscie = nazwy_wejscie
    if wejscie:
        variable_in.set(wejscie[0])  # default value
        drop_wejscie = OptionMenu(tab1, variable_in, *wejscie)
    else:
        variable_in.set("wszyscy sa na silowni")  # default value
        drop_wejscie = OptionMenu(tab1, variable_in, "wszyscy sa na silowni")
    drop_wejscie.grid(row=2, column=0)
    wyjscie = nazwy_wyjscie
    if wyjscie:
        variable_out.set(wyjscie[0])  # default value
        drop_wyjscie = OptionMenu(tab1, variable_out, *wyjscie)
    else:
        variable_out.set("brak osob na silowni")  # default value
        drop_wyjscie = OptionMenu(tab1, variable_out, "brak osob na silowni")
    drop_wyjscie.grid(row=2, column=2)

    open(filename, "w+")
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def f_wyjscie():
    i = 0
    for x in rows:
        if variable_out.get()==rows[i][0]:
            rows[i][3]=0
            rows[i][2]=int(rows[i][2])-(timestamp()-int(rows[i][4]))
            rows[i][4]=0
        i+=1
    i=0
    for x in nazwy_wyjscie:
        if variable_out.get() == x:
            nazwy_wejscie.append(nazwy_wyjscie[i])
            nazwy_wyjscie.pop(i)
        i += 1
    wejscie = nazwy_wejscie
    if wejscie:
        variable_in.set(wejscie[0])  # default value
        drop_wejscie = OptionMenu(tab1, variable_in, *wejscie)
    else:
        variable_in.set("wszyscy sa na silowni")  # default value
        drop_wejscie = OptionMenu(tab1, variable_in, "wszyscy sa na silowni")
    drop_wejscie.grid(row=2, column=0)
    wyjscie = nazwy_wyjscie
    if wyjscie:
        variable_out.set(wyjscie[0])  # default value
        drop_wyjscie = OptionMenu(tab1, variable_out, *wyjscie)
    else:
        variable_out.set("brak osob na silowni")  # default value
        drop_wyjscie = OptionMenu(tab1, variable_out, "brak osob na silowni")
    drop_wyjscie.grid(row=2, column=2)
    open(filename, "w+")
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)



file = open(filename, encoding='utf-8')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
nazwy_wejscie = []
nazwy_wyjscie = []
i=0
for row in csvreader:
    rows.append(row)

for x in rows: #wypisanie w drop downach

    if int(rows[i][1]): #sprawdzenie czy ma karnet
        if int(rows[i][3]): #sprawdzenie czy jest na silowni
            nazwy_wyjscie.append(rows[i][0])
        else:
            nazwy_wejscie.append(rows[i][0])
    i += 1



#tab1
wejscie = nazwy_wejscie
wyjscie = nazwy_wyjscie


greeting = Label(tab1, text="Wybierz uczestnika")
uzytkownik_wejscie = Label(tab1, text="Do wejscia")
uzytkownik_wyjscie = Label(tab1, text="Do wyjscia")

variable_in = StringVar(master)
if wejscie:
    variable_in.set(wejscie[0]) # default value
    drop_wejscie = OptionMenu(tab1,  variable_in, *wejscie)
else:
    variable_in.set("wszyscy sa na silowni")  # default value
    drop_wejscie = OptionMenu(tab1, variable_in, "wszyscy sa na silowni")

variable_out = StringVar(master)
if wyjscie:
    variable_out.set(wyjscie[0]) # default value
    drop_wyjscie = OptionMenu(tab1,  variable_out, *wyjscie)
else:
    variable_out.set("brak osob na silowni")  # default value
    drop_wyjscie = OptionMenu(tab1, variable_out, "brak osob na silowni")

button_wejscie = Button(tab1, text="Wejście", command=f_wejscie)
button_wyjscie = Button(tab1, text="Wyjście", command=f_wyjscie)

greeting.grid(row=0, column=1)
uzytkownik_wejscie.grid(row=1, column=0)
uzytkownik_wyjscie.grid(row=1, column=2)
drop_wejscie.grid(row=2, column=0)
drop_wyjscie.grid(row=2, column=2)

button_wejscie.grid(row=3, column=0)
button_wyjscie.grid(row=3, column=2)

#tab2
def slider_changed(event):
    licznik = Label(tab2, text=math.floor(slider.get()))
    licznik.grid(row=4, column=1)

def karnet():
    i=0
    for x in rows:
        if var_all.get() == x[0]:
            rows[i][2] = int(rows[i][2])+(int(slider.get())*60)
            open(filename, "w+")
            with open(filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(rows)
        i=i+1




wszyscy = []

for x in rows:
    wszyscy.append(x[0])

var_all = StringVar(master)
var_all.set(wszyscy[0]) # default value
current_value = tk.DoubleVar()
slider = ttk.Scale(tab2, from_=0, to=20, orient=HORIZONTAL, variable=current_value, command=slider_changed)
licznik = Label(tab2, text=math.floor(slider.get()))
drop_karnet = OptionMenu(tab2, var_all, *wszyscy)






Label(tab2, text="Wybierz Osobę").grid(row=0, column =1)

drop_karnet.grid(row=1, column=1)

Label(tab2, text="Wybierz Liczbę godzin do kupna").grid(row=2, column =1)
slider.grid(row=3, column=1)
licznik.grid(row=4, column=1)
Button(tab2, text="Zatwierdź", command=karnet).grid(row=5, column=1)

#tab3

def dodaj():
    osoba = []
    osoba.append(input_imie.get(1.0, "end-1c"))
    osoba.append("1")
    osoba.append("0")
    osoba.append("0")
    osoba.append("0")
    rows.append(osoba)
    open(filename, "w+")
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

input_imie = tk.Text(tab3,height = 1, width = 20)
Label(tab3, text="Wpisz imię i nazwisko").grid(row=0, column =0)
input_imie.grid(row=1, column = 0)
Button(tab3, text="Zatwierdź", command=dodaj).grid(row=3, column=0)


master.mainloop()