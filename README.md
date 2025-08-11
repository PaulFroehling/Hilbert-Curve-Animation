# Hilbert Curve - Computation, Visualization und Animations of John Skillings' Algorithm
The hilbert curve as a space filling curve (SFC) is a fascinating mathematical object. 
Since Cantor we know, that the unit interval $[0,1]$ in $\mathbb{R}$ has just as many points as $[0,1]^2$ in $\mathbb{R}^2$.
Thus, mathematicians wondered if a continuous bijective mapping between those intervals was possible.
Today, we know thanks to E. Netto that this is not the case, but surjective and continuous is.
This was the birth of space fillings curves like the hilbert curve - a curve that traverses every point in $[0,1]^2$. 
More than 100 years after definition of the hilbert curve, John Skillings' found a very elegant algorithm, for computing coordinates of the hilbert curves, given so called hilbert indices (1,2,3,..) and also for getting hilbert indicis for coordinates of the curve. 

## Computation of the Hilbert Curve

For the <b>computation</b> of the hilbert curve, John Skillings' algorithm is used, that works on bit level.
Since I had no access to his paper (Programming the Hilbert Curve, 2004) I relied heavily on this repository from Princeton University:https://github.com/PrincetonLIPS/numpy-hilbert-curve since I used their code for guidance, to create my own implementation and gain a better understanding what the algorithm is doing. 
Thus, if you just need a library for encoding and decoding I suggest to simply install their package. 

## Visualization:
For static visualization purpose you can use the visualize_hilbert_curve script (based on matplotlib) with the following parameters:<br>
Dimensions: <b>-dims (int)</b>: Can be 2 or 3<br>
Bits      : <b>-bits (int)</b>: Can range from 1 to 8 (since the implementation builds up on 8 bits, which already gives a very good impression how the Hilbert Curve converges towards a square/cube)
Stroke Width: <b>--stroke-width (float)</b>: The width of the lines, being plotted. Default is 0.4.

## Animation:


<figure markdown>
<img src="hilbert_curve_animation\animation_gifs\animation_small.gif" height="350px">
<img src="hilbert_curve_animation\animation_gifs\3d_animation_small.gif" height="350px">
<figcaption>Construction process of Skillings' algorithm of the 2D hilbert curve with 4 bits in 2D (265 points) and 3D (32.768 points) </figcaption>

</figure>

In the folder hilbert_curve_animation you'll find a Processing sketch that can animate the generation of the Hilbert Curve via the Skilling algorithm. I modified the decode function (hilbert index -> coordinate), so it is possible to store intermediate results of the algorithm.
Those are placed in a folder, that is used in the processing sketch to read those csv files with intermediate results. During the animation, the sketch interpolates between points of two files, starting from the earliest until it ends at the final hilbert curve.



## Installation
Anleitung zur Installation.

## Nutzung
Kurze Beispiele.