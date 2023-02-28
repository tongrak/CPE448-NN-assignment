from functools import reduce; 

inFile = open('RawData/ecoli.data','r');
outFile1 = open('ProcessedData/type1data.data','w');
texts = inFile.readlines();

rowCount = len(texts);
colCount = len(texts[0].split());
dataMatr=[[0 for _ in range(rowCount)] for _ in range(colCount)]
for i in range(rowCount):
    rowData = texts[i].split();
    rowData.pop(0);
    type1Data = rowData.copy();
    type1Text = reduce(lambda a,b: a+"    "+b,type1Data);
    outFile1.write(type1Text+"\n")


# for j in range(colCount):
#     dataMatr[j][i] = rowData[j];