'''
Jack:

You correctly identified that the input list nums does not change during the algorithm. That is true.

However, in this assignment, STI is focused on modeling the process of solving the problem, not just describing the input. 
The important “state” is the working state of the algorithm—the variables that evolve as you scan through the list 
(for example, current run, direction, counts, and longest run).

Your writeup treats these as descriptions of the list, but they are actually the mechanism that allows the computation to happen. 
Because of that, your transitions section is incomplete: transitions should describe how this working state changes 
(e.g., when a run continues, ends, or switches direction).

The good news is that your code does implement these transitions correctly—you just didn’t express them in STI terms.

How to improve:

Keep your assumptions (they are strong)
Redefine “state” to include the tracking variables used during the scan
Describe transitions as how those variables change at each step

If you align your STI description with what your code is already doing, this would be a very strong submission.

Grade B+

'''
