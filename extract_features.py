#path = 'C:/Users/Pierre Pinson/Documents/Cours/Supélec/3A/Stages/ML-challenge-Owkin/x_train/'
import numpy as np
import pandas as pd
from glob import glob



def extract_features(path):
    clinical = pd.read_csv(path+'features/clinical_data.csv', sep=',')

    features = pd.read_csv(path+'features/radiomics.csv', sep=',', header = 1)
    features['Adenocarcinoma'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "Adenocarcinoma"))
    features['Large cell'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "large cell")) 
    features['Squamous cell carcinoma'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "squamous cell carcinoma"))
    features['NOS'] = clinical.Histology.apply(lambda x: unsensitive_compare(x, "nos")) | clinical.Histology.apply(lambda x: unsensitive_compare(x, "NSCLC NOS (not otherwise specified)")) 
    features['age'] = clinical.age
    features.age[np.isnan(features.age)] = 0
    return features

def unsensitive_compare(str1, str2):
    if type(str1) == str:
        return int(str1.lower() == str2.lower())
    else:
        return 0
    
    
def extract_images(path, masked = True):
    dirs = glob(path+"images/*.npz" )
    scan_size = (np.load(dirs[0])['scan']).shape
    imgs = np.zeros((len(dirs), scan_size[0], scan_size[1], scan_size[2], 1))
    for i, d in enumerate(dirs):
        archive  = np.load(d)
        scan = archive ['scan']
        if masked:
            scan = scan * archive['mask']
        imgs[i,:,:,:, 0] =  scan
    return imgs