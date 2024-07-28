import requests
import threading

files = []


def download_file(src, dst):
    print(f"Starting download of {dst}")
    response = requests.get(src)
    with open(dst, 'wb') as file:
        file.write(response.content)
    print(f"Finished download of {dst}")


for src, dst in files:
    thread = threading.Thread(
        target=download_file,
        args=(src, dst)
    )
    thread.start()
