import sys
import os

sys.path.append('/home/koerstz/git/tQMC/QMC')
from qmconf import QMConf


def compare_lists(a, b):
    for pair in zip(a,b):
        if pair[0] != pair[1]:
            return False
    return True

def test_qmconf():
    """ """
    test_dir = os.path.dirname(os.path.realpath(__file__)) + '/data/formats/'
    test_structures = {'xyz': 'propanol.xyz',
                       'gaussian': 'propanol.g16out',
                       'xtb': 'propanol.xtbout',
                       'orca': 'propanol.orcaout'}
    
    ref_atomic_symbols = ['C', 'C', 'C', 'O', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
    ref_atomic_numbers = [6, 6, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1]

    for fmt, f in test_structures.items():
        name = f.split('.')[0]
        qmconf = QMConf(input_mol=test_dir + f, fmt=fmt, label=name, charge=0,
                        multiplicity=1, charged_fragments=True)
        
        
        assert compare_lists(ref_atomic_symbols, qmconf.atomic_symbols), "Failed parsing symbols"
        assert compare_lists(ref_atomic_numbers, qmconf.atomic_numbers), "Failes parsing numbers"
        assert compare_lists(test_ref_structure(fmt), qmconf.structure), "Failed paring structure"

        print("{}: passed.".format(fmt))


def test_ref_structure(fmt):

    if fmt == 'gaussian':
        ref_structure = [[ 1.866940,-0.156388, 0.000352],
                         [ 0.525089, 0.539557,-0.000390],
                         [-0.611954,-0.480052,-0.000411],
                         [-1.826813, 0.234340, 0.000461],
                         [ 2.690032, 0.569470, 0.001226],
                         [ 1.994091,-0.794841,-0.884201],
                         [ 1.992826,-0.795502, 0.884615],
                         [ 0.440336, 1.204810,-0.882479],
                         [ 0.439718, 1.205592, 0.881053],
                         [-0.552311,-1.134882,-0.892604],
                         [-0.551580,-1.135806, 0.891064],
                         [-2.519060,-0.412260, 0.000327]]
    
    if fmt == 'xyz':
          ref_structure = [[1.51778, 1.31942, 0.20030],
                           [3.03508, 1.31309, 0.03796],
                           [3.55739,-0.09409,-0.24789],
                           [4.94969,-0.05094,-0.38676],
                           [1.17070, 2.35245, 0.41324],
                           [1.21678, 0.66242, 1.04409],
                           [1.02809, 0.96445,-0.73153],
                           [3.50100, 1.69514, 0.97227],
                           [3.31300, 1.98843,-0.80039],
                           [3.28452,-0.76021, 0.60206],
                           [3.10076,-0.47346,-1.18945],
                           [5.24739,-0.99362,-0.47499]]

    if fmt == 'xtb':
        ref_structure = [[1.51374993409431, 1.33139778587887, 0.19927281979160],
                         [3.02784566290880, 1.30327526416028, 0.04271925258250],
                         [3.54350930563507,-0.10477745272061,-0.23537122195370],
                         [4.94883373482566,-0.04667522761892,-0.36625899093790],
                         [1.17410982244636, 2.34460663409381, 0.39846267196699],
                         [1.20182605394798, 0.69537443826539, 1.02521809884346],
                         [1.02779990887351, 0.97763633771062,-0.70771327376871],
                         [3.50833797375176, 1.67127960714270, 0.95031026986899],
                         [3.33468339713600, 1.94946736053592,-0.78087025356745],
                         [3.26203817406596,-0.77356581429383, 0.59141645071180],
                         [3.08825031552411,-0.49154072336992,-1.15948258981964],
                         [5.29119571679048,-0.93339820978429,-0.51879323371794]]
    
    if fmt == 'orca':
        ref_structure = [[1.535783, 1.320600, 0.196511],
                         [3.039258, 1.308517, 0.041787],
                         [3.542156,-0.105580,-0.239840],
                         [4.942927,-0.043108,-0.378999],
                         [1.165847, 2.333583, 0.399913],
                         [1.207240, 0.679483, 1.025553],
                         [1.030853, 0.963812,-0.711247],
                         [3.520766, 1.709370, 0.955842],
                         [3.344670, 1.991484,-0.775743],
                         [3.265083,-0.792439, 0.584793],
                         [3.085861,-0.507895,-1.166527],
                         [5.241737,-0.934748,-0.493133]]

    return ref_structure

if __name__ == '__main__':
    test_qmconf()









