import types


from StdSuites.Type_Names_Suite import string
from sys import argv


import sys

print [bits for bits in 32,64 if sys.maxint+1 == 2**(bits-1)]

def print_all(f): print f.read()
def rewind(f): f.seek(0)
def print_a_line(line_count, f): print line_count, f.readline()


def read_file_to_array(f):
    arr = []
    inp = open(f, "r")
    for line in inp.readlines():
        arr.append([])
        for i in line.split():
            arr[-1].append(i)
    return arr


odom_dict = ({
    '1202163225' : ['1202163225738', 'odom', '0.0', '0.0', '0.0', '0.0']
             })

def to_dict(a):
    for i in range(len(a)):
        key = str(int(a[i][0])/1000)
        if odom_dict.has_key(key):
            odom_dict[key].append(a[i])
        else:
            odom_dict[key] = list()
            odom_dict[key].append(a[i])
    return odom_dict


def to_seconds(odom_reading):
    print odom_reading
    key = str(int(odom_reading[0])/1000)
    if odom_dict.has_key(key)==false:
        odom_dict = list()
    odom_dict.append[key](odom_reading[3])




#def to_k_v(a):


#def to_dict2(a):
#    key = str(int(a[0])/1000)
#    if odom_dict.has_key(key)==false:
#        odom_dict[key] = list()
#    odom_dict[key].append(a)


def avg(x,y):
    result = '0'
    try:
        if type(x) == types.ListType:
            result = str(float((float(x[3])+float(y[3]))/2))
        else:
            result = str(float((float(x)+float(y[3]))/2))
    except (ValueError, IndexError):
        print "value error =>"
        print x
        print y
        print "-------"
        print ""
    return result

#    print "x[3] = " + x[3]
#    print "y[3] = " + y[3]
#    x = float(x[3])
#    y = float(y[3])
#    sum = x + y
#    print "sum => " + str(sum)
#    return (sum)/2

#    key_x = str(int(x[0])/1000)
#    if odom_dict.has_key(key):
#        odom_dict[key].append(a[i])
#    else:
#        odom_dict[key] = list()
#        odom_dict[key].append(a[i])
#
#    print "x = " + x[0]
#    print "y = " + y[0]





#b = reduce(sum, b)

#odom_dict[1202163225] = "something"

working_dir = "/Users/Ahsen/Documents/workdir/drexel/CS-610/programming_hw5/experiments/20080204-T1/"
odom_file = working_dir + "odom_T1.log"

#script, user_name = argv
#prompt = '> '
#
#print "Hello, I'm the %s script." % (script)
#print "I'd like to ask you a few questions."
#print "What is odometer file location?"

#odom_file = raw_input(prompt)

#print "Where do you live %s?" % user_name
#lives = raw_input(prompt)
#
#print "What kind of computer do you have?"
#computer = raw_input(prompt)

#current_file = open(odom_file)

print """
Alright, I loaded up the the file odomter file
"""
#print_all(current_file)
#arr = read_file_to_array(odom_file)
#print(arr)

#dict = map(to_dict, arr)
#print(dict)

#dict = to_dict(arr)
#print(dict)

odom_readings = read_file_to_array(odom_file)
odom_dictionary = to_dict(odom_readings)
#print(to_dict(odom_readings))



odom_dictionary2 = ({})
for k, v in odom_dictionary.iteritems():
#    print k, v
    odom_dictionary2[k] = reduce(avg, v)


#for k, v in odom_dictionary2.iteritems():
#    print k, v


for key in sorted(odom_dictionary2.iterkeys()):
    print "%s: %s" % (key, odom_dictionary2[key])

#seconds = map(to_seconds,odom_readings)
#
#print seconds


#array =[('1202163225738', 10), ('1202163225738', 10), ('1202163225738', 1)]
#print reduce(avg, array)


#dict_x = ({})
#
#def to_k_v(arr_of_arr):
#    for k in arr_of_arr:
#        key = str(int(k[0])/1000)
#        if dict_x.has_key(key)
#            dict_x[key].append([])
#            dict_x[key][-1] =
#
#dict()

#dict = map(dict(arr), arr)
#print dict



#
#from sys import argv
#script, filename = argv
#txt = open(filename)
#print "Here's your file %r:" % filename
#print txt.read()
#print "I'll also ask you to type it again:"
#file_again = raw_input("> ")
#txt_again = open(file_again)
#print txt_again.read()



#
#
#
#
#
#a = [1, 2, 3 , 4, 5]
#
#
#def foo(x):
#    return 3*x
#
##b = map(foo,a)
#
#b = map(lambda x: 3*x, a)
#
#
#
#print b
#
#
#
#def sum(x,y):
#    return x+y
#
#b = reduce(sum, b)
#
#print b
#
#


