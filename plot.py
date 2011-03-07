from pylab import *

import csv



def csv_to_arrays(f):
    x = []
    y = []
    spamReader = csv.reader(open(f, 'rb'), delimiter=' ', quotechar='|')
    for row in spamReader:
        x.append(row[0])
        y.append(row[1])
    return x,y


def plot_for(t, odom, signal, output):
    x,y = csv_to_arrays(signal)
    plot (x, y,'.-', label='signal-strength' )

    x,y = csv_to_arrays(odom)
    plot (x, y,'.-', label='odom' )


    xlabel('time - seconds')
    ylabel('signal strength / distance')
    title(t)
    legend(('Signal Strength', 'Distance to Router'))
    savefig(output,dpi=(640/8))
    cla()
    clf()


plot_for('Router 1 - Test 1', 'out/r1_odom.csv', 'out/r1_rssi.csv', "out/r1.png")
plot_for('Router 2 - Test 1', 'out/r2_odom.csv', 'out/r2_rssi.csv', "out/r2.png")
plot_for('Router 3 - Test 1', 'out/r3_odom.csv', 'out/r3_rssi.csv', "out/r3.png")
plot_for('Router 4 - Test 1', 'out/r4_odom.csv', 'out/r4_rssi.csv', "out/r4.png")

#plot_for('Router 4 - Test 1', 'out/odom.csv', '', "out/odom.png")


signal = 'out/r1_rssi.csv'
odom = 'out/r1_odom.csv'
t,s = csv_to_arrays(signal)
t,o = csv_to_arrays(odom)
n = len(t)


(ar,br)=polyfit(x,y,1)
xr=polyval([ar,br],x)
err=sqrt(sum((xr-y)**2)/n)

title('Linear Regression')
plot(x)