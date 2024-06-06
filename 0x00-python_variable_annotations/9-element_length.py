#!/usr/bin/env python3
"""Task 9"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function defined in the project's last mandatory task"""
    return [(i, len(i)) for i in lst]
