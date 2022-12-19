from math import floor
import requests
from random import choices
from concurrent.futures import ThreadPoolExecutor

NR_GETS = 15
ALL_HOSTS_IP = [
    '10.10.101.2',
    '10.10.101.3',
    '10.10.102.2',
    '10.10.102.3',
    '10.10.103.2',
    '10.10.103.3'
]
EQUAL_WEIGHTS = len(ALL_HOSTS_IP) * [1]
cnt = len(ALL_HOSTS_IP) - 1
host_response_procentage = []
TIME_PENALTY = 3000000


def round_robin():
    global cnt
    cnt = (cnt + 1) % len(ALL_HOSTS_IP)
    return ALL_HOSTS_IP[cnt]


def random_robin():
    return choices(ALL_HOSTS_IP, EQUAL_WEIGHTS, k=1)[0]


def responsive_robin():
    return choices(ALL_HOSTS_IP, host_response_procentage, k=1)[0]


def send_request(get_destination):
    dst = get_destination()
    url = 'http://' + dst + ':9000'
    host_nr = ALL_HOSTS_IP.index(dst)
    try:
        req = requests.get(url, allow_redirects=False)
        return (ALL_HOSTS_IP.index(dst), req.elapsed.microseconds)
    except requests.ConnectionError:
        return (host_nr, TIME_PENALTY)


def test_distribution(scheduling_func):
    total_respone_time = len(ALL_HOSTS_IP) * [0]
    total_responses = len(ALL_HOSTS_IP) * [0]
    args = NR_GETS * [scheduling_func]

    with ThreadPoolExecutor() as executor:
        results = executor.map(send_request, args)

    for host_nr, time in results:
        total_respone_time[host_nr] = total_respone_time[host_nr] + time
        total_responses[host_nr] = total_responses[host_nr] + 1

    average_respone_time = [int(time / responses) if responses else 0 for time,
                            responses in zip(total_respone_time, total_responses)]

    return average_respone_time


if __name__ == '__main__':
    with open('host_response_procentage.txt', 'r') as file:
        for line in file:
            host_response_procentage.append(int(line))

    host_response_procentage[0] = floor(9 * host_response_procentage[0] / 10)

    print('Times for each host for a equal distribution: ' + ' '.join(map(str,
          test_distribution(round_robin))))

    print('Times for each host for a random distribution: ' + ' '.join(map(str,
          test_distribution(random_robin))))

    print('Times for each host for a responsiveness weighted distribution: ' + ' '.join(map(str,
          test_distribution(responsive_robin))))
