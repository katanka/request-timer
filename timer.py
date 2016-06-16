import requests
import time
from tqdm import tqdm
import sys
import numpy as numpy
import matplotlib.pyplot as plt
import random

times = []

def mean(input):
	return float(sum(input))/len(input) if len(input) > 0 else float('nan')

if len(sys.argv) != 3:
	print 'Usage: python timer.py [URL] [sample size]'
	exit()

print "Timing requests to " + sys.argv[1]

r = requests.get(sys.argv[1])
r.content

for x in tqdm(xrange(1,int(sys.argv[2])+1)):
	start = time.time()
	r = requests.get(sys.argv[1])
	r.content  # wait until full content has been transfered
	roundtrip = time.time() - start
	times.append(roundtrip)

print "Done!\n\nStatistics:"

n, bins, patches = plt.hist(times, 50, facecolor='green', alpha=0.75)

xMax = max(times)*1.1
yMax = max(n)*1.25

plt.xlabel('Request Time (s)')
plt.ylabel('Count')
plt.title(r'$\mathrm{Histogram\ of\ Request Times}$')
plt.axis([0, xMax, 0, yMax])
plt.grid(True)

plt.text(xMax*0.04, yMax*0.9, "Average time: %.2f s" % mean(times), style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

plt.show()


