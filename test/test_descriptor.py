import sys
sys.path.append("..")

import aflowpy

material = aflowpy.descriptor(sets='AlCu_pvMn_pv',
        calculations='T0001.A2BC',
        library='LIB3_RAW')

print(material.compound)

print('Supported Properties:')
for i in range(len(material.supported_properties)):
        print('{num}th: {property}'.format(num=i,property=material.supported_properties[i]))

#print(material.savefile()) # Download all files from AFlowlib.org