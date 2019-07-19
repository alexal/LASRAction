import argparse
import io
import os
import sys


def check_installation(version):
    current_version = sys.version_info
    if current_version[0] == version[0] and current_version[1] >= version[1]:
        pass
    else:
        sys.stderr.write(
            "[%s] - Error: Your Python interpreter must be %d.%d or greater (within major version %d)\n" % (
                sys.argv[0], version[0], version[1], version[0]))
        sys.exit(-1)
    return 0


check_installation((3, 0))

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
                    
                    try:
                        if attr[0] == 'ID' and int(attr[1]) == args.id:
                            print_line = True
                        elif attr[0] == 'ID' and int(attr[1]) != args.id:
                            print_line = False
                    except:
                        pass

                if print_line:
                    print(line, end='')


if __name__ == '__main__':
    main()