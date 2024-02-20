#!/usr/bin/env python

"""
Tests for `elapsedtimer` package.
   See more at: https://doc.pytest.org/en/latest/fixture.html
"""

import pytest
import time

from elapsedtimer.timer import elapsedTimer, calc_elapsed_smh


@pytest.fixture(params=[(3, 'seconds'), (61, 'minutes')])
def data(request):
    return request.param


def test_data(data):
    elapsedTimer()
    time.sleep(data[0])
    msg = elapsedTimer()
    assert data[1] in msg


def test_millisecond():
    start_time_ns = 365539781000000
    end_time_ns = 365539782000000
    s, m, h = calc_elapsed_smh(end_time_ns - start_time_ns)
    assert s == 0.001 and m == 0 and h == 0


def test_centisecond():
    start_time_ns = 365539781000000
    end_time_ns = 365539791000000
    s, m, h = calc_elapsed_smh(end_time_ns - start_time_ns)
    assert s == 0.01 and m == 0 and h == 0


def test_decisecond():
    start_time_ns = 365539781000000
    end_time_ns = 365539881000000
    s, m, h = calc_elapsed_smh(end_time_ns - start_time_ns)
    assert s == 0.1 and m == 0 and h == 0


def test_second():
    start_time_ns = 365538781000000
    end_time_ns = 365539781000000
    s, m, h = calc_elapsed_smh(end_time_ns - start_time_ns)
    assert s == 1.0 and m == 0 and h == 0


def test_minute():
    start_time_ns = 365538781000000
    end_time_ns = 365638781000000
    s, m, h = calc_elapsed_smh(end_time_ns - start_time_ns)
    assert s == 40.0 and m == 1 and h == 0


def test_hour():
    start_time_ns = 365538781000000
    end_time_ns = 375538781000000
    s, m, h = calc_elapsed_smh(end_time_ns - start_time_ns)
    assert s == 40.0 and m == 46 and h == 2
