import sys
sys.path.append("..")

import aflowpy

material = aflowpy.descriptor(sets='AlCu_pvMn_pv',
        calculations='T0001.A2BC',
        library='LIB3_RAW')

print(material.compound)