from bc import TicToc,FindE
import os
from threading import Thread

if __name__ =="__main__":
    tt=TicToc()
    tt.tic()
    n=10000000
    find_es=[]
    threads=[]
    for i in range(os.cpu_count()):
        find_es.append(FindE())
        threads.append(Thread(target=find_es[i].throw_points,args=(n,)))
        print("Started thread number #%d"%i)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    totalN=0
    numberN=0
    for value_of_e in find_es:
        totalN+= value_of_e.sumOfN
        numberN+=value_of_e.N
    print("e=%12.8f| N=%d / %d|TIME=%.5f seconds"%((totalN/numberN),numberN,totalN,tt.toc()))