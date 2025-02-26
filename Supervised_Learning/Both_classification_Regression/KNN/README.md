# KNN (K - Nearest Neighbours)

It is one of the most simplest and most intuitive algorithm used in machine learning for classification and regression task.
KNN is a non parametric lazy learning algorithm .

### Lazy Learning 

It doesn't compute the discriminating function during the training phase but instead it memorises the training data and computes during the prediction phase. Hence the name lazy learner

KNN works by comparing the new input data points with the data points in the training dataset that are closest in feature space.

KNN Working

1) Choose the number k , i.e k is the number of nearest neighbours to consider.
2) calculate the distance using methods such as

   
   Euclidean Distance


   manhattan distance


   Minkowski distance : generalisation form which includes both euclidean and manhattan distance as special cases


   Hamming distance.
4) Sort the distances.
5) pick the nearest neighbours.
6) Vote for classification task , Average for regression task.


## Advantages of KNN

Simple and intuitive


No training period


Adaptable to new data

## Disadvantages of KNN

Computationally expensive (comparing the input point with all other points in the dataset)


Slow


Memory intensive


sensitivity to irrelevant features


choice of K


not scalable.
