import numpy as np
import pandas as pd
import h5py


def load_data(file_path):
    with h5py.File(file_path, 'r') as f:
        data = np.array(f['/Channel_1/Data'][:], dtype=float)
        YInc = np.array(f['/Channel_1/YInc'][0][0], dtype=float)
        YOrg = np.array(f['/Channel_1/YOrg'][0][0], dtype=float)
        signal_v = data* YInc + YOrg
    return data.flatten(), signal_v.flatten()