__author__ = 'Ahsen'
import types
import csv

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

def process_router(r_readings, file_name):
    r_dict = to_dict(r_readings, ({}))

    for k, v in r_dict.iteritems():
        r_dict[k] = reduce(avg_signal_strength, v)

        spamWriter = csv.writer(open(out_dir+file_name, 'wb'), delimiter=' ')

    for key in sorted(r_dict.iterkeys()):
        if(type(r_dict[key]) == types.StringType):
    #        print "%s: %f" % (key, float(r_dict[key]))
            spamWriter.writerow((key, float(r_dict[key])))
        else:
            print type(r_dict[key])


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
        else:
            print type(odom_dict[key])

def csv_to_arrays(f):
    x = []
    y = []
    spamReader = csv.reader(open(f, 'rb'), delimiter=' ', quotechar='|')
    for row in spamReader:
        x.append(row[0])
        y.append(row[1])
    return x,y


odom_readings = read_file_to_array(odom_file)

print """
Alright, I loaded up the the file for odomter readings.
"""

process_odom(odom_readings, 'odom_p.csv')

print """
Aaaand written sorted odomoter readings, approximated to the second.
"""

#x,y = csv_to_arrays('../odom_p.csv')
#odom
#for i in x:




r1_readings = read_file_to_array(r1_file_1) + read_file_to_array(r1_file_2)
r2_readings = read_file_to_array(r2_file_1) + read_file_to_array(r2_file_2)
r3_readings = read_file_to_array(r3_file_1) + read_file_to_array(r3_file_2)
r4_readings = read_file_to_array(r4_file_1) + read_file_to_array(r4_file_2)

print """
OK now I loaded up the the file for router readings as well...
"""

process_router(r1_readings, 'r1_p.csv')
process_router(r2_readings, 'r2_p.csv')
process_router(r3_readings, 'r3_p.csv')
process_router(r4_readings, 'r4_p.csv')




