import subprocess
import re
import math
import os

def capture_packets(interface, dst_ip, dst_port, pcap_file, packet_count=5):
    # Command to capture packets using tcpdump
    tcpdump_command = [
        'sudo', 'tcpdump', '-i', interface, 'dst', dst_ip, 'and', 'dst port', str(dst_port), '-c', str(packet_count), '-w', pcap_file
    ]
    print(f"Capturing {packet_count} packets on {interface}...")
    subprocess.run(tcpdump_command, check=True)
    print(f"Packets captured and saved to {pcap_file}.")

def extract_packet_info(pcap_file):
    # Command to read the pcap file and get the packet details
    tcpdump_read_command = ['tcpdump', '-nn', '-r', pcap_file]
    result = subprocess.run(tcpdump_read_command, stdout=subprocess.PIPE, universal_newlines=True)
    
    packet_sizes = []
    timestamps = []
    
    # Regular expression to match the length field in TCP packets
    length_pattern = re.compile(r'length (\d+)')
    
    for line in result.stdout.splitlines():
        # Match packet size
        length_match = length_pattern.search(line)
        if length_match:
            packet_size = int(length_match.group(1))
            packet_sizes.append(packet_size)
            
            # Extract timestamp from the beginning of the line
            timestamp_str = line.split()[0]
            h, m, s = map(float, timestamp_str.split(':'))
            timestamp = h * 3600 + m * 60 + s
            timestamps.append(timestamp)
    
    # Calculate average packet size
    avg_packet_size = round(sum(packet_sizes) / len(packet_sizes), 2) if packet_sizes else 0
    
    # Calculate inter-departure rate (packets per second)
    if len(timestamps) > 1:
        inter_departure_times = [
            timestamps[i + 1] - timestamps[i] for i in range(len(timestamps) - 1)
        ]
        avg_inter_departure_rate = round(1 / (sum(inter_departure_times) / len(inter_departure_times)), 2) if inter_departure_times else 0
    else:
        avg_inter_departure_rate = 0

    # Round to the nearest whole number
    avg_packet_size = int(round(avg_packet_size))
    avg_inter_departure_rate = int(round(avg_inter_departure_rate))    

    return avg_packet_size, avg_inter_departure_rate

def predict_bandwidth(packet_size, inter_departure_rate):
    try:
        result = subprocess.run(
            ["python", "usePolyReg.py", str(packet_size), str(inter_departure_rate)],
            stdout=subprocess.PIPE, universal_newlines=True
        )
        # Extracting the bandwidth value from the script output
        bandwidth = float(re.search(r'Predicted Bandwidth \(Mbps\): ([\d.]+)', result.stdout).group(1))
        return round(bandwidth, 2)
    except Exception as e:
        print(f"Error during bandwidth prediction: {e}")
        return 1.00  # Default value if prediction fails

def apply_bandwidth(ip_address, bandwidth):
    try:
        formatted_bandwidth = "{:.2f}".format(bandwidth)
        cmd = ["sudo", "python", "dymn_adj.py", "ap1-wlan1", "--stations", f"{ip_address}={bandwidth}mbit"]
        subprocess.check_call(cmd)
        print(f"Adjusted bandwidth for {ip_address} to {bandwidth} Mbps.")
    except Exception as e:
        print(f"Error during bandwidth adjustment: {e}")

def main():
    interface = 'ap1-wlan1'
    dst_ip = '10.0.0.4'  # Replace with the desired destination IP
    dst_port = 8999  # Replace with the desired destination port
    pcap_file = 'capture.pcap'

    os.system('sudo tc qdisc del dev ap1-wlan1 root')    

    # Capture packets
    capture_packets(interface, dst_ip, dst_port, pcap_file)
    
    # Extract and average packet sizes and inter-departure rates
    avg_packet_size, avg_inter_departure_rate = extract_packet_info(pcap_file)
    
    # Predict bandwidth
    predicted_bandwidth = predict_bandwidth(avg_packet_size, avg_inter_departure_rate)
    
    # Apply bandwidth adjustment
    apply_bandwidth(dst_ip, predicted_bandwidth)

    # Display the results
    print("\nAverage Packet Size (in bytes):")
    print(avg_packet_size)
    
    print("\nAverage Inter-Departure Rate (packets per second):")
    print(avg_inter_departure_rate)
    
    print("\nPredicted Bandwidth (in Mbit/s):")
    print(predicted_bandwidth)


if __name__ == '__main__':
    main()
