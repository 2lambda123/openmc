#!/usr/bin/env python

import sys
import numpy as np

sys.path.insert(0, '../../src/utils')

from openmc.statepoint import StatePoint

# read in statepoint file
if len(sys.argv) > 1:
    sp = StatePoint(sys.argv[1])
else:
    sp = StatePoint('statepoint.19.binary')

sp.read_results()

# extract tally results and convert to vector
sum1 = sp._tallies[1]._sum
sum_sq1 = sp._tallies[1]._sum_sq
results1 = np.concatenate([sum1, sum_sq1])

sum2 = sp._tallies[2]._sum
sum_sq2 = sp._tallies[2]._sum_sq
results2 = np.concatenate([sum2, sum_sq2])

results = np.concatenate([results1.flatten(), results2.flatten()])

# set up output string
outstr = ''
 
# write out k-combined
outstr += 'k-combined:\n'
outstr += "{0:12.6E} {1:12.6E}\n".format(sp.k_combined[0], sp.k_combined[1])

# write out tally results
outstr += 'tallies:\n'
for item in results:
  outstr += "{0:12.6E}\n".format(item)

# write results to file
with open('results_test.dat','w') as fh:
    fh.write(outstr)
