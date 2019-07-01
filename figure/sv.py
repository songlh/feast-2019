import numpy as np 
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':

	#rawList = [31, 25, 2, 3, ]
	svList = ['2', '3', '4', '5', '>=6']
	numList = [31, 25, 2, 3, 5]

	totalNum = sum(numList)

	XList = svList
	YList = [ num * 1.0 / totalNum for num in numList]

	
	ind = np.arange(5)
	width = 0.5
	fig, ax = plt.subplots()
	rects = ax.bar(ind, YList, width, color='b')

	datemin = 0 - 0.2
	datemax = 5 #+ 0.2

	ax.set_xlim(datemin, datemax)

	#datemin = 0 
	#datemax = 5.9

	

	#ax.set_ylim(datemin, datemax)

	ax.xaxis.set_tick_params(labelsize=18)
	ax.yaxis.set_tick_params(labelsize=18)

	plt.xticks(ind+width/2, XList)

	
	#plt.yticks(ind, ['0', '10', '10^2', '10^3', '10^4', '10^5'])

	#plt.show()
	plt.xlabel('# of States', fontsize=22)
	plt.ylabel('% of FSMs', fontsize=22)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	plt.xticks(ind+width/2, XList)

	#plt.show()
	fig.savefig('sv-dist.pdf')
	fig.savefig('sv-dist.png')
	plt.close(fig)