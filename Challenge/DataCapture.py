from collections import OrderedDict

class DataCapture():
    '''
    This Class will implement a queue to Keep O(1) on add method.
    For less, greater and between a dictionary is built with the stats, to keep it O(1).
    For the build stats we have two loops (independent, not nested) so while it becomes O(2n), in practice O(2n)
    becomes O(n).
    '''

    def __init__(self):
        # Stats will be a list since a list makes lookup easier for ranges.
        self.stats = dict()
        self.less_dict = dict()
        self.less_counter = 0
        self.greater_dict = dict()
        self.greater_counter = 0
        self.num_index = list()
        self.data = dict()
        self.queue = list()
        self.queue_size = 0

    def add(self, val: int):
        if type(val) != int:
            raise TypeError
        self.queue.append(val)
        # self.data[val] =  self.data.get(val, 0) + 1
        print(f"Element {val} added")

    def build_stats(self):
        if self.queue:
            # In these loops we build a simple dict with the numbers on queue and their frequency
            for ele in self.queue:
                self.data[ele] = self.data.get(ele, 0) + 1
            self.data = OrderedDict(sorted(self.data.items()))
            self.num_index = list(self.data.keys())
            self.greater_counter = len(self.queue)
            self.queue_size = len(self.queue)
            # In this loop we start building the stats on the less and greater dictionary. We use the first dictionary
            # to build lesser and greater stats correctly according to the frecuency of the values added.
            for ele in range(0,1000):
                if self.num_index:
                    if ele < self.num_index[0]:
                        self.less_dict[ele] = self.less_counter
                        self.greater_dict[ele] = self.greater_counter
                    else:
                        self.less_dict[ele] = self.less_counter
                        self.num_index.pop(0)
                        self.less_counter += self.data[ele]
                        self.greater_counter -= self.data[ele]
                        self.greater_dict[ele] = self.greater_counter
                else:
                    self.less_dict[ele] = self.greater_counter
                    self.greater_dict[ele] = 0
            print(f"Stats built correctly")
        else:
            print(f"Empty queue")
        return self

    def less(self, val: int) -> int:
        if type(val) != int:
            raise TypeError
        result = self.less_dict[val]
        print(f"Result: {result}")
        return result

    def greater(self, val: int) -> int:
        if type(val) != int:
            raise TypeError
        result = self.greater_dict[val]
        print(f"Result: {result}")
        return result

    def between(self, start: int, finish: int) -> int:
        if type(start) != int or type(finish) != int:
            raise TypeError
        result = self.queue_size - self.less_dict[start - 1] - self.greater_dict[finish + 1]
        print(f"Result: {result}")
        return result
