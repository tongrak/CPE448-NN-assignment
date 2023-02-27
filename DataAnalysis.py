import statistics as stt

# Read data
fil = open('RawData/ecoli.data', "r")
texts = fil.readlines()

attrNameList = ["mcg", "gvh", "lip", "chg", "aac", "alm1", "alm2"]
classList = ["cp", "im", "pp", "imU", "om", "omL", "imL", "imS"]

rowCount = len(texts);
colCount = len(texts[0].split());
# set the data matric
dataMatr=[[0 for i in range(rowCount)] for j in range(colCount)]
for i in range(rowCount):
    rowData = texts[i].split();
    for j in range(colCount):
        dataMatr[j][i] = rowData[j];

# show
def find_median(numbers): #Thank ChatGPT
    length = len(numbers)
    if length % 2 == 0:
        return (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        return numbers[length // 2]

def find_quartiles(numbers): #Thank ChatGPT
    length = len(numbers)
    Q1 = numbers[length//4]
    Q3 = numbers[length*3//4]
    return (Q1, Q3)

def printStat(name:str, attrL:list):
    tempCopy = attrL.copy()
    tempCopy.sort()
    qV = find_quartiles(tempCopy)
    fLi = list(map(float, tempCopy))
    print(name + " basic stats:")
    print("number of val:", len(tempCopy))
    print("number of unique val:", len(set(tempCopy)))
    print("min:", tempCopy[0])
    print("max:", tempCopy[len(attrL)-1])
    # print("median:", find_median(tempCopy))
    print("Q1:", qV[0])
    print("mean:", f'{(sum(fLi)/len(tempCopy)):,.2f}')
    print("Q3:", qV[1])
    print("SD:", f'{stt.stdev(fLi):,.2f}')

# show
seqLiCop = dataMatr[0].copy()
print("number of unique seq name: ", len(set(seqLiCop)))
print();


for i in range(1,8):
# i = 1
    printStat(attrNameList[i-1], dataMatr[i])
    print();

clasLiCop = dataMatr[8].copy()
print("number of unique classes: ",len(set(clasLiCop)))