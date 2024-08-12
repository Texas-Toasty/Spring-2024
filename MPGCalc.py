import tkinter as tk


class MPG:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('MPG Calculator')

        self.top_frame = tk.Frame(self.main_window, padx=10, pady=10)
        self.bottom_frame = tk.Frame(self.main_window, padx=10, pady=10)

        self.miles_label = tk.Label(self.top_frame, text='Miles per Tank:')
        self.miles_label.grid(row=0, column=0, padx=5, pady=5)

        self.miles_entry = tk.Entry(self.top_frame)
        self.miles_entry.grid(row=0, column=1, padx=5, pady=5)

        self.gallons_label = tk.Label(self.top_frame, text='Gallons per Tank:')
        self.gallons_label.grid(row=1, column=0, padx=5, pady=5)

        self.gallons_entry = tk.Entry(self.top_frame)
        self.gallons_entry.grid(row=1, column=1, padx=5, pady=5)

        self.final_miles_label = tk.Label(self.bottom_frame, text='Miles per Gallon:')
        self.final_miles_label.grid(row=0, column=0, padx=5, pady=5)

        self.calc_button = tk.Button(self.bottom_frame, text='Calculate MPG', command=self.calculate_mpg)
        self.calc_button.grid(row=1, column=0, padx=5, pady=5)

        self.result_label = tk.Label(self.bottom_frame, text='', state='disabled')
        self.result_label.grid(row=0, column=1, padx=5, pady=5)

        self.exit_button = tk.Button(self.bottom_frame, text='Exit', command=self.main_window.destroy)
        self.exit_button.grid(row=1, column=1, padx=5, pady=5)

        self.top_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def calculate_mpg(self):
        miles = float(self.miles_entry.get())
        gallons = float(self.gallons_entry.get())
        miles_per_gallon = miles / gallons
        self.result_label.config(text=f'{miles_per_gallon:.2f}')


if __name__ == '__main__':
    mpg = MPG()
