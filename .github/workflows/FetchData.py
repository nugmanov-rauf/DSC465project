#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofchicago.org", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofchicago.org,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("m6dm-c72p", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

#Output to COC.csv file for R
results_df.to_csv("coc.csv", sep=',')

#print some summary info
print(results_df.head(7))
print(results_df.tail(3))
print(results_df.describe())
