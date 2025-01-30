import os
import platform
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.withdraw()  # Hide the root window

CLEAR_COMMAND = "cls" if platform.system() == "Windows" else "clear"
"""
The clear screen command determined by the operating system.
"""

try:
    os.system(CLEAR_COMMAND)
    # Step 1: Find the image.
    image = filedialog.askopenfile("C:\\Users\\adnan\\Pictures")
except Exception as e:
    print(e)
finally:
    input("Press any key to exit the program.")
