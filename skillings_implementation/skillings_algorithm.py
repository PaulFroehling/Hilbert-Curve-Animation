"""
Script for calculating n-dimensional coordinates from hilbert indicies (hc_decode) and back (hc_encode)
All of this code is highly(!) influenced by https://github.com/PrincetonLIPS/numpy-hilbert-curve/tree/main
Since I had no access to the original paper of John Skilling (Programming the Hilbert Curve) 
I used this repo to understand the algorithm and this worked best for me by coding it on my own with the help of the Princeton repo 
"""

import numpy as np
from .export_utils import save_intermediate_points
from .binary_utils import hilbert_to_gray, bin_to_dec, dec_tuples_to_binary



def hc_decode(h_indices: list[int], n_dims:int, n_bits:int, save_intermediate_results:bool=False) -> list[int]:
    """
    Converts hilber indices, given as integers into n-D coordinates in decimal format
    Args:
        -h_indices(list[int])           : List of hilbert indices as decimals 
        -n_dims(int)                    : Number of dimensions for the resulting coordinates
        -n_bits(int)                    : Number of bits for each axis of the coordinate system
        -save intermediate_results(bool): Flag if intermediate results of Skillings' algorithm should be saved to disk
    
    Returns:
    """
    x_gray = hilbert_to_gray(h_indices, n_dims, n_bits)
    coordinates = skillings_decode(n_dims, n_bits, x_gray, save_intermediate_results)
    return coordinates


def hc_encode(point:tuple, n_dims:int, n_bits:int) -> int:
    """
    Converts coordinates of the hilbert curve to hilbert indices
    Args:
        -point(tuple)                   : List of hilbert indices as decimals 
        -n_dims(int)                    : Number of dimensions for the resulting coordinates
        -n_bits(int)                    : Number of bits for each axis of the coordinate system    
    Returns:
    """
    binary = dec_tuples_to_binary(point, n_bits)
    binary_coords = skillings_encode(binary, n_dims, n_bits)
    
    hilbert_index = np.packbits([np.pad(binary_coord,(8-len(binary_coord[-8:]),0))[-8:] for binary_coord in binary_coords])
    return hilbert_index


def skillings_encode(binary, n_dims, n_bits):
    """
    Converts a point with decimal coordinates to binary and applies transformation rules
    Args:
        -point(tuple)                   : List of hilbert indices as decimals 
        -n_dims(int)                    : Number of dimensions for the resulting coordinates
        -n_bits(int)                    : Number of bits for each axis of the coordinate system    
    Returns:
    """
    for bit in range(0, n_bits):
        for dim in range(0,n_dims):
            mask = binary[:,dim,bit]
            #If the current bit is 1, invert the lower bits of the lower dimension.  Skillings always compares against dimension 0
            binary = skillings_invert_transformation(binary, mask, bit)
          
            #If the current bit is 0, compare lower bits of current dimension and dimension 0 and switch value in both, if values are different
            binary = skillings_swap_transformation(binary, mask, dim, bit)
    
    gray = binary.T.reshape(-1, n_dims*n_bits) #flatten and entangle bits (reverse to decode, where bits are disentangled)
    return gray


def skillings_decode(n_dims, n_bits, gray, save_intermediate_results=False):
    """
    Converts/maps a binary representation of a hilbert index to a coordinate of the hilbert curve using skillings' transformations
    Args:
        -point(tuple)                   : List of hilbert indices as decimals 
        -n_dims(int)                    : Number of dimensions for the resulting coordinates
        -n_bits(int)                    : Number of bits for each axis of the coordinate system    
    Returns:
    """
    for bit in range(n_bits-1, -1, -1):
        for dim in range(n_dims-1, -1, -1):
            mask = gray[:,dim, bit]
            
            #If the current bit is 1, invert the lower bits of the lower dimension.  Skillings always compares against dimension 0
            gray = skillings_invert_transformation(gray, mask, bit)
          
            #If the current bit is 0, compare lower bits of current dimension and dimension 0 and switch value in both, if values are different
            gray = skillings_swap_transformation(gray, mask, dim, bit)
            
            if save_intermediate_results: 
                save_intermediate_points( bin_to_dec(gray, n_dims, n_bits), bit+1, dim+1, n_dims, n_bits)
            
            
    dec_coordinates = bin_to_dec(gray, n_dims, n_bits)
    return dec_coordinates



def skillings_invert_transformation(gray, mask, bit):
    """
    If the current bit (mask) is on invert lower bits in dimension 0 (x)
    Args:
        -gray(np.array)              : Gray code that needs manipulation
        -dim(int)                    : Current dimension in the transformation loop
        -bit(int)                    : Current bit in the transformation loop
    Returns:
    """
    bits_for_turning = gray[:,0,bit+1:]
    gray[:,0,bit+1:] =  np.logical_xor(bits_for_turning, mask)
    
    return gray


def skillings_swap_transformation(gray, mask, dim, bit):
    """
    If the current bit (mask) is off swap lower bit-values of dimension zero with lower bits in current dimension, if values differ
    Args:
        -gray(np.array)               : Gray code that needs manipulation
        -dims(int)                    : Current dimension in the transformation loop
        -bits(int)                    : Current bit in the transformation loop
    Returns:
    """
    is_zero = np.logical_not(mask)
    bit_comparison= np.logical_xor(gray[:,0,bit+1:], gray[:,dim,bit+1:])
    switch = np.logical_and(is_zero, bit_comparison)

    if switch.size > 0:
        gray[:,0,bit+1:] = np.logical_xor(gray[:,0,bit+1:],switch)
        gray[:,dim,bit+1:] = np.logical_xor(gray[:,dim,bit+1:],switch)
        
    return gray

