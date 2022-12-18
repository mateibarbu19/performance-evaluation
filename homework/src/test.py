import pingparsing
from statistics import mean
import requests
from concurrent.futures import ThreadPoolExecutor
from random import randint, choices

NR_REQUEST_PER_HOST = 100
TIMEOUT = 2
NR_GETS = 100
ALL_HOSTS = ["h1", "h2", "h3", "h4", "h5", "h6"]


def add_route_stats(node, ip, latency_list, loss_list):
    parser = pingparsing.PingParsing()
    ping_str = "ping -c 100 "

    stats = parser.parse(node.cmd(ping_str + ip))
    latency_list.append(stats.rtt_avg / 2)
    loss_list.append(stats.packet_loss_rate)


def add_node_to_hosts_routes_stats(net, node, hosts):
    routes_latency = []
    routes_loss = []

    for host in hosts:
        add_route_stats(net.get(node), net.get(
            host).IP(), routes_latency, routes_loss)

    return (routes_latency, routes_loss)


def print_command_unit_routes_info(command_unit_routes_stats):
    lat = command_unit_routes_stats[0]
    loss = command_unit_routes_stats[1]

    print('Latency for ASIA: {} (ms)'.format((lat[0] + lat[1]) / 2))

    print('Latency for EMEA: {} (ms)'.format((lat[2] + lat[3]) / 2))

    print('Latency for US: {} (ms)'.format((lat[4] + lat[5]) / 2))

    print('Route from the command unit to h{} has minimum latency'.format(
        lat.index(min(lat)) + 1))
    print('Route from the command unit to h{} has maximum latency'.format(
        lat.index(max(lat)) + 1))

    print('Route from the command unit to h{} has the greatest loss procentace'.format(
        loss.index(max(loss)) + 1))


def print_host_nr_in_time_requests(net, command_unit_str, host_str):
    command_unit = net.get(command_unit_str)
    host = net.get(host_str)

    not_missed = NR_REQUEST_PER_HOST

    command = "timeout -v " + str(TIMEOUT) + " python3 client.py -p http {}:9000".format(
        host.IP())

    for _ in range(NR_REQUEST_PER_HOST):
        if command_unit.cmd(command).startswith('timeout'):
            not_missed = not_missed - 1

    response_procentage = int((not_missed / NR_REQUEST_PER_HOST) * 100)

    print('{} can respond to {} procent of requests with a {}sec timeout.'.format(
        host_str, response_procentage, TIMEOUT))

    return response_procentage


def print_latency_of_r0(c1_routes_stats, r1_routes_stats, r2_routes_stats, r3_routes_stats):
    routers_latency = r1_routes_stats[0] + \
        r2_routes_stats[0] + r3_routes_stats[0]
    command_unit_latency = c1_routes_stats[0]

    r0_latency = [x - y for x, y in zip(command_unit_latency, routers_latency)]

    print('Router r0 introduces a average latency of {}'.format(mean(r0_latency)))


def send_request(arg):
    net = arg[0]
    host_nr = arg[1]

    host = net.get("h" + str(host_nr + 1))
    url = 'https://' + host.IP()
    print(url)
    req = requests.get(url, allow_redirects=False)
    return req.elapsed.microseconds


def test_distribution(net, hosts_nr):
    total_respone_time = [0 for _ in ALL_HOSTS]
    total_responses = [0 for _ in ALL_HOSTS]

    args = [(net, host_nr) for host_nr in hosts_nr]

    with ThreadPoolExecutor() as executor:
        times = executor.map(send_request, args)

    for host_nr, time in zip(hosts_nr, times):
        total_respone_time[host_nr] = average_respone_time[host_nr] + time
        total_responses = total_responses + 1

    average_respone_time = [time / responses for time,
                            responses in zip(total_respone_time, total_responses)]

    return average_respone_time


def test(net):
    command_unit_routes_stats = add_node_to_hosts_routes_stats(
        net, "c1", ALL_HOSTS)

    print_command_unit_routes_info(command_unit_routes_stats)

    r1_routes_stats = add_node_to_hosts_routes_stats(net, "r1", ALL_HOSTS[0:2])

    r2_routes_stats = add_node_to_hosts_routes_stats(net, "r2", ALL_HOSTS[2:4])

    r3_routes_stats = add_node_to_hosts_routes_stats(net, "r3", ALL_HOSTS[4:6])

    print_latency_of_r0(command_unit_routes_stats,
                        r1_routes_stats, r2_routes_stats, r3_routes_stats)

    for host in ALL_HOSTS:
        net.get(host).sendCmd("python3 -m http.server 9000 &")

    host_response_procentage = []
    for host in ALL_HOSTS:
        host_response_procentage.append(
            print_host_nr_in_time_requests(net, "c1", host))

    # saved in case of emergency
    # host_response_procentage = [99, 23, 31, 66, 2, 2]

    equal_distribution = [packet % len(ALL_HOSTS)
                          for packet in range(NR_GETS)]

    random_distribution = [randint(0, len(ALL_HOSTS) - 1)
                           for _ in range(NR_GETS)]

    throughput_distribution = throughput_distribution = choices(
        range(len(ALL_HOSTS)), host_response_procentage, k=NR_GETS)

    print(test_distribution(net, equal_distribution))

    return
