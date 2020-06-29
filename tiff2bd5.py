#
# tiff2bd5.py
# kkyoda@riken.jp (Feb.24,2020)
#

import sys
import tables
from tables import *
import numpy as np
import cv2

# input & output files
img_path = sys.argv[1]
hdf5_out = sys.argv[2]

class Data(IsDescription):
	oID	= StringCol(8, dflt="", pos=0)
	t	= Int32Col(dflt=0, pos=1)
	entity	= StringCol(8, dflt="", pos=2)
	sID	= Int32Col(dflt=0, pos=3)
	x	= UInt16Col(dflt=0, pos=4)
	y	= UInt16Col(dflt=0, pos=5)

# preprocessing
img = cv2.imread(img_path)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

# find contours of ROIs
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours = [np.squeeze(cnt, axis=1) for cnt in contours]

# output to bd5 file
h5file = open_file(hdf5_out, mode="w", title="bd5 file")
group = h5file.create_group('/', 'data', 'data group')
series = h5file.create_group('/data', '0', 'time index 0')
object = h5file.create_group('/data/0', 'object', 'object0')

table = h5file.create_table('/data/0/object', '0', Data, "dataset")

data = table.row

# store xy coordinates to bd5 dataset table
for i, cnt in enumerate(contours):
	for j in cnt:
		data['oID']	= '%06d' % (i)
		data['t']	= 0
		data['entity']	= 'line'
		data['sID'] = i
		data['x']	= j[0]
		data['y']	= j[1]
		data.append()
	# for closed line
	data['oID']	= ' %06d' % (i)
	data['t']	= 0
	data['entity']	= 'line'
	data['sID']	= i
	data['x']	= cnt[0, 0]
	data['y']	= cnt[0, 1]
	data.append()
	

table.flush()

h5file.close()
