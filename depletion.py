import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# Simulation parameters
initial_clients = 120  # Initial number of clients
target_clients = 7000  # Final number of clients
adoption_duration_days = 4 * 365  # 4 years in days
slope = 0.008  # Growth rate for logistic function

# Logistic growth function for user adoption
def logistic_growth(t, start, end, growth_rate, duration):
    return start + (end - start) / (1 + np.exp(-growth_rate * (t - duration / 2)))

# Generate time period
days = np.arange(adoption_duration_days)
clients_over_time = np.array([logistic_growth(t, initial_clients, target_clients, slope, adoption_duration_days) for t in days])

# Compute daily new clients (derivative of logistic function)
daily_new_clients = np.diff(clients_over_time, prepend=clients_over_time[0])

# Generate deposits using a truncated normal distribution
np.random.seed(42)
mu, sigma = 5000, 7000  # Mean and standard deviation
lower, upper = 500, 50000  # Truncation bounds
deposit_distribution = truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
base_deposits = deposit_distribution.rvs(len(days))

# Scale deposits by the number of new clients each day
deposits = base_deposits * (daily_new_clients / daily_new_clients.max())

# Plot deposit distribution
plt.figure(figsize=(12, 6))
plt.hist(deposits, bins=50, color='purple', alpha=0.7, edgecolor='black')
plt.xlabel("Deposit Amount (USD)")
plt.ylabel("Frequency")
plt.title("Distribution of Investment Deposits")
plt.show()

# Generate cumulative deposit arrivals over time
cumulative_deposits = np.cumsum(deposits)

# Plot deposit arrivals over time with cumulative deposits
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(days, deposits, color='orange', label="Daily Deposits")
ax1.set_xlabel("Days")
ax1.set_ylabel("Deposit Amount (USD)")
ax1.legend(loc="upper left")

ax2 = ax1.twinx()
ax2.plot(days, cumulative_deposits, color='brown', label="Cumulative Deposits")
ax2.set_ylabel("Cumulative Deposit Amount (USD)")
ax2.legend(loc="upper right")

plt.title("Daily and Cumulative Deposits Over Time")
plt.show()
