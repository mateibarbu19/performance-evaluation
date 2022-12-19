import requests
from random import randint, choices
from concurrent.futures import ThreadPoolExecutor

NR_GETS = 1
ALL_HOSTS = ["h1", "h2", "h3", "h4", "h5", "h6"]


def send_request(address):
    url = 'http://' + address + ':9000'
    req = requests.get(url, allow_redirects=False)
    return req.elapsed.microseconds


def test_distribution(hosts_nr, all_hosts_ips):
    total_respone_time = [0 for _ in ALL_HOSTS]
    total_responses = [0 for _ in ALL_HOSTS]

    addresses = [all_hosts_ips[host_nr] for host_nr in hosts_nr]

    with ThreadPoolExecutor() as executor:
        times = executor.map(send_request, addresses)

    print(times)

    for host_nr, time in zip(hosts_nr, times):
        total_respone_time[host_nr] = total_respone_time[host_nr] + time
        total_responses[host_nr] = total_responses[host_nr] + 1

    average_respone_time = [time / responses for time,
                            responses in zip(total_respone_time, total_responses)]

    return average_respone_time


if __name__ == '__main__':
    host_response_procentage = []
    all_hosts_ips = []

    with open('host_response_procentage.txt', 'r') as file:
        cnt = 0
        for line in file:
            if cnt < len(ALL_HOSTS):
                all_hosts_ips.append(line[:-1])
            else:
                host_response_procentage.append(int(line))
            cnt = cnt + 1

    print(all_hosts_ips)
    print(host_response_procentage)

    equal_distribution = [packet % len(ALL_HOSTS)
                          for packet in range(NR_GETS)]

    random_distribution = [randint(0, len(ALL_HOSTS) - 1)
                           for _ in range(NR_GETS)]

    throughput_distribution = throughput_distribution = choices(
        range(len(ALL_HOSTS)), host_response_procentage, k=NR_GETS)

    print(test_distribution(equal_distribution, all_hosts_ips))
