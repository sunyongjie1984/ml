# -*- coding: UTF-8 -*-
# this is my knn
from numpy import *
# operator need when sorting
import operator
import pdb

# create dataset and labels
def createDataSet():
    pdb.set_trace( );
    group = array( [ [ 1.0, 1.1 ], [ 1.0, 1.0 ], [ 0, 0 ], [ 0, 0.1 ] ] );
    labels = [ 'A', 'A', 'B', 'B' ];
    return group, labels;

# knn algorithm
# inX: [ 0, 0 ]
# dataSet: array( [ [ 1, 1.1 ], [ 1,0, 1.0 ], [ 0, 0 ], [ 0, 0.1 ] ] )
# labels: [ 'A', 'A', 'B', 'B' ]
# k: 3
def classify0( inX, dataSet, labels, k ):
    pdb.set_trace( );
    # data set size: 4
    dataSetSize = dataSet.shape[ 0 ];
    # array( [ [ -1, -1.1 ], [ -1, -1 ], [ 0, 0 ], [ 0, -0.1 ] ] )
    diffMat = tile( inX, ( dataSetSize, 1 ) ) - dataSet;
    # array( [ [ 1, 1.21 ], [ 1, 1 ], [ 0, 0 ], [ 0, 0.01 ] ] )
    sqDiffMat = diffMat ** 2;
    # array( [ 2.21, 2, 0, 0.01 ] )
    sqDistances = sqDiffMat.sum( axis = 1 );
    # array( [ 1.48660687, 1.41421356, 0, 0.1 ] )
    distances = sqDistances ** 0.5;
    # argsort函数返回的是数组值从小到大的索引值
    # array( [ 2, 3, 1, 0 ] )
    sortedDistIndicies = distances.argsort( );
    # // 空字典{ }
    classCount = { };
    for i in range( k ) :
        # i: 0, 1, 2
        # voteIlabel: 'B', 'B', 'A'
        voteIlabel = labels[ sortedDistIndicies[ i ] ];
        # dict.get(key, default=None)
        # 返回指定键的值，如果值不在字典中返回default值
        # 'B': 2 'A': 1 ( classCount['B']: 2, classCount[ 'A' ]: 1 )
        classCount[ voteIlabel ] = classCount.get( voteIlabel, 0 ) + 1;
    # classCount的iteritems(),返回classCount的所有迭代器
    # key = operator.itemgetter(1), 以classCount的第二个域进行排序
    # sortedClassCount:[ ( 'B', 2 ), ( 'A', 1 ) ]
    # 字典classCount: { 'A': 1, 'B': 2 }
    sortedClassCount = sorted( classCount.iteritems( ),
            key = operator.itemgetter( 1 ), reverse = True );
    # sortedClassCount[ 0 ][ 0 ]: 'B'
    return sortedClassCount[ 0 ][ 0 ];
