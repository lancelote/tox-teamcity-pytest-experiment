import pytest


@pytest.mark.xfail
def test_fail():
    assert False


def test_pass():
    assert True
