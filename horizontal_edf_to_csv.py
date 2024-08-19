import numpy as np
import mne, sys
from mne.io import read_raw_edf
import pandas as pd  # Import pandas for CSV handling

def edf_to_df(edf_path:str)-> pd.DataFrame:
    raw = read_raw_edf(edf_path, preload=True)
    eog_data, times = raw.copy().pick_channels(['EEGFp2CPz']).get_data(return_times=True)
    return pd.DataFrame(data={'Time': times, 'C4': eog_data[0, :]})



if __name__ == "__main__":
    args = sys.argv
    if len(args) <3:
        edf_file = '9_10_2.edf'
    else:
        edf_file = args[-1]
    df = edf_to_df(edf_path=edf_file)
    df.to_csv('y9_10_2one.csv', index=False)
    print("Horizontal EOG data saved to 'Fp2data.csv'")


