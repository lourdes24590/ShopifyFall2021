# -*- coding: utf-8 -*-
"""shopify q1 code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PgeYVW-pLQ2Y8GNUzWnPO6dAIF3XQg52
"""

from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

worksheet = gc.open('Copy of 2019 Winter Data Science Intern Challenge Data Set').sheet1

rows = worksheet.get_all_values()
print(rows)

# Convert to a DataFrame and render.
import pandas as pd
sheet = pd.DataFrame.from_records(rows[1:],columns=rows[0])
print(sheet)

sheet=sheet.astype({'order_amount': int})
sheet['order_amount'].describe()