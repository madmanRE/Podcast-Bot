import schedule
import time
import os

FILES = [
    file
    for file in os.listdir()
    if file != "__pycache__" and file.split(".")[1] == "mp3"
]


def check_files():
    print("start checking...")
    print(FILES)
    for file in FILES:
        print(file)
        milliseconds = int(round(time.time()))
        file_creation_time = int(file.split("_")[1].split(".")[0])
        print(milliseconds - file_creation_time)
        if milliseconds - file_creation_time > 100:
            print(f"{file} is deleted")
            os.remove(file)
            FILES.remove(file)


schedule.every(60).minutes.do(check_files)


while True:
    schedule.run_pending()
