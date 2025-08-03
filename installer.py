import time as tm
import tkinter as tk
from tkinter import filedialog, messagebox
def select_folder():
    folder_path = filedialog.askdirectory(
        title="选择文件夹",
        initialdir="/",
    )
    if not folder_path:
            select_folder()
    else:
        return folder_path
