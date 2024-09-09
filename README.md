Dynamic Bandwidth Management Using SDN, Machine Learning, and Linux Traffic Control


This project demonstrates the use of Software-Defined Networking (SDN) combined with machine learning and Linux traffic control (tc) to dynamically manage network bandwidth based on real-time traffic statistics. It simulates both static and dynamic bandwidth allocation to compare performance and efficiency across different traffic flows.


Project Overview

In modern networks, efficient bandwidth management is crucial for optimal performance. Static allocation often leads to resource underutilization or congestion. To address this, this project proposes a dynamic bandwidth allocation system using SDN with a Ryu controller, machine learning for bandwidth prediction, and Linux traffic control tools like tc and HTB.


Key Features

Dynamic Bandwidth Management: Adjust bandwidth in real-time based on packet size and inter-departure rate.

Machine Learning Integration: Predict bandwidth using a trained model based on network traffic characteristics.

Traffic Simulation: Traffic generation using D-ITG for both static and dynamic scenarios.

Linux tc and HTB: Implement traffic shaping to control bandwidth per station.

Performance Monitoring: Evaluate network performance through metrics such as bitrate, delay, and packet loss.


Directory Structure

├── ML_model/               # Machine learning scripts and models

├── dynamic_sim/            # dynamic configuration simulation scripts and simulation logs 

├── results/                # Logs and output from simulations

├── static_sim/             # static configuration simulation scripts and simulation logs

└── README.md               # Project description


Software and Tools

Python (version 3.6 and 2.7)

Mininet VM and Mininet-WiFi for network emulation

Ryu SDN controller for flow management

D-ITG for traffic generation

Matplotlib for plotting results

Linux tc and HTB for bandwidth control

tcpdump for packets capture

Python scikit learn


Contact

For further information, you can reach me via:

Email: derrickdansodd3@gmail.com

