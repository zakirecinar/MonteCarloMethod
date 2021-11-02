import time
import random
from numba import jit

class TicToc:
    def __init__ (self):
        self.t1=0
        self.t2=0
    def tic(self):
        self.t1=time.time()
    def toc(self):
        self.t2=time.time()
        return self.t2-self.t1
class FindE:
    def __init__ (self):
        self.sumOfN=0
        self.N=0
    def throw_points(self,nn):
        (self.sumOfN,self.N)=self.throw_points_static(nn)
    @staticmethod
    @jit(nopython=True, nogil=True)
    def throw_points_static(nn):
        sumOfR = 0
        R = 0
        for _ in range(nn):
            R=0
            sumOfR=0
            while sumOfR < 1:
                r = random.random()
                sumOfR += r
                R += 1

            sumOfN += R
            N += 1
        return N,sumOfN

    def value_of_e(self):
        return self.sumOfN / self.N






