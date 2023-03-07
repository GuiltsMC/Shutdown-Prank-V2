# This is for education purposes only. Do not use or modify code to damage another user, even a "harmless" prank can lead to something terrible happening.
import tkinter as tk
import os
from tkinter import messagebox

#Creating the Tkinter window

root = tk.Tk()
root.withdraw()


# The actual pop up message

messagebox.showinfo("Not really though, your friend is messing with you.", "You have been hacked. Lol. Also your computer is gonna shut down, code has already been executed.  ")
os.system("shutdown /s /t 10")
#Running an event loop so the window does not close upon activation.
root.mainloop()