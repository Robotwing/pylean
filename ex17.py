from sys import argv
from os.path import exists

script,from_file,to_file= argv

indata = open(from_file).read();

print "There are %s bytes." % len(indata)
print "Dose outfile exist? %r" %exists(to_file)
outdata = open(to_file,'w').write(indata);
