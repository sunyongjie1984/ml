# -*- coding: UTF-8 -*-
# this is my knn
from numpy import *
# operator need when sorting
import operator
import pdb

# create dataset and labels
def createDataSet():
    #pdb.set_trace( );
    group = array( [ [ 1.0, 1.1 ], [ 1.0, 1.0 ], [ 0, 0 ], [ 0, 0.1 ] ] );
    labels = [ 'A', 'A', 'B', 'B' ];
    return group, labels;

# knn algorithm
# inX: [ 0, 0 ]
# dataSet: array( [ [ 1, 1.1 ], [ 1,0, 1.0 ], [ 0, 0 ], [ 0, 0.1 ] ] )
# labels: [ 'A', 'A', 'B', 'B' ]
# k: 3
def classify0( inX, dataSet, labels, k ):
    #pdb.set_trace( );
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
    for i in range( k ):
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

#将特征输入到分类器之前，必须将待处理数据的格式改变为分类器可以接受的格式。
#本函数用来处理输入格式的问题。输入为文件名字符串，输出为训练样本和类标签向量。
def file2matrix( filename ):
    fr = open( filename );
    arrayOLines = fr.readlines( );
    numberOfLines = len( arrayOLines );        # get the number of lines in the file
    returnMat = zeros( ( numberOfLines, 3 ) ); # prepare matrix to return
    classLabelVector = [ ];                    # prepare labels return
    index = 0;
    for line in arrayOLines:
        line = line.strip( );
        listFromLine = line.split( '\t' );
        returnMat[ index, : ] = listFromLine[ 0 : 3 ];
        #classLabelVector.append( int( listFromLine[ -1 ] ) );
        classLabelVector.append( int( listFromLine[ -1 ] ) )
        index += 1;
    return returnMat, classLabelVector;

def autoNorm( dataSet ):
    minVals = dataSet.min( 0 ); # the min value of the 0 column
    maxVals = dataSet.max( 0 );
    ranges = maxVals - minVals;
    normDataSet = zeros( shape( dataSet ) );
    m = dataSet.shape[ 0 ];
    normDataSet = dataSet - tile( minVals, ( m, 1 ) );
    normDataSet = normDataSet / tile( ranges, ( m, 1 ) );
    return normDataSet, ranges, minVals;

def datingClassTest( ):
    hoRatio = 0.1;
    datingDataMat, datingLabels = file2matrix( 'datingTestSet2.txt' );
    normMat, ranges, minVals = autoNorm( datingDataMat );
    m = normMat.shape[ 0 ];
    numTestVecs = int( m * hoRatio );
    errorCount = 0.0;
    for i in range( numTestVecs ):
        classifierResult = classify0( normMat[ i, : ], normMat[ numTestVecs : m, : ],\
                datingLabels[ numTestVecs : m ], 3 );
        #print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        print "the classifier came back with: %d, the real answer is: %d"\
                % ( classifierResult, datingLabels[ i ] );
        if ( classifierResult != datingLabels[ i ] ):
            errorCount += 1.0;
    print " the total error rate is: %f" % (errorCount / float( numTestVecs) );

def classifyPerson( ):
    resultList = [ 'not at all', 'in small doses', 'in large doses' ];
    percentTats = float( raw_input( \
            "percentage of time spent playing video gamrs?" ) );
    ffMiles = float( raw_input( " frequent fliter miles earned per year?" ) );
    iceCream = float( raw_input( "liters of ice cream consumed per year?" ) );
    datingDataMat, datingLabels = file2matrix( 'datingTestSet2.txt' );
    normMat, ranges, minVals = autoNorm( datingDataMat );
    inArr = array( [ ffMiles, percentTats, iceCream ] );
    classifierResult = classify0( ( inArr - \
            minVals ) / ranges, normMat, datingLabels, 3);
    print " You will probably like this person: ", \
            resultList[ classifierResult - 1 ];
