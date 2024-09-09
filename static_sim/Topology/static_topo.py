from mininet.node import Controller
from mininet.link import TCLink
from mn_wifi.link import WirelessLink
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSAP
from mn_wifi.cli import CLI

def create_network():
    net = Mininet_wifi(controller=Controller, accessPoint=OVSAP, link=WirelessLink)
    
    info("*** Creating nodes\n")
    c0 = net.addController('c0')
    ap1 = net.addAccessPoint('ap1', ssid='simplewifi', mode='g', channel='1')
    server = net.addHost('server', ip = '10.0.0.1/8')
    sta_list = []
    for i in range(1, 6):
        sta = net.addStation('sta%d' % i, ip='10.0.0.%d/8' % (i+1))
        sta_list.append(sta)
    
    info("*** Configuring wifi nodes\n")
    net.configureNodes()

    info("*** Creating links\n")
    net.addLink(server, ap1, cls=TCLink, bw=100)
    for sta in sta_list:
        net.addLink(sta, ap1, cls=WirelessLink)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
