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
    
    def log_prior(self, beta):
        return np.sum(stats.norm.logpdf(beta, self.prior_mean, np.sqrt(self.prior_variance)))

    def log_posterior(self, beta):
        return self.log_prior(beta) + self.log_likelihood(beta)
    
    def find_map_estimate(self):
        initial_beta = np.zeros(self.n_features)
        result = optimize.minimize(lambda beta: -self.log_posterior(beta), initial_beta)
        self.beta_map = result.x
        return self.beta_map
    
    def metropolis_hastings(self, iterations = 5000, step_size = 0.1, burn_in = 1000):
        if self.beta_map is None:
            raise ValueError("Map estimate not found")
        
        beta_samples = [self.beta_map]
        current_log_post = self.log_posterior(self.beta_map)

        for i in range(iterations):
            proposal = beta_samples[-1] + np.random.normal(0, step_size, size= self.beta_map.shape)
            proposal_log_post = self.log_posterior(proposal)

            acceptance_prob = np.exp(proposal_log_post - current_log_post)
            if acceptance_prob > np.random.rand():
                beta_samples.append(proposal)
                current_log_post = proposal_log_post
            else:
                beta_samples.append(beta_samples[-1])

        self.beta_samples = np.array(beta_samples[burn_in:])
        return self.beta_samples
    
    def plot_posterior_distributions(self):
        if self.beta_samples is None:
            raise ValueError("MCMC sampling not done. Run metropolis_hastings() first.")
        
        for i in range(self.n_features):
            plt.hist(self.beta_samples[:, i], bins=30, alpha=0.5, label=f'Beta {i}')
        plt.legend()
        plt.show()

    def posterior_predictive_check(self):
        if self.beta_samples is None:
            raise ValueError("MCMC sampling not done. Run metropolis_hastings() first.")
        
        pred_probs = self.sigmoid(np.dot(self.X, self.beta_samples.T).mean(axis=1))
        plt.scatter(self.X[:, 1], self.X[:, 2], c=pred_probs, cmap='viridis', alpha=0.5)
        plt.colorbar(label='Predicted probability')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('Posterior Predictive Check')
        plt.show()

np.random.seed(42)
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)
X = ( X - X.mean(axis=0)) / X.std(axis=0)
X = np.hstack([np.ones((X.shape[0],1)), X])

blr = BayesianLogisticRegression(X, y)

beta_map = blr.find_map_estimate()
print("MAP Estimate:", beta_map)

beta_samples = blr.metropolis_hastings()

blr.plot_posterior_distributions()

blr.posterior_predictive_check()