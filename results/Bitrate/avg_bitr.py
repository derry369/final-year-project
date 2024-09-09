import matplotlib.pyplot as plt

# Example average bitrate values in kbps (six decimal places)
average_bitrate_static_kbps = 1998.152415  # Replace with your actual value
average_bitrate_dynamic_kbps = 2842.958536  # Replace with your actual value

# Convert kbps to Mbps and round to two decimal places
average_bitrate_static_mbps = round(average_bitrate_static_kbps / 1000, 2)
average_bitrate_dynamic_mbps = round(average_bitrate_dynamic_kbps / 1000, 2)

# Identifiers for the bar chart
identifiers = ['Static', 'Dynamic']

# Average bitrate values in Mbps
average_bitrate_values = [average_bitrate_static_mbps, average_bitrate_dynamic_mbps]

# Create a bar chart
plt.figure(figsize=(8, 6))
colors = ['#1f77b4', '#ff7f0e']  # Choose your colors for the bars

plt.bar(identifiers, average_bitrate_values, color=colors)

# Add labels and title
plt.xlabel('System Type')
plt.ylabel('Average Bitrate (Mbps)')
plt.title('Average Bitrate Comparison Between Static and Dynamic Systems')

# Show values on top of bars
for i, value in enumerate(average_bitrate_values):
    plt.text(i, value + 0.05, f'{value} Mbps', ha='center', va='bottom')

# Show the plot
plt.show()
