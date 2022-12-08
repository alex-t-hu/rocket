import numpy as np
import argparse
import pickle

def weight(chord, span, sweep, tip):
    t = 0.25
    p = 0.0975 #( lbs / in^3)
    A = span * (chord + sweep) / 2
    return p * t * A
def totalWeight(chord, span, sweep, tip):
    return 4 * weight(chord, span, sweep, tip)

TEMPLATE = 'template.CDX1'
SUSTAINER_BASE_WT = 22.66 # Verify later
BOOSTER_BASE_WT = 62.75
def createNewDesign(booster, sustainer, sustainer_weight, booster_weight):
    '''
    Create new design with booster & sustainer = {'Chord': -, 'Span': -, ...} and specified weight.
    '''
    with open(TEMPLATE) as f:
        file = f.readlines()
    SUSTAINERIDX = 42
    BOOSTERIDX = 80

    map_ = {'Chord': 2, 'Span': 3, 'SweepDistance': 4, 'TipChord': 5}
    indent = file[SUSTAINERIDX+1].split('<')[0]
    for x in map_:
        file[map_[x] + SUSTAINERIDX] = (f"{indent}<{x}>{sustainer[x]}</{x}>\n")
        file[map_[x] + BOOSTERIDX] = (f"{indent}<{x}>{booster[x]}</{x}>\n")
    
    SUSTAINERWT = 131
    BOOSTERWT = 136
    
    wt_indent = file[SUSTAINERWT].split('<')[0]
    file[SUSTAINERWT] = f"{wt_indent}<SustainerLaunchWt>{sustainer_weight}</SustainerLaunchWt>\n"
    file[BOOSTERWT] = f"{wt_indent}<Booster1LaunchWt>{booster_weight}</Booster1LaunchWt>\n"
    
    return file

def generateNewDesign(booster, sustainer, fname):
    booster_weight = BOOSTER_BASE_WT + totalWeight(booster['Chord'], booster['Span'], booster['SweepDistance'], 
                                                      booster['TipChord'])
    
    sustainer_weight = SUSTAINER_BASE_WT + totalWeight(sustainer['Chord'], sustainer['Span'], sustainer['SweepDistance'], 
                                                      sustainer['TipChord'])
    file = createNewDesign(booster, sustainer, sustainer_weight, booster_weight)
    with open(fname, 'w') as f:
        f.write(''.join(file))

def sample(low, high, num):
    samples = {}
    for i in range(num):        
        sustainer = {'Chord': np.random.uniform(low = low, high = high),
                     'Span': np.random.uniform(low = low, high = high),
                     'SweepDistance': np.random.uniform(low = low, high = high),
                     'TipChord': np.random.uniform(low = low, high = high)}
        
        booster = {'Chord': np.random.uniform(low = low, high = high),
                     'Span': np.random.uniform(low = low, high = high),
                     'SweepDistance': np.random.uniform(low = low, high = high),
                     'TipChord': np.random.uniform(low = low, high = high)}

        samples[i] = {'S': sustainer, 'B': booster}
        generateNewDesign(booster, sustainer, f"samples/sample_{i}.CDX1")
    
    f = open('sample_list.pkl', 'wb')
    pickle.dump(samples, f)
    f.close()


