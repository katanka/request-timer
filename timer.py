import requests
import time
from tqdm import tqdm
import sys

times = []

def mean(input):
	return float(sum(input))/len(input) if len(input) > 0 else float('nan')

if len(sys.argv) != 3:
	print 'Usage: python timer.py [URL] [sample size]'

print "Timing requests to " + sys.argv[1]

for x in tqdm(xrange(1,int(sys.argv[2])+1)):
	start = time.time()
	r = requests.get(sys.argv[1])
	r.content  # wait until full content has been transfered
	roundtrip = time.time() - start
	times.append(roundtrip)

print "Done!\n\nStatistics:"

print "Average time: %.2f s" % mean(times)

