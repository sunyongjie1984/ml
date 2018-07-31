# -*- coding: UTF-8 -*-
'''
Created on 20180726

@author: Yongjies
'''
from numpy import *;
import matplotlib;
import matplotlib.pyplot as plt;
from matplotlib.patches import Rectangle;
import pdb;
#pdb.set_trace( );


#n = 1; #number of points to create
n = 1000; #number of points to create
k0 = 0;
k1 = 0;
k2 = 0;
k3 = 0;
xcord = zeros( ( n ) );
ycord = zeros( ( n ) );
markers = [ ];
colors = [ ];
fw = open( 'testSet.txt', 'w' );
fig = plt.figure();
for i in range( n ):
    # numpy.random.standard_normal(size=None)：生产一个浮点数或N维浮点数组，取数范围：标准正态分布随机样本
    [ r0, r1 ] = random.standard_normal( 2 );
    # uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内
    myClass = random.uniform( 0, 1 );
    if ( myClass <= 0.16 ):
        fFlyer = random.uniform( 22000, 60000 );
        tats = 3 + 1.6 * r1;
        markers.append( 20 );
        colors.append( 2.1 );
        classLabel = 1; #'didntLike'
        if 0 == k0:
            plt.annotate( ( ( "myClass is %f, <= 0.16, %d, %d" ) % (myClass, fFlyer, tats ) ), xy=(fFlyer, tats), xytext=(fFlyer + 2, tats + 2),arrowprops=dict(facecolor='yellow', shrink=0.05))
        k0 = k0 + 1;
        print ( "%d, %f, class1" ) % ( fFlyer, tats );
    elif ( ( myClass > 0.16 ) and ( myClass <= 0.33 ) ):
        fFlyer = 6000 * r0 + 70000;
        tats = 10 + 3 * r1 + 2 * r0;
        markers.append( 20 );
        colors.append( 1.1 );
        classLabel = 1; #'didntLike'
        if 0 == k1:
            plt.annotate('this is a annotate', xy=(fFlyer, tats), xytext=(fFlyer + 2, tats + 2),arrowprops=dict(facecolor='yellow', shrink=0.05))
        k1 = k1 + 1;
        print ( "%d, %f, class1" ) % ( fFlyer, tats );
    elif ( ( myClass > 0.33 ) and ( myClass <= 0.66 ) ):
        fFlyer = 5000 * r0 + 10000;
        tats = 3 + 2.8 * r1;
        markers.append( 30 );
        colors.append( 1.1 );
        classLabel = 2; #'smallDoses'
        if 0 == k2:
            plt.annotate('this is a annotate', xy=(fFlyer, tats), xytext=(fFlyer + 2, tats + 2),arrowprops=dict(facecolor='yellow', shrink=0.05))
        k2 = k2 + 1;
        print ( "%d, %f, class2" ) % ( fFlyer, tats );
    else:
        fFlyer = 10000 * r0 + 35000
        tats = 10 + 2.0 * r1
        markers.append( 50 )
        colors.append( 0.1 )
        classLabel = 3; #'largeDoses'
        if 0 == k3:
            plt.annotate('this is a annotate', xy=(fFlyer, tats), xytext=(fFlyer + 2, tats + 2),arrowprops=dict(facecolor='yellow', shrink=0.05))
        k3 = k3 + 1;
        print ("%d, %f, class3") % (fFlyer, tats);
    if (tats < 0): tats =0
    if (fFlyer < 0): fFlyer =0
    xcord[i] = fFlyer; ycord[i]=tats
    fw.write( "%d\t%f\t%f\t%d\n" % ( fFlyer, tats, random.uniform( 0.0, 1.7 ), classLabel ) );

fw.close();
#fig = plt.figure();
ax = fig.add_subplot( 1, 1, 1 );
ax.scatter( xcord, ycord, c = colors, s = markers );
type1 = ax.scatter( [ -10 ], [ -10 ], s = 20, c = 'red' );
type2 = ax.scatter( [ -10 ], [ -15 ], s = 30, c = 'green' );
type3 = ax.scatter( [ -10 ], [ -20 ], s = 50, c = 'blue' );
ax.legend([type1, type2, type3], ["Class 1", "Class 2", "Class 3"], loc=2);
#ax.axis([-5000,100000,-2,25])
plt.xlabel('Frequent Flyier Miles Earned Per Year');
plt.ylabel('Percentage of Body Covered By Tatoos');
plt.show();
