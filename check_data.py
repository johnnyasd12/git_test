import pandas as pd
import h5py

h5_path = 'Data_SumMe_google_p5.h5'
#df = pd.read_hdf(h5_path)
#print(df)

#f = h5py.File(h5_path,'r+')
#
#group_keys = list(f.keys())
#a_group_key = group_keys[0]
#data = {}
#for key in group_keys:
#    print(key)
#    data[key] = list(f[key])


list_path = ['Data_SumMe_google_p5.h5','Data_TVSum_google_p5.h5','Data_Youtube_google_p5.h5','Data_OVP_google_p5.h5']

data_all = {}
for path in list_path:
    print(path)
    fl = h5py.File(path,'r+')
    dt = {}
    grp_keys = list(fl.keys())
    for key in grp_keys:
        print(key)
        dt[key] = list(fl[key])
    data_all[path] = dt


shot_data_all = {}

list_name = ['SumMe','TVSum']

