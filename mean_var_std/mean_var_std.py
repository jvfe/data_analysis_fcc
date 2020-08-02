import numpy as np


def make_array(func, arr):
    results = [func(arr, axis=0), func(arr, axis=1), func(arr)]
    convert = [a.tolist() for a in results]
    return convert


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.reshape(np.asarray(list), (3, 3))

    mean_arr = make_array(np.mean, arr)
    var_arr = make_array(np.var, arr)
    std_arr = make_array(np.std, arr)
    max_arr = make_array(np.max, arr)
    min_arr = make_array(np.min, arr)
    sum_arr = make_array(np.sum, arr)

    calculations = {
        "mean": mean_arr,
        "variance": var_arr,
        "standard deviation": std_arr,
        "max": max_arr,
        "min": min_arr,
        "sum": sum_arr,
    }

    return calculations
