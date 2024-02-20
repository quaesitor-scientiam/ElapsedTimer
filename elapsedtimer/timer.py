"""Main module."""

import time


def calc_elapsed_smh(etime_ns: int) -> (float, int, int):
    """
    Determine seconds, minutes, and hours in the elapsed time
    :param etime_ns: nanoseconds since the epoch
    :return: seconds, minutes, and hours
    """
    etime_s = etime_ns / 1000000000
    h = 0
    m, s = divmod(etime_s, 60)
    if m > 0:
        h, m = divmod(m, 60)

    m = int(m)
    h = int(h)

    return s, m, h


def get_elapsed_time(stime_ns: int) -> (float, int, int):
    """
    Determine seconds, minutes, and hours in the elapsed time
    :param stime_ns: nanoseconds since the epoch
    :return: seconds, minutes, and hours
    """
    stop_time_ns = time.monotonic_ns()
    etime_ns = stop_time_ns - stime_ns

    return calc_elapsed_smh(etime_ns)


def format_elapsed_message(s: float, m: int, h: int) -> str:
    if h == 0:
        if m == 0:
            msg = '   {:05.2f} seconds'.format(s)
        else:
            msg = '{:02}:{:05.2f} minutes'.format(m, s)
    else:
        msg = '{:02}:{:02}:{:05.2f} hours'.format(h, m, s)

    return msg


def elapsedTimer(subTimer=False, keepTimer=False, returnNumeric=False):
    """
    First time it is called starts the timer. Second time it is called it returns
    a message of the elapsed time since its last call.  Use keepTimer to track
    continuous time increments.  Use returnNumeric to return total seconds only.
    :rtype: str or numeric
    :return: elapsed time (2nd call only)
    """
    if not hasattr(elapsedTimer, '__private_start__'):
        setattr(elapsedTimer, '__private_start__', [])
    if not elapsedTimer.__private_start__:  # list is empty
        elapsedTimer.__private_start__.append(time.monotonic())
        return
    if subTimer:
        elapsedTimer.__private_start__.append(time.monotonic())
        return

    start_time = elapsedTimer.__private_start__.pop()
    if keepTimer:
        elapsedTimer.__private_start__.append(start_time)

    if returnNumeric:
        return time.monotonic() - start_time

    s, m, h = get_elapsed_time(start_time)
    time.start = 0  # Clear this time tracker

    return format_elapsed_message(s, m, h)
