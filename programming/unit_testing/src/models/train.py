import numpy as np

def split_into_training_and_testing_sets(data_array):
    dim = data_array.ndim
    if dim != 2:
        msg = "Argument data_array must be two dimensional. "
        msg += "Got {0} dimensional array instead!"
        raise ValueError(msg.format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        msg = "Argument data_array must have at least 2 rows, "
        msg += "it actually has just {0}"
        raise ValueError(msg.format(num_rows))
    num_training = int(0.75 * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]

def model_test(testing_set, slope, intercept):
    dim = testing_set.ndim
    if dim != 2:
        msg = "Argument testing_set must be two dimensional. "
        msg += "Got {0} dimensional array instead!"
        raise ValueError(msg.format(dim))
    num_cols = testing_set.shape[1]
    if num_cols != 2:
        msg = "Argument testing_set must have 2 columns for univariate linear regression. "
        msg+= "It actually has {0} columns"
        raise ValueError(msg.format(num_cols))
    actual_price = testing_set[:, 1]
    predicted_price = slope*testing_set[:, 0] + intercept
    residual_sum_of_squares = np.sum(np.square(predicted_price - actual_price)) / testing_set.shape[0]
    return 1 - residual_sum_of_squares / np.var(actual_price)
