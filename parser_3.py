from pygcode import Line
import re

X = 0
Y = 0
Z = 0
feedrate = 0

with open('Cube_3d_printing_sample_0.15mm_PLA_MINI_37m.gcode', 'r') as fh:
    for line_text in fh.readlines()[1:200]:
        line = Line(line_text)
        x = re.findall("^;",line_text)
        if not x and len(line.block.gcodes) != 0 and line_text.startswith("G1"):
            split_line = line_text.split()
            print(line.block.gcodes)
            print(split_line)

            resX = [idx for idx in split_line if idx[0].lower() == 'X'.lower()]
            resY = [idx for idx in split_line if idx[0].lower() == 'Y'.lower()]
            resZ = [idx for idx in split_line if idx[0].lower() == 'Z'.lower()]
            resF = [idx for idx in split_line if idx[0].lower() == 'F'.lower()]

            if len(resX) != 0:
                X = resX[0].replace('X','')
            if len(resY) != 0:
                Y = resY[0].replace('Y','')
            if len(resZ) != 0:
                Z = resZ[0].replace('Z','')
            if len(resF) != 0:
                feedrate = resF[0].replace('F','')
            print(X,Y,Z,feedrate)



