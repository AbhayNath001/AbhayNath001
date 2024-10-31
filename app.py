import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski, DataStructs
from difflib import SequenceMatcher

# Load dataset
df = pd.read_excel("Final Dataset.xlsx", usecols=[1])

# Function to check Lipinski's Rule of Five
def check_lipinski_rule(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    mw = round(Descriptors.MolWt(mol), 2)
    logp = round(Chem.Crippen.MolLogP(mol), 2)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)

    criteria = [
        mw <= 500,
        logp <= 5,
        hbd <= 5,
        hba <= 10
    ]
    satisfied_rules = sum(criteria)

    return {
        "MW (Molecular Weight)": mw,
        "LogP (Octanol-Water Partition Coefficient)": logp,
        "HBD (Hydrogen Bond Donors)": hbd,
        "HBA (Hydrogen Bond Acceptors)": hba,
        "Lipinski's Rule Satisfaction": f"Follows {satisfied_rules} out of 4 rules"
    }

# Simulate ADMET evaluation based on molecular properties
def admet_evaluation_simulate(input_smiles):
    mol = Chem.MolFromSmiles(input_smiles)
    logp = round(Chem.Crippen.MolLogP(mol), 2)
    mw = round(Descriptors.MolWt(mol), 2)
    tpsa = round(Descriptors.TPSA(mol), 2)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)

    admet_results = {
        "LogP (Octanol-Water Partition Coefficient)": logp,
        "TPSA (Topological Polar Surface Area)": tpsa,
        "MW (Molecular Weight)": mw,
        "HBD (Hydrogen Bond Donors)": hbd,
        "HBA (Hydrogen Bond Acceptors)": hba,
    }

    # Simulate Absorption
    admet_results["Absorption"] = "Poor" if logp > 5 or tpsa > 140 else "Good"

    # Simulate Distribution
    admet_results["Distribution"] = "Limited" if mw > 500 or hbd > 5 else "Extensive"

    # Simulate Metabolism
    admet_results["Metabolism"] = "Fast" if mw < 300 else "Slow"

    # Simulate Excretion
    admet_results["Excretion"] = "Delayed" if tpsa > 120 else "Normal"

    # Simulate Toxicity
    toxicity = "High" if hba > 10 or logp > 5 else "Low"
    admet_results["Toxicity"] = toxicity

    return admet_results

# Calculate Tanimoto Similarity
def calculate_similarity(input_smiles, dataset_smiles):
    mol1 = Chem.MolFromSmiles(input_smiles)
    mol2 = Chem.MolFromSmiles(dataset_smiles)
    if mol1 and mol2:
        fps1 = Chem.RDKFingerprint(mol1)
        fps2 = Chem.RDKFingerprint(mol2)
        return round(DataStructs.TanimotoSimilarity(fps1, fps2), 2)
    return 0.0

# Streamlit app starts here
st.title("Cancer Drug Prediction and ADMET Evaluation")

# Sidebar for reference information
st.sidebar.header("Tanimoto Score Classification")
st.sidebar.markdown(
    """
    **Reference:**
    - **High Chance Anti-Cancer Compound:** Score ≥ 0.58  
    - **Low Chance Anti-Cancer Compound:** 0.40 ≤ Score < 0.58  
    - **Non-Anti-Cancer Compound:** Score < 0.40





    **Cite the software: coming soon...**
    """
)

# Default input SMILES
default_smiles = "C[C@]12CCC(=O)C=C1CC[C@@H]3[C@@]2([C@H](C[C@]4([C@H]3CC[C@]4(C)O)C)O)F"

input_smiles = st.text_input("Enter SMILES String", value=default_smiles)
process_button = st.button("Evaluate")

if process_button and input_smiles:
    tanimoto_threshold = 0.58
    found = False

    for index, row in df.iterrows():
        smiles = row['SMILES']
        tanimoto_similarity = calculate_similarity(input_smiles, smiles)
        string_similarity = round(SequenceMatcher(None, input_smiles, smiles).ratio(), 2)

        if tanimoto_similarity >= tanimoto_threshold:
            st.write("### High Chance: This is a cancer-related drug")
            st.write(f"- **Tanimoto Similarity**: {tanimoto_similarity}")
            st.write(f"- **String Similarity**: {string_similarity}")
            found = True

            lipinski_results = check_lipinski_rule(input_smiles)
            st.write("#### Lipinski's Rule of Five Results")
            st.json(lipinski_results)

            admet_results = admet_evaluation_simulate(input_smiles)
            st.write("#### ADMET Evaluation Results")
            st.json(admet_results)
            break

        elif 0.40 <= tanimoto_similarity < tanimoto_threshold:
            st.write("### Low Chance: This may be a cancer-related drug")
            st.write(f"- **Tanimoto Similarity**: {tanimoto_similarity}")
            st.write(f"- **String Similarity**: {string_similarity}")
            found = True

            lipinski_results = check_lipinski_rule(input_smiles)
            st.write("#### Lipinski's Rule of Five Results")
            st.json(lipinski_results)

            admet_results = admet_evaluation_simulate(input_smiles)
            st.write("#### ADMET Evaluation Results")
            st.json(admet_results)
            break

    if not found:
        st.write("### Not a cancer-related drug")
        st.write(f"- **Tanimoto Similarity**: {tanimoto_similarity}")
        st.write(f"- **String Similarity**: {string_similarity}")

        lipinski_results = check_lipinski_rule(input_smiles)
        st.write("#### Lipinski's Rule of Five Results")
        st.json(lipinski_results)

        admet_results = admet_evaluation_simulate(input_smiles)
        st.write("#### ADMET Evaluation Results")
        st.json(admet_results)