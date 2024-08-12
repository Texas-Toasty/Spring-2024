import tkinter as tk


class MaintenanceApp:
    def __init__(self, master):
        self.check_buttons = None
        self.master = master
        master.title("Joe's Automotive")

        self.total_charges = tk.StringVar()
        self.total_charges.set("Total Charges: $0.00")

        self.oil_change_var = tk.IntVar()
        self.lube_job_var = tk.IntVar()
        self.radiator_flush_var = tk.IntVar()
        self.transmission_fluid_var = tk.IntVar()
        self.inspection_var = tk.IntVar()
        self.muffler_replacement_var = tk.IntVar()
        self.tire_rotation_var = tk.IntVar()

        self.calculate_button = tk.Button(self.master, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=8, column=0, sticky="w")

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=8, column=1, sticky="w")

        self.total_label = tk.Label(self.master, textvariable=self.total_charges)
        self.total_label.grid(row=7, column=0, sticky="w")

        self.create_widgets()

    def create_widgets(self):
        self.check_buttons = []

        oil_change_cb = tk.Checkbutton(self.master, text="Oil Change - $30.00", variable=self.oil_change_var)
        oil_change_cb.grid(row=0, column=0, sticky="w")
        self.check_buttons.append(oil_change_cb)

        lube_job_cb = tk.Checkbutton(self.master, text="Lube Job - $20.00", variable=self.lube_job_var)
        lube_job_cb.grid(row=1, column=0, sticky="w")
        self.check_buttons.append(lube_job_cb)

        radiator_flush_cb = tk.Checkbutton(self.master, text="Radiator Flush - $40.00",
                                           variable=self.radiator_flush_var)
        radiator_flush_cb.grid(row=2, column=0, sticky="w")
        self.check_buttons.append(radiator_flush_cb)

        transmission_fluid_cb = tk.Checkbutton(self.master, text="Transmission Fluid - $100.00",
                                               variable=self.transmission_fluid_var)
        transmission_fluid_cb.grid(row=3, column=0, sticky="w")
        self.check_buttons.append(transmission_fluid_cb)

        inspection_cb = tk.Checkbutton(self.master, text="Inspection - $35.00", variable=self.inspection_var)
        inspection_cb.grid(row=4, column=0, sticky="w")
        self.check_buttons.append(inspection_cb)

        muffler_replacement_cb = tk.Checkbutton(self.master, text="Muffler Replacement - $200.00",
                                                variable=self.muffler_replacement_var)
        muffler_replacement_cb.grid(row=5, column=0, sticky="w")
        self.check_buttons.append(muffler_replacement_cb)

        tire_rotation_cb = tk.Checkbutton(self.master, text="Tire Rotation - $20.00", variable=self.tire_rotation_var)
        tire_rotation_cb.grid(row=6, column=0, sticky="w")
        self.check_buttons.append(tire_rotation_cb)

    def calculate_total(self):
        total = 0
        if self.oil_change_var.get():
            total += 30
        if self.lube_job_var.get():
            total += 20
        if self.radiator_flush_var.get():
            total += 40
        if self.transmission_fluid_var.get():
            total += 100
        if self.inspection_var.get():
            total += 35
        if self.muffler_replacement_var.get():
            total += 200
        if self.tire_rotation_var.get():
            total += 20

        self.total_charges.set("Total Charges: $" + "{:.2f}".format(total))


root = tk.Tk()
app = MaintenanceApp(root)
root.mainloop()
