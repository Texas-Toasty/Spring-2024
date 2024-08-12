import tkinter
import tkinter.messagebox


class Test:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="William")
        self.label2 = tkinter.Label(self.top_frame, text="Franklin")
        self.label3 = tkinter.Label(self.top_frame, text="Roosevelt")

        self.label4 = tkinter.Label(self.bottom_frame, text="William")
        self.label5 = tkinter.Label(self.bottom_frame, text="Franklin")
        self.label6 = tkinter.Label(self.bottom_frame, text="Roosevelt")

        self.mybutton = tkinter.Button(self.main_window, text="Yo", command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, textvariable=self.value)
        self.address_button = tkinter.Button(self.bottom_frame, text="Show Info", command=self.show_info)

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")
        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.mybutton.pack()
        self.quit_button.pack()
        self.address_label.pack()
        self.address_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Name", "Thanks")

    def show_info(self):
        self.value.set("Jameson James \n Gregory games \n Minnesota")


if __name__ == "__main__":
    test = Test()
###############################################################
import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.button1 = tkinter.Radiobutton(self.top_frame, text='option 1', variable=self.radio_var, value=1)
        self.button2 = tkinter.Radiobutton(self.top_frame, text='option 2', variable=self.radio_var, value=2)
        self.button3 = tkinter.Radiobutton(self.top_frame, text='option 3', variable=self.radio_var, value=3)

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You selected option ' + str(self.radio_var.get()))


if __name__ == '__main__':
    my_gui = MyGUI()
#####################################################
import tkinter


class ListBox:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.listbox = tkinter.Listbox(self.main_window)
        self.listbox.pack(padx=10, pady=10)

        self.listbox.insert(0, 'Monday')
        self.listbox.insert(1, 'Tuesday')
        self.listbox.insert(2, 'Wednesday')
        self.listbox.insert(3, 'Thursday')
        self.listbox.insert(4, 'Friday')
        self.listbox.insert(5, 'Saturday')
        self.listbox.insert(6, 'Sunday')

        tkinter.mainloop()


if __name__ == '__main__':
    listbox = ListBox()
#####################################################
