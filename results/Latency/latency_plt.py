import matplotlib.pyplot as plt

# Average delay values in seconds (replace with your actual values)
average_delay_static = 7.169886  # Example value
average_delay_dynamic = 0.051832  # Example value

# Convert to milliseconds
average_delay_static_ms = average_delay_static * 1000
average_delay_dynamic_ms = average_delay_dynamic * 1000

# Data for plotting
systems = ['Static', 'Dynamic']
delays = [average_delay_static_ms, average_delay_dynamic_ms]

# Create a bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(systems, delays, color=['skyblue', 'salmon'])

# Adding values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f} ms', ha='center', va='bottom')

# Labeling the chart
plt.xlabel('System Type')
plt.ylabel('Average Delay (ms)')
plt.title('Comparison of Average Delay Between Static and Dynamic Systems')
plt.ylim(0, max(delays) * 1.1)  # Adjusting the y-axis for better visibility

# Show plot
plt.show()
