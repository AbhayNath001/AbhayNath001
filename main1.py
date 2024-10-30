import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit.Chem import Lipinski
from rdkit.Chem import DataStructs
import matplotlib.pyplot as plt

df = pd.read_excel("ML_Big_with_70.xlsx", usecols=[3, 4], names=["SMILES", "Status"])

P_Inhibitor = 0.51
P_Activator = 0.49

def bayesian_posterior(tanimoto_similarity, P_prior):
    likelihood = tanimoto_similarity
    P_posterior = (likelihood * P_prior) / (likelihood * P_prior + (1 - likelihood) * (1 - P_prior))
    return P_posterior

def check_lipinski_rule(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    mw = Chem.Descriptors.MolWt(mol)
    logp = Chem.Crippen.MolLogP(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)

    tpsa = Descriptors.TPSA(mol)
    nrb = Descriptors.NumRotatableBonds(mol)
    nar = Descriptors.NumAromaticRings(mol)
    nha = mol.GetNumHeavyAtoms()

    num_ring_atoms = 0
    for ring in mol.GetRingInfo().BondRings():
        num_ring_atoms += len(ring)
    num_steric_atoms = mol.GetNumHeavyAtoms() - num_ring_atoms
    
    if mw <= 500 and logp <= 5 and hbd <= 5 and hba <= 10:
        return True
    else:
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

input_smiles = input('Your_Input_SMILES_Goes_Here: ')

tanimoto_threshold = 0.75

max_similarity_inhibitor = 0
max_similarity_activator = 0
best_match_inhibitor = None
best_match_activator = None

for index, row in df.iterrows():
    smiles = row['SMILES']
    status = row['Status']
    tanimoto_similarity = calculate_similarity(input_smiles, smiles)
    
    if status == 'Inhibitor' and tanimoto_similarity >= max_similarity_inhibitor:
        max_similarity_inhibitor = tanimoto_similarity
        best_match_inhibitor = smiles
        
    if status == 'Activator' and tanimoto_similarity >= max_similarity_activator:
        max_similarity_activator = tanimoto_similarity
        best_match_activator = smiles

posterior_inhibitor = bayesian_posterior(max_similarity_inhibitor, P_Inhibitor)
posterior_activator = bayesian_posterior(max_similarity_activator, P_Activator)

print("------------------------------------------------------------------------------------")
if posterior_activator > posterior_inhibitor:
    print(f"Predicted as: Activator")
    print(f"Tanimoto Similarity: {max_similarity_activator:.2f}")
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

elif posterior_inhibitor > posterior_activator:
    print(f"Predicted as: Inhibitor")
    print(f"Tanimoto Similarity: {max_similarity_inhibitor:.2f}")
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
    print("Uncertain Classification")
    print(f"Tanimoto Similarity (Inhibitor): {max_similarity_inhibitor:.2f}")
    print(f"Tanimoto Similarity (Activator): {max_similarity_activator:.2f}")
    if check_lipinski_rule(input_smiles):
        print("The compound follows Lipinski's Rule of Five.")
    else:
        print("The compound does not follow Lipinski's Rule of Five.")