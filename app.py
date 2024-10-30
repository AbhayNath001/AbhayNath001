import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski, DataStructs, Draw
import difflib  # For string similarity
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel("ML_Big_with_70.xlsx", usecols=[3, 4], names=["SMILES", "Status"])

# Bayesian posterior function
def bayesian_posterior(tanimoto_similarity, P_prior):
    likelihood = tanimoto_similarity
    P_posterior = (likelihood * P_prior) / (likelihood * P_prior + (1 - likelihood) * (1 - P_prior))
    return round(P_posterior, 2)

# Lipinski's Rule of Five and molecular properties
def lipinski_properties(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    mw = round(Descriptors.MolWt(mol), 2)
    logp = round(Chem.Crippen.MolLogP(mol), 2)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)

    criteria = [mw <= 500, logp <= 5, hbd <= 5, hba <= 10]
    satisfied_rules = sum(criteria)

    return {
        "MW (Molecular Weight)": mw,
        "LogP (Octanol-Water Partition Coefficient)": logp,
        "HBD (Hydrogen Bond Donors)": hbd,
        "HBA (Hydrogen Bond Acceptors)": hba,
        "Lipinski's Rule Satisfaction": f"Follows {satisfied_rules} out of 4 rules"
    }

# ADMET Evaluation
def admet_evaluation(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    logp = round(Chem.Crippen.MolLogP(mol), 2)
    mw = round(Descriptors.MolWt(mol), 2)
    tpsa = round(Descriptors.TPSA(mol), 2)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)

    admet_results = {
        "LogP": logp,
        "TPSA": tpsa,
        "MW": mw,
        "HBD": hbd,
        "HBA": hba,
        "Absorption": "Poor" if logp > 5 or tpsa > 140 else "Good",
        "Distribution": "Limited" if mw > 500 or hbd > 5 else "Extensive",
        "Metabolism": "Fast" if mw < 300 else "Slow",
        "Excretion": "Delayed" if tpsa > 120 else "Normal",
        "Toxicity": "High" if hba > 10 or logp > 5 else "Low"
    }

    return admet_results

# Calculate Tanimoto similarity
def calculate_similarity(input_smiles, dataset_smiles):
    mol1 = Chem.MolFromSmiles(input_smiles)
    mol2 = Chem.MolFromSmiles(dataset_smiles)
    if mol1 and mol2:
        fps1 = Chem.RDKFingerprint(mol1)
        fps2 = Chem.RDKFingerprint(mol2)
        tanimoto = round(DataStructs.TanimotoSimilarity(fps1, fps2), 2)
        string_sim = round(difflib.SequenceMatcher(None, input_smiles, dataset_smiles).ratio(), 2)
        return tanimoto, string_sim
    return 0.0, 0.0

# Streamlit App
st.title("HSP90 Inhibitor/Activator Prediction & ADMET Evaluation")

default_smiles = "COC1=CC=C(C=C1)/C=C/C=C2C(=O)NC(=O)NC2=O"
input_smiles = st.text_input("Enter SMILES String", value=default_smiles)
process_button = st.button("Evaluate")

P_Inhibitor = 0.51
P_Activator = 0.49

if process_button and input_smiles:
    max_similarity_inhibitor = 0
    max_similarity_activator = 0
    best_match_inhibitor = None
    best_match_activator = None

    # Iterate through dataset to find best matches
    for index, row in df.iterrows():
        smiles = row['SMILES']
        status = row['Status']
        tanimoto_similarity, string_similarity = calculate_similarity(input_smiles, smiles)

        if status == 'Inhibitor' and tanimoto_similarity >= max_similarity_inhibitor:
            max_similarity_inhibitor = tanimoto_similarity
            best_match_inhibitor = (smiles, string_similarity)

        if status == 'Activator' and tanimoto_similarity >= max_similarity_activator:
            max_similarity_activator = tanimoto_similarity
            best_match_activator = (smiles, string_similarity)

    # Check if similarities are identical
    if max_similarity_inhibitor == max_similarity_activator:
        st.write("### Uncertain Classification")
        st.write(f"- **Tanimoto Similarity (Inhibitor):** {max_similarity_inhibitor}")
        st.write(f"- **String Similarity (Inhibitor):** {best_match_inhibitor[1]}")
        st.write(f"- **Tanimoto Similarity (Activator):** {max_similarity_activator}")
        st.write(f"- **String Similarity (Activator):** {best_match_activator[1]}")
    else:
        # Determine the predicted class based on higher similarity
        if max_similarity_inhibitor > max_similarity_activator:
            st.write("### Predicted as: **Inhibitor**")
            st.write(f"- **Tanimoto Similarity:** {max_similarity_inhibitor}")
            st.write(f"- **String Similarity:** {best_match_inhibitor[1]}")
        else:
            st.write("### Predicted as: **Activator**")
            st.write(f"- **Tanimoto Similarity:** {max_similarity_activator}")
            st.write(f"- **String Similarity:** {best_match_activator[1]}")

    # Display Lipinski's properties and ADMET results
    st.write("#### Lipinski's Rule of Five")
    st.json(lipinski_properties(input_smiles))

    st.write("#### ADMET Evaluation Results")
    st.json(admet_evaluation(input_smiles))

    # Display molecule structure
    mol = Chem.MolFromSmiles(input_smiles)
    mol_img = Draw.MolToImage(mol)
    st.image(mol_img, caption="Molecule Structure", use_column_width=True)
else:
    st.write("Enter a valid SMILES string and click 'Evaluate'.")