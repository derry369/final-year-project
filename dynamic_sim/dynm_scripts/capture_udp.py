import subprocess
import re
import math
import os

def capture_packets(interface, dst_ip, dst_port, pcap_file, packet_count=5):
    # Command to capture packets using tcpdump
    tcpdump_command = [
        'sudo', 'tcpdump', '-i', interface, 'dst', dst_ip, 'and', 'dst port', str(dst_port),
        '-c', str(packet_count), '-w', pcap_file
    ]
    
    print(f"Capturing {packet_count} packets on {interface}...")
    subprocess.run(tcpdump_command, check=True)
    print(f"Packets captured and saved to {pcap_file}.")

def extract_packet_info(pcap_file):
    # Command to read the pcap file and get the packet details
    tcpdump_read_command = ['sudo', 'tcpdump', '-nn', '-r', pcap_file]
    
    result = subprocess.Popen(tcpdump_read_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()
    packet_lines = stdout.decode('utf-8').splitlines()

    total_packet_size = 0
    timestamps = []
    packet_count = 0
    pattern = re.compile(r'bad length (\d+)')

    for line in packet_lines:
        # Find the "bad length" in the packet
        match = pattern.search(line)
        if match:
            packet_size = int(match.group(1))
            total_packet_size += packet_size
            
            # Extract timestamp from the beginning of the line
            timestamp = line.split(' ')[0]
            timestamps.append(float(timestamp.split(':')[-1]))  # Take the seconds part
            packet_count += 1

    # Calculate the average packet size
    avg_packet_size = total_packet_size / packet_count if packet_count > 0 else 0
    
    # Calculate the inter-departure rates and average it
    total_inter_departure_rate = 0
    for i in range(1, len(timestamps)):
        elapsed_time = timestamps[i] - timestamps[i-1]
        inter_departure_rate = 1 / elapsed_time if elapsed_time > 0 else 0
        total_inter_departure_rate += inter_departure_rate
    
    avg_inter_departure_rate = (total_inter_departure_rate / (packet_count - 1)) if packet_count > 1 else 0
    
    # Round to the nearest whole number
    avg_packet_size = int(round(avg_packet_size))
    avg_inter_departure_rate = int(round(avg_inter_departure_rate))
    
    return avg_packet_size, avg_inter_departure_rate

def predict_bandwidth(packet_size, inter_departure_rate):
    try:
        # Run the prediction script and capture the output
        bandwidth_output = subprocess.check_output(
            ["python", "tst_Breg.py", str(packet_size), str(inter_departure_rate)],
            universal_newlines=True
        )

        # Extract the numeric part from the output
        bandwidth_str = bandwidth_output.strip().split(':')[-1].strip()

        # Convert the extracted value to a float and round to 2 decimal places
        bandwidth = round(float(bandwidth_str), 2)
        return bandwidth
    except Exception as e:
        print("Error during bandwidth prediction: %s" % e)
        return 1.00  # Default value if prediction fails

def apply_bandwidth(ip_address, bandwidth):
    try:
        # Format the bandwidth with 2 decimal places
        formatted_bandwidth = "{:.2f}".format(bandwidth)
        cmd = ["sudo", "python", "dymn_adj.py", "ap1-wlan1", "--stations", f"{ip_address}={formatted_bandwidth}mbit"]
        subprocess.check_call(cmd)
        print(f"Adjusted bandwidth for {ip_address} to {formatted_bandwidth} Mbit")
    except Exception as e:
        print("Error during bandwidth adjustment: %s" % e)

def main():
    interface = 'ap1-wlan1'
    dst_ip = '10.0.0.4'  # Replace with the desired destination IP
    dst_port = 8999           # Replace with the desired destination port
    pcap_file = 'capture.pcap'    

    os.system('sudo tc qdisc del dev ap1-wlan1 root')

    # Capture packets
    capture_packets(interface, dst_ip, dst_port, pcap_file)
    
    # Extract and average packet sizes and inter-departure rates
    avg_packet_size, avg_inter_departure_rate = extract_packet_info(pcap_file)
    
    # Predict the required bandwidth
    bandwidth = predict_bandwidth(avg_packet_size, avg_inter_departure_rate)
    
    # Apply the bandwidth adjustment
    apply_bandwidth(dst_ip, bandwidth)
    
    # Display the results
    print("\nAverage Packet Size (in bytes):")
    print(avg_packet_size)
    
    print("\nAverage Inter-Departure Rate (packets per second):")
    print(avg_inter_departure_rate)
    
    print("\nPredicted Bandwidth (in Mbit/s):")
    print(bandwidth)

if __name__ == '__main__':
    main()
