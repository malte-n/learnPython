# properly store my expenditures each month
import pandas as pd

# Add class for prepocessing steps?
exp_2018 = pd.read_csv(
    'bankstatements/1059880433.csv',
    encoding='iso-8859-1',
    skiprows=5,
    error_bad_lines=False,
    delimiter=';',
    decimal=",",
    index_col=None
)

# Convert numbers to floats
exp_2018['Betrag (EUR)'] = [x.replace('.', '') for x in exp_2018['Betrag (EUR)']]
exp_2018['Betrag (EUR)'] = [x.replace(',', '.') for x in exp_2018['Betrag (EUR)']]
exp_2018['Betrag (EUR)'] = exp_2018['Betrag (EUR)'].astype(float)

# Convert dates to datetime64
exp_2018['Buchungstag'] = pd.to_datetime(exp_2018['Buchungstag'], format='%d.%m.%Y')
exp_2018['Wertstellung'] = pd.to_datetime(exp_2018['Wertstellung'], format='%d.%m.%Y')

# Rename and use only the necessary data
exp_2018.rename(columns={
    "Betrag (EUR)": "Betrag",
}, inplace=True)

exp_2018_adj = exp_2018[['Buchungstag', 'Wertstellung', 'Buchungstext', 'Betrag']].copy()

# categorise expenditures in different categories
    # groceries
    # travel
    # fun
    # recurring
# be able to easily recategorise the outputs
# get the total for each month
