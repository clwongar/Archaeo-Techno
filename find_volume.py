import pyvista
import argparse
import os
import sys
import pandas as pd


#D:\ararat\data\files\N\38\478130\4419430\1\finds\3dbatch\2022\batch_004\registration_reso1_maskthres242\final_output\piece_0_world_sample0_3_mesh

parser = argparse.ArgumentParser()
parser.add_argument('--folder_num', default='3', type=str)
parser.add_argument('--year', default='2022', type=str)
parser.add_argument('--max_batch', default='100', type=str)
parser.add_argument('--max_piece', default='100', type=str)
parser.add_argument('--outdir', default="volume.xlsx", type=str)
args = parser.parse_args()

folder_num = int(args.folder_num)
outputs = []
for i in range(folder_num):
    batch_num_count = 0
    for batch_num_count in range(int(args.max_batch)):
        batch_num = str(batch_num_count).zfill(3)
        dir1 = 'D:/ararat/data/files/N/38/478130/4419430/' + str(i+1) + '/finds/3dbatch/' + args.year + '/batch_' + batch_num + '/'
        if os.path.exists(dir1):
            for piece_num_count in range(int(args.max_piece)):
                dir2 = 'registration_reso1_maskthres242/final_output/piece_' + str(piece_num_count) + '_world_sample0_3_mesh.ply'
                out_path = os.path.join(dir1, dir2)
                if os.path.exists(out_path):
                    mesh = pyvista.read(os.path.join(dir1, dir2))
                    output_text = 'folder' + str(i+1) + ' batch_' + str(batch_num) + ' piece_' + str(piece_num_count) + ' volume: ' + str(mesh.volume)
                    outputs.append([i+1, batch_num, piece_num_count, mesh.volume])
                    print(output_text)
                else:
                    break
        else:
            break

df = pd.DataFrame(outputs, columns=['Folder', 'Batch_Num', 'Piece_Num', 'Volume'])
df.to_excel(args.outdir, index=False) 
