# Hilbert Curve – Computation, Visualization, and Animation of John Skilling’s Algorithm

The Hilbert curve, as a space-filling curve (SFC), is a fascinating mathematical object.  
Since Cantor, we know that the unit interval \([0,1]\) in \(\mathbb{R}\) has the same cardinality as the unit square \([0,1]^2\) in \(\mathbb{R}^2\).  
This led mathematicians to wonder whether a continuous bijection between these intervals is possible.  
Today, thanks to E. Netto, we know that such a continuous bijection does **not** exist, but a continuous surjection does.  
This discovery led to the creation of space-filling curves like the Hilbert curve — a curve that passes through every point in \([0,1]^2\).  
More than 100 years after Hilbert defined the curve, John Skilling found a very elegant algorithm for computing the coordinates of the Hilbert curve given so-called Hilbert indices (1, 2, 3, …), and also for retrieving Hilbert indices from coordinates on the curve.

## Computation of the Hilbert Curve

For the **computation** of the Hilbert curve, John Skilling’s algorithm is used, which works at the bit level.  
Since I did not have access to his original paper (*Programming the Hilbert Curve*, 2004), I relied heavily on this repository from Princeton University: https://github.com/PrincetonLIPS/numpy-hilbert-curve.  
I used their code as a guide to create my own implementation and to better understand how the algorithm works.  
If you only need a library for encoding and decoding, I recommend simply installing their package.

## Visualization

For static visualization, you can use the `visualize_hilbert_curve` script (based on matplotlib) with the following parameters:  
- **Dimensions**: `-dims (int)` — Can be 2 or 3  
- **Bits**: `-bits (int)` — Ranges from 1 to 8 (the implementation builds on 8 bits, which already provides a good impression of how the Hilbert curve converges toward a square or cube)  
- **Stroke Width**: `--stroke-width (float)` — The width of the lines plotted. Default is 0.4.

## Animation

<img src="hilbert_curve_animation/animation_gifs/animation_small.gif" height="350px" />
<img src="hilbert_curve_animation/animation_gifs/3d_animation_small.gif" height="350px" />

*Construction process of Skilling’s algorithm for the 2D Hilbert curve with 4 bits (265 points) and 3D (32,768 points)*

In the folder `hilbert_curve_animation`, you will find a Processing sketch that animates the generation of the Hilbert curve using Skilling’s algorithm.  
I modified the decode function (Hilbert index → coordinate) to allow storing intermediate results of the algorithm.  
These intermediate results are saved as CSV files in a folder that the Processing sketch reads during animation.  
The sketch interpolates between points of two consecutive files, starting from the earliest and ending with the final Hilbert curve.

## Installation

Instructions for installation.

## Usage

Short examples.
