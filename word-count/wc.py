import os
import cmd
import sys
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("l")
args = parser.parse_args()
print(args.l)
def count_words(file_path):
    count = 0
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            for word in words:
                if not word.isnumeric():
                    count += 1
        return count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = count_words(file_path)
    if result is not None:
        print(f"{result} {file_path}")
