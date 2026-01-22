#!/usr/bin/env python3
"""Module for type-annotated to_kv function."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with string k and the square of v as a float."""
    return (k, float(v ** 2))
