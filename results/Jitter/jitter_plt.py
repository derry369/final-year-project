import matplotlib.pyplot as plt

# Average jitter values in seconds
jitter_static = 0.001315  # Example value
jitter_dynamic = 0.000710  # Example value

# Convert jitter values to milliseconds
jitter_static_ms = jitter_static * 1000
jitter_dynamic_ms = jitter_dynamic * 1000

# Data to plot
jitter_values = [jitter_static_ms, jitter_dynamic_ms]
identifiers = ['Static System', 'Dynamic System']

# Create a bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(identifiers, jitter_values, color=['green', 'orange'])

# Add text labels for each bar showing the value
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.6f} ms', ha='center', va='bottom')

# Add labels and title
plt.xlabel('System Type')
plt.ylabel('Average Jitter (ms)')
plt.title('Comparison of Average Jitter in Static and Dynamic Systems')

# Show the plot
plt.show()
