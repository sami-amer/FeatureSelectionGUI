import scipy.io
import numpy as np
import pandas as pd
from math import log
from statistics import mean, stdev
from sklearn.model_selection import train_test_split
from skfeature.function.statistical_based import t_score
from jaccard_stability import jaccard_stability




def tTest(X,y,runs,ens):
    n_samples, n_features = np.shape(X)
    n_labels = np.shape(y)
    sel_features = int(log(n_features,2)) # edit this for feature selections
    print(sel_features)
    testSize = 0.2 #this should pull from GUI


    FeatSel = np.zeros((ens, sel_features))
    Fvotes = np.zeros((1, n_features))
    fea_final = np.zeros((runs, sel_features))
    for run in range(runs):
        for en in range(ens):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testSize) # train test split code

            # print(Xd_train.shape)
            # print(y_train.shape)
            
            score = t_score.t_score(X_train, y_train)
            # print(score)
            FeatSel[en, :] = score[0:sel_features]
        
        Fvotes = [np.count_nonzero(FeatSel == x) for x in range(n_features)]

        idxs = np.array(Fvotes).argsort()[::-1][:n_features]
        fea_final[run,:] = idxs[0:sel_features]

    # test stability
    JI = jaccard_stability(fea_final)
    print ('jaccard=', JI)
    np.savetxt('Ttest_fea_final.csv', fea_final, delimiter=',',fmt='%d')

if __name__ == "__main__":
    features = pd.read_csv(r'resources\wellness_nonverbal_features.csv')
    labels = pd.read_csv(r'resources\wellness_nonverbal_condition_lable.csv')
    X = features.to_numpy()
    y = labels.to_numpy()
    y = y.reshape((y.shape[0],))
    runs = 10
    ens = 100 #folds?
    tTest(X,y,runs,ens)