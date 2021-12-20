from unittest import TestCase, main

from day_16 import packet_to_bin, part_1, part_2


class TestDay16(TestCase):
    def test_part_1(self):
        for i, (packet, version_sum) in enumerate(zip(['8A004A801A8002F478', '620080001611562C8802118E34',
                                                       'C0015000016115A2E0802F182340',
                                                       'A0016C880162017C3686B18A3D4780'], [16, 12, 23, 31])):
            with self.subTest(i=i):
                self.assertEqual(part_1(packet_to_bin(packet)), version_sum)

    def test_part_2(self):
        for i, (packet, version_sum) in enumerate(zip(['C200B40A82', '04005AC33890', '880086C3E88112', 'CE00C43D881120',
                                                       'D8005AC2A8F0', 'F600BC2D8F', '9C005AC2F8F0',
                                                       '9C0141080250320F1802104A08'], [3, 54, 7, 9, 1, 0, 0, 1])):
            with self.subTest(i=i):
                self.assertEqual(part_2(packet_to_bin(packet))[0], version_sum)


if __name__ == '__main__':
    main()
