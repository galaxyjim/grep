import sys
import os
import glob

#
def ProcessFile(filename, value):
    cnt = 0
    with open(filename) as f:
        for line in f:
            cnt += 1
            if len(line) > 0 and line[-1] == '\n':
                line = line[:-1]
            if line.lower().find(value.lower()) >= 0:
                print( filename, cnt, ":", line)
            

# check parameters
if len(sys.argv) < 3:
    print( "usage: grep string file[s]")
    exit()

# process arguments
for arg in sys.argv[2:]:
    # expand argument to files
    for filename in glob.glob(arg):
        if not os.path.isfile(filename):
            continue
        ProcessFile(filename, sys.argv[1])

