# -*- coding: UTF-8 -*-
# this is my knn
from numpy import *
# operator need when sorting
import operator
import pdb

# create dataset and labels
def createDataSet():
    pdb.set_trace( );
    group = array([[1.0,1.1],[1.0, 1.0],[0,0],[0,0.1]]);
    labels = ['A','A','B','B'];
    return group, labels;

# knn algorithm
def classify0( inX, dataSet, labels, k ):
    pdb.set_trace( );
    dataSetSize = dataSet.shape[ 0 ];
    diffMat = tile( inX, ( dataSetSize, 1 ) ) - dataSet;
    sqDiffMat = diffMat ** 2;
    sqDistances = sqDiffMat.sum( axis = 1 );
    distances = sqDistances ** 0.5;
    # argsort函数返回的是数组值从小到大的索引值
    sortedDistIndicies = distances.argsort( );
    classCount = { };
    for i in range( k ) :
        voteIlabel = labels[ sortedDistIndicies[ i ] ];
        classCount[ voteIlabel ] = classCount.get( voteIlabel, 0 ) + 1;
    sortedClassCount = sorted( classCount.iteritems( ),
            key=operator.itemgetter( 1 ), reverse = True );
    return sortedClassCount[ 0 ][ 0 ];
