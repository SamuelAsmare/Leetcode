class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.stream = []
        self.k = k
        self.sum = 0
        self.matchedvalues = 0
    def consec(self, num: int) -> bool:
        self.sum += num
        if num==self.value:
            self.matchedvalues += 1
        else:
            self.matchedvalues = 0
        return self.matchedvalues >= self.k

        