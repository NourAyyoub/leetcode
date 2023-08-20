import random

class RandomizedSet(object):

    def __init__(self):
        self.data = []

    def insert(self, val):
        if val not in self.data:
            self.data.append(val)
            return True
        return False

    def remove(self, val):
        if val in self.data:
            self.data.remove(val)
            return True
        return False

    def getRandom(self):
        if len(self.data) > 0:
            return random.choice(self.data)
        return None 