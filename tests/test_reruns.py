import random
import pytest


PLATFORM = "Windows"

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_reruns():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:

    def test_reruns_1(self):
        assert random.choice([True, False])

    def test_reruns_2(self):
        assert random.choice([True, False])



@pytest.mark.flaky(reruns = 3, reruns_delay = 2, condition = PLATFORM == "Windows")
def test_reruns_with_conditions():
    assert random.choice([False, True])