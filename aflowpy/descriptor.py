import json
import warnings
from urllib.request import urlopen

__author__ = "Yang Long"
__version__ = "0.1"
__email__="longyang_123@yeah.net"

SERVER='http://aflowlib.duke.edu'
PROJECT='AFLOWDATA'

class descriptor:
    supported_properties = ('aurl','auid','data_api','data_source','loop',
            'code','compound','prototype','nspecies','natoms','composition',
            'density','scintillation_attenuation_length','stoichiometry',
            'species','species_pp','dft_type','species_pp_version',
            'species_pp_ZVAL','valence_cell_iupac','valence_cell_std',
            'volume_cell','volume_atom','pressure','stress_tensor',
            'pressure_residual','Pulay_stress','geometry','Egap','Egap_fit',
            'Egap_type','energy_cell','energy_atom','energy_cutoff',
            'delta_electronic_energy_convergence','delta_electronic_energy_threshold',
            'kpoints','enthalpy_atom','enthalpy_cell','eentropy_atom','eentropy_cell',
            'enthalpy_formation_atom','enthalpy_formation_cell','entropic_temperature',
            'PV_cell','PV_atom','spin_atom','spin_cell','spinF','spinD','stoich',
            'calculation_time','calculation_memory','calculation_cores','nbondxx',
            'sg','sg2','spacegroup_orig','spacegroup_relax','forces',
            'positions_cartesian','positions_fractional','Bravais_lattice_orig',
            'lattice_variation_orig','lattice_system_orig','Pearson_symbol_orig',
            'Bravais_lattice_relax','lattice_variation_relax','lattice_system_relax',
            'Pearson_symbol_relax','files','aflow_version','catalog','aflowlib_version',
            'aflowlib_date','aapi','keywords')

    def __init__(self,sets,calculations,library,SERVER=SERVER,PROJECT=PROJECT):
        self.sets = sets
        self.calculations = calculations 
        self.library = library
        self.SERVER = SERVER
        self.PROJECT = PROJECT

        entries = self.__getdata(sets,calculations,library,
                resources=None,SERVER=SERVER,PROJECT=PROJECT)

        self.aurl = entries['aurl']
        self.auid = entries['auid']
        self.data_api = entries['data_api']
        self.data_source = entries['data_source']
        self.loop = entries['loop']
        self.code = entries['code']
        self.compound = entries['compound']
        self.prototype = entries['prototype']
        self.nspecies = entries['nspecies']
        self.natoms = entries['natoms']
        self.composition = entries['composition']
        self.density = entries['density']
        self.scintillation_attenuation_length = entries['scintillation_attenuation_length']
        self.stoichiometry = entries['stoichiometry']
        self.species = entries['species']
        self.species_pp = entries['species_pp']
        self.dft_type = entries['dft_type']
        self.species_pp_version = entries['species_pp_version']
        self.species_pp_ZVAL = entries['species_pp_ZVAL']
        self.valence_cell_jupac = entries['valence_cell_iupac']
        self.valence_cell_std = entries['valence_cell_std']
        self.volume_cell = entries['volume_cell']
        self.volume_atom = entries['volume_atom']
        self.pressure = entries['pressure']
        self.stress_tensor = entries['stress_tensor']
        self.pressure_residual = entries['pressure_residual']
        self.Pulay_stress = entries['Pulay_stress']
        self.geometry = entries['geometry']
        self.Egap = entries['Egap']
        self.Egap_fit = entries['Egap_fit']
        self.Egap_type = entries['Egap_type']
        self.energy_cell = entries['energy_cell']
        self.energy_atom = entries['energy_atom']
        self.energy_cutoff = entries['energy_cutoff']
        self.delta_electronic_energy_convergence = entries['delta_electronic_energy_convergence']
        self.delta_electronic_energy_threshold = entries['delta_electronic_energy_threshold']
        self.kpoints = entries['kpoints']
        self.enthalpy_cell = entries['enthalpy_cell']
        self.enthalpy_atom = entries['enthalpy_atom']
        self.eentropy_cell = entries['eentropy_cell']
        self.eentropy_atom = entries['eentropy_atom']
        self.enthalpy_formation_cell = entries['enthalpy_formation_cell']
        self.enthalpy_formation_atom = entries['enthalpy_formation_atom']
        self.entropic_temperature = entries['entropic_temperature']
        self.PV_cell = entries['PV_cell']
        self.PV_atom = entries['PV_atom']
        self.spin_cell = entries['spin_cell']
        self.spin_atom = entries['spin_atom']
        self.spinD = entries['spinD']
        self.spinF = entries['spinF']
        self.stoich = entries['stoich']
        self.calculation_time = entries['calculation_time']
        self.calculation_memory = entries['calculation_memory']
        self.calculation_cores = entries['calculation_cores']
        self.nbondxx = entries['nbondxx']
        self.sg = entries['sg']
        self.sg2 = entries['sg2']
        self.spacegroup_orig = entries['spacegroup_orig']
        self.spacegroup_relax = entries['spacegroup_relax']
        self.forces = entries['forces']
        self.positions_cartesian = entries['positions_cartesian']
        self.positions_fractional = entries['positions_fractional']
        self.Bravais_lattice_orig = entries['Bravais_lattice_orig']
        self.lattice_variation_orig = entries['lattice_variation_orig']
        self.lattice_system_orig = entries['lattice_system_orig']
        self.Pearson_symbol_orig = entries['Pearson_symbol_orig']
        self.Bravais_lattice_relax = entries['Bravais_lattice_relax']
        self.lattice_variation_relax = entries['lattice_variation_relax']
        self.lattice_system_relax = entries['lattice_system_relax']
        self.Pearson_symbol_relax = entries['Pearson_symbol_relax']
        self.aflow_version = entries['aflow_version']
        self.catalog = entries['catalog']
        self.aflowlib_version = entries['aflowlib_version']
        self.aflowlib_date = entries['aflowlib_date']
        self.keywords = entries['keywords']
        self.aapi = entries['aapi']

    def savefile(self):
        return self.__savefile(sets=self.sets,
            calculations=self.calculations,
            library=self.library,
            filename=None,
            savepath='./',
            SERVER=self.SERVER,
            PROJECT=self.PROJECT)
    
    def __getdata(self,sets,calculations,library,resources,SERVER,PROJECT):
        # Standard resources request head
        URL= SERVER+'/'+PROJECT+'/' + library + '/' + sets + '/' + calculations + '/?format=json' 

        # Add resources request behind the head
        if resources is not None:      #Default settings: It will get all info of the material
            for resource in resources:
                URL += '&' + resource

        # Request the resource from AFLOWlib
        urlresponse = urlopen(URL)
        entries = json.loads(urlresponse.read().decode('utf-8'))

        return entries

    def __savefile(self,sets,calculations,library,filename,savepath,SERVER,PROJECT):
        # Standard resources request head
        URL= SERVER+'/'+PROJECT+'/' + library + '/' + sets + '/' + calculations + '/' 

        # Request the resource from AFLOWlib
        urlresponse = urlopen(URL + '?format=json&files')
        filenames = json.loads(urlresponse.read().decode('utf-8'))

        for filename in filenames['files']:
             target = urlopen(URL + filename)
             data = target.read()
             with open(savepath + filename,"wb") as obj:
                 obj.write(data)

        return True