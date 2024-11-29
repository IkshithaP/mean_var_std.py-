import numpy as np

def calculate(numbers):
    # Checking if the input list has exactly 9 numbers
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converting the input list into a 3x3 NumPy array
    matrix = np.array(numbers).reshape(3, 3)
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean along columns
            matrix.mean(axis=1).tolist(),  # Mean along rows
            matrix.mean().tolist()         # Mean of entire matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }
    
    return calculations
numbers = list(map(int, input("Enter 9 numbers separated by spaces: ").split()))

# Call the calculate function
try:
    result = calculate(numbers)
    print(result)
except ValueError as e:
    print(e)
