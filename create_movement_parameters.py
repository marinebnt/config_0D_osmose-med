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

import pandas as pd
import xarray as xr
import numpy as np
data = pd.read_csv('osm_param-movement.csv', sep=';', header=None)
data

parnames = data.iloc[:, 0]
parnames

toproc = [p for p in parnames if p.startswith('movement.species')]
toproc[:5]

pfile = [p.replace('.species', '.file') for p in toproc]
pfile[:5]

pvar = [p.replace('.species', '.variable') for p in toproc]
pvar[:5]

psteps = [p.replace('.species', '.nsteps.year') for p in toproc]
psteps[:5]

with open('osm_param-movement2.csv', 'w') as fout:
    for p in pvar:
        out = '%s,%s\n' %(p, 'movement')
        fout.write(out)
    for p in pfile:
        out = '%s,%s\n' %(p, 'movements_map0D.nc')
        fout.write(out)
    for p in psteps:
        out = '%s,%d\n' %(p, 24)
        fout.write(out)
    fout.write('movement.netcdf.enabled,true\n')

dsout = xr.Dataset()
dsout['movement'] = (['time', 'y', 'x'], np.ones((24, 1, 1)))
dsout.to_netcdf('movements_map0D.nc')


