import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py

def print_all_datasets(h5group, path="/"):
    for key in h5group:
        item = h5group[key]
        current_path = path + key
        if isinstance(item, h5py.Group):
            # 그룹이면 재귀 탐색
            print_all_datasets(item, current_path + "/")
        elif isinstance(item, h5py.Dataset):
            # 데이터셋이면 출력
            print(f"📁 Dataset: {current_path}")
            print(f"   └ Shape: {item.shape}, Dtype: {item.dtype}")

def drowGraph(file_path):
    with h5py.File(file_path, 'r') as f:
        # Y축 신호 데이터
        data = np.array(f['/Channel_1/Data'][:]).flatten()  # shape: (5000000,)
        yinc = f['/Channel_1/YInc'][0][0]  # float (스칼라)
        yorg = f['/Channel_1/YOrg'][0][0]  # float (스칼라)
        y = data * yinc + yorg

        x_origin = f['/Channel_1/XOrg'][0][0]      # float (스칼라)
        x_inc = f['/Channel_1/XInc'][0][0]         # float (스칼라)
        #x_disp_range = f['/Channel_1/XDispRange'][0][0]  # float64
        # X축 시간 벡터 생성
        timeline = np.array(range(len(data)), float)
        x = timeline * x_inc + x_origin

        # X 단위 추출
        x_unit_raw = f['/Channel_1/XUnits'][:]  # 예: (6, 1)
        x_unit = ''.join(chr(c[0]) for c in x_unit_raw)
        print("X축 단위:", x_unit)
        y_unit_raw = f['/Channel_1/YUnits'][:]
        y_unit = ''.join(chr(c[0]) for c in y_unit_raw)
        print("y축 단위:",y_unit)

    # 시각화 (앞부분만)
    plt.figure(figsize=(12, 4))
    plt.plot(x[:10000], y[:10000])
    plt.title("RF Signal")
    plt.xlabel(x_unit)
    plt.ylabel(y_unit)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def getSTR(f, file_path):
    unit_raw = f[file_path][:]
    unit = ''.join([chr(c[0]) for c in unit_raw])  
    return unit 