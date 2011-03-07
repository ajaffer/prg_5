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




x,y = csv_to_arrays('../r4_p.csv')
#print x
#print y
plot (x, y,'.-', label='odom' )
xlabel('time - seconds')
ylabel('rtouer 4 - signal strength')
title('Router 4 Signal Strenght Data')
legend(('sample1'))
#legend(('sample1','sample2'))
savefig("r4.png",dpi=(640/8))