import numpy as np
import pandas as pd

# Specify the mean and standard deviation of your x and y variables
mean = [0, 0]
std_dev = [1, 1]

# Specify the desired correlation
corr = 0.5

# Create the covariance matrix
cov = [[std_dev[0]**2, std_dev[0]*std_dev[1]*corr], 
       [std_dev[0]*std_dev[1]*corr, std_dev[1]**2]]

# Generate the samples
samples = np.random.multivariate_normal(mean, cov, 1000)

# Convert to DataFrame
df = pd.DataFrame(samples, columns=['x', 'y'])

# Save to csv
df.to_csv('data.csv', index=False)
