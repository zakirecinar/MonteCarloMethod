import random
import time
start_time=time.time()
sumOfN=0
k=10000
for _ in range(k):
    R=0
    sumOfR=0
    while sumOfR < 1:
        r = random.random()
        sumOfR +=r
        R+=1
    sumOfN +=R
print(sumOfN)
e=sumOfN/k
print(e)
end_time=time.time()
print("Time= %.5f"%(end_time-start_time))
