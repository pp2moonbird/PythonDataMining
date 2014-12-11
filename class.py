# classify indian diabete data
import os
class Classifier:
	def __init__(self):
		print 'start Classifier'
		self.data = []
		self.trainingSet = []
		self.testSet = [] 
		self.medianAndASD = []
	def readDataFileFromPath(self, path):
		
		bucket = 1
		for name in os.listdir(path):
			# print name
			file = open(path+ '\\' +name)
			
			for line in file:
				temp = line.rstrip().split('\t')
				vector = []
				for i in range(0, len(temp)-1):
					vector.append(float(temp[i]))
				ill = float(temp[len(temp)-1])

				self.data.append((vector, ill, bucket))
				# print temp
				
			bucket = bucket + 1
	
	
	#predict one bucket based on other training data
	def predictBucket(self, bucketID):
		for t in self.data:
			if(t[2] == bucketID):
				self.testSet.append(t)
			else:
				self.trainingSet.append(t)				
	
	#calculate median
	def getMedian(self, list):
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
	def getAbsoluteStandardDeviation(self, list, m):
		sum = 0
		for i in list:
			sum = sum + abs(i - m)
		return sum / float(len(list))
	
	#normalize training set
	def normalizeTrainingSet(self):
		vectorSize = len(self.data[0][0])
		#print 'vectorSize:', vectorSize
		for vectorIndex in range(vectorSize):
			list = []
			for i in range(len(self.trainingSet)):
				list.append(self.trainingSet[i][0][vectorIndex])
			median = self.getMedian(list)
			asd = self.getAbsoluteStandardDeviation(list, median)
			self.medianAndASD.append((median, asd))
			
		self.printMedianAndASD()

			
		for i in range(len(self.trainingSet)):
			vector = self.trainingSet[i][0]
			for j in range(len(vector)):
				# print 'j:', j
				# print self.medianAndASD[j]
				median = self.medianAndASD[j][0]
				asd = self.medianAndASD[j][1]
				vector[j] = (vector[j]-median)/asd
			
	#predict each item in testset
	#item is a tuple like any row in self.data
	def classifyItem(self, item, k):
		#normalize item
		pass
		
	#get nearest neighbour
	def getNearestNeighbour(self, item, k):
		pass
		
	#calculate distance
	def calculateDistance(self, item):
		pass
	
	#calculate influence
	
	#calculate final result
	
	def printTrainingSet(self):
		for i in self.trainingSet:
			print i
			
	def printMedianAndASD(self):
		print '* print median and asd'
		for i in self.medianAndASD:
			print '\t', i
		print '* print median and asd done'
		print ''
		
classifier = Classifier()
classifier.readDataFileFromPath('C:\Users\pengpe\Desktop\Data Mining\ch5\pima\pima')



classifier.predictBucket(4)
	
classifier.normalizeTrainingSet()

# for i in classifier.medianAndASD:
	# print i

# classifier.printTrainingSet()

print classifier.trainingSet[2]