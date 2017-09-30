
# NAMESPACE

# import argv from sys module to read text file as argument from command line
from sys import argv
# import strings from lingpy.compare to calculate lingpy bisim scores directly in the script
from lingpy.compare import strings
# import check_output from subprocess to get the output from the perl script
from subprocess import check_output
# import csv to write a csv file at the end of the process
import csv


# unpack argv as script and source variables
script, source = argv


#  FUNCTIONS

# open text file into file object, read lines, strip lines of whitespace and push lines into
# a list named lines_list
def makelineslist(source):
    with open(source, mode='r', encoding='utf-8', errors='strict') as input_file:
        lines = input_file.read()
    lines_list = []
    for line in lines.splitlines():
        line.strip()
        lines_list.append(line)
    return(lines_list)

# take a list of text lines and recursively compute all possible pairs
pairs = []
def pair(lines):
    if len(lines) == 1:
        return pairs
    else:
        current = lines.pop()
        for l in lines:
            pairs.append([current, l])
    return(pair(lines))
    
# compute bisim scores using lingpy, from a list of two items (pair)
# will return 3 scores
def bisim_lingpy(p):
    bisim1 = strings.bisim1(p[0],p[1],normalized=True)
    bisim2 = strings.bisim2(p[0],p[1],normalized=True)
    bisim3 = strings.bisim3(p[0],p[1],normalized=True)
    return(float(bisim1), float(bisim2), float(bisim3))
    
# compute bisim score using perl eval.pl, from a tuple of two items (pair)
# will return one score
def bisim_perl(t):
    bisim_raw = check_output(["perl", "eval.pl", p[0], p[1], "BI-SIM", "1"])
    bisim = float(bisim_raw.decode().strip())
    return(bisim)


# RUNTIME
# will return top 5 000 scores, change the upper boundary on line 74 to get a different number of results

lines_list = makelineslist(source)
pairs = pair(lines_list)

title_lines = ["string1", "string2", "lingpy_bisim1", "lingpy_bisim2", "lingpy_bisim3", "evalpl"]

for p in pairs:
    bisim1, bisim2, bisim3 = bisim_lingpy(p)
#    bisim4 = bisim_perl(p)
    p.extend([bisim1, bisim2, bisim3])#, bisim4])

# at the following line adjust the list index to choose on which score to sort
pairs = sorted(pairs, key=lambda p: p[3], reverse=False)
if len(pairs) > 5000:
    pairs = pairs[0:5000]
else:
    pass

with open('bisimoutput.csv', mode='w', newline='', encoding='utf-8', errors='strict') as output_file:
    writer = csv.writer(output_file, dialect='excel', delimiter=';')
    writer.writerow(title_lines)
    for p in pairs:
        writer.writerow(p)

    
