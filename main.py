# import sklearn

def load_labels(f):
    labels = []
    length = 0
    with open(f) as f:
        for line in f:
            length += 1
            line = line.strip('\n')
            labels.append(float(line))
    return labels, length

def load_features(f):
    features=[]
    

if __name__ == "__main__":
    # print(load_labels('resources/wellness_nonverbal_condition_lable.csv'))
