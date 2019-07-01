import scipy



if __name__=='__main__':
	numTestList = [34, 26, 3, 2, 5]
	numStudyList = [8, 10, 1, 3, 3]

	#print numTestList
	#print [sum(numTestList) * 0.32, sum(numTestList) * 0.4, sum(numTestList) * 0.04, sum(numTestList) * 0.12, sum(numTestList) * 0.12]

	print numStudyList
	print [sum(numStudyList) * 0.48, sum(numStudyList) * 0.37, sum(numStudyList) * 0.04 , sum(numStudyList) * 0.03 , sum(numStudyList) * 0.07]


	#print [ num * 1.0 / sum(numTestList) for num in numTestList]
	#print [ num * 1.0 / sum(numStudyList) for num in numStudyList]


	#print scipy.stats.chisquare(numTestList, f_exp=numStudyList)
