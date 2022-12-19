import pingparsing
from statistics import mean


NR_REQUEST_PER_HOST = 100
TIMEOUT = 2
ALL_HOSTS = ["h1", "h2", "h3", "h4", "h5", "h6"]


def map_hostname_to_ip(net, hostname):
    return net.get(hostname).IP()


def add_route_stats(node, ip, latency_list, loss_list):
    parser = pingparsing.PingParsing()
    ping_str = "ping -c 100 "

    stats = parser.parse(node.cmd(ping_str + ip))
    latency_list.append(stats.rtt_avg / 2)
    loss_list.append(stats.packet_loss_rate)


def add_node_to_hosts_routes_stats(net, node, hosts_ips):
    routes_latency = []
    routes_loss = []

    for host_ip in hosts_ips:
        add_route_stats(net.get(node), host_ip,
                        routes_latency, routes_loss)

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


def print_host_nr_in_time_requests(net, command_unit_str, hostname):
    command_unit = net.get(command_unit_str)

    not_missed = NR_REQUEST_PER_HOST

    command = "timeout -v " + str(TIMEOUT) + " python3 client.py -p http {}:9000".format(
        map_hostname_to_ip(net, hostname))

    for _ in range(NR_REQUEST_PER_HOST):
        if command_unit.cmd(command).startswith('timeout'):
            not_missed = not_missed - 1

    response_procentage = int((not_missed / NR_REQUEST_PER_HOST) * 100)

    print('{} can respond to {} procent of requests with a {}sec timeout.'.format(
        hostname, response_procentage, TIMEOUT))

    return response_procentage


def print_latency_of_r0(c1_routes_stats, r1_routes_stats, r2_routes_stats, r3_routes_stats):
    routers_latency = r1_routes_stats[0] + \
        r2_routes_stats[0] + r3_routes_stats[0]
    command_unit_latency = c1_routes_stats[0]

    r0_latency = [x - y for x, y in zip(command_unit_latency, routers_latency)]

    print('Router r0 introduces a average latency of {}'.format(mean(r0_latency)))


def test(net):
    all_hosts_ips = list(map(lambda h: map_hostname_to_ip(net, h), ALL_HOSTS))

    # weird transient errors
    for host_ip in all_hosts_ips:
        net.get("c1").cmd("ping -c1 " + host_ip)

    command_unit_routes_stats = add_node_to_hosts_routes_stats(
        net, "c1", all_hosts_ips)

    print_command_unit_routes_info(command_unit_routes_stats)

    r1_routes_stats = add_node_to_hosts_routes_stats(
        net, "r1", all_hosts_ips[0:2])

    r2_routes_stats = add_node_to_hosts_routes_stats(
        net, "r2", all_hosts_ips[2:4])

    r3_routes_stats = add_node_to_hosts_routes_stats(
        net, "r3", all_hosts_ips[4:6])

    print_latency_of_r0(command_unit_routes_stats,
                        r1_routes_stats, r2_routes_stats, r3_routes_stats)

    for host in ALL_HOSTS:
        net.get(host).sendCmd("python3 -m http.server 9000 &")

    # weird transient errors
    for host_ip in all_hosts_ips:
        net.get("c1").cmd("python3 client.py -p http " + host_ip + ":9000")

    host_response_procentage = []
    for host in ALL_HOSTS:
        host_response_procentage.append(
            print_host_nr_in_time_requests(net, "c1", host))

    # saved in case of emergency
    # host_response_procentage = [99, 23, 31, 26, 2, 2]

    with open('host_response_procentage.txt', 'w') as file:
        file.writelines("\n".join(str(r) for r in host_response_procentage))

    net.get("c1").cmdPrint("python3 test_distributions.py")

    return
