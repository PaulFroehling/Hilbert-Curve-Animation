"""
From/to binary or graycode helper functions for the construction process of the hilbert curve 
Since maximum number of bits are 8, all functions are limited here.
"""

import numpy as np

MAX_NUMBER_OF_BITS = 8

def hilbert_to_gray(hilberts: list[int], num_dims: int, num_bits: int) -> np.ndarray:
    """
    Since Skillings' algorithm relies on gray code, the transformation goes from decimals to binary to gray
    Args:
        -hilberts(list): List of integers
        -num_dims(int) : Number of dimensions of the hilbert curve
        -num_bits(int) : Number of bits per dimensions - this directly affects the grid size. 2 bits per axis -> 4x4 grid
        
    Returns:
        -gray(np.ndarray)    : List of gray code representations for each hilbert index in hilberts
    """
    arr = np.atleast_1d(hilberts).astype('>u8')     #Ensures that input is a 1d array of type unsigned big endian - highest bit first. This is important for the decode algorithms that goes from MSB to LSB
    arr_uint8 = arr.view(np.uint8).reshape(-1, 8)   #Convert to 8 bit integer and reshape to format, so that every hilbert index in hilbert has one 8 bit 
    bits = np.unpackbits(arr_uint8, axis=1)[:, -num_dims*num_bits:] #Convert decimals indices to binary numbers
    gray = np.bitwise_xor(bits, np.pad(bits[:, :-1], ((0, 0), (1, 0)), constant_values=0)) #Transforms binary to gray. First (MS) bit stays, remaining will be xor-red with the one before.
    gray = np.reshape(gray, (-1, num_bits, num_dims)).swapaxes(1, 2) # Reshape in (batch, num_dims, num_bits)
    return gray


def dec_tuples_to_binary(dec:tuple, n_bits:int) -> np.ndarray:
    """
    Converts a decimal tuple, representing a coordinate of the hilbert curve to 8-bit binaries
    Args:
        -dec    (tuple)  : Decimals that needs to be converted
        -n_bits (int)    : Number of bits       -> for final shape
    Returns:
        bits (np.array) : Binary representation of decimal input
    """

    bits = np.unpackbits(np.uint8(dec)).reshape([-1, 8])
    bits = np.array([bit[len(bit) - n_bits:] for bit in bits])
    bits = np.expand_dims(bits, axis=0)

    return bits


def bin_to_dec(binaries:np.ndarray, n_dims:int, n_bits:int) -> list:
    """
    Converts max 8bit-binaries to decimals
    Args:
        -binaries   (list) : Binary that needs conversion
        -n_dims     (int)  : Number of dimensions
        -n_bits     (int)  : Number of bits - maximal 8 bit
    Returns:
        bits (np.array)    : Decimal representation of binary input
    """
    dec_results = []
    for binary in binaries:
        dec_coordinates = []
        for dim in range(0,n_dims):
            padding = 8-n_bits
            padded_binary_number = np.pad(binary[dim],(padding, 0), mode='constant')
            decimal_number = np.packbits(padded_binary_number, axis=0)
            dec_coordinates.append(decimal_number[0])
        dec_results.append(dec_coordinates)
    
    return dec_results


def gray_to_binary(gray:np.ndarray) -> list:
    """
    Converts gray code to binary. Copy current gray and xor every bit (except the first) with the former gray bit.
    Args:
        -gray         (list)     : Graycode that needs to be transformed
    Returns:
        binary_coords (np.array) : Binary output
    """
    binary_coords = []
    for coord in gray:
        binary = np.copy(coord) 
        for bit in range(1, len(coord)):
            binary[bit] = np.logical_xor(coord[bit] , binary[bit-1])
        binary_coords.append(binary)
    return binary_coords