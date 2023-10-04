import tkinter
from pytube import YouTube
import os
from pathlib import Path
import threading
from tkinter import ttk, messagebox
from multiprocessing import Process

def d_task():
    link = youtube_link.get()
    youtube_link.delete('0', 'end')

    p1 = Process(target=download,args=[link])
    p1.run()
def download(link):
    w2 = tkinter.Tk()
    w2.title("Downloading...")

    progress_bar = ttk.Progressbar(w2, length=200, mode="determinate")
    progress_bar.pack()

    def downloading_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = int(bytes_downloaded / total_size * 100)
        progress_bar['value'] = percentage_of_completion





    def kaam(link):


        try:
            url = YouTube(link)
            url.register_on_progress_callback(downloading_progress)

            video = url.streams.get_highest_resolution()


            path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

            video.download(path_to_download_folder)
            progress_bar['value'] = 100
            w2.destroy()
        except:
            messagebox.showerror(title="Error",message="Invalid Url")
            w2.destroy()
        finally:
            exit()





    t2 = threading.Thread(target=kaam,args=[link])
    t2.start()
    w2.mainloop()






window = tkinter.Tk()
window.geometry("500x200")
window.title("YouTube Downloader")
window.resizable()
youtube_link = tkinter.Entry(window)
youtube_link.config(width=50)
youtube_link.pack()
button = tkinter.Button(window,command=d_task, text="Download")
button.config(height=2, width=10)
button.pack()



window.mainloop()
