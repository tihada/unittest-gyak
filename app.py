import unittest

def fibo(n):
    fibon = [0,1]
    if n < len(fibon):
        return fibon[n]
    
    for i in range(2, n+1):
        fibon.append(fibon[i-1] + fibon[i-2])

    return fibon[n]

class TestFibo(unittest.TestCase):
    def test_one(self):
        fgv = fibo(10)
        self.assertEqual(fgv, 55)

    def test_two(self):
        fgv = fibo(42)
        self.assertEqual(fgv, 267914296)

    def test_three(self):
        fgv = fibo(5)
        self.assertEqual(fgv, 5)

    def test_zeroeth(self):
        fgv = fibo(0)
        self.assertEqual(fgv, 0)

    def test_positive(self):
        fgv = fibo(5)
        self.assertGreater(fgv, 0)

unittest.main()