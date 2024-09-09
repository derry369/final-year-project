import matplotlib.pyplot as plt

# Function to import and process data from a .dat file
def import_and_process_data(filename):
    time = []
    bitrate_kbps = []
    
    with open(filename, 'r') as file:
        # Skip the header line
        next(file)
        
        for line in file:
            columns = line.split()
            time.append(float(columns[0]))  # Time in seconds
            bitrate_kbps.append(float(columns[1]))  # Bitrate in kbps
    
    # Convert bitrate from kbps to Mbps, keeping two decimal places
    bitrate_mbps = [round(b / 1000, 2) for b in bitrate_kbps]
    
    return time, bitrate_mbps

# Import data for static and dynamic systems
time_static, bitrate_static_mbps = import_and_process_data('st_bitrate.dat')
time_dynamic, bitrate_dynamic_mbps = import_and_process_data('dy_bitrate.dat')

# Plot the data
plt.figure(figsize=(10, 6))

# Plot static system bitrate
plt.plot(time_static, bitrate_static_mbps, label='Static System', color='blue', linestyle='-')

# Plot dynamic system bitrate
plt.plot(time_dynamic, bitrate_dynamic_mbps, label='Dynamic System', color='orange', linestyle='--')

# Add labels and title
plt.xlabel('Time (seconds)')
plt.ylabel('Bitrate (Mbps)')
plt.title('Bitrate Evolution Over Time for Static and Dynamic Systems')

# Add a legend
plt.legend()

plt.grid(True)  # Add grid for better readability

# Show the plot
plt.show()
