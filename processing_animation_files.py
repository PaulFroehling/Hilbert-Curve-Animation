"""
Creates files that are used by the processing sketch for animating the creation process of a hilbert curve with the Skilling algorithm.

Command-line arguments
----------------------
--create-animation-files' : bool
    Set true to create animation files based on -dims and -bits
    
--delete-animation-files' : bool
    Deletes all currently stored animation files
-dims : int
    Dimensionality of the Hilbert curve (2 or 3).
-bits : int
    Number of bits for the Hilbert curve, controlling grid resolution (1–8).
    
"""

import argparse
from skillings_implementation.skillings_algorithm import hc_decode
from skillings_implementation.export_utils import clear_intermediate_result_folder


def create_lists_for_animation(args):
    clear_intermediate_result_folder()
    points = []
    n_points = (2**args.bits)**args.dims
    for i in range(0, n_points):
        points.append(hc_decode([i],n_dims=args.dims, n_bits=args.bits, save_intermediate_results=True))


def get_inputs():
    '''
    Reads input variables after script is called from "main"
    Args:
        - args:list: Arguments relevant for the plot
    Returns:
        None    
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--create-animation-files', dest = 'create_animation_files', type=bool)
    parser.add_argument('-bits', dest='bits', type=int)
    parser.add_argument('-dims', dest='dims', type=int)
    parser.add_argument('--delete-animation-files', dest = 'delete_files', type=bool)
    args = parser.parse_args()
    
    return args


if __name__ == '__main__':
    args = get_inputs()
    
    if args.create_animation_files != None and args.create_animation_files ==True:
        create_lists_for_animation(args)
    if args.delete_files != None and args.delete_files == True:
        clear_intermediate_result_folder()