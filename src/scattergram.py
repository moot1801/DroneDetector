import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from kymatio.torch import Scattering1D
import torch


df = pd.read_csv(r"C:\AIEEE\Prossessed_CardRF\Processed_CardRF\Train\UAV_Controller\DJI_MAVICPRO.csv")
scattering = Scattering1D(J=6, Q=8, shape=1024, oversampling=3)

data = df.iloc[2000, :1024].values.astype(float)
x_tensor = torch.from_numpy(data).float().unsqueeze(0)  

scat = scattering(x_tensor)

plt.figure(figsize=(10, 6))
plt.imshow(scat.view(126,128).numpy(), aspect='auto', cmap='jet', origin='lower')
plt.xlabel('Time bins')
plt.ylabel('2nd-order Scattering Coefficient')
plt.title('Scattergram (2nd-order WST)')
plt.colorbar(label='Amplitude')
plt.tight_layout()
plt.show()