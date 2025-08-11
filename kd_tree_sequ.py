from skillings_implementation.skillings_algorithm import hc_encode

import matplotlib.pyplot as plt
import numpy as np

quadtree = [[[1,2,3,4]], [5,6], [7],[[8,9]]]
coords = []
for quadrant in quadtree:
    for element in quadrant:
        if type(element) == int:
            n_bits = 1
            coords.append(hc_encode(element,n_dims=2, n_bits=n_bits))
        elif type(element)==list:
            for idx in element:
                n_bits = 2
                coords.append(hc_encode(idx,n_dims=2, n_bits=n_bits))

print(coords)
hilbert_coords = np.reshape(coords,(9,2))
print(hilbert_coords)
plt.plot(hilbert_coords[:, 0], hilbert_coords[:, 1], color="orange", zorder=-1)


plt.show()
