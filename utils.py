import sys
python_version = sys.version_info[0]


def print_(str):
    if python_version < 3:
        print str
    else:
        print(str)

