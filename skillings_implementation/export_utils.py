"""
Script with additional helper functions for the hilber curve visualization/animation
"""

import csv
import os

INTERMEDIATE_RESULTS_FOLDER  = "./skillings_intermediate_results"

def append_point_to_csv_list(list_name:str, data_point:list):
    """
    Apends/create lists of points of intermediate results, that are used for plotting in Processing
    Args:
        list_name(str)  : Name for the list, the point should be stored in
        data_point(list): Point to append
    Returns:
        -
    """
    with open(list_name, mode='a', newline='') as datei:
        writer = csv.writer(datei)
        if len(data_point[0])==2:
            writer.writerow([data_point[0][0], data_point[0][1]]) 
        elif len(data_point[0])==3:
            writer.writerow([data_point[0][0], data_point[0][1], data_point[0][2]]) 
        
def clear_intermediate_result_folder():
    """
    Clears the forder of intermediate results. 
       -
    Returns:
        -
    """
    for file in os.listdir(INTERMEDIATE_RESULTS_FOLDER):
        file_path = os.path.join(INTERMEDIATE_RESULTS_FOLDER, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    
def save_intermediate_points(point:list, bit:int, dim:int, n_dims:int, n_bits:int):
    """
    Saves intermediate results of the Skilling algorithm in a dedicated folder, from which files can be read by Processing
       point(list)  : Point to append
       bit(int)     : Bit of the current intermediate stage
       dim(int)     : Dim of the current intermediate stage
       n_dims(int)  : Total number of dims
       n_bits(int)  : Total number of bits
    Returns:
        -
    """
    if True:
        file_name = f"{bit}_{dim}.csv"
        file_path = os.path.join(INTERMEDIATE_RESULTS_FOLDER, file_name)
        append_point_to_csv_list(file_path, point)