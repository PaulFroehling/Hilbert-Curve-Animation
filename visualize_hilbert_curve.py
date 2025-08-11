"""
hilbert_plot.py

Visualizes Hilbert curves in 2D or 3D using Skillings' algorithm.

Command-line arguments
----------------------
-dims : int
    Dimensionality of the Hilbert curve (2 or 3).
-bits : int
    Number of bits for the Hilbert curve, controlling grid resolution (1–8).
--stroke-width : float, optional
    Line thickness for plotting. Defaults to 0.4.

Example
-------
    python .\visualize_hilbert_curve.py -bits 2 -dims 2 
"""


from skillings_implementation.skillings_algorithm import hc_decode
import matplotlib.pyplot as plt
import numpy as np
import argparse

DEFAULT_STROKE_WIDTH = 0.4
MIN_DIM = 2
MAX_DIM = 3

def plot_visualization(coord_lists:list, n_dims:int, stroke_width:float):
    """
    Plot the Hilbert curve in 2D or 3D.

    Args:
        - n_bits(int)          : Number of bits for the Hilbert curve. The number of points is (2^n_bits)^n_dimensions.
                                  The higher the bit count (up to 8 is feasible), the finer the curve resolution.
        - n_dims(int)          : Number of dimensions for the Hilbert curve (can be 2 or 3).
        - stroke_width(float)  : Stroke width of the plotted curve.

    Returns:
        None
    """
    fig = plt.figure()
    if n_dims == 3:
        ax = fig.add_subplot(111, projection='3d')
    else:
        ax = fig.add_subplot()
    ax.plot(*coord_lists, linewidth=stroke_width)
    ax.set_axis_off()
    plt.show()
    
    
def compute_points(n_bits:int, n_dims:int) -> list[np.ndarray]:
    '''
    Computes 2D or 3D points of the Hilbert Curve for given bits and dims using Skillings' implementation.
    Args:
        - n_bits(int)       : Number of bits i.e. the resolution of the grid. 
        - n_dims(int)       : Dimensionality of the Hilbert Curve. 2D or 3D
        
    Returns:
        - coord_lists(list) :List of points, defining the Hilbert Curve in 2 or 3 dimensions   
    '''
    points = []
    n_points = (2**n_bits)**n_dims                                  #For n bits you have 2**n entries on the axis. For two axis (2**n)**dims
    print(f"Points_plotted: {n_points}")
    for i in range(0, n_points):
        points.append(hc_decode([i],n_dims=n_dims,n_bits=n_bits, save_intermediate_results=False))   #Compute coordinates using hc_encode of the Skillings' algorithm
        
    points =np.reshape(points,(-1,n_dims))                          #Reformate to allow unpacking in the next step
    coord_lists = [points[:, i] for i in range(0,n_dims)]           #Unpacks the values of each dimension, ready for plotting
    return coord_lists


def correct_input_values(args:argparse.Namespace) -> bool:
    '''
    Checks if the ranges of the given input values are valid.  
    Args:
        - args(argparse.Namespace) :Arguments relevant for the plot
        
    Returns:
        - is_correct(bool)         :Indicates if given input values are correct     
    '''
    no_none_values = args.dims != None and args.bits != None                          
    dim_values_ranges_correct = args.dims >= MIN_DIM and args.dims <= MAX_DIM 
    bit_value_ranges_correct = args.bits >= 1 and args.bits <= 8
    is_correct = no_none_values and dim_values_ranges_correct and bit_value_ranges_correct
    
    if no_none_values == False:
        print("Please set -bits and -dims.")
    if (dim_values_ranges_correct and bit_value_ranges_correct) == False:
        print("Dims need to be set to 2 or 3 and bits between 1 and 8")
    
    return is_correct

        
def prepare_plot(args:argparse.Namespace):
    '''
    Routes Args to plotting function   
    Args:
        - args(argparse.Namespace): Arguments relevant for the plot
        
    Returns:
        None    
    '''
    if correct_input_values(args):
        stroke_width = DEFAULT_STROKE_WIDTH if args.stroke_width is None else args.stroke_width
        coord_lists = compute_points(args.bits, args.dims)
        plot_visualization(coord_lists, args.dims, stroke_width)
            

def get_inputs() -> argparse.Namespace:
    '''
    Reads input variables after script is called from "main"
    Args:
        - args(argparse.Namespace): Arguments relevant for the plot
        
    Returns:
        None    
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-dims', dest = "dims", type=int, help="Dimensions for hilbert curve plot (2 or 3)")
    parser.add_argument('-bits', dest = "bits", type=int, help="Bits for hilbert curve plot i.e. gridsize. (1-8)")
    parser.add_argument('--stroke-width', dest = "stroke_width", type=float, help="Strokewidth for your plot")
    args = parser.parse_args()
    
    return args
    
if __name__ == "__main__":
    args = get_inputs()
    prepare_plot(args)