'''
Created on Oct 6, 2010

@author: yongjies
'''
from numpy import *;
import matplotlib;
import matplotlib.pyplot as plt;
from matplotlib.patches import Rectangle;
import pdb;
#pdb.set_trace( );

n = 1000; #number of points to create
k0 = 0;
k1 = 0;
k2 = 0;
k3 = 0;
xcord1 = [ ];
ycord1 = [ ];
xcord2 = [ ];
ycord2 = [ ];
xcord3 = [ ];
ycord3 = [ ];
markers = [ ];
colors = [ ];
fig = plt.figure( );
random.seed( 8888 );
fw = open( 'testYongjies.txt', 'w' )
for i in range( n ):
    [ r0, r1 ] = random.standard_normal( 2 )
    fw.write("%f\t%f\n" % ( r0, r1 ) );
    myClass = random.uniform( 0, 1 )
    if ( myClass <= 0.16 ):
        fFlyer = random.uniform( 22000, 60000 );
        tats = 3 + 1.6 * r1;
        if 0 == k0:
            plt.annotate( ( ( "myClass is %f, <= 0.16, %d, %d" ) % (myClass, fFlyer, tats ) ), xy = ( fFlyer, tats ), xytext = ( fFlyer + 2, tats + 2 ), arrowprops = dict( facecolor = 'yellow', shrink = 0.05 ) )
        k0 = k0 + 1;
        xcord1.append( fFlyer );
        ycord1.append( tats );
    elif ( ( myClass > 0.16 ) and ( myClass <= 0.33 ) ):
        fFlyer = 6000 * r0 + 70000
        tats = 10 + 3 * r1 + 2 * r0
        if ( tats < 0 ):
            tats = 0;
        if ( fFlyer < 0 ):
            fFlyer = 0;
        xcord1.append( fFlyer );
        ycord1.append( tats );
    elif ( ( myClass > 0.33 ) and ( myClass <= 0.66 ) ):
        fFlyer = 5000 * r0 + 10000;
        tats = 3 + 2.8 * r1;
        if ( tats < 0 ):
            tats = 0;
        if ( fFlyer < 0 ):
            fFlyer = 0;
        xcord2.append( fFlyer );
        ycord2.append( tats );
    else:
        fFlyer = 10000 * r0 + 35000;
        tats = 10 + 2.0 * r1;
        if 0 == k3:
            plt.annotate( ( ( "myClass is %f, > 0.66, %d, %d" ) % ( myClass, fFlyer, tats ) ), xy = ( fFlyer, tats ), xytext = ( fFlyer + 2, tats + 2 ), arrowprops = dict( facecolor = 'red', shrink = 0.05 ) );
        k3 = k3 + 1;
        if ( tats < 0 ):
            tats = 0;
        if ( fFlyer < 0 ):
            fFlyer = 0;
        xcord3.append( fFlyer );
        ycord3.append( tats );

fw.close( );
ax = fig.add_subplot( 1, 1, 1 );
#ax.scatter(xcord,ycord, c=colors, s=markers)
type1 = ax.scatter( xcord1, ycord1, s = 20, c = 'red' );
type2 = ax.scatter( xcord2, ycord2, s = 30, c = 'green' );
type3 = ax.scatter( xcord3, ycord3, s = 50, c = 'blue' );
ax.legend( [ type1, type2, type3 ], [ "Did Not Like", "Liked in Small Doses", "Liked in Large Doses" ], loc = 2 );
ax.axis( [ -5000, 100000, -2, 25 ] );
plt.xlabel( 'Frequent Flyier Miles Earned Per Year' );
plt.ylabel( 'Percentage of Time Spent Playing Video Games' );
plt.show( );
