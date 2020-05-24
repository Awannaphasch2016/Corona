from tables import *
import tables
h5file = open_file("tutorial1.h5", mode="w", title="Test file")
group = h5file.create_group("/", 'detector', 'Detector information')
# class Particle(tables.IsDescription):
#     def __init__(self):
#         self.columns = tables.Float16Col(shape=10)
Particle = {'a':tables.Float16Col(shape=10)}
table = h5file.create_table(group, 'readout', Particle, "Readout example")
h5file.close()

import tables
import numpy as np
param = 10
with tables.open_file('save.hdf','w') as saveFile:
    tabledef = {'var1':tables.Float64Col(shape=(param))}
    table = saveFile.create_table(saveFile.root,'test',tabledef)
    tablerow = table.row
    tablerow['var1'] = np.array([1,2,3,4,5,6,7,8,9,0])
    tablerow.append()
    print(table)
    table.flush()

with tables.open_file('save.hdf','r') as sv:
    sv.root.test.read()
