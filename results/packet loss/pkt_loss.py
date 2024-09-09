import matplotlib.pyplot as plt

# Data for packet loss
packet_loss = {'Static System': 43.07, 'Dynamic System': 2.81}

# Extract identifiers and values
systems = list(packet_loss.keys())
values = list(packet_loss.values())

# Create the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(systems, values, color=['blue', 'green'])

# Add a title and labels
plt.title('Packet Loss in Static vs Dynamic Systems')
plt.ylabel('Packet Loss (%)')
plt.xlabel('System Type')

# Adding value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.1f}%', ha='center', va='bottom')

# Display the chart
plt.show()
