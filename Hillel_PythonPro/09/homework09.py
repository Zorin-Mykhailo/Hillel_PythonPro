import os
from multiprocessing import Process
from threading import Thread, current_thread
from time import perf_counter

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f'Processing image from "{path}" in process "{os.getpid()}"')
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(f'Downloading image from "{image_url}" in thread "{current_thread().name}"')
    response = requests.get(image_url)

    file_name = os.path.abspath(os.getcwd() + "../../.data/image.jpg")
    with open(file_name, "wb") as img_file:
        img_file.write(response.content)


def main():
    print(f"Current thread:  {current_thread().name}")
    print(f"Current process: {os.getpid()}\n")
    try:
        # encrypt_file("rockyou.txt")
        # download_image("https://picsum.photos/1000/1000")
        #
        p = Process(target=encrypt_file, args=("rockyou.txt",))
        t = Thread(
            target=download_image,
            args=("https://picsum.photos/1000/1000",),
            name="Alternate_thread",
        )

        start_time = perf_counter()
        p.start()
        t.start()

        t.join()
        download_counter = perf_counter() - start_time
        p.join()
        encryption_counter = perf_counter() - start_time
        total_counter = perf_counter() - start_time

        print(
            f"\nTime taken for encryption task: {encryption_counter:00.2f}, I/O-bound task: {download_counter:00.2f}, Total: {total_counter:00.2f} seconds"
        )
    except Exception as e:
        print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()
