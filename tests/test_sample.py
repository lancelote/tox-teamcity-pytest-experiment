import pytest


@pytest.mark.xfail
def test_fail():
    assert False


def test_pass():
    assert True


@pytest.mark.skip
def test_fail_2():
    assert False
