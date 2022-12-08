from tools import *
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'integers', metavar='int', type=int,
         nargs=3, help='low high n_samples')

    args = parser.parse_args()
    
    low = args.integers[0]
    high = args.integers[1]
    n = args.integers[2]

    sample(low, high, n)
    print(f'Done sampling.')