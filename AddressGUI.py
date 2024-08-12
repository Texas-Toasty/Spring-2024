import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("190x100")
        self.main_window.title("Address GUI")

        self.info_frame = tkinter.Frame(self.main_window)
        self.info_frame.pack(fill=tkinter.BOTH, expand=True)

        # Pack the frame in the center
        self.info_frame.place()

        self.address_label = tkinter.Label(self.main_window, text="",
                                           padx=15, pady=15, relief=tkinter.SOLID, borderwidth=1)
        self.address_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.address_label.pack()

        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.quit)
        self.quit_button.pack(side=tkinter.RIGHT)

        self.show_info_button = tkinter.Button(self.main_window, text="Show Info", command=self.show_info)
        self.show_info_button.pack(side=tkinter.LEFT)

        tkinter.mainloop()

    def show_info(self):
        address = "Reece Parry\n 24307 Panama Avenue\n Elko, MN 55020 "
        self.address_label.config(text=address)


if __name__ == "__main__":
    my_gui = MyGUI()
