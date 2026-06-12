import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
# by default ascending
df.sort_values("english")

# descending
df.sort_values("english",ascending=False,inplace=True)
df
