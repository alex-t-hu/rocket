from tools import *
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'floats', metavar='float', type=float,
         nargs=8, help='2x4 values specifying chord span sweep tip for sustainer + booster')

    args = parser.parse_args()
    
    sustainer = args.floats[:4]
    booster = args.floats[4:]
    
    sustainer = {'Chord': sustainer[0], 'Span': sustainer[1], 'SweepDistance': sustainer[2] , 'TipChord': sustainer[3]}
    booster = {'Chord': booster[0], 'Span': booster[1], 'SweepDistance': booster[2] , 'TipChord': booster[3]}
    fname = f"samples/new_{''.join([str(x) for x in args.floats])}"
    generateNewDesign(booster, sustainer, fname)
    print(f'Done generating file {fname}.')