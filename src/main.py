import src.function as f
import src.Preprocessing as p
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import h5py

file_path = r"C:\AIEEE\DATASET\CARDRF\LOS\Test\UAV\BEEBEERUN\FLYING\BEEBEERUN_0000100002.mat"
file_path = file_path.replace("\\", "/")
print(file_path)

f.drowGraph(file_path)


# .mat -> pandas DataFrame 변환
# data, data_ch, data_xy, frame = p.h5pyToData(file_path)
# df = pd.DataFrame(data)
# df_ch = pd.DataFrame(data_ch)
# df_xy = pd.DataFrame(data_xy)
# frame = pd.DataFrame(frame)
