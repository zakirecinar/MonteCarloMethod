from bc import TicToc,FindE
if __name__=="__main__":
    tt=TicToc()
    tt.tic()
    finding_e=FindE()
    finding_e.throw_points(100000)
    e=finding_e.value_of_e()
    print("e=%12.8f|sum of N=%d| sum of R=%d|number of N=%d|number Of R=%d"%(e,finding_e.sumOfN,finding_e.sumOfR,finding_e.N,finding_e.R))
    print("TIME=%.6f seconds"%(tt.toc()))