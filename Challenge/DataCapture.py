class DataCapture():
    '''
    For this Class I will use a Build Stats method and a queue since its specified in the skeleton, but
    the build stats is redundant since I will handle the stats with a list of 0-1000 with the frecuency of
    those numbers in a tuple.
    A better approach would be a binary search but that is not valid for this challenge since that library pretty
    much does everything.
    O(1) will be achieved on each method except add by iterating through the entire list so the output its constant
    regardless of the input, but since we have an orderded list, we could just slice instead (my initial thoughts
    when designing this).
    '''

    def __init__(self):
        # Stats will be a list since a list makes lookup easier for ranges.
        self.stats = [(x, 0) for x in range(0, 1000)]
        self.queue = list()

    def add(self, val: int):
        if type(val) != int:
            raise TypeError
        self.queue.append(val)
        print(f"Element {val} added")

    def build_stats(self):
        if self.queue:
            for ele in self.queue:
                self.stats[ele] = (ele, self.stats[ele][1] + 1)
            print(f"Stats built correctly")
        else:
            print(f"Empty queue")
        return self

    def less(self, val: int) -> int:
        result = 0
        for ele in self.stats:
            if ele[0] == val or ele[0] > val:
                continue
            result += ele[1]
        print(f"Result: {result}")
        return result

    def greater(self, val: int) -> int:
        result = 0
        for ele in self.stats:
            if ele[0] == val or ele[0] < val:
                continue
            result += ele[1]
        print(f"Result: {result}")
        return result

    def between(self, start: int, finish: int) -> int:
        result = 0
        for ele in self.stats:
            if ele[0] < start or ele[0] > finish:
                continue
            result += ele[1]
        print(f"Result: {result}")
        return result
