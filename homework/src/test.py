import pingparsing
from statistics import mean


def add_route_stats(node, ip, latency_list, loss_list):
    parser = pingparsing.PingParsing()
    ping_str = "ping -c 100 "
    node.sendCmd(ping_str + ip)

    stats = parser.parse(node.waitOutput())
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


def print_latency_of_r0(c1_routes_stats, r1_routes_stats, r2_routes_stats, r3_routes_stats):
    routers_latency = r1_routes_stats[0] + \
        r2_routes_stats[0] + r3_routes_stats[0]
    command_unit_latency = c1_routes_stats[0]

    r0_latency = [x - y for x, y in zip(command_unit_latency, routers_latency)]

    print('Router r0 introduces a average latency of {}'.format(mean(r0_latency)))


def test(net):
    all_hosts = ["h1", "h2", "h3", "h4", "h5", "h6"]
    command_unit_routes_stats = add_node_to_hosts_routes_stats(
        net, "c1", all_hosts)

    print_command_unit_routes_info(command_unit_routes_stats)

    r1_routes_stats = add_node_to_hosts_routes_stats(
        net, "r1", all_hosts[0:2])

    r2_routes_stats = add_node_to_hosts_routes_stats(
        net, "r2", all_hosts[2:4])

    r3_routes_stats = add_node_to_hosts_routes_stats(
        net, "r3", all_hosts[4:6])

    print_latency_of_r0(command_unit_routes_stats,
                        r1_routes_stats, r2_routes_stats, r3_routes_stats)

    return
