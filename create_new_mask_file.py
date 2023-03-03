# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#data = xr.open_dataset('eco3m_med.nc')
#data
# -

#test = np.ma.getmaskarray(data['ltl_biomass'].to_masked_array())
#test = np.sum(test, axis=(0, 1))
# np.unique(test)

np.unique(1)

datamask = 1 - (test > 0).astype(int)
cs = plt.imshow(datamask)
plt.colorbar(cs)

csvmask = pd.read_csv('grid-mask.csv', header=None)
csvmask = csvmask.values[::-1]
csvmask[csvmask == 0] = 1
csvmask[csvmask < 0] = 0

cs = plt.imshow(csvmask)
plt.colorbar(cs)

# Let's compare masks by computing $M_{LTL} - M_{grid}$ 
# - If LTL has data ($M_{LTL} = 1$) and grid is land ($M_{grid} = 0$), then $M_{LTL} - M_{grid} = 1$.
# - If LTL has no data ($M_{LTL} = 0$) and grid is ocean ($M_{grid} = 1$), then $M_{LTL} - M_{grid} = -1$. **Critical error since NaN value will be read**
# - If both masks are consistent, the diff is 0.

diffmask = datamask -csvmask
cs = plt.imshow(diffmask)
plt.colorbar(cs)
print(np.unique(diffmask))

# Let's try to save the CSV mask in a NetCDF file:

dsout = xr.Dataset()
dsout['longitude'] = data['longitude']
dsout['latitude'] = data['latitude']
dsout['mask'] = (['ny', 'nx'], csvmask)
dsout.to_netcdf('corrected_mask.nc')
