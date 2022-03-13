import demo_ylesanne
import random

def test_proov():
    assert demo_ylesanne.proov(1, 1) == 2
    assert demo_ylesanne.proov(3, 4) == 7

    for i in range(10):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        assert demo_ylesanne.proov(a, b) == a + b
