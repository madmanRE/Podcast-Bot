from pytube import YouTube
import os
import random
import time


def download_audio(link):
    milliseconds = int(round(time.time()))
    try:
        yt = YouTube(link)
        name = f"file_{milliseconds}.mp3"
        yt.streams.filter(only_audio=True).first().download(filename=name)
        return name
    except Exception as e:
        print(f"Возникла ошибка {e}")
