import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df

# anjali -> marks = null
df.loc[4,"marks"]=np.nan
print(df)