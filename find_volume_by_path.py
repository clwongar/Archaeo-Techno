import pyvista as pv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='a.ply', type=str)
args = parser.parse_args()

try:
    mesh = pv.read(args.path)
    print(mesh.volume)
except Exception as error:
    print(error)