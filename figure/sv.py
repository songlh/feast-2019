import numpy as np 
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':

	
	svList = ['2', '3', '4', '5', '>=6']

	#{2: 34, 3: 26, 4: 3, 5: 2, 6: 1, 7: 1, 9: 1, 11: 2},
	numTestList = [34, 26, 3, 2, 5]
	#{2: 8, 3: 10, 4: 1, 5: 3, 9: 1, 11: 2},
	numStudyList = [8, 10, 1, 3, 3]


	XList = svList
	YTestList = [ num * 1.0 / sum(numTestList) for num in numTestList]
	YStudyList = [num * 1.0 / sum(numStudyList) for num in numStudyList]

	
	ind = np.arange(5)
	width = 0.35
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, YTestList, width, color='g', label='Test', edgecolor='black', hatch='+')
	rects2 = ax.bar(ind + width, YStudyList, width, color='b', label='Study', edgecolor='black', hatch='.')

	datemin = 0 - 0.2
	datemax = 5 #+ 0.2

	ax.set_xlim(datemin, datemax)

	#datemin = 0 
	#datemax = 5.9

	

	#ax.set_ylim(datemin, datemax)

	ax.xaxis.set_tick_params(labelsize=23)
	ax.yaxis.set_tick_params(labelsize=23)

	plt.xticks(ind+width/2, XList)

	
	#plt.yticks(np.arange(6), ['0', '10', '20', '30', '40', '50'])

	#plt.show()
	plt.xlabel('# of States', fontsize=28)
	plt.ylabel('Proportion of FSMs', fontsize=28)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	plt.legend(fontsize='x-large')

	plt.xticks(ind + width, XList)

	#plt.show()
	fig.savefig('sv-dist.pdf')
	fig.savefig('sv-dist.png')
	plt.close(fig)