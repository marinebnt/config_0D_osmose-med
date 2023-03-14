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

nx = ny = 1
latitude = [43.142]
longitude = [5.233]

output = np.ones((len(latitude), len(latitude)))

dsout = xr.Dataset()
dsout['lat'] = (['lat'], latitude)
dsout['lon'] = (['lon'], longitude)
dsout['map'] = (['lat', 'lon'], output)
dsout
# -

dsout.to_netcdf('map0D.nc')
dsout


