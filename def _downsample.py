import numpy as np


def _downsample(
    src_arr: np.ndarray, src_cellsize: float, cellsize: float
) -> np.ndarray:
    """Creates a smaller array by aggregating several cells of the `src_arr` into each cell of the resulting array.

    `cellsize` must be a multiple of 0.1, which is the base cellsize used in surface sharing.
    """
    factor = round(cellsize * 10) // round(src_cellsize * 10)

    arr = np.empty(
        (2, src_arr.shape[1] // factor, src_arr.shape[2] // factor),
        dtype=np.float64,
    )
    for i in range(0, arr.shape[1]):
        for j in range(0, arr.shape[2]):
            arr[0][i][j] = np.nanmean(
                src_arr[0][i * factor : (i + 1) * factor, j * factor : (j + 1) * factor]
            )
            arr[1][i][j] = np.nanmax(
                src_arr[1][i * factor : (i + 1) * factor, j * factor : (j + 1) * factor]
            )
    return arr


src_arr = np.array(
    [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]],
    ]
)


print(_downsample(src_arr, 1.0, 2.0))

# Signal 0:
# [[ (1+2+5+6)/4 , (3+4+7+8)/4 ]
#  [ (9+10+13+14)/4 , (11+12+15+16)/4 ]]

# [[ 3.5 , 5.5 ]
#  [11.5 , 13.5 ]]

# Signal 1:
# [[ max(10,20,50,60) , max(30,40,70,80) ]
#  [ max(90,100,130,140) , max(110,120,150,160) ]]

# [[ 60 , 80 ]
#  [140 , 160 ]]

# Final Output:
# [[[  3.5   5.5]
#   [ 11.5  13.5]]

#  [[ 60.   80. ]
#   [140.  160. ]]]
