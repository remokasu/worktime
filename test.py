import unittest
from worktime import WorkTime

class TestWorkTime(unittest.TestCase):

    def test_from_hhmm(self):
        self.assertEqual(WorkTime.from_hhmm(745), WorkTime(7, 45))
        self.assertEqual(WorkTime.from_hhmm(1230), WorkTime(12, 30))

    def test_from_str(self):
        self.assertEqual(WorkTime.from_str('07:45'), WorkTime(7, 45))
        self.assertEqual(WorkTime.from_str('12:30'), WorkTime(12, 30))
        with self.assertRaises(ValueError):
            WorkTime.from_str('1245')

    def test_to_minutes(self):
        self.assertEqual(WorkTime(7, 45).to_minutes(), 465)
        self.assertEqual(WorkTime(12, 30).to_minutes(), 750)

    def test_from_minutes(self):
        self.assertEqual(WorkTime.from_minutes(465), WorkTime(7, 45))
        self.assertEqual(WorkTime.from_minutes(750), WorkTime(12, 30))

    def test_to_decimal(self):
        self.assertAlmostEqual(WorkTime(7, 45).to_decimal(), 7.75)
        self.assertAlmostEqual(WorkTime(12, 30).to_decimal(), 12.5)

    def test_addition(self):
        self.assertEqual(WorkTime(7, 45) + WorkTime(0, 15), WorkTime(8, 0))
        self.assertEqual(WorkTime(12, 30) + WorkTime(2, 45), WorkTime(15, 15))

    def test_subtraction(self):
        self.assertEqual(WorkTime(8, 0) - WorkTime(0, 15), WorkTime(7, 45))
        self.assertEqual(WorkTime(15, 15) - WorkTime(2, 45), WorkTime(12, 30))

    def test_multiplication(self):
        self.assertEqual(WorkTime(7, 45) * 2, WorkTime(15, 30))
        self.assertEqual(WorkTime(3, 0) * 3, WorkTime(9, 0))

    def test_equality(self):
        self.assertTrue(WorkTime(7, 45) == WorkTime(7, 45))
        self.assertFalse(WorkTime(7, 45) == WorkTime(8, 0))

    def test_comparison(self):
        self.assertTrue(WorkTime(7, 45) < WorkTime(8, 0))
        self.assertTrue(WorkTime(8, 0) > WorkTime(7, 45))
        self.assertTrue(WorkTime(7, 45) <= WorkTime(7, 45))
        self.assertTrue(WorkTime(8, 0) >= WorkTime(7, 45))

if __name__ == '__main__':
    unittest.main()