import scipy.io
import numpy as np
import pandas as pd
from math import log
from statistics import mean, stdev
from sklearn.model_selection import train_test_split
from jaccard_stability import jaccard_stability

import ccm

mat = scipy.io.loadmat("fisher.mat")

X = mat['X']
y = mat['Y'][:, 0]

n_samples, n_features = np.shape(X)
n_labels = np.shape(y)
sel_features = int(log(n_features,2))

runs = 10
ens = 100
FeatSel = np.zeros((ens, sel_features))
Fvotes = np.zeros((1, n_features))
fea_final = np.zeros((runs, sel_features))
for run in range(runs):
    for en in range(ens):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        Xd_train = np.zeros(np.shape(X_train))
        Xd_test = np.zeros(np.shape(X_test))
        for nf in range(n_features):
            edges = [min(X_train[:, nf]), mean(X_train[:, nf])-stdev(X_train[:, nf]), mean(X_train[:, nf]), mean(X_train[:, nf])+stdev(X_train[:, nf]), max(X_train[:, nf])];
            Ss = np.array(pd.cut(X_train[:, nf], edges, labels=False, include_lowest=True), dtype=np.int)
            Xd_train[:, nf] = np.array(pd.cut(X_train[:, nf], edges, labels=False, include_lowest=True), dtype=np.int)
            Xd_test[:, nf] = np.array(pd.cut(X_test[:, nf], edges, labels=False, include_lowest=True), dtype=np.int)

        score = ccm.ccm(Xd_train, y_train, sel_features, 'binary', 0.001, iterations=100, verbose=False)
        FeatSel[en, :] = np.argsort(score)[:sel_features]


    Fvotes = [np.count_nonzero(FeatSel == x) for x in range(n_features)]

    idxs = np.array(Fvotes).argsort()[::-1][:n_features]
    fea_final[run,:] = idxs[0:sel_features]

# test stability
JI = jaccard_stability(fea_final)
print ('jaccard=', JI)
np.savetxt('CCM_fea_final.csv', fea_final, delimiter=',',fmt='%d')
