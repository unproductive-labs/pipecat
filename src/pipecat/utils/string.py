#
# Copyright (c) 2024, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

import re
import logging

logger = logging.getLogger(__name__)

ENDOFSENTENCE_PATTERN_STR = r"""
    (?<![A-Z])       # Negative lookbehind: not preceded by an uppercase letter (e.g., "U.S.A.")
    (?<!\d)          # Negative lookbehind: not preceded by a digit (e.g., "1. Let's start")
    (?<!\d\s[ap])    # Negative lookbehind: not preceded by time (e.g., "3:00 a.m.")
    (?<!Mr|Ms|Dr)    # Negative lookbehind: not preceded by Mr, Ms, Dr (combined bc. length is the same)
    (?<!Mrs)         # Negative lookbehind: not preceded by "Mrs"
    (?<!Prof)        # Negative lookbehind: not preceded by "Prof"
    [\.\?\!:;\\\n]|  # Match a period, question mark, exclamation point, colon, semicolon, or newline
    [。？！：；]       # the full-width version (mainly used in East Asian languages such as Chinese)
"""
ENDOFSENTENCE_PATTERN = re.compile(ENDOFSENTENCE_PATTERN_STR, re.VERBOSE)


def match_endofsentence(text: str) -> int:
    logger.debug(f"Pattern being used: {ENDOFSENTENCE_PATTERN_STR}")
    logger.debug(f"Attempting to match on text: [{repr(text)}]")
    match = ENDOFSENTENCE_PATTERN.search(text)
    logger.debug(f"Match result: {match}")
    if match:
        logger.debug(f"Match span: {match.span()}")
    return match.end() if match else 0
