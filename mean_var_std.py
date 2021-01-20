import numpy as np

def calculate(list):

    if len(list) == 9:
      operations = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation" : np.std,
        "max": np.max,
        "min": np.min,
        "sum":np.sum
        }

      results = [ [0] * 3 for i in range(len(operations)) ]
    
      calculations = dict()

      matrix = np.array(list)
      matrix = matrix.reshape(3,3)

      for i, operation in enumerate(operations.keys()):
        results[i] = [operations[operation](matrix, axis=0).tolist(), operations[operation](matrix, axis=1).tolist(), operations[operation](matrix)]

        calculations[operation] = results[i]

    else:  
      raise ValueError('List must contain nine numbers.')

    return calculations