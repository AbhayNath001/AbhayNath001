import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit.Chem import Lipinski
from rdkit.Chem import DataStructs
import matplotlib.pyplot as plt

# Read the SMILES and status columns from the Excel file
#df = pd.read_excel("ML.xlsx", usecols=[3, 4], names=["SMILES", "Status"])
#df = pd.read_excel("ML_Big.xlsx", usecols=[3, 4], names=["SMILES", "Status"])
df = pd.read_excel("ML_Big_with_70.xlsx", usecols=[3, 4], names=["SMILES", "Status"])

def check_lipinski_rule(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    mw = Chem.Descriptors.MolWt(mol)                # Molecular Weight
    logp = Chem.Crippen.MolLogP(mol)                # Partition Coefficient
    hbd = Lipinski.NumHDonors(mol)                  # Hydrogen Bond Donor
    hba = Lipinski.NumHAcceptors(mol)               # Hydrogen Bond Acceptor

    tpsa = Descriptors.TPSA(mol)                    # Topological Polar Surface Area
    nrb = Descriptors.NumRotatableBonds(mol)        # Number of Rotatable Bonds
    nar = Descriptors.NumAromaticRings(mol)         # Number of Aromatic Rings
    nha = mol.GetNumHeavyAtoms()                    # Number of Heavy Atoms

    num_ring_atoms = 0
    for ring in mol.GetRingInfo().BondRings():
        num_ring_atoms += len(ring)
    num_steric_atoms = mol.GetNumHeavyAtoms() - num_ring_atoms  # Number of Steric Atoms
    
    if mw <= 500 and logp <= 5 and hbd <= 5 and hba <= 10:
        print(f"MW: {mw:.2f}, LogP: {logp:.2f}, HBD: {hbd}, HBA: {hba}")
        print(f"TPSA: {tpsa:.2f}, NRB: {nrb}, NAR: {nar}, NHA: {nha}, NSA: {num_steric_atoms}")
        return True
    else:
        print(f"MW: {mw:.2f}, LogP: {logp:.2f}, HBD: {hbd}, HBA: {hba}")
        print(f"TPSA: {tpsa:.2f}, NRB: {nrb}, NAR: {nar}, NHA: {nha}, NSA: {num_steric_atoms}")
        return False

def calculate_similarity(input_smiles, dataset_smiles):
    mol1 = Chem.MolFromSmiles(input_smiles)
    mol2 = Chem.MolFromSmiles(dataset_smiles)
    if mol1 is not None and mol2 is not None:
        fps1 = Chem.RDKFingerprint(mol1)
        fps2 = Chem.RDKFingerprint(mol2)
        similarity = DataStructs.TanimotoSimilarity(fps1, fps2)
        return similarity
    else:
        return 0.0
    
def calculate_similarity_Morgan(input_smiles, dataset_smiles):
    mol1 = Chem.MolFromSmiles(input_smiles)
    mol2 = Chem.MolFromSmiles(dataset_smiles)
    if mol1 is not None and mol2 is not None:
        fps1 = AllChem.GetMorganFingerprintAsBitVect(mol1, radius=2, nBits=2048)
        fps2 = AllChem.GetMorganFingerprintAsBitVect(mol2, radius=2, nBits=2048)
        similarity = DataStructs.TanimotoSimilarity(fps1, fps2)
        return similarity
    else:
        return 0.0

input_smiles = input('Your_Input_SMILES_Goes_Here: ')

tanimoto_threshold = 0.75

max_similarity = 0
best_match = None
best_status = None

for index, row in df.iterrows():
    smiles = row['SMILES']
    status = row['Status']
    tanimoto_similarity = calculate_similarity(input_smiles, smiles)
    
    if tanimoto_similarity >= max_similarity:
        max_similarity = tanimoto_similarity
        best_match = smiles
        best_status = status

if max_similarity >= tanimoto_threshold:
    print("------------------------------------------------------------------------------------\n")
    print(f"Tanimoto Similarity: {max_similarity:.2f}")
    print(f"Status: {best_status}")
    if check_lipinski_rule(input_smiles):
        print("The compound follows Lipinski's Rule of Five.")
    else:
        print("The compound does not follow Lipinski's Rule of Five.")
    
    mol = Chem.MolFromSmiles(input_smiles)
    mol_img = Draw.MolToImage(mol)
    mol_weight = Descriptors.MolWt(mol)

    plt.figure(figsize=(5, 5))
    plt.imshow(mol_img)
    plt.title(f"Molecular Weight: {mol_weight:.3f}")
    plt.axis('off')
    plt.show()
elif max_similarity >= 0.10:
    print("------------------------------------------------------------------------------------")
    print(f"Tanimoto Similarity: {max_similarity:.2f}")
    print(f"Status: {best_status}")
    if check_lipinski_rule(input_smiles):
        print("The compound follows Lipinski's Rule of Five.")
    else:
        print("The compound does not follow Lipinski's Rule of Five.")
    
    mol = Chem.MolFromSmiles(input_smiles)
    mol_img = Draw.MolToImage(mol)
    mol_weight = Descriptors.MolWt(mol)

    plt.figure(figsize=(5, 5))
    plt.imshow(mol_img)
    plt.title(f"Molecular Weight: {mol_weight:.3f}")
    plt.axis('off')
    plt.show()
else:
    print("------------------------------------------------------------------------------------")
    print("Not a Hsp90-related compound")
    print(f"Tanimoto Similarity: {max_similarity:.2f}")
    if check_lipinski_rule(input_smiles):
        print("The compound follows Lipinski's Rule of Five.")
    else:
        print("The compound does not follow Lipinski's Rule of Five.")
