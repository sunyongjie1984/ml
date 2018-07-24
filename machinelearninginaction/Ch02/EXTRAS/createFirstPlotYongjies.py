'''
Created on Oct 27, 2010

@author: Peter
'''
from numpy import *
#import kNN
import pdb;
import sys
sys.path.append("..")
import kNN
import matplotlib
import matplotlib.pyplot as plt
pdb.set_trace( );
fig = plt.figure()
ax = fig.add_subplot(111)
#datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], s = 15.0*array(datingLabels), c=15.0*array(datingLabels))
ax.axis([-2,25,-0.2,2.0])
plt.grid( True );
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()
