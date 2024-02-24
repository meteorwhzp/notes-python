import unittest


def test_something():
    for i in range(0, 10):
        print(i)


class MyTestCase(unittest.TestCase):
    test_something()


if __name__ == '__main__':
    unittest.main()
