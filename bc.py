import random
import time


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindE:
    def __init__(self):
        self.sumOfN = 0
        self.sumOfR = 0
        self.R=0
        self.N=0

    def throw_points(self, nn):
        for _ in range(nn):
            self.sumOfR = 0
            self.R=0
            #k = 10000
            while self.sumOfR < 1:
                r = random.random()
                self.sumOfR += r
                self.R += 1
            self.sumOfN += self.R
            self.N+=1
        #print(self.sumOfN)



    def value_of_e(self):
        return self.sumOfN/self.N
