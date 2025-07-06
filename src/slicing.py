import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import ruptures as rpt
import h5py
import torch
from kymatio.torch import Scattering1D

from src.functions import load_data

file_path = r"C:\AIEEE\DATASET\CARDRF\LOS\Test\UAV\BEEBEERUN\FLYING\BEEBEERUN_0000100002.mat"

data, signal_v = load_data(file_path)


model = "l2"  # 평균 변화 기준
algo = rpt.Binseg(model='l2').fit(data)
change_points = algo.predict(n_bkps=1)

print("Change Points:", change_points)