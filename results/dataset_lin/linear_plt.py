import pandas as pd

# Load your data and select relevant columns
data = pd.read_csv('traffic_log.csv')

# Keep only relevant columns
relevant_data = data[['Packet Size (bytes)', 'Inter-Departure Rate (packets/second)', 'Bandwidth Required (Mbps)']]

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Packet Size (bytes)', y='Bandwidth Required (Mbps)', data=relevant_data)
plt.title('Packet Size vs Bandwidth')
plt.xlabel('Packet Size (bytes)')
plt.ylabel('Bandwidth Required (Mbps)')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Inter-Departure Rate (packets/second)', y='Bandwidth Required (Mbps)', data=relevant_data)
plt.title('Inter-Departure Rate vs Bandwidth')
plt.xlabel('Inter-Departure Rate (packets/second)')
plt.ylabel('Bandwidth Required (Mbps)')
plt.show()
