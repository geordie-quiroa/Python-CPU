class registers:
    inUse = 0

    def __init__(self, n=0):
        if n == 0:
            self.storedValue = n
        else:
            self.storedValue = n
            registers.inUse += 1

    def clearRegistry(self):
        self.storedValue = 0
        registers.inUse -= 1

    def withValue(self):
        if self.storedValue > 0:
            return 1
        else:
            return 0