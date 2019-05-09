import sys
from brute_hs256 import brute_from_file_with_key, print_bruted


if __name__ == '__main__':
    if len(sys.argv) == 3:
        bruted = brute_from_file_with_key(sys.argv[1], sys.argv[2], True)
        print_bruted(bruted)
