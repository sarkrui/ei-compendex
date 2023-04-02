import pandas as pd

excel_file = 'CPXSourceList.xlsx'

file_name_mapping = {
    'CHINESE JRS on SERIALS LIST': 'chinese-jrs',
    'DEFINITIONS': 'definitions',
    'DISCONTINUED': 'blacklist',
    'NON-SERIALS': 'proceedings',
    'SERIALS': 'journals',
    'DISCLAIMER-TERMS&CONDITIONS': 'disclaimer'
}

xls = pd.read_excel(excel_file, sheet_name=None)

for sheet_name, df in xls.items():
    new_file_name = file_name_mapping.get(sheet_name, sheet_name)
    df.to_csv(f'{new_file_name}.csv', index=False)
    df.to_html(f'{new_file_name}.html', index=False)
