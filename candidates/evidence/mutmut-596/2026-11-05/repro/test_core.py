from repro812.core import make_garbage


def test_make_garbage():
    for i in range(200_000):
        assert make_garbage(i % 13) == 2
