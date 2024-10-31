import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem, Lipinski, DataStructs
from difflib import SequenceMatcher

# Load dataset
df = pd.read_excel("Final Dataset.xlsx", usecols=[1])

# Function to check Lipinski's Rule of Five with scoring
def check_lipinski_rule(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    mw = Descriptors.MolWt(mol)
    logp = Chem.Crippen.MolLogP(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)

    # Checking each criterion and calculating score
    criteria = [
        mw <= 500,
        logp <= 5,
        hbd <= 5,
        hba <= 10
    ]
    score = criteria.count(True) / len(criteria)  # Score calculation

    print(f"MW: {mw:.2f}, LogP: {logp:.2f}, HBD: {hbd}, HBA: {hba}")
    print(f"Lipinski Rule Score: {score:.2f}")

    return score

# Simulate ADMET evaluation based on molecular properties
def admet_evaluation_simulate(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    logp = Chem.Crippen.MolLogP(mol)
    mw = Descriptors.MolWt(mol)
    tpsa = Descriptors.TPSA(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)

    print("\nADMET Simulation Results:")
    print(f"LogP: {logp:.2f}, TPSA: {tpsa:.2f}, MW: {mw:.2f}, HBD: {hbd}, HBA: {hba}")

    # Simulating Absorption
    if logp > 5 or tpsa > 140:
        print("Absorption: Poor")
    else:
        print("Absorption: Good")

    # Simulating Distribution
    if mw > 500 or hbd > 5:
        print("Distribution: Limited")
    else:
        print("Distribution: Extensive")

    # Simulating Metabolism
    if mw < 300:
        print("Metabolism: Fast")
    else:
        print("Metabolism: Slow")

    # Simulating Excretion
    if tpsa > 120:
        print("Excretion: Delayed")
    else:
        print("Excretion: Normal")

    # Simulating Toxicity
    if hba > 10 or logp > 5:
        print("Toxicity: High")
        return False
    else:
        print("Toxicity: Low")
        return True

# Calculate Tanimoto Similarity
def calculate_similarity(input_smiles, dataset_smiles):
    mol1 = Chem.MolFromSmiles(input_smiles)
    mol2 = Chem.MolFromSmiles(dataset_smiles)
    if mol1 and mol2:
        fps1 = Chem.RDKFingerprint(mol1)
        fps2 = Chem.RDKFingerprint(mol2)
        return DataStructs.TanimotoSimilarity(fps1, fps2)
    return 0.0

# Calculate Morgan Fingerprint Similarity
def calculate_similarity_Morgan(input_smiles, dataset_smiles):
    mol1 = Chem.MolFromSmiles(input_smiles)
    mol2 = Chem.MolFromSmiles(dataset_smiles)
    if mol1 and mol2:
        fps1 = AllChem.GetMorganFingerprintAsBitVect(mol1, radius=2, nBits=2048)
        fps2 = AllChem.GetMorganFingerprintAsBitVect(mol2, radius=2, nBits=2048)
        return DataStructs.TanimotoSimilarity(fps1, fps2)
    return 0.0

# Main Logic
input_smiles = input('Your_Input_SMILES_Goes_Here: ')
tanimoto_threshold = 0.75
found = False

for index, row in df.iterrows():
    smiles = row['SMILES']
    tanimoto_similarity = calculate_similarity(input_smiles, smiles)
    tanimoto_similarity_Morgan = calculate_similarity_Morgan(input_smiles, smiles)
    string_similarity = SequenceMatcher(None, input_smiles, smiles).ratio()

    if tanimoto_similarity >= tanimoto_threshold:
        print("------------------------------------------------------------------------------------")
        print("High Chance--->This is a cancer-related drug (from Final Dataset.xlsx)")
        print(f"Tanimoto Similarity: {tanimoto_similarity:.2f}")
        print(f"Tanimoto Similarity (using Morgan Fingerprint): {tanimoto_similarity_Morgan:.2f}")
        print(f"String Similarity: {string_similarity:.2f}")
        found = True

        lipinski_score = check_lipinski_rule(input_smiles)
        if lipinski_score == 1.0:
            print("The drug follows Lipinski's Rule of Five.")
        else:
            print(f"The drug doesn't follows Lipinski's Rule of Five with a score of {lipinski_score:.2f}.")

        if admet_evaluation_simulate(input_smiles):
            print("The drug has favorable ADMET properties.")
        else:
            print("The drug has not favorable ADMET properties.")
        print("------------------------------------------------------------------------------------")
        break

if not found:
    print("------------------------------------------------------------------------------------")
    print("Not a cancer-related drug")
    lipinski_score = check_lipinski_rule(input_smiles)
    if lipinski_score == 1.0:
        print("The drug follows Lipinski's Rule of Five.")
    else:
        print(f"The drug doesn't follows Lipinski's Rule of Five with a score of {lipinski_score:.2f}.")

    if admet_evaluation_simulate(input_smiles):
        print("The drug has favorable ADMET properties.")
    else:
        print("The drug has not favorable ADMET properties.")
    print("------------------------------------------------------------------------------------")