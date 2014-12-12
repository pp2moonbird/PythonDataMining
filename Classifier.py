__author__ = 'pp'


def getMedian(list):
    list.sort()
    if (len(list) % 2 == 0):
        left = len(list)/2 - 1
        right = len(list)/2
        median = (list[left] + list[right])/float(2)
    else:
        index = len(list)/2
        median = list[index]
    return median

#calculate AbsoluteStandDeviation(asd)


def getAbsoluteStandardDeviation(list, m):
    sum = 0
    for i in list:
        sum = sum + abs(i - m)
    return sum / float(len(list))


class Classifier:
    def __init__(self, folderPath, bucket, k):
        self.trainingSet = []
        self.testSet = []
        self.k = k
        self.medians = []
        self.asds = []

        # load data from bucket to test set
        fileName = folderPath + 'pima-{:0>2d}'.format(bucket)
        dataFile = file(fileName)
        for line in dataFile:
            temp = line.rstrip().split('\t')
            measures = []
            stringMeasures = temp[0:len(temp)-1]
            for i in stringMeasures:
                measures.append(float(i))
            myclass = temp[len(temp)-1]
            self.testSet.append((measures, myclass))

        # load data from other buckets to training set
        for i in range(1,11):
            if(i!=bucket):
                fileName = folderPath + 'pima-{:0>2d}'.format(i)
                dataFile = file(fileName)
                for line in dataFile:
                    temp = line.rstrip().split('\t')
                    measures = []
                    stringMeasures = temp[0:len(temp)-1]
                    for i in stringMeasures:
                        measures.append(float(i))
                    myclass = temp[len(temp)-1]
                    self.trainingSet.append((measures, myclass))
        # for i in testSet:
        #     print i

        # normalize training set
        columnNumber = len(self.trainingSet[1][0])
        trainingSize = len(self.trainingSet)
        print columnNumber
        for i in range(0,columnNumber):
            fieldList = []
            for j in range(0,trainingSize):
                fieldList.append(self.trainingSet[j][0][i])
            median = getMedian(fieldList)
            asd = getAbsoluteStandardDeviation(fieldList, median)
            self.medians.append(median)
            self.asds.append(asd)


        for i in self.medians:
            print i
        for i in self.asds:
            print i
        self.columnNumber = len(self.trainingSet[0][0])

    def normalizeData(self):
        columnNumber = len(self.trainingSet[0][0])
        print 'columnNumber ' + str(columnNumber)
        for i in self.trainingSet:
            for j in range(0,columnNumber):
                i[0][j] = (i[0][j] - self.medians[j])/self.asds[j]

        for i in self.trainingSet:
            print i

    def writeTrainingSetToFile(self, filePath):
        writeFile = open(filePath, 'w')
        data = self.trainingSet
        for i in data:
            mystr = ''
            measure = data[0][0]
            fieldsize = len(measure)
            for j in range(0, fieldsize):
                s = str(i[0][j])
                mystr = mystr + s + '\t'
            writeFile.write(mystr)
            writeFile.write('\r')
        writeFile.close()

    # calculate test data i based on KNN
    def classifiyBasedOnKNN(self, i):
        k = self.k
        columnNumber = self.columnNumber
        # standardize column values
        measures = self.testSet[i][0]
        for i in range(0, columnNumber):
            measures[i] = (measures[i] - self.medians[i])/self.asds[i]

        # calculate distance between training set
        trainingSet = self.trainingSet
        distances = []
        for i in trainingSet:
            distance = 0
            for j in range(0, columnNumber):
                distance += abs(measures[i]-i[0][j])
            distances.append(distance)


        # classify with biggest vote



    # standardize training set
    # compute median and asd for each field of training set


classfier = Classifier('C:/Users/pengpe/Desktop/Data Mining/ch5/PythonCh5/ch5/pima/pima/', 1, 3)

classfier.writeTrainingSetToFile('C:/Users/pengpe/Desktop/Data Mining/ch5/PythonCh5/testTraining.txt')

classfier.normalizeData()

classfier.classifiyBasedOnKNN(0)


# a = range(1, 10)
# a[4] = 18
# b = []
# for i in a:
#     b.append((i, a.index(i)))
# b = sorted(b, key=lambda i: i[0])
# print b