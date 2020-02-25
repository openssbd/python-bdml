# python-bdml
Python codes for BDML/BD5 files.

## tiff2bd5.py
### Synopsis
tiff2bd5.py is python a program to find contours in a binary image tiff file and saved the contours into BD5 file, an open HDF5-based file format. It can be used together with Galaxy workflow

### Background
BD5 is an open HDF5-based format for representing quantitative data of biological dynamics. Such data can be obtained by segmenting images but are often saved as binary image data. By using bioimage informatics techniques such as ImageJ, cell profiler, and segmenter, we can segment and extract those data in numerical form as contours. These numerical data can then saved in the BD5 open HDF5-based format.

### Get started
usage: tiff2bd5.py input.tiff output.h5
- input.tiff: binary TIF image file, e.g. result of segmentation . The ROI (region of interest) should be detected as white pixel.
- output.h5: contours are calculated from input.tiff image and saved as bd5 formatted data file. 

### Issues
1. Only single TIF image file can be applied as input.
2. objectDef and scaleUnit datasets must be added separately to meet the specification of BD5 format.
3. A warning (NaturalNameWarning) will occur while running tiff2bd5.py, but BD5 file can be generated.

### For the galaxy workflow
1. Create a myTools folder in your galaxy/tools folder
2. Add the tiff2bd5.py and its definition file (tiff2bd5.xml) to the galaxy/tools/myTools folder
3. Edit galaxy/tool_conf.xml to use tiff2bd5.py

### Links
-	BD5: http://ssbd.qbic.riken.jp/bdml/
-	HDF5: https://www.hdfgroup.org/solutions/hdf5/
-	Installation of galaxy: https://galaxyproject.org/admin/get-galaxy/
-	ImageJ on galaxy: https://github.com/mutterer/ij-galaxy
-	ImageJ2 on galaxy: https://github.com/bgruening/galaxytools/tree/master/tools/image_processing/imagej2
