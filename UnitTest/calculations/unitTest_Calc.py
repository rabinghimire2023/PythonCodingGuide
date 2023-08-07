import unittest
from calculations import calculate_statistics

class TestStatisticsCalculation(unittest.TestCase):
    def test_mean_median_std_dev(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_statistics(data)
        self.assertEqual(result["mean"], 3.0)
        self.assertEqual(result["median"], 3.0)
        self.assertAlmostEqual(result["std_dev"], 1.58113883008, places=10)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_single_element(self):
        data = [42]
        result = calculate_statistics(data)
        self.assertEqual(result["mean"], 42.0)
        self.assertEqual(result["median"], 42.0)
        self.assertAlmostEqual(result["std_dev"], 0.0, places=10)

if __name__ == "__main__":
    unittest.main()
