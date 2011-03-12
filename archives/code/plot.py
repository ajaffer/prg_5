from pylab import *

import numpy as np
import csv
import math



def csv_to_arrays(f):
    x = []
    y = []
    spamReader = csv.reader(open(f, 'rb'), delimiter=' ', quotechar='|')
    for row in spamReader:
        x.append(row[0])
        y.append(row[1])
    return x,y


def plot_for(t, odom_signle, output):
    x,y = csv_to_arrays(odom_signle)
    plot (x, y,'.-', label='distance-signal' )

    #L = 10n log(d) + c
    #y = 10*n * log(x) + c
    # m = 10*n
    #y = Ap
    #A = [[log(x) 1]]
    #p = [[10*n], [c]]




    xx = map(lambda x: math.log(float(x)), x)

    #y = m * xx + c
    #m = 10 * n
    #xx = log(d)

#    print "lens x,y %s,%s" % (str(len(xx)), str(len(y)))

    A = np.vstack([xx, np.ones(len(x))]).T
    print "A => "
    print A

    m, c = np.linalg.lstsq(A, y)[0]
    print "m,c = %s, %s" % (m,c)

#    print xx
#    print "x,y %f,%f" % (len(x), len((m*xx+c)))
    plt.plot(x, map(lambda x: m*float(x)+c, xx), 'r', label='Fitted line')



    xlabel('distance')
    ylabel('signal strength')
    title(t)
    legend(('Signal Strength', 'Distance to Router'))
    savefig(output,dpi=(640/8))
    cla()
    clf()


plot_for('Router 1 - Test 1', 'out/r1_odom_rssi.csv', "out/r1.png")
plot_for('Router 2 - Test 1', 'out/r2_odom_rssi.csv', "out/r2.png")
plot_for('Router 3 - Test 1', 'out/r3_odom_rssi.csv', "out/r3.png")
plot_for('Router 4 - Test 1', 'out/r4_odom_rssi.csv', "out/r4.png")

#plot_for('Router 1 - Test 1', 'out/r1_odom.csv', 'out/r1_rssi.csv', "out/r1.png")
#plot_for('Router 2 - Test 1', 'out/r2_odom.csv', 'out/r2_rssi.csv', "out/r2.png")
#plot_for('Router 3 - Test 1', 'out/r3_odom.csv', 'out/r3_rssi.csv', "out/r3.png")
#plot_for('Router 4 - Test 1', 'out/r4_odom.csv', 'out/r4_rssi.csv', "out/r4.png")
#
#plot_for('Router 4 - Test 1', 'out/odom.csv', '', "out/odom.png")


#signal = 'out/r1_rssi.csv'
#odom = 'out/r1_odom.csv'
#t,s = csv_to_arrays(signal)
#t,o = csv_to_arrays(odom)
#n = len(t)
#
#
#(ar,br)=polyfit(x,y,1)
#xr=polyval([ar,br],x)
#err=sqrt(sum((xr-y)**2)/n)
#
#title('Linear Regression')
#plot(x)



#import numpy as np
#
## Fit a line, ``y = mx + c``, through some noisy data-points:
#
#x = np.array([0, 1, 2, 3])
#y = np.array([-1, 0.2, 0.9, 2.1])
#
## By examining the coefficients, we see that the line should have a
## gradient of roughly 1 and cut the y-axis at, more or less, -1.
#
## We can rewrite the line equation as ``y = Ap``, where ``A = [[x 1]]``
## and ``p = [[m], [c]]``.  Now use `lstsq` to solve for `p`:
#
#A = np.vstack([x, np.ones(len(x))]).T
#A
## array([[ 0.,  1.],
## [ 1.,  1.],
## [ 2.,  1.],
## [ 3.,  1.]])
#
#m, c = np.linalg.lstsq(A, y)[0]
#print m, c
## 1.0 -0.95
#
## Plot the data along with the fitted line:
#
#import matplotlib.pyplot as plt
#plt.plot(x, y, 'o', label='Original data', markersize=10)
#plt.plot(x, m*x + c, 'r', label='Fitted line')
#plt.legend()
#plt.show()




