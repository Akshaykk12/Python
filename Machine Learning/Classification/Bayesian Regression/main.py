import numpy as np
import scipy.stats as stats
import scipy.optimize as optimize
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

class BayesianLogisticRegression :

    def __init__(self, X, y, prior_mean=0, prior_variance=100):
        self.X = X
        self.y = y
        self.prior_mean = prior_mean
        self.prior_variance = prior_variance
        self.n_sample , self.n_features = X.shape
        self.beta_map = None
        self.beta_sample = None

    def sigmoid(self, z):
        return 1 / (np.exp(-z) + 1)
    
    def log_likelihood(self, beta):
        z = np.dot(self.X , beta)
        return np.sum(self.y * z - np.log(1+ np.exp(z)))

np.random.seed(42)
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)
X = ( X - X.mean(axis=0)) / X.std(axis=0)
X = np.hstack([np.ones((X.shape[0],1)), X])

blr = BayesianLogisticRegression(X, y)