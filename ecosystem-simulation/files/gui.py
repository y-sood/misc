import tkinter as tk
from tkinter import messagebox

class ConfigGUI:
    def __init__(self, root, submit_callback):
        self.root = root
        self.submit_callback = submit_callback

        #Creating frame to build upon
        self.frame = tk.Frame(root)
        self.frame.pack(side="bottom", fill="x")

        #Parameters with default value
        self.frames = self.create_entry("Refresh Rate", "1")
        self.counts = self.create_entry("Counts:", "5, 10, 15")
        self.velocityt = self.create_entry("Top bound of velocity:", "10, 10, 10")
        self.velocityb = self.create_entry("Bottom bound of velocity (Negative):", "10, 10, 10")
        self.lifespans = self.create_entry("Lifespans:", "60, 80, 100")
        self.rc = self.create_entry("Reproduction Cooldowns:", "10, 10, 6")
        self.ec = self.create_entry("Eating Cooldowns:", "2, 2, 0")
        self.lifegain = self.create_entry("Lifegain:", "5, 10, 5")
        self.stdtop = self.create_entry("Standard Deviation Top:", "0.75, 0.8, 0.5")
        self.stdbottom = self.create_entry("Standard Deviation Bottom:", "1.25, 1.2, 1.5")

        #Start button
        start_btn = tk.Button(self.frame, text="Start", command=self.submit)
        start_btn.pack()
        #Stop button
        stop_btn = tk.Button(self.frame, text="Stop", command=self.exiter)
        stop_btn.pack()
        
    #To create entry fields for parameters
    def create_entry(self, label_text, default_value):
        label = tk.Label(self.frame, text=label_text)
        label.pack(side="top", anchor="w")
        entry = tk.Entry(self.frame)
        entry.insert(0, default_value)
        entry.pack(side="top", anchor="w")
        return entry

    def exiter(self):
        if messagebox.askokcancel("Quit", "This will end simulation"):
            self.root.quit()

    def submit(self):
        #Use information collected from data fields to make dictionary
        config = {
            'frames' : int(self.frames.get()),
            'lifespans': [int(x) for x in self.lifespans.get().split(',')],
            'rc': [int(x) for x in self.rc.get().split(',')],
            'ec': [int(x) for x in self.ec.get().split(',')],
            'lifegain': [int(x) for x in self.lifegain.get().split(',')],
            'stdtop': [float(x) for x in self.stdtop.get().split(',')],
            'stdbottom': [float(x) for x in self.stdbottom.get().split(',')],
            'velocityt': [float(x) for x in self.velocityt.get().split(',')],
            'velocityb': [float(x) for x in self.velocityb.get().split(',')],
        }
        counts = [int(x) for x in self.counts.get().split(',')]
        #Callback to begin sim anew with dictionary
        self.submit_callback(config, counts)