# bandwidth_allocation.py

import os
import argparse

def setup_htb(interface):
    os.system('sudo tc qdisc del dev ap1-wlan1 root')
    os.system('sudo tc qdisc add dev {} root handle 1:0 htb default 10'.format(interface))
    os.system('sudo tc class add dev {} parent 1:0 classid 1:1 htb rate 12mbit'.format(interface))

def allocate_bandwidth(interface, classid, rate):
    os.system('sudo tc class add dev {} parent 1:1 classid 1:{} htb rate {}'.format(interface, classid, rate))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Allocate bandwidth on an interface.')
    parser.add_argument('interface', type=str, help='The interface to configure (e.g., ap1-wlan1)')
    parser.add_argument('--stations', nargs='+', help='List of station ip and their rates (e.g., 10.0.0.5=10mbit 10.0.0.7=15mbit)')

    args = parser.parse_args()

    setup_htb(args.interface)

    for i, station in enumerate(args.stations):
        station_ip, rate = station.split('=')
        allocate_bandwidth(args.interface, i+2, rate)
        os.system('sudo tc filter add dev {} protocol ip parent 1:0 prio 1 u32 match ip dst {} flowid 1:{}'.format(args.interface, station_ip, i+2))
