import time
import tkinter as tk
from tkinter import simpledialog
import numpy as np
import qt5062
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Application")

        # Bind the function to the window destroy event
        self.root.bind("<Destroy>", self.on_window_destroy)
        self.destroy_flag = False
        # Bind the function to the window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_window_close)

        # Set the window size as a percentage of the screen resolution
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        self.window_width_percentage = 25
        self.window_height_percentage = 25

        self.window_width = int((self.window_width_percentage / 100) * self.screen_width)
        self.window_height = int((self.window_height_percentage / 100) * self.screen_height)

        # Set the window size
        self.root.geometry(f"{self.window_width}x{self.window_height}")

        self.window2 = False
        self.stabilizing_time = 2e-3
        self.microstep_size = 10
        self.microsteps = np.arange(0, 60e3 + self.microstep_size, self.microstep_size, dtype = int)
        self.global_step = 0
        self.current_steps = [0, 0, 0]
        self.output = {}
        self.output['step'] = []
        self.output['step0'] = []
        self.output['step1'] = []
        self.output['step2'] = []
        self.output['diode0'] = []
        self.output['diode1'] = []
        self.output['diode2'] = []
        self.output['action'] = []
        self.output['time'] = []
        self.pid_dict = {}
        self.pid_dict['setpoints'] = [0, 0, 0]
        self.pid_dict['pid_sign'] = [1, 1, 1] #used to invert the sign of all pid parameters
        self.pid_dict['error'] = [0, 0, 0]
        self.pid_dict['previous_error'] = [0, 0, 0]
        self.pid_dict['coefs'] = [5e-3, 5e-3, 0e-3] #kp, ki, kd


        self.lasers = qt5062.LaserController()
        for i in range(3):
            self.lasers.set_laser(i, qt5062.LaserController.LASER_660)

        # Variables for input boxes
        self.input_var1 = tk.StringVar()
        self.input_var2 = tk.StringVar()
        self.input_var3 = tk.StringVar()
        self.input_var4 = tk.StringVar()

        # Create and place input boxes and labels
        self.label1 = tk.Label(root, text="Starting value")
        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry1 = tk.Entry(root, textvariable=self.input_var1)
        self.entry1.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.label2 = tk.Label(root, text="Ending value")
        self.label2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry2 = tk.Entry(root, textvariable=self.input_var2)
        self.entry2.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.label3 = tk.Label(root, text="Number of steps")
        self.label3.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry3 = tk.Entry(root, textvariable=self.input_var3)
        self.entry3.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)


        # Button to change layout
        self.fpi_stepper_button = tk.Button(root, text="Initiate FPI", command=self.fpi_stepper_window)
        self.fpi_stepper_button.grid(row=3, column=0, columnspan=2, pady=10)

        for i in range(2):
            self.root.columnconfigure(i, weight=1)
        for i in range(4):
            self.root.rowconfigure(i, weight=1)


    def fpi_stepper_window(self):
        self.window2 = True
        self.step_idx = 0
        self.step_start = int(self.entry1.get())
        self.step_end = int(self.entry2.get())
        self.n_steps = int(self.entry3.get())
        self.steps = np.linspace(self.step_start, self.step_end, self.n_steps+1)


        # Remove input boxes and labels
        self.label1.grid_remove()
        self.entry1.grid_remove()
        self.label2.grid_remove()
        self.entry2.grid_remove()
        self.label3.grid_remove()
        self.entry3.grid_remove()
        self.fpi_stepper_button.grid_remove()

        # Add new labels and buttons
        self.new_label1_text = tk.StringVar()
        self.new_label1_text.set(f"Current value: {self.steps[self.step_idx]}")
        self.new_label1 = tk.Label(self.root, textvariable = self.new_label1_text)
        self.new_label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.dummy_button1 = tk.Button(self.root, text="Next step", command=self.next_step)
        self.dummy_button1.grid(row=1, column=0, columnspan=1, pady=10)

        self.dummy_button2 = tk.Button(self.root, text="Previous step", command=self.previous_step)
        self.dummy_button2.grid(row=1, column=1, columnspan=1, pady=10)

        self.dummy_button3 = tk.Button(self.root, text="Go to first step", command=self.to_first_step)
        self.dummy_button3.grid(row=2, column=0, columnspan=1, pady=10)

        self.dummy_button4 = tk.Button(self.root, text="Go to last step", command=self.to_last_step)
        self.dummy_button4.grid(row=2, column=1, columnspan=1, pady=10)

        self.dummy_button5 = tk.Button(self.root, text="Close FPI", command=self.close_fpi)
        self.dummy_button5.grid(row=3, column=0, columnspan=1, pady=10)

        self.dummy_button6 = tk.Button(self.root, text="Completely open FPI", command=self.open_fpi)
        self.dummy_button6.grid(row=3, column=1, columnspan=1, pady=10)

        self.dummy_button7 = tk.Button(self.root, text="Save data and close application", command=self.on_window_close)
        self.dummy_button7.grid(row=4, column=0, columnspan=2, pady=10)

        self.time0 = time.time()
        self.to_first_step()
        self.hold()

    def write_output(self):
        self.output['diode0'][-1].append(self.lasers.read_adc(0))
        self.output['diode1'][-1].append(self.lasers.read_adc(1))
        self.output['diode2'][-1].append(self.lasers.read_adc(2))
        self.output['step'][-1].append(self.global_step)
        self.output['step0'][-1].append(self.current_steps[0])
        self.output['step1'][-1].append(self.current_steps[1])
        self.output['step2'][-1].append(self.current_steps[2])
        self.output['time'][-1].append(time.time() - self.time0)
        
    def append_new_output(self):
        self.output['step'].append([])
        self.output['step0'].append([])
        self.output['step1'].append([])
        self.output['step2'].append([])
        self.output['diode0'].append([])
        self.output['diode1'].append([])
        self.output['diode2'].append([])
        self.output['time'].append([])
        
    def step2step(self, start_step, end_step):
        if start_step <= end_step:
            return np.arange(start_step, end_step + self.microstep_size, self.microstep_size, dtype = int)
        else:
            return np.flip(np.arange(end_step + self.microstep_size, start_step, self.microstep_size, dtype = int))

    def move_all(self, end_step):
        steps0 = self.step2step(self.current_steps[0], end_step)
        steps1 = self.step2step(self.current_steps[1], end_step)
        steps2 = self.step2step(self.current_steps[2], end_step)
        for i in range(max([len(steps0), len(steps1), len(steps2)])):
            if i < len(steps0):
                self.lasers.write_dac(0, steps0[i])
                self.current_steps[0] = steps0[i]
            if i < len(steps1):
                self.lasers.write_dac(1, steps1[i])
                self.current_steps[1] = steps1[i]
            if i < len(steps2):
                self.lasers.write_dac(2, steps2[i])
                self.current_steps[2] = steps2[i]
            self.write_output()
            time.sleep(self.stabilizing_time)
    def next_step(self):
        self.holding = False
        if self.global_step < self.steps[-1]:
            self.append_new_output()
            self.output['action'].append('Stepping up')
            self.move_all(self.steps[self.step_idx+1])
            self.global_step = self.steps[self.step_idx+1]
            self.step_idx += 1
            self.new_label1_text.set(f"Current value: {self.global_step}")
        else:
            print("You are already at the last step")
        self.holding = True

    def previous_step(self):
        self.holding = False
        if self.global_step > self.steps[0]:
            self.append_new_output()
            self.output['action'].append('Stepping down')
            self.move_all(self.steps[self.step_idx - 1])
            self.global_step = self.steps[self.step_idx + 1]
            self.step_idx -= 1
            self.new_label1_text.set(f"Current value: {self.global_step}")
        else:
            print("You are already at the first step")
        self.holding = True

    def close_fpi(self):
        self.holding = False
        if self.global_step > 0:
            self.append_new_output()
            self.output['action'].append('Closing FPI')
            print('Resetting')
            self.move_all(0)
            self.global_step = 0
            self.step_idx = 0
            if self.window2 == True:
                self.new_label1_text.set(f"Current value: {self.global_step}")
        else:
            print("FPI is already closed")
        self.holding = True

    def open_fpi(self):
        self.holding = False
        if self.global_step < self.microsteps[-1]:
            print('Opening completely')
            self.append_new_output()
            self.output['action'].append('Opening FPI')
            self.move_all(self.steps[-1])
            self.global_step = self.steps[-1]
            self.step_idx = self.n_steps
            self.new_label1_text.set(f"Current value: {self.global_step}")
        else:
            print("FPI is already open")
        self.holding = True

    def to_first_step(self):
        self.holding = False
        print('Going to first step')
        if self.global_step != self.steps[0]:
            self.append_new_output()
            self.output['action'].append('Going to first')
            self.move_all(self.steps[0])
            self.global_step = self.steps[0]
        else:
            self.append_new_output()
            self.output['action'].append('Holding')
        self.step_idx = 0
        self.new_label1_text.set(f"Current value: {self.global_step}")
        self.holding = True

    def to_last_step(self):
        self.holding = False
        print('Going to last step')
        if self.global_step != self.steps[-1]:
            self.move_all(self.steps[-1])
            self.global_step = self.steps[-1]
        self.step_idx = self.n_steps
        self.new_label1_text.set(f"Current value: {self.global_step}")
        self.holding = True

    def maintain_distance(self):
        self.holding = False
        states = [self.output['diode0'][-1][-1], self.output['diode1'][-1][-1], self.output['diode2'][-1][-1]]
        pid_scores = [0, 0, 0]
        for i in range(3):
            self.pid_dict['error'][i] = states[i] - self.pid_dict['setpoints'][i]
            pid_scores[i] = self.pid(kp=self.pid_dict['coefs'][0], ki=self.pid_dict['coefs'][1], kd=self.pid_dict['coefs'][2],
                                     error=self.pid_dict['error'][i], previous_error=self.pid_dict['previous_error'][i],
                                     pid_sign=self.pid_dict['pid_sign'][i])
            self.pid_dict['previous_error'][i] = self.pid_dict['error'][i]

        max_step = self.global_step + 10 * self.microstep_size
        # min_step = self.global_step - 10 * self.microstep_size

        for i in range(3):
            if self.current_steps[i] - 5*self.microstep_size > 0 and self.current_steps[i] + 5*self.microstep_size <= self.microsteps[-1]:
                if abs(pid_scores[i]) < 5*self.microstep_size: #Maximum correction at a time is 5 micro steps
                    if self.current_steps[i] + pid_scores[i] < max_step:
                        self.current_steps[i] += int(pid_scores[i])
                    else:
                        self.pid_dict['pid_sign'][i] *= -1
                else:
                    if self.current_steps[i] + np.sign(pid_scores[i])*5*self.microstep_size < max_step:
                        self.current_steps[i] += int(np.sign(pid_scores[i])*5*self.microstep_size)
                    else:
                        self.pid_dict['pid_sign'][i] *= -1
        for i in range(3):
            self.lasers.write_dac(i, self.current_steps[i])

        self.write_output()

        print(f"target0: {self.pid_dict['setpoints'][0]}, current: {states[0]}, PID: {pid_scores[0]}\n"
              f"target1: {self.pid_dict['setpoints'][1]}, current: {states[1]}, PID: {pid_scores[1]}\n"
              f"target2: {self.pid_dict['setpoints'][2]}, current: {states[2]}, PID: {pid_scores[2]}")
        self.holding = True

    def pid(self, kp, ki, kd, error, previous_error, pid_sign):
        p = error * kp * pid_sign
        i = (min(error, previous_error) + abs(error - previous_error) * 0.5) * ki * pid_sign
        d = (error - previous_error) * kd * pid_sign
        return p + i + d

    def hold(self):
        if self.holding == True:
            if self.output['action'][-1] != 'Holding' and len(self.output['diode0'][-1]) > 0:
                self.hold_counter = 0
                self.pid_dict['setpoints'] = [self.output['diode0'][-1][-1], self.output['diode1'][-1][-1], self.output['diode2'][-1][-1]]
                self.append_new_output()
                self.output['action'].append('Holding')

            self.write_output()
            self.hold_counter += 1
            if self.hold_counter >= 10 and len(self.output['diode0']) > 1:
                self.maintain_distance()
                self.hold_counter = 0

            self.root.after(5, self.hold)

    def on_window_destroy(self, event):
        # This function will be called when the window is being destroyed
        self.destroy_flag = True

    def on_window_close(self):
        # This function will be called when the window is closed
        if not self.destroy_flag:
            print('Resetting FPI')
            self.close_fpi()
            for i in range(3):
                self.lasers.set_laser(i, qt5062.LaserController.LASER_OFF)

            # Create a popup box to prompt the user for a string
            file_name = simpledialog.askstring("Save putput file", "File name")

            # Check if the user pressed OK or Cancel
            if file_name != "" and file_name is not None:
                # open file for writing
                if not file_name.endswith(".txt"):
                    file_name = file_name + ".txt"
                f = open(f"{file_name}", "w")
                # write file
                f.write(str(self.output))
                # close file
                f.close()
                print(f"File saved as: {file_name}")
            else:
                print("File not saved")

            self.root.quit()
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
