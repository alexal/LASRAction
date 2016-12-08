import argparse
import io
import os
import sys

if sys.version_info[0] < 3:
    print("Error: Your Python interpreter must be version 3 or greater")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="")
parser.add_argument("id", type=int, help="")
args = parser.parse_args()


def main():
    print_line = False

    if os.path.isfile(args.file):
        with io.open(args.file, encoding='utf-8-sig', errors='ignore') as f:
            for line in f:
                for item in line.split(','):
                    attr = item.split('=')

                    if attr[0] == 'ID' and int(attr[1]) == args.id:
                        print_line = True
                    elif attr[0] == 'ID' and int(attr[1]) != args.id:
                        print_line = False

                if print_line:
                    print(line, end='')


if __name__ == '__main__':
    main()
