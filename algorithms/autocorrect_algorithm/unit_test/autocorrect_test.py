import unittest

from autocorrect import autocorrect


class MyTestCase(unittest.TestCase):
    def test_equal_string_first_variance(self):
        self.assertEqual(autocorrect(text="We have sent the deliverables to u"),
                         "We have sent the deliverables to your client")

    def test_equal_string_second_variance(self):
        self.assertEqual(autocorrect(text="We have sent the deliverables to you"),
                         "We have sent the deliverables to your client")

    def test_equal_string_the_third_variance(self):
        self.assertEqual(autocorrect(text="We have sent the deliverables to youuu"),
                         "We have sent the deliverables to your client")

    def test_equal_string_fourth_variance(self):
        self.assertEqual(autocorrect(text="youtube"),
                         "youtube")


if __name__ == '__main__':
    unittest.main()
