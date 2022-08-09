To run this repo, please install pytest, or run `pip install -r requirements.txt`

Explanation of solution:

For this Class I will use a Build Stats method and a queue since its specified in the skeleton, but
the build stats is redundant since I will handle the stats with a list of 0-1000 with the frecuency of
those numbers in a tuple.
A better approach would be a binary search but that is not valid for this challenge since that library pretty
much does everything.
O(1) will be achieved on each method except add by iterating through the entire list so the output its constant
regardless of the input, but since we have an orderded list, we could just slice instead (my initial thoughts
when designing this).