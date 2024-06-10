import subprocess
import tkinter

from tkinter import filedialog
from moviepy.editor import VideoFileClip


def read_video_data():
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    folder_path = filedialog.askopenfile().name
    video_data = VideoFileClip(folder_path)
    return video_data
    
read_video_data()