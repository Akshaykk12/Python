import numpy as np
import  matplotlib.pyplot as plt

class LogisticRegression:
    
    def __init__(self, learning_rate = 0.01, epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.beta = None
        self.log_likelihood_hist = []
        
    def logistic_function(self, z):
        return 1 / (1 + np.exp(-z))
    
    def predict_proba(self, X):
        z = np.dot(X, self.beta)
        return self.logistic_function(z)
        
    def log_likelihood(self, X, y):
        p = self.predict_proba(X)
        likelihood = y * np.log(p) + (1 - y) * np.log(1 - p)
        return sum(likelihood)
    
    def gradient(self, X, y):
        p = self.predict_proba(X)
        gradient = np.dot(X.T, (y - p))
        return gradient
    
    def fit(self, X, y):
        n_sample, n_features = X.shape
        self.beta = np.zeros(n_features)

        for i in range(self.epochs):
            grad = self.gradient(X, y)
            self.beta += self.learning_rate * grad

            log_likelihood = self.log_likelihood(X, y)
            self.log_likelihood_hist.append(log_likelihood)

            if i % 100 == 0:
                print(f'Iteration {i}, Log- Likelihood: {log_likelihood}')
    
    
    
    def predict(self, X, threshold = 0.5):
        return self.predict_proba(X) >= threshold
    

    
np.random.seed(0)
n_sample = 1000
n_features = 2

X = np.random.rand(n_sample, n_features)
X = np.hstack((np.ones((n_sample, 1)), X))

beta_true = np.array([1,2,-1])

z = np.dot(X, beta_true)
p = LogisticRegression().logistic_function(z)
y = np.random.binomial(1, p)

model = LogisticRegression(learning_rate=0.01, epochs=1000)
model.fit(X, y)

print("Estimated Parameters:", model.beta)
