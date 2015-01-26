#!/usr/bin/python
from operator import itemgetter
import re
import random

def dict_items_sorted_by_value(d, reverse=True):
    return sorted(d.iteritems( ), key=itemgetter(1), reverse=reverse)

def random_n( n ):
    return random.choice( range(n) )

# read all lines into memory
N = 25
modified_count = N
filename = 'coding-test-v4-data.txt'
file = open( filename )
full_dict = {}
last_dict = {}
first_dict = {}
modified_list = {}
modified_lasts = []
modified_firsts = []
for line in file.readlines():
    name = re.match(r"^(\w+), (\w+)", line)
    if not name: continue
    fullname = str( name.group(1) + ", " + name.group(2) )
    lastname = name.group(1)
    firstname = name.group(2)
#    print "%d: full=%s, last=%s, first=%s" % ( i, fullname, lastname, firstname )
    if full_dict.has_key( fullname ): 
        full_dict[fullname] += 1
    else:
        full_dict[fullname] = 1

    # modified list?
    if modified_count:
        if not last_dict.has_key( lastname ) and not first_dict.has_key( firstname ):
            modified_list[fullname] = 1
            modified_lasts.append( lastname )
            modified_firsts.append( firstname )
            modified_count -= 1

    if last_dict.has_key(lastname):
        last_dict[lastname] += 1
    else:
        last_dict[lastname] = 1
    if first_dict.has_key(firstname):
        first_dict[firstname] += 1
    else:
        first_dict[firstname] = 1
file.close()
num_full = len( full_dict.keys() )
num_last = len( last_dict.keys() )
num_first = len( first_dict.keys() )

sorted_lasts = dict_items_sorted_by_value( last_dict )[0:10]
sorted_firsts = dict_items_sorted_by_value( first_dict )[0:10]

# generate N random and unique full names
final_modified = []
for i in range(N):
    while True:
        lastn = modified_lasts[ random_n( N ) ]
        firstn = modified_firsts[ random_n( N ) ]
        full = lastn + ", " + firstn
        if not modified_list.has_key( full ):
            final_modified.append( full )
            break

    

# report our results ================


"""1. The unique count of full, last, and first names (i.e. duplicates are
     counted only once)"""
print "Q1 --  Distinct Counts:  fullnames: %d, lastnames: %d, firstnames: %d\n" % (num_full, num_last, num_first)


"""  2. The ten most common last names (the names and number of occurrences -
     choose arbitrarily if there are ties)"""
print "Q2 -- 10 most frequent lastnames (and counts): %s\n " % (repr( sorted_lasts ))

"""  3. The ten most common first names (the names and number of occurrences -
     choose arbitrarily if there are ties)"""
print "Q3 --  10 most frequent firstnames (and counts): %s\n" % repr( sorted_firsts )

"""  4. A list of modified names (see below for details) """
print "\nQ4 -- Modified names:"
print "\n   *** initial (unrandomized+unique) list of %d names: %s " % (N, repr(modified_list.keys()))
print "\n   *** final (randomized+unique) modified list of %d names: %s" % (N, repr( final_modified ))
