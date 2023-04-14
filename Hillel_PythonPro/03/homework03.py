import os
from pympler import asizeof
from sys import getsizeof


def get_data_dir_path():
    data_dir_path = os.path.abspath(os.getcwd() + '../../.data/')
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)
    return data_dir_path


def get_rockyou_file_path() -> str:
    data_dir_path = get_data_dir_path()
    rockyou_file_path = os.path.abspath(data_dir_path + '/rockyou.txt')
    if not os.path.exists(rockyou_file_path):
        print(f'To avoid tis message you can put put rockyou.txt file inside directory "{data_dir_path}"')
        rockyou_file_path = input("But now please set full path to 'rockyou' file: ")
        if not os.path.exists(rockyou_file_path):
            raise FileNotFoundError(rockyou_file_path)
    return rockyou_file_path


def get_result_file_path():
    return os.path.abspath(get_data_dir_path() + '/results.txt')


def find_in_file(file_path: str, word: str):
    with open(file=file_path, mode="r", encoding="utf-8", newline="\n") as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if word in line:
                yield line.rstrip("\n")


def main():
    rockyou_file_path = get_rockyou_file_path()
    results_file_path = get_result_file_path()

    word = ""
    while len(word) == 0:
        word = input('What find: ')
    print()

    founded_lines = 0
    with open(file=results_file_path, mode="w", encoding="utf-8", newline="\n") as file:
        for e in find_in_file(file_path=rockyou_file_path, word=word):
            file.write(e+"\n")
            founded_lines += 1

    print(f'Founded {founded_lines} lines')
    print(f'Results stored in file "{results_file_path}"')
    print(f'File size (on disk): {os.path.getsize(results_file_path)} bytes')

    print(f'sys.getsizeof   (file): {getsizeof(file)}')
    print(f'pympler.azizeof (file): {asizeof.asized(file)}')

    input('\nTo exit program press "Enter"')


if __name__ == "__main__":
    main()
