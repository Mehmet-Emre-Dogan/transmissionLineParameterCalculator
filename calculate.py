import numpy as np
import sympy.physics.units as u
from statistics import geometric_mean as geomean
from math import log
from math import pi
import csv
import os
from json import load
from msvcrt import getch
from functs import *

def calculate(dataPath: str):
    currPath = os.path.dirname(__file__) # find the current directory
    # Read the input data
    dataDict = {}
    with open(dataPath, 'r') as fptr:
        dataDict = load(fptr)
    
    # Read the library data
    libDict = {}
    # https://www.skillsugar.com/convert-csv-into-dictionary-in-python
    with open(currPath + "\\" + 'library.csv', 'r') as fptr:
        reader = csv.DictReader(fptr, skipinitialspace=True)
        for line in reader:
            if line["CodeWord"] == dataDict["ACSR conductor name"]:
                libDict = line

    S_base = dataDict["Sbase (MVA)"]*1e6 # MVA
    V_base = dataDict["Vbase (kV)"]*1e3 # kV
    N_circuit = dataDict["Number of circuits"]
    N_bundle = dataDict["Number of bundle conductors per phase"]
    d_bundle = dataDict["Bundle distance (m)"]
    length = dataDict["Length of the line (km)"]*1e3 # km
    
    if DEBUG:
        print(libDict)
    outside_diameter = u.convert_to(float(libDict["Outside_Diameter_in_"])*u.inches, u.m)
    outside_diameter = float(outside_diameter/u.m) # get rid of prefix
    R_AC = float(libDict["AC_50_Hz_Resistance_20_C_ohm_mi_"])/u.convert_to(1*u.mi, u.m)
    R_AC = float(R_AC*u.m) # get rid of prefix
    GMR_conductor = u.convert_to(float(libDict["GMR_ft_"])*u.ft, u.m)
    GMR_conductor = float(GMR_conductor/u.m) # get rid of prefix

    Z_base = (V_base**2)/S_base
    radius = outside_diameter/2

    # predefined arrays & constants
    freq = 50
    inductorCoeff = 2e-7
    epsilon = 8.85418782e-12
    capCoeff = 2*pi*epsilon
    omg = 2*pi*freq

    a1 = np.array(dataDict["C1 Phase A (centre)"])
    b1 = np.array(dataDict["C1 Phase B (centre)"])
    c1 = np.array(dataDict["C1 Phase C (centre)"])

    a2 = np.array(dataDict["C2 Phase A (centre)"])
    b2 = np.array(dataDict["C2 Phase B (centre)"])
    c2 = np.array(dataDict["C2 Phase C (centre)"])
        # calculations
    if N_circuit == 1:
        dist1 = norm(a1 - b1); dist2 = norm(b1 - c1); dist3 = norm(a1 - c1); 

        GMD = geomean([dist1, dist2, dist3])
        GMR = (GMR_conductor**(1/N_bundle))*(d_bundle**((N_bundle-1)/N_bundle))*calcScalingFactor(N_bundle)
        req = (radius**(1/N_bundle))*(d_bundle**((N_bundle-1)/N_bundle))*calcScalingFactor(N_bundle)

        # effect of earth on capacitance & p means prime
        ap = np.array(symmetryWrtX(a1))
        bp = np.array(symmetryWrtX(b1))
        cp = np.array(symmetryWrtX(c1))
        h1 = norm(a1-ap); h2 = norm(b1-bp); h3 = norm(c1-cp)
        h12 = norm(a1-bp); h23 = norm(c1-bp); h13 = norm(cp-a1)

    if N_circuit == 2:
        # GMD calculation
        # red, yellow, purple colored lines in supplementary notes pic.
        red1 = norm(a1-b1); red2 = norm(a1-b2); red3 = norm(b1-a2); red4 = norm(a2-b2)
        yel1 = norm(a1-c1); yel2 = norm(a1-c2); yel3 = norm(c1-a2); yel4 = norm(a2-c2)
        pur1 = norm(b1-c1); pur2 = norm(b1-c2); pur3 = norm(c1-b2); pur4 = norm(c2-b2)

        gmdAB = geomean([red1, red2, red3, red4])
        gmdAC = geomean([yel1, yel2, yel3, yel4])
        gmdBC = geomean([pur1, pur2, pur3, pur4])

        GMD = geomean([gmdAB, gmdAC, gmdBC])

        # GMR & req calculation
        GMR_bundle = (GMR_conductor**(1/N_bundle))*(d_bundle**((N_bundle-1)/N_bundle))*calcScalingFactor(N_bundle)
        req_bundle = (radius**(1/N_bundle))*(d_bundle**((N_bundle-1)/N_bundle))*calcScalingFactor(N_bundle)
        
        # red, purple, green colored lines in supplementary notes pic.
        redDist = norm(a1-a2); purpDist = norm(b1-b2); greenDist = norm(c1-c2)

        gmrAA = geomean([GMR_bundle, redDist])
        gmrBB = geomean([GMR_bundle, purpDist])
        gmrCC = geomean([GMR_bundle, greenDist])
        GMR = geomean([gmrAA, gmrBB, gmrCC])

        reqAA = geomean([req_bundle, redDist])
        reqBB = geomean([req_bundle, purpDist])
        reqCC = geomean([req_bundle, greenDist])
        req = geomean([reqAA, reqBB, reqCC])

        # earth effect & p means prime
        a1p = symmetryWrtX(a1); b1p = symmetryWrtX(b1); c1p = symmetryWrtX(c1); 
        a2p = symmetryWrtX(a2); b2p = symmetryWrtX(b2); c2p = symmetryWrtX(c2); 

        h12 = geomean([norm(a1-b1p), norm(a1-b2p), norm(a2-b1p), norm(a2-b2p)])
        h13 = geomean([norm(a1-c1p), norm(a1-c2p), norm(a2-c1p), norm(a2-c2p)])
        h23 = geomean([norm(b1-c1p), norm(b1-c2p), norm(b2-c1p), norm(b2-c2p)])

        h1 = geomean([norm(a1-a1p), norm(a1-a2p), norm(a2-a1p), norm(a2-a2p)])
        h2 = geomean([norm(b1-b1p), norm(b1-b2p), norm(b2-b1p), norm(b2-b2p)])
        h3 = geomean([norm(c1-c1p), norm(c1-c2p), norm(c2-c1p), norm(c2-c2p)])

    capEarthCorrector = log(geomean([h12, h23, h13])/geomean([h1, h2, h3]))
    L = inductorCoeff*log(GMD/GMR)*length
    C = capCoeff/(log(GMD/req) - capEarthCorrector )*length

    R = R_AC*length/N_bundle/N_circuit
    X_L = omg*L
    B_C = omg*C

    R_pu = R/Z_base
    X_pu = X_L/Z_base
    B_pu = B_C*Z_base

    return {"R_pu": R_pu, "X_pu":X_pu, "B_pu":B_pu, "R": R, "X_L": X_L, "B_C": B_C}

if __name__ == "__main__":
    print("Standalone mode")
    files = []
    currDirectory = os.path.dirname(__file__) # find the current directory
    for item in os.listdir(currDirectory):
        if item.endswith(".json") or item.endswith(".JSON"):
            files.append(item)
    files = naturalSort(files)
    for i, file in enumerate(files):
        print(f"{str(i).rjust(3)}- {file}")

    while True:
        dataIdx = input("-> Enter the index of the data file.\n--> ")
        try:
            dataIdx = int(dataIdx)
        except Exception as ex:
            print(ex)
        else:
            if dataIdx >= 0 and dataIdx < len(files):
                break
            else:
                print(f"Index must be in the interval [0, {len(files)-1}]")

    calcRes = calculate(os.path.abspath(currDirectory + "\\" + files[dataIdx]))

    print(f'#R_pu: {calcRes["R_pu"]} pu  #X_pu:{calcRes["X_pu"]} pu  #B_pu:{calcRes["B_pu"]} pu')
    print(f'#R: {calcRes["R"]} Ω  #X:{calcRes["X_L"]} Ω  #B:{calcRes["B_C"]} S')
    print("Press any key to exit...")
    getch()