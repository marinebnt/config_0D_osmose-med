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

data = xr.open_dataset('eco3m_med_0D.nc')
data
# -

varnames = [v for v in data.variables if 'biomass' in v]
varnames

rename = {}
for v in varnames:
    rename[v] = v.replace(' biomass', '')
rename

data = data.rename(rename)
data

data.to_netcdf('eco3m_med_0D.nc')
