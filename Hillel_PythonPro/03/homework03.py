import os

FILE_PATH = "rockyou.txt"


def find_in_file(file_path: str, look_for: str):
    with open(file=file_path, mode="r", encoding="utf-8", newline="\n") as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if look_for in line:
                yield line.rstrip("\n")


def main():
    os.chdir("../.data/")

    items_amount = 0
    for e in find_in_file(file_path=FILE_PATH, look_for=""):
        print(e)
        items_amount += 1

    print(f"Total items: {items_amount}")


if __name__ == "__main__":
    main()
