import pandas as pd
from rdkit import Chem          #pip install pandas rdkit
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs

# Load the "Name_and_SMILES.csv" and "SMILES.csv" datasets
name_and_smiles_df = pd.read_csv("Name_and_SMILES.csv")
smiles_df = pd.read_csv("SMILES.csv")

# Extract SMILES representations from both datasets
cancer_smiles = name_and_smiles_df["SMILES Representation"]
additional_smiles = smiles_df["Smiles"]

# Create a set to store unique augmented SMILES
unique_augmented_smiles = set()

# Define a function to augment SMILES
def augment_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        # Example augmentation: generating isomeric SMILES
        augmented_mols = [Chem.MolToSmiles(m, isomericSmiles=True) for m in AllChem.EnumerateStereoisomers(mol)]
        return augmented_mols
    return []

# Iterate through the SMILES in both datasets
for smiles in cancer_smiles:
    augmented_smiles = augment_smiles(smiles)
    unique_augmented_smiles.update(augmented_smiles)

# Iterate through the additional SMILES dataset
for smiles in additional_smiles:
    augmented_smiles = augment_smiles(smiles)
    unique_augmented_smiles.update(augmented_smiles)

# Create a DataFrame from the unique augmented SMILES
augmented_smiles_df = pd.DataFrame({"Unique Augmented SMILES": list(unique_augmented_smiles)})

# Save the augmented SMILES to an Excel file
augmented_smiles_df.to_excel("Unique_Augmented_SMILES.xlsx", index=False)