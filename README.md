To run this repo, please install pytest, or run `pip install -r requirements.txt`

Explanation of solution:

This Class will implement a queue to Keep O(1) on add method.
For less, greater and between a dictionary is built with the stats, to keep it O(1).
For the build stats we have two loops (independent, not nested) so while it becomes O(2n), in practice O(2n)
becomes O(n).
