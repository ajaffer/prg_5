__author__ = 'Ahsen'
import types
import csv
import math
import operator
from pylab import *


source_dir = "/Users/Ahsen/Documents/workdir/drexel/CS-610/programming_hw5/experiments/20080211-T3/"
out_dir = "arffprepout/"
classification_dir = out_dir + "classification/"
regression_x_dir = out_dir + "regressionx/"
regression_y_dir = out_dir + "regressiony/"

REGRESSION_X = "RegressionX"
REGRESSION_Y = "RegressionY"
CLASSIFICATION = "Classification"

#odom_file = source_dir + "odom_T1.log"
r1_file_1 = source_dir + "sigstr_ext0_r01_20080211_T3.log"
r1_file_2 = source_dir + "sigstr_ext1_r01_20080211_T3.log"
r1_file_3 = source_dir + "sigstr_int_r01_20080211_T3.log"

r2_file_1 = source_dir + "sigstr_ext0_r02_20080211_T3.log"
r2_file_2 = source_dir + "sigstr_ext1_r02_20080211_T3.log"
r2_file_3 = source_dir + "sigstr_int_r02_20080211_T3.log"

r3_file_1 = source_dir + "sigstr_ext0_r03_20080211_T3.log"
r3_file_2 = source_dir + "sigstr_ext1_r03_20080211_T3.log"
r3_file_3 = source_dir + "sigstr_int_r03_20080211_T3.log"

r4_file_1 = source_dir + "sigstr_ext0_r04_20080211_T3.log"
r4_file_2 = source_dir + "sigstr_ext1_r04_20080211_T3.log"
r4_file_3 = source_dir + "sigstr_int_r04_20080211_T3.log"



def convert_to_ARFF(router_stoppoint_rssi, mode):
    file_name = 'training_arff.txt'

    spamWriter = csv.writer(open((classification_dir if mode==CLASSIFICATION else regression_x_dir if mode==REGRESSION_X else regression_y_dir)+file_name, 'wb'), delimiter=',')

    r1_stopppont_rssi = router_stoppoint_rssi[0]
    r2_stopppont_rssi = router_stoppoint_rssi[1]
    r3_stopppont_rssi = router_stoppoint_rssi[2]
    r4_stopppont_rssi = router_stoppoint_rssi[3]

    for stoppoint in range(len(r1_stopppont_rssi)):
        r1_rssi = r1_stopppont_rssi[stoppoint]
        r2_rssi = r2_stopppont_rssi[stoppoint]
        r3_rssi = r3_stopppont_rssi[stoppoint]
        r4_rssi = r4_stopppont_rssi[stoppoint]

        min_rssi_len = min(len(r1_rssi), len(r2_rssi), len(r3_rssi), len(r4_rssi))

        for i in range(min_rssi_len):
            if mode == CLASSIFICATION:
                spamWriter.writerow((r1_rssi[i], r2_rssi[i], r3_rssi[i], r4_rssi[i], "pos"+str(stoppoint+1)))
            if mode == REGRESSION_X:
                spamWriter.writerow((r1_rssi[i], r2_rssi[i], r3_rssi[i], r4_rssi[i], start_end_dict[stoppoint][2]))
            if mode == REGRESSION_Y:
                spamWriter.writerow((r1_rssi[i], r2_rssi[i], r3_rssi[i], r4_rssi[i], start_end_dict[stoppoint][3]))


def read_file_to_array(f):
    arr = []
    inp = open(f, "r")
    for line in inp.readlines():
        arr.append([])
        for i in line.split():
            arr[-1].append(i)
    return arr


def to_dict(a, result_dict):
    for i in range(len(a)):
        key = a[i][0]
#        result_dict[key] = list()
#        result_dict[key].append(a[i])
        result_dict[key] = a[i]
    return result_dict

def sort_to_file(r_readings, file_name):
    r_dict = to_dict(r_readings, ({}))

    spamWriter = csv.writer(open(out_dir+file_name, 'wb'), delimiter=' ')

    for key in sorted(r_dict.iterkeys()):
        if(type(r_dict[key]) == types.StringType):
            spamWriter.writerow((key, float(r_dict[key])))
    return r_dict

def to_r_stoppoint_rssi(start_end_dict, r_sorted_dict):
    r_stopppont_rssi = [[]]

    for stop,time in start_end_dict.iteritems():
        start_time = time[0]
        stop_time = time[1]

        vals = []
        for k,v in r_sorted_dict.iteritems():
            if (float(k) >= start_time and float(k) <= stop_time):
                vals.append(v[4])

        r_stopppont_rssi.insert(stop, vals)

    return r_stopppont_rssi


#ARFF Setup
start_end_dict = ({})
start_end_dict[0] = [1202769678737, 1202769700377, 6489, 5700]
start_end_dict[1] = [1202769741260, 1202769762898, 10477, 5740]
start_end_dict[2] = [1202769803340, 1202769824964, 14452, 5790]
start_end_dict[3] = [1202769865818, 1202769887467, 18440, 5840]
start_end_dict[4] = [1202769927525, 1202769949569, 22364, 5930]
start_end_dict[5] = [1202769990412, 1202770012031, 26403, 6000]
start_end_dict[6] = [1202770052469, 1202770074089, 30378, 6100]
start_end_dict[7] = [1202770114961, 1202770136578, 34353, 6190]
start_end_dict[8] = [1202770177034, 1202770198670, 38341, 6300]
start_end_dict[9] = [1202770239119, 1202770261136, 42316, 6420]
start_end_dict[10] = [1202770301599, 1202770323622, 46329, 6580]
start_end_dict[11] = [1202770364058, 1202770385680, 50317, 6780]
start_end_dict[12] = [1202770426119, 1202770448140, 54279, 6940]
start_end_dict[13] = [1202770488185, 1202770510609, 58293, 7110]
start_end_dict[14] = [1202770541035, 1202770551443, 62306, 7320]

#print start_end_dict


r1_readings = read_file_to_array(r1_file_1) + read_file_to_array(r1_file_2) + read_file_to_array(r1_file_3)
r2_readings = read_file_to_array(r2_file_1) + read_file_to_array(r2_file_2) + read_file_to_array(r2_file_3)
r3_readings = read_file_to_array(r3_file_1) + read_file_to_array(r3_file_2) + read_file_to_array(r3_file_3)
r4_readings = read_file_to_array(r4_file_1) + read_file_to_array(r4_file_2) + read_file_to_array(r4_file_3)


r1_sorted_dict = sort_to_file(r1_readings, 'r1_readings.csv')
r2_sorted_dict = sort_to_file(r2_readings, 'r2_readings.csv')
r3_sorted_dict = sort_to_file(r3_readings, 'r3_readings.csv')
r4_sorted_dict = sort_to_file(r4_readings, 'r4_readings.csv')

router_stoppoint_rssi = [[[]]]

r1_stopppont_rssi = to_r_stoppoint_rssi(start_end_dict, r1_sorted_dict)
r2_stopppont_rssi = to_r_stoppoint_rssi(start_end_dict, r2_sorted_dict)
r3_stopppont_rssi = to_r_stoppoint_rssi(start_end_dict, r3_sorted_dict)
r4_stopppont_rssi = to_r_stoppoint_rssi(start_end_dict, r4_sorted_dict)

router_stoppoint_rssi.insert(0, r1_stopppont_rssi)
router_stoppoint_rssi.insert(1, r2_stopppont_rssi)
router_stoppoint_rssi.insert(2, r3_stopppont_rssi)
router_stoppoint_rssi.insert(3, r4_stopppont_rssi)

#print r1_stopppont_rssi

convert_to_ARFF(router_stoppoint_rssi, CLASSIFICATION)
convert_to_ARFF(router_stoppoint_rssi, REGRESSION_X)
convert_to_ARFF(router_stoppoint_rssi, REGRESSION_Y)


#reduce(lambda x: math.avg(x[0]),arr)

def to_dict(predicted, param_no):
    actual_dict = ({})
    for i in range(len(predicted)):
        p = predicted[i]

        if len(p) > 0:
            actual_value = p[param_no]
            if(actual_dict.has_key(actual_value)==False):
                actual_dict[actual_value] = list()
            actual_dict[actual_value].append(p)
    return actual_dict

def sum_a(x,y):
    if(type(x) == types.ListType and type(y) == types.ListType):
        return float(x[4] if x[3]=='+' else x[3])+float(y[4] if y[3]=='+' else y[3])
    if(type(x) == types.FloatType and type(y) == types.ListType):
        return x + float(y[4] if y[3]=='+' else y[3])
    if(type(x) == types.FloatType):
        return float(x[4] if x[3]=='+' else x[3])

    return float(-1)


def convert_to_actual_predicted_array(actual_dict):
    for actual,predicted_arr in actual_dict.iteritems():
        predicted_dict = to_dict(predicted_arr, 2)

        for predicted,v in predicted_dict.iteritems():
            sum_of = reduce(sum_a ,v)
            if(type(sum_of) == types.FloatType):
                value = str(sum_of/len(v))
#                print "value = %s " % value
                predicted_dict[predicted] = value
            if(len(v)==1):
                value = (v[0][4] if v[0][3]=='+' else v[0][3])
#                print "value = %s " % value
                predicted_dict[predicted] = value


        sorted_x = sorted(predicted_dict.iteritems(), key=operator.itemgetter(1))
#        print sorted_x[len(sorted_x)-1][0]
        actual_dict[actual] = sorted_x[len(sorted_x)-1][0]

    return actual_dict


def plot_dict(dict, output):
    plot (range(len(dict.keys())), dict.keys(),'.-', label='distance-signal' )
    plot (range(len(dict.values())), dict.values(),'.-', label='distance-signal' )

    xlabel('')
    ylabel('Locations')
    title("test")
    legend(('Atcual', 'Predicted'))
    savefig(output,dpi=(640/8))
    cla()
    clf()


predicted_file = "/Users/Ahsen/Documents/workdir/drexel/CS-610/programming_hw5/code/out/plot/predicted.txt"
predicted = read_file_to_array(predicted_file)

#print predicted

actual_dict = to_dict(predicted, 1)

#print actual_dict


actual_dict = convert_to_actual_predicted_array(actual_dict)

print actual_dict

d = ({})
for k,v in actual_dict.iteritems():
    d[k.partition(":")[0]] = v.partition(":")[0]

print d
plot_dict(d, out_dir+"plot.png")