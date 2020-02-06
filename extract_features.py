#path = 'C:/Users/Pierre Pinson/Documents/Cours/Supélec/3A/Stages/Owkin ML challenge/x_train/'
import numpy as np
import pandas as pd



def extract_features(path):
    clinical = pd.read_csv(path+'features/clinical_data.csv', sep=',')

    features = (pd.read_csv(path+'features/radiomics.csv', sep=',', header = 1))
    features['Adenocarcinoma'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "Adenocarcinoma"))
    features['Large cell'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "large cell")) 
    features['Squamous cell carcinoma'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "squamous cell carcinoma"))
    features['NOS'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "nos")) | clinical.Histology.apply(lambda x: unsensitive_compare(x, "NSCLC NOS (not otherwise specified)")) 
    features['age'] = clinical.age
    features.age[np.isnan(features.age)] = 0
    features = features.drop("PatientID", axis=1)
    return features

def unsensitive_compare(str1, str2):
    if type(str1) == str:
        return int(str1.lower() == str2.lower())
    else:
        return 0