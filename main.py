import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://www.elsevier.com/solutions/engineering-village/databases"

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

excel_file_link = driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div[2]/div[2]/div/table/tbody[2]/tr[3]/td/p/a[2]')
excel_file_url = excel_file_link.get_attribute('href')
driver.quit()

output_file_name = 'CPXSourceList.xlsx'
os.system(f'curl -L -o {output_file_name} "{excel_file_url}"')

file_name_mapping = {
    'CHINESE JRS on SERIALS LIST': 'chinese-jrs',
    'DEFINITIONS': 'definitions',
    'DISCONTINUED': 'blacklist',
    'NON-SERIALS': 'proceedings',
    'SERIALS': 'journals',
    'DISCLAIMER-TERMS&CONDITIONS': 'disclaimer'
}

xls = pd.read_excel(output_file_name, sheet_name=None)

for sheet_name, df in xls.items():
    new_file_name = file_name_mapping.get(sheet_name, sheet_name)
    df.to_csv(f'{new_file_name}.csv', index=False)
    df.to_html(f'{new_file_name}.html', index=False)
