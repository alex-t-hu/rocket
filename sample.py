from tools import *
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'integers', metavar='int', type=int,
         nargs=4, help='low high n_samples prefix')

    args = parser.parse_args()
    
    low = args.integers[0]
    high = args.integers[1]
    n = args.integers[2]
    prefix = args.integers[3]

    sample(low, high, n, prefix)
    print(f'Done sampling.')