# Archaeo-Techno

This repo finds volume and density of a mesh in .ply file in specific file locations. Pyvista library is used to find volume.

#### Environment
In order to run the code, open anaconda prompt and type in the following.

```
#create conda environment
conda create -n test1_env python=3.8

#activate conda environment
conda activate test1_env

#install libraries
pip install pyvista[all]
pip install pandas
pip install openpyxl
```

#### 1. Find Volume

The code in find_volume.py gets the volume (in $mm^3$) of the 3d models under D:\ararat\data\files\N\38\478130\4419430\Y\finds\3dbatch\2022\batch_XXX\registration_reso1_maskthres242\final_output\piece_0_world_sample0_3_mesh.ply
in folder 1, 2, and 3 (Y) and replace XXX with final number

```
python find_volume.py
```
Sample: (output file is named 'volume.xlsx')

<img width="276" alt="image" src="https://user-images.githubusercontent.com/61493193/235313392-27adbaf0-ac51-4d46-8dbc-7ee331cde218.png">


The code in find_volume_by_path.py gets the volume (in $mm^3$) of the 3d models in path specified
```
python find_volume_by_path.py --path=YOUR_PATH
```

#### 2. Find Density
The code in density.py gets the weight and volume of the sherds and calculate the density (in $g/mm^3$).
Mesh directory (Find volume): D:/ararat/data/files/N/38/478130/4419430/xxx/finds/individual/xxx/3d/gp/a.ply
Weight directory: D:/ararat/data/files/N/38/478130/4419430/xxx/finds/individual/xxx/a.xlsx

```
python density.py
```

Sample: (output file is named 'density.xlsx')

<img width="205" alt="image" src="https://user-images.githubusercontent.com/61493193/235314411-46ceeb3a-d627-4523-93da-0e339a4e9979.png">

Remarks: 
- Only sherds with both a.ply and a.xlsx files are calculated. 
- a.ply files with only points will give error and not calculated. These files are handled separately.
- density_edit.xlsx is the file that group all densities required.




