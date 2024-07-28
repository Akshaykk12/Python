import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.randn(100,1)
y = 3 * X[:, 0] + np.random.randn(100)
# print(X, X.shape)
# print(y, y.shape)

X= np.column_stack((np.ones(X.shape[0]), X))
# print(X, X.shape)

beta_prior_mean = np.zeros(X.shape[1])
beta_prior_cov = np.eye(X.shape[1]) * 10
# print(beta_prior_mean)
# print(beta_prior_cov)

sigma2 = 1
beta_post_cov = np.linalg.inv(np.linalg.inv(beta_prior_cov) + (X.T @ X) / sigma2)
beta_post_mean = beta_post_cov @ (np.linalg.inv(beta_prior_cov) @ beta_prior_mean + (X.T @ y) / sigma2)

X_new = np.linspace(-3, 3, 100)
X_new = np.column_stack((np.ones(X_new.shape[0]), X_new))

y_pred_mean = X_new @ beta_post_mean

y_pred_var = np.array([X_new[i] @ beta_post_cov @ X_new[i].T for i in range(X_new.shape[0])]) + sigma2
y_pred_std = np.sqrt(y_pred_var)

plt.figure(figsize=(10, 6))
plt.scatter(X[:, 1], y, c='blue', label='Data')
plt.plot(X_new[:, 1], y_pred_mean, 'r-', label='Predictive mean')
plt.fill_between(X_new[:, 1], y_pred_mean - 1.96 * y_pred_std, y_pred_mean + 1.96 * y_pred_std, color='red', alpha=0.3, label='95% CI')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()