import pandas as pd
from columns import ORIG_COLS

def load_orig(year):
    path =f"data/raw/sample_{year}/sample_orig_{year}.txt"
    
    #seperate the column by "|", first line is NOT header.
    df = pd.read_csv(path, sep="|",header=None,dtype=str)
    print(year,df.shape)
    df.columns = ORIG_COLS

    #the year the loan originated
    df["vintage"] = year
    return df

orig = pd.concat([load_orig(y) for y in range(2005, 2026)], ignore_index=True)
#save the data in .parquet type. No need to read .txt file everytime. 
orig.to_parquet("data/processed/orig_2005_2020.parquet")
