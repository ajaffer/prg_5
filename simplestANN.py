__author__ = 'Ahsen'
from pybrain.datasets            import SupervisedDataSet
#from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
import csv





def csv_to_dict(f):
    dict = ({})
    spamReader = csv.reader(open(f, 'rb'), delimiter=' ', quotechar='|')
    for row in spamReader:
        dict[row[0]] = row[1]
    return dict

def csv_to_arrays(f):
    x = []
    y = []
    z = []
    spamReader = csv.reader(open(f, 'rb'), delimiter=' ', quotechar='|')
    for row in spamReader:
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
    return x,y,z


def plot_for(time, odom, odom_p):
    plot (time, odom,'.-', label='Original Odom' )
    plot(time, odom_p, 'r', label='Predicted Odom')

    xlabel('Time')
    ylabel('Odom-x')
    title('Original vs. Predicted Odom-x')
    legend(('Orignal Odom', 'Predicted Odom'))
    savefig(output,dpi=(640/8))
    cla()
    clf()



#odom_dict = csv_to_dict('out/odom.csv')
#print odom_dict
#
#r1_rssi_dict = csv_to_dict('out/r1_rssi.csv')
#print r1_rssi_dict
#
#r1_odom_rssi_dict = csv_to_dict('out/r1_odom_rssi.csv')
#print r1_odom_rssi_dict


time,odom,rssi = csv_to_arrays('out/r1_time_odom_rssi.csv')


trndata = SupervisedDataSet( 4, 1 )
trndata.appendLinked( [1,2,3,4], [5] )
print len(trndata)
print trndata['input']


#trndata.addSample((-15,-85,-25,-75), (0))
#trndata.addSample((-70,-70,-35,-35), (5))
#trndata.addSample((-85,-15,-75,-25), (50))

for i in range(len(odom)):
    trndata.addSample(rssi[i], odom[i])


print "Number of training patterns: ", len(trndata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0]


fnn = buildNetwork( trndata.indim, 3, trndata.outdim)

#print fnn


trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

trainer.train()
#trainer.trainUntilConvergence()

odom_p = []

for i in range(len(odom)):
    predicted = fnn.activate(rssi[i])
    print "orignal: time: $s, odom: %s predicted: odom: %s " %(time[i], odom[i], predicted)
    odom_p.append(predicted)

plot_for(time, odom, odom_p)

