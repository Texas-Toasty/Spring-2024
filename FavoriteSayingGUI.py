import tkinter as tk


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Favorite Saying")
        self.main_window.geometry("300x125")
        self.main_window.configure(borderwidth=0)  # Remove outside border

        self.frame = tk.Frame(self.main_window)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, text="My favorite class is Python\nI'm always excited to learn!",
                              padx=5, pady=5, relief=tk.SOLID, borderwidth=1)
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
