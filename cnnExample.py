import numpy as np

# Define the original image (6x6 matrix)
image = np.array([
    [1, 2, 3, 0, 1, 2],
    [4, 5, 6, 1, 0, 1],
    [7, 8, 9, 0, 1, 2],
    [1, 3, 2, 2, 1, 0],
    [0, 1, 4, 3, 2, 1],
    [1, 2, 0, 1, 3, 4]
])

# Define the filter (3x3 matrix)
filter = np.array([
    [1, 0, -1],
    [0, 1, 0],
    [-1, 0, 1]
])

# Get dimensions of the image and filter
image_size = image.shape[0]
filter_size = filter.shape[0]

# Calculate the output size
output_size = image_size - filter_size + 1

# Initialize the output matrix
output = np.zeros((output_size, output_size))

# Perform the convolution operation
for i in range(output_size):
    for j in range(output_size):
        # Extract the current region of interest from the image
        region = image[i:i + filter_size, j:j + filter_size]
        # Perform element-wise multiplication and sum the results
        output[i, j] = np.sum(region * filter)

# Print the resulting convoluted image
print("Convoluted Output:")
print(output)
