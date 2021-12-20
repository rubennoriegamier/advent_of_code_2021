from functools import partial, reduce
from operator import mul


def main():
    packet = input()
    bin_packet = packet_to_bin(packet)

    print(part_1(bin_packet))
    print(part_2(bin_packet)[0])


def packet_to_bin(packet: str) -> str:
    return ''.join(map('{0:04b}'.format, map(partial(int, base=16), packet)))


def part_1(bin_packet: str, max_packets: int | None = None) -> int | tuple[int, int]:
    version_sum = 0
    idx = 0

    try:
        while max_packets is None or max_packets > 0:
            if max_packets is not None:
                max_packets -= 1
            version_sum += int(bin_packet[idx:idx + 3], 2)
            idx += 3
            if bin_packet[idx:idx + 3] == '100':
                idx += 3
                while bin_packet[idx] == '1':
                    idx += 5
                idx += 5
            else:
                idx += 3
                if bin_packet[idx] == '0':
                    idx += 1
                    length = int(bin_packet[idx:idx + 15], 2)
                    idx += 15
                    version_sum += part_1(bin_packet[idx:idx + length])
                    idx += length
                else:
                    idx += 1
                    max_packets_ = int(bin_packet[idx:idx + 11], 2)
                    idx += 11
                    version, idx_ = part_1(bin_packet[idx:], max_packets_)
                    version_sum += version
                    idx += idx_
    except (IndexError, ValueError):
        pass

    return version_sum if max_packets is None else (version_sum, idx)


def part_2(bin_packet: str, max_packets: int = None):
    numbers = []
    idx = 0

    try:
        while max_packets is None or max_packets > 0:
            if max_packets is not None:
                max_packets -= 1
            idx += 3
            type_id = int(bin_packet[idx:idx + 3], 2)
            if type_id == 4:
                idx += 3
                bin_number = ''
                while bin_packet[idx] == '1':
                    bin_number += bin_packet[idx + 1:idx + 5]
                    idx += 5
                bin_number += bin_packet[idx + 1:idx + 5]
                idx += 5
                numbers.append(int(bin_number, 2))
            else:
                idx += 3
                if bin_packet[idx] == '0':
                    idx += 1
                    length = int(bin_packet[idx:idx + 15], 2)
                    idx += 15
                    numbers_ = part_2(bin_packet[idx:idx + length])
                    idx += length
                else:
                    idx += 1
                    max_packets_ = int(bin_packet[idx:idx + 11], 2)
                    idx += 11
                    numbers_, idx_ = part_2(bin_packet[idx:], max_packets_)
                    idx += idx_

                match type_id:
                    case 0:
                        numbers.append(sum(numbers_))
                    case 1:
                        numbers.append(reduce(mul, numbers_))
                    case 2:
                        numbers.append(min(numbers_))
                    case 3:
                        numbers.append(max(numbers_))
                    case 5:
                        numbers.append(numbers_[0] > numbers_[1])
                    case 6:
                        numbers.append(numbers_[0] < numbers_[1])
                    case 7:
                        numbers.append(numbers_[0] == numbers_[1])
    except (IndexError, ValueError):
        pass

    return numbers if max_packets is None else (numbers, idx)


if __name__ == '__main__':
    main()
