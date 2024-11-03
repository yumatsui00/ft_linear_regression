import numpy as np


def _sum(arr):
    total = 0
    for value in arr:
        total += value
    return total

def _len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def _mean(arr):
    total = _sum(arr)
    count = _len(arr)
    return total / count if count > 0 else 0

#pd.to_numeric(val, err)
def _to_numeric(values, errors='raise'):
    result = []
    for value in values:
        try:
            num = float(value)
            result.append(num)
        except ValueError:
            if errors == 'raise':
                raise ValueError(f"Unable to parse '{value}' as a number")
            elif errors == 'coerce':
                result.append(np.nan)
            elif errors == 'ignore':
                result.append(value)
            else:
                raise ValueError(f"Invalid value for 'errors' parameter")
    return result

#.notnull()
def _notnull(arr):
    return [x is not None and not np.isnan(x) for x in arr]

#np.isnan()
def _isnan(value):
    if value is None:
        return True
    return value != value

#np.isinf()
def _isinf(value):
    return value == float('inf') or value == float('-inf')