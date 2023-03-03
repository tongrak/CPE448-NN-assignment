from functools import reduce; 
import numpy as np;
from statistics import stdev;

inFile = open('RawData/ecoli.data','r');
outFile1 = open('ProcessedData/type1data.data','w');
texts = inFile.readlines();

rowCount = len(texts);
colCount = len(texts[0].split())-1;
dataMatr=[[0 for _ in range(rowCount)] for _ in range(colCount)]

for i in range(rowCount):
    rowData = texts[i].split();
    rowData.pop(0);
    type1Data = rowData.copy();
    type1Text = reduce(lambda a,b: a+"    "+b,type1Data);
    outFile1.write(type1Text+"\n")

    for j in range(colCount):
        dataMatr[j][i] = rowData[j];

classList = dataMatr.pop(len(dataMatr)-1)

def writeMatrTo(dataPath: str, matr: list):
    outFile = open(dataPath, 'w');
    matrCopy = matr.copy()
    matrCopy.insert(len(matrCopy),classList)
    turnedMatr = np.swapaxes(matrCopy,0,1);
    for tempTexts in turnedMatr:
        strList = list(map(str,tempTexts))
        longText = reduce(lambda a,b: a+"    "+b,strList);
        outFile.write(longText+"\n")

def normalize(x, minVal, maxVal):
    return (x-minVal)/(maxVal-minVal);

def standarize(x, meanVal, stddVal):
    return (x-meanVal)/stddVal

type2Matr = []
type3Matr = []
for i in range(colCount-1):
    temp = list(map(float,dataMatr[i]));
    minVal = min(temp);
    maxVal = max(temp);
    meanVal = np.mean(temp);
    stddVal = stdev(temp);
    type2Matr.append(list(map(lambda x: round(normalize(x,minVal,maxVal),2), temp)))
    type3Matr.append(list(map(lambda x: round(standarize(x,meanVal,stddVal)) , temp)))


writeMatrTo('ProcessedData/type2data.data', type2Matr);
writeMatrTo('ProcessedData/type3data.data', type3Matr);
