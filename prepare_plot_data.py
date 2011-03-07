__author__ = 'Ahsen'
import types
import csv
import math

source_dir = "/Users/Ahsen/Documents/workdir/drexel/CS-610/programming_hw5/experiments/20080204-T1/"
out_dir = "out/"
odom_file = source_dir + "odom_T1.log"
r1_file_1 = source_dir + "sigstr_ath8_router01.log"
r1_file_2 = source_dir + "sigstr_ath9_router01.log"
r2_file_1 = source_dir + "sigstr_ath8_router02.log"
r2_file_2 = source_dir + "sigstr_ath9_router02.log"
r3_file_1 = source_dir + "sigstr_ath8_router03.log"
r3_file_2 = source_dir + "sigstr_ath9_router03.log"
r4_file_1 = source_dir + "sigstr_ath8_router04.log"
r4_file_2 = source_dir + "sigstr_ath9_router04.log"


#result_dict = ({})

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
        key = str(int(a[i][0])/1000)
        if result_dict.has_key(key):
            result_dict[key].append(a[i])
        else:
            result_dict[key] = list()
            result_dict[key].append(a[i])
    return result_dict

def avg_odom(x,y):
    result = '0.0'
    try:
        if type(x) == types.ListType:
            result = str(float((float(x[3])+float(y[3]))/2))
        else:
            result = str(float((float(x)+float(y[3]))/2))
    except (ValueError, IndexError):
        print "value error, %s, %s" % (x,y)
    return result

def avg_signal_strength(x,y):
    result = '0.0'
    try:
        if type(x) == types.ListType:
            result = str(float((float(x[4])+float(y[4]))/2))
        else:
            result = str(float((float(x)+float(y[4]))/2))
    except (ValueError, IndexError):
        print "value error, %s, %s" % (x,y)
    return result

def scale_signal_strength(r_readings):
#    r_readings[4] = str(875*((-1*float(r_readings[4]))+0))
    r_readings[4] = str(1*((+1*float(r_readings[4]))+0))
    return r_readings

def process_router(r_readings, file_name):
    map(scale_signal_strength, r_readings)
    r_dict = to_dict(r_readings, ({}))

    for k, v in r_dict.iteritems():
        r_dict[k] = reduce(avg_signal_strength, v)

        spamWriter = csv.writer(open(out_dir+file_name, 'wb'), delimiter=' ')

    for key in sorted(r_dict.iterkeys()):
        if(type(r_dict[key]) == types.StringType):
    #        print "%s: %f" % (key, float(r_dict[key]))
            spamWriter.writerow((key, float(r_dict[key])))
#        else:
#            print type(r_dict[key])

    return r_dict


def process_odom(odom_readings, file_name):
    odom_dict = to_dict(odom_readings, ({}))

    #odom_dictionary2 = ({})
    for k, v in odom_dict.iteritems():
    #    print k, v
        odom_dict[k] = reduce(avg_odom, v)


    spamWriter = csv.writer(open(out_dir+file_name, 'wb'), delimiter=' ')

    for key in sorted(odom_dict.iterkeys()):
        if(type(odom_dict[key]) == types.StringType):
    #        print "%s: %f" % (key, float(odom_dict[key]))
            spamWriter.writerow((key, float(odom_dict[key])))
#        else:
#            print type(odom_dict[key])

    return odom_dict


def process_odom_router(odom_dict, r_dict, file_name):
    odom_rssi_dict = ({})

    for k, v in odom_dict.iteritems():
#        print "odom_rssi_dict = "
#        print odom_rssi_dict
        if(r_dict.has_key(k) and type(r_dict[k]) == types.StringType):
#            print "v,k = %s,%s" % (v,k)
            if(type(v) == types.StringType):
                odom_rssi_dict[v] = r_dict[k]

    spamWriter = csv.writer(open(out_dir+file_name, 'wb'), delimiter=' ')

    for key in sorted(odom_rssi_dict.iterkeys()):
        if(type(odom_rssi_dict[key]) == types.StringType):
#            print "%s: %f" % (key, float(odom_rssi_dict[key]))
            spamWriter.writerow((key, float(odom_rssi_dict[key])))
        else:
            print type(odom_rssi_dict[key])

#    return odom_rssi_dict


#
#def csv_to_arrays(f):
#    x = []
#    y = []
#    spamReader = csv.reader(open(f, 'rb'), delimiter=' ', quotechar='|')
#    for row in spamReader:
#        x.append(row[0])
#        y.append(row[1])
#    return x,y


def to_r1(odom_reading):
    odom_reading[3] = str(float(odom_reading[3])+3000)
    return odom_reading

def to_r2(odom_reading):
    odom_reading[3] = str(75000 - float(odom_reading[3])+3000)
    return odom_reading

def to_r3(odom_reading):
    odom_reading[3] = str(math.sqrt( (23000-float(odom_reading[3])+3000)**2 + ((17-5.5)*1000)**2))
    return odom_reading

def to_r4(odom_reading):
    odom_reading[3] = str(math.sqrt( (47000-float(odom_reading[3])+3000)**2 + ((5.5)*1000)**2))
    return odom_reading


odom_readings = read_file_to_array(odom_file)

print """
Alright, I loaded up the the file for odomter readings.
"""

process_odom(odom_readings, 'odom.csv')

print """
Aaaand written sorted odomoter readings, approximated to the second.
"""


odom_readings = read_file_to_array(odom_file)
r1_odom_dict = process_odom(map(to_r1, odom_readings), 'r1_odom.csv')

odom_readings = read_file_to_array(odom_file)
r2_odom_dict = process_odom(map(to_r2, odom_readings), 'r2_odom.csv')

odom_readings = read_file_to_array(odom_file)
r3_odom_dict = process_odom(map(to_r3, odom_readings), 'r3_odom.csv')

odom_readings = read_file_to_array(odom_file)
r4_odom_dict = process_odom(map(to_r4, odom_readings), 'r4_odom.csv')





r1_readings = read_file_to_array(r1_file_1) + read_file_to_array(r1_file_2)
r2_readings = read_file_to_array(r2_file_1) + read_file_to_array(r2_file_2)
r3_readings = read_file_to_array(r3_file_1) + read_file_to_array(r3_file_2)
r4_readings = read_file_to_array(r4_file_1) + read_file_to_array(r4_file_2)

print """
OK now I loaded up the the file for router readings as well...
"""

r1_rssi_dict = process_router(r1_readings, 'r1_rssi.csv')
r2_rssi_dict = process_router(r2_readings, 'r2_rssi.csv')
r3_rssi_dict = process_router(r3_readings, 'r3_rssi.csv')
r4_rssi_dict = process_router(r4_readings, 'r4_rssi.csv')


process_odom_router(r1_odom_dict, r1_rssi_dict, 'r1_odom_rssi.csv')
process_odom_router(r2_odom_dict, r2_rssi_dict, 'r2_odom_rssi.csv')
process_odom_router(r3_odom_dict, r3_rssi_dict, 'r3_odom_rssi.csv')
process_odom_router(r4_odom_dict, r4_rssi_dict, 'r4_odom_rssi.csv')



