import numpy as np


def jaccard_stability(fea_final):
    runs , features = fea_final.shape

    r= np.empty((runs, runs,)) * np.nan
    rr= np.empty((runs, runs,)) * np.nan

    t = 0
    for n in range(runs - 1):
        for m in range(n+1,runs):
            t = t + 1
            r[n, m] = len(set.intersection(set(fea_final[n, :]), set(fea_final[m, :])))
            rr[n, m] = len(set.union(set(fea_final[n, :]), set(fea_final[m, :])))
        #end
    #end

    a = np.divide(r, rr)
    a1 = np.nan_to_num(a)

    return np.sum(a1) / t