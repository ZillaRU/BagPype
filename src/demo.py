import bagpype


mydna = bagpype.molecules.Protein()

parser = bagpype.parsing.PDBParser('data/1bna.pdb', download=False)
parser.parse(mydna, strip = {'res_name': ['HOH']})

ggenerator = bagpype.construction.Graph_constructor()
ggenerator.construct_graph(mydna)

