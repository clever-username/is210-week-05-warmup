#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Returns a number of winks and nudges based on input.

    Args:
        wink: Key that defines responses for 'Know what I mean?'.
        numwink: Number of instances of wink.

    Returns:
        'Know what I mean?' followed by wink value and 'nudge ' per number set
        in numwink.

    Example:

        >>> know_what_i_mean(wink='blink ', numwink=1)
            Know what I mean? blink, nudge
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
