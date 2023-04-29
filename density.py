import pyvista
import argparse
import os
import sys
import pandas as pd


#D:\ararat\data\files\N\38\478130\4419430\128\finds\individual\20\3d\gp\a.ply
#D:\ararat\data\files\N\38\478130\4419430\128\finds\individual\20\a.xlsx
#path = 'D:/ararat/data/files/N/38/478130/4419430/128/finds/individual/55/3d/gp/a.ply'

parser = argparse.ArgumentParser()
#parser.add_argument('--folder_num', default='128', type=str)
parser.add_argument('--outdir', default="density.xlsx", type=str)
args = parser.parse_args()

outputs = []
output_vol_failed = []

def convert_to_num(path_list):
    return_list = []
    for item in path_list:
        if item.isdigit():
            return_list.append(int(item))
    return_list.sort()
    return return_list


def find_volume(path):
    try:
        mesh = pyvista.read(path)
        return float(mesh.volume)
    except Exception as error:
        print(error)
        return 0

def get_weight(path):
    df = pd.read_excel(path)
    if len(df['Weight']) == 0:
        return 0
    return float(df['Weight'][0])

def find_density(ply_path, xlsx_path):
    volume = find_volume(ply_path)
    weight = get_weight(xlsx_path)
    if volume == 0:
        print(f'mesh volume not found in {ply_path}')
        output_vol_failed.append(ply_path)
        return weight, volume, 0
    return weight, volume, weight / (volume / 1000.0)

path = 'D:/ararat/data/files/N/38/478130/4419430/'
path_list = convert_to_num(os.listdir(path))

for num1 in path_list:
    path2 = path + str(num1) + '/finds/individual/'
    
    if os.path.exists(path2):
        path_list2 = convert_to_num(os.listdir(path2))
        for num2 in path_list2:
            ply_path = path2 + str(num2) + '/3d/gp/a.ply'
            xlsx_path = path2 + str(num2) + '/a.xlsx'
            if os.path.exists(ply_path) and os.path.exists(xlsx_path):
                print(f'get density in {path2 + str(num2)}')
                weight, volume, density = find_density(ply_path, xlsx_path)
                if density != 0:
                    outputs.append([num1, num2, weight, volume, density])
                
df_density = pd.DataFrame(outputs, columns=['num1', 'num2', 'weight', 'volume', 'density'])
df_density.to_excel(args.outdir, index=False) 

print('--failed ouput files--')
for i in range(len(output_vol_failed)):
    print(output_vol_failed)
