import xarray as xr
import numpy as np

names = {}
names['plankton.name.plk0'] = 'picophyto'
names['plankton.name.plk1'] = 'nanophyto'
names['plankton.name.plk2'] = 'microphyto'
names['plankton.name.plk3'] = 'nanozoo'
names['plankton.name.plk4'] = 'microzoo'
names['plankton.name.plk5'] = 'mesozoo'
names['plankton.name.plk6'] = 'benthos'
names

data = xr.open_dataset('eco3m_med.nc')
data


nx = data.dims['nx']
ny = data.dims['ny']
ntime = data.dims['Time']
ntime, ny, nx

lon = data['longitude']
lat = data['latitude']
lon

dx = lon.values[:, 1:] - lon.values[:, :-1]
dx = np.unique(dx)
dx

dy = lat.values[1:, :] - lat.values[:-1, :]
dy = np.unique(dy)
dy

surf = np.full((ny, nx), dx[0] * dx[0])
surf

# +
dsout = xr.Dataset()

for i in range(0, 6):
    
    key = 'plankton.name.plk%d' %i
    name = names[key]
    
    temp = data['ltl_biomass'].isel(ltl=i).to_masked_array()
    dsout[name] = (['Time', 'ny', 'nx'], temp)
    
dsout['Time'] = data['Time']
dsout['longitude'] = data['longitude']
dsout['latitude'] = data['latitude']
dsout['surface'] = (['ny', 'nx'], surf)
dsout.to_netcdf('corrected_eco3m_med.nc')
# -


