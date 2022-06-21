import math
import numpy as np
import re

DEBUG = False
################### FUNCTIONS ###################

def symmetryWrtX(arr):
    if len(arr) != 2:
        raise Exception("List must be dim 2")
    try:
        arr = [float(item) for item in arr]
    except:
        raise Exception("Elements must be float")
    else: return [arr[0], -1*arr[1]]

# https://iq.opengenus.org/norm-method-of-numpy-in-python/
def norm(arr):
    # arr = np.array(arr)
    return np.linalg.norm(arr, 2) # "Euclidian Norm"

def multiplyList(arr):
    res = 1
    for i in arr:
        res = res * i
    return res

def calcDiagonal(a, b, angleBtwn):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(angleBtwn)))

def calcScalingFactor(n):
    if n <= 3:
        return 1
    
    externalAngle = 360/n; internalAngle = 180 - externalAngle; 
    oneSegmentAngle = 360/n/2
    diaonals = []
    diagLength = 1
    currAngle = internalAngle
    if n % 2 == 0: # even number of sides
        for i in range(int((n/2) - 2)):
            diagLength = calcDiagonal(1, diagLength, currAngle)
            diaonals.append(diagLength)
            diaonals.append(diagLength)
            currAngle = currAngle - oneSegmentAngle
        diagLength = calcDiagonal(1, diagLength, currAngle)
        diaonals.append(diagLength)
        currAngle = currAngle - oneSegmentAngle
    elif n % 2 == 1: # odd number of sides
        for i in range(int((n-3)/2)):
            diagLength = calcDiagonal(1, diagLength, currAngle)
            diaonals.append(diagLength)
            diaonals.append(diagLength)
            currAngle = currAngle - oneSegmentAngle
    
    scalingFactor = (multiplyList(diaonals))**(1/n)
    if DEBUG:
        print("Diagonals:", diaonals)
        print("Scaling Factor:", scalingFactor)
    
    return scalingFactor

# https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
def naturalSort(arr): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(arr, key=alphanum_key)