import unittest
from partition import get_partitions
from algorithms import greedy_algorithm, brute_force_algorithm

def create_partitions(items):
    partitions = []
    for item in get_partitions(items):
        partitions.append(item)

    return partitions

class TestGetPartitions(unittest.TestCase):
    def test_number_of_partitions_1(self):
       self.assertEqual(len(create_partitions(['a'])), 1)

    def test_number_of_partitions_2(self):
       self.assertEqual(len(create_partitions(['a','b'])), 2)

    def test_number_of_partitions_3(self):
       self.assertEqual(len(create_partitions(['a','b', 'c'])), 5)

    def test_number_of_partitions_5(self):
       self.assertEqual(len(create_partitions(['a','b', 'c', 'd', 'e'])), 52)

                        
class TestGreedyAlgorithm(unittest.TestCase):
    def test_greedy_transport(self):
        items = {'dog': 3, 'cow': 2, 'cat': 3, 'parrot': 1}
        self.assertEqual(greedy_algorithm(items, 5), 
                    ([['dog', 'cow'], ['cat', 'parrot']])
                    )

class TestBruteForceAlgorithm(unittest.TestCase):
    def test_brute_force_transport(self):
        items = {'dog': 5, 'cow': 2, 'cat': 3, 'parrot': 1}
        self.assertEqual(len(brute_force_algorithm(items, 5)), 3)


if __name__ == '__main__':
    unittest.main()
