import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk, messagebox
from Results import *
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from algo import *



def wt_percent2(numStocks,numSieves,sievegrad,entries,sieve_entries,root,mainroot,wp,pan):
    flag = True
    for i in range(len(entries)):
        if (len(entries[i].get())) == 0:
            flag = False

    for i in range(len(sieve_entries)):
        if (len(sieve_entries[i].get())) == 0:
            flag = False

    if (flag == False):
        messagebox.showerror("Error", "Please enter all the fields", icon='error')
        return
    root.withdraw()
    window = Toplevel(root)
    screen_width=window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    app_width=1280
    app_height=720
    x=(screen_width/2)-(app_width/2)
    y=(screen_height/2)-(app_height/2)-30
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    window.title("STAB")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        80.0,
        fill="#3888FF",
        outline="")

    canvas.create_text(
        63.0,
        121.0,
        anchor="nw",
        text="Percent Passing",
        fill="#3888FF",
        font=("Inter Medium", 28 * -1)
    )

    canvas.create_text(
        70.0,
        23.0,
        anchor="nw",
        text="STAB",
        fill="#FFFFFF",
        font=("Inter Bold", 28 * -1)
    )

    canvas.create_text(
        1176.0,
        28.0,
        anchor="nw",
        text="Version 2.1",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        1129.0,
        48.0,
        anchor="nw",
        text="All Rights Reserved",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        63.0,
        99.0,
        anchor="nw",
        text="Define stockPiles & sieves",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        227.0,
        99.0,
        anchor="nw",
        text="Enter values",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    image_image_1 = PhotoImage(
        file="assets/next_write.png")
    image_1 = canvas.create_image(
        215.0,
        107.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file="assets/IITR_Logo.png")
    image_2 = canvas.create_image(
        35.0,
        40.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file="assets/copyright.png")
    image_3 = canvas.create_image(
        1118.0,
        55.0,
        image=image_image_3
    )

    image_4 = canvas.create_image(
        301.0,
        107.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        63.0,
        180.0,
        1039.0,
        687.0,
        fill="#F1F5FF",
        outline="")

    button_image_1 = PhotoImage(
        file="assets/calculate_button.png")

    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: calculate(numStocks.get(),sievenum,entries,sieve_entries,window,mainroot,wp,pan,0),
        relief="flat"
    )
    button_1.place(
        x=1109.0,
        y=184.0,
        width=108.0,
        height=31.0
    )

    canvas.create_rectangle(
        20.0,
        124.0,
        48.0,
        152.0,
        fill="#000000",
        outline="")

    button_image_3 = PhotoImage(
        file="assets/back_button.png")
    button_3 = Button(
        window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_utl(root, window),
        relief="flat"
    )
    button_3.place(
        x=20.0,
        y=124.0,
        width=28.0,
        height=28.0
    )

    canvas.create_rectangle(
        63.0,
        180.0,
        1039.0,
        687.0,
        fill="#F1F5FF",
        outline="")






    canvas.create_rectangle(
        20.0,
        124.0,
        48.0,
        152.0,
        fill="#000000",
        outline="")

    ###Upper Lower Bound Blue box###
    canvas.create_rectangle(
        147.0,
        190.0,
        248.0,
        219.0,
        fill="#C1D6FF",
        outline="")
    canvas.create_rectangle(
        256.0,
        190.0,
        357.0,
        219.0,
        fill="#C1D6FF",
        outline="")
    ###Upper Lower Bound Blue box###

    ######Upper Lower Bound######
    canvas.create_text(
        155.0,
        195.0,
        anchor="nw",
        text="Lower Bound",
        fill="#273340",
        font=("OpenSansRoman SemiBold", 12 * -1)
    )

    canvas.create_text(
        264.0,
        195.0,
        anchor="nw",
        text="Upper Bound",
        fill="#273340",
        font=("OpenSansRoman SemiBold", 12 * -1)
    )

    #####SIEVE ENTRIES####
    sievenum=numSieves.get()
    if(sievegrad.get()=="BC - 19mm"):
        sievenum=11
    elif(sievegrad.get()=="BC - 13.2mm"):
        sievenum = 10
    elif (sievegrad.get() == "SMA - 13mm"):
        sievenum =9
    elif (sievegrad.get() == "SMA - 19mm"):
        sievenum =10
    elif (sievegrad.get() == "DBM - 37.5mm"):
        sievenum =8
    elif (sievegrad.get() == "DBM - 26.5mm"):
        sievenum =8
    elif (sievegrad.get() == "PQC - 31.5mm  (crushed)"):
        sievenum=9
    elif (sievegrad.get() == "PQC - 31.5mm (natural)"):
        sievenum=9
    elif (sievegrad.get() == "PQC - 26.5mm  (crushed)"):
        sievenum=9
    elif (sievegrad.get() == "PQC - 26.5mm (natural)"):
        sievenum=9
    elif (sievegrad.get() == "PQC - 19mm  (crushed)"):
        sievenum=9
    elif (sievegrad.get() == "PQC - 19mm (natural)"):
        sievenum = 9
    elif (sievegrad.get() == "DLC"):
        sievenum =9
    elif (sievegrad.get() == "WMM"):
        sievenum = 8

    # sieve_entries = []
    sieve_size=[]                               ##built text boxes for sieves
    y1=233
    temp=0
    for i in range(sievenum):
        entry_1 = Entry(
            window,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=147.0,
            y=y1,
            width=101.0,
            height=22.0
        )
        entry_1.insert(0, sieve_entries[temp].get())
        entry_1.configure(state="disabled")
        temp+=1
        entry_2 = Entry(
            window,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_2.place(
            x=256.0,
            y=y1,
            width=101.0,
            height=22.0
        )

        entry_2.insert(0, sieve_entries[temp].get())
        entry_2.configure(state="disabled")
        temp += 1
        y1+=30

    array=[]
    ssize=[]
    if (sievegrad.get() == "BC - 19mm"):
        array=[100,100,90,100,59,79,52,72,35,55,28,44,20,34,15,27,10,20,5,13,2,8]
        ssize=[26.5,19,13.2,9.5,4.75,2.36,1.18,0.6,0.3,0.15,0.075]
    elif (sievegrad.get() == "BC - 13.2mm"):
        array=[100,100,90,100,70,88,53,71,42,58,34,48,26,38,18,28,12,20,4,10]
        ssize=[19,13.2,9.5,4.75,2.36,1.18,0.6,0.3,0.15,0.075]
    elif (sievegrad.get() == "SMA - 13mm"):
        array=[100,100,90,100,50,75,20,28,16,24,13,21,12,18,10,20,8,12]
        ssize=[19,13.2,9.5,4.75,2.36,1.18,0.600,0.300,0.075]
    elif(sievegrad.get() == "SMA - 19mm"):
        array=[100,100,90,100,45,70,25,60,20,28,16,24,13,21,12,18,10,20,8,12]
        ssize=[26.5,19,13.2,9.5,4.75,2.36,1.18,0.600,0.300,0.075]
    elif(sievegrad.get() == "DBM - 37.5mm"):
        array=[100,100,95,100,63,93,55,75,38,54,28,42,7,21,2,8]
        ssize=[45,37.5,26.5,13.2,4.75,2.36,0.3,0.075]
    elif(sievegrad.get() == "DBM - 26.5mm"):
        array=[100,100,90,100,71,95,56,80,38,54,28,42,7,21,2,8]
        ssize=[37.5,26.5,19,13.2,4.75,2.36,0.3,0.075]
    elif (sievegrad.get() == "PQC - 31.5mm  (crushed)"):
        array=[100,100,90,100,85,95,68,88,45,65,30,55,8,30,0,10,0,5]
        ssize=[37.5,31.50,26.50,19.0,9.50,4.75,0.6,0.15,0.075]
    elif (sievegrad.get() =="PQC - 26.5mm  (crushed)"):
        array=[100,100,100,100,95,100,75,95,50,70,30,55,8,30,0,10,0,5]
        ssize = [37.5, 31.50, 26.50, 19.0, 9.50, 4.75, 0.6, 0.15, 0.075]
    elif (sievegrad.get() =="PQC - 19mm  (crushed)"):
        array=[100,100,100,100,100,100,90,100,48,78,30,58,8,35,0,12,0,5]
        ssize = [37.5, 31.50, 26.50, 19.0, 9.50, 4.75, 0.6, 0.15, 0.075]
    elif (sievegrad.get() == "PQC - 31.5mm (natural)"):
        array=[100,100,90,100,85,95,68,88,45,65,30,55,8,30,0,10,0,2]
        ssize = [37.5, 31.50, 26.50, 19.0, 9.50, 4.75, 0.6, 0.15, 0.075]
    elif (sievegrad.get() =="PQC - 26.5mm (natural)"):
        array=[100,100,100,100,95,100,75,95,50,70,30,55,8,30,0,10,0,2]
        ssize = [37.5, 31.50, 26.50, 19.0, 9.50, 4.75, 0.6, 0.15, 0.075]
    elif (sievegrad.get() =="PQC - 19mm (natural)"):
        array=[100,100,100,100,100,100,90,100,48,78,30,58,8,35,0,12,0,2]
        ssize = [37.5, 31.50, 26.50, 19.0, 9.50, 4.75, 0.6, 0.15, 0.075]
    elif(sievegrad.get() == "DLC"):
        array=[100,100,75,95,50,70,30,55,17,42,8,22,7,17,2,12,0,10]
        ssize=[26.5,19.00,9.50,4.75,2.36,0.6,0.3,0.15,0.075]
    elif (sievegrad.get() == "WMM"):
        array=[100,100,95,100,60,80,40,60,25,40,15,30,8,22,0,5]
        ssize=[53.00,45.00,22.40,11.20,4.75,2.36,0.6,0.075]





    if (sievegrad.get() == "BC - 19mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "BC - 13.2mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "SMA - 13mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif(sievegrad.get() == "SMA - 19mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif(sievegrad.get() == "DBM - 37.5mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif(sievegrad.get() == "DBM - 26.5mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "PQC - 31.5mm  (crushed)"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "PQC - 26.5mm  (crushed)"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "PQC - 19mm  (crushed)"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "PQC - 31.5mm (natural)"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "PQC - 26.5mm (natural)"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "PQC - 19mm (natural)"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif(sievegrad.get() == "DLC"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")
    elif (sievegrad.get() == "WMM"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
        for i in range(len(sieve_size)):
            sieve_size[i].insert(0,ssize[i])
            sieve_size[i].configure(state="disabled")








    #####SIEVE ENTRIES####

    #####Sieve labels#####
    y1=236.0
    for i in range(sievenum):
        canvas.create_text(
            79.0,
            y1,
            anchor="nw",
            text="Sieve"+str(i+1),
            fill="#273340",
            font=("OpenSansRoman Regular", 12 * -1)
        )
        y1+=30


    #####Sieve labels#####

    #####Stock Labels#####
    x1=377.0
    # print(numStocks.get())
    for i in range(numStocks.get()):
        canvas.create_rectangle(
            x1,
            190.0,
            x1+101,
            219.0,
            fill="#C1D6FF",
            outline="")

        canvas.create_text(
            x1+8,
            195.0,
            anchor="nw",
            text="StockPile "+str(i+1),
            fill="#273340",
            font=("OpenSansRoman SemiBold", 12 * -1)
        )
        x1 += 109
    #####Stock Labels#####

    #####Creating Entries#####

    temp=0
    x1 = 377
    # print(entries)
    # print(pan)
    # print(numSieves.get())
    data=convert(entries,numSieves.get(),pan)
    for i in range(numStocks.get()):
        y1 = 233
        for j in range(sievenum):
            entry_1 = Entry(
                window,
                bd=0,
                bg="#FFFFFF",
                highlightthickness=0
            )
            # entry_1.insert(0,0)

            entry_1.place(
                x=x1,
                y=y1,
                width=101.0,
                height=22.0
            )
            y1 += 30
            entry_1.insert(0, data[i][j])
            entry_1.configure(state="disabled")
            temp += 1

        x1 += 109


    #####Creating Entries#####


    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            mainroot.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.resizable(False, False)
    window.mainloop()