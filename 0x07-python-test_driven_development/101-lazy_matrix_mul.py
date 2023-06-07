#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix

    Args:
        m_a (list): First matrix
        m_b (list): second matrix

    Returns:
        The result of multiply m_a by m_b

    """
    return matmul(m_a, m_b)
