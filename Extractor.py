import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
from zipfile import ZipFile
from bs4 import BeautifulSoup

root = tk.Tk()
root.withdraw()

#extracts total time ran from summary file
def extractTotalTime(summaryReport):
  soup = BeautifulSoup(open(summaryReport), "html.parser")

  list = soup.find_all(attrs={"class":"scenario-settings-data"})
  duration = list[1].text

  hour, min, sec = duration.split(": ")
  hour, rest = hour.split('h')
  min, rest = min.split('m')
  sec, rest = sec.split('s')

  #total time elapsed in seconds
  return int(hour)*3600 + int(min)*60 + int(sec)

#Zipped report File directory
zippedFile = "//insert you zipped Report file location here"
#Report summary file extract directory
unZippedFile = "//insert your directory for unzip file destination"
#Output directory for HTML report for excel file
output_file = "file location .xlsx"

#Extracts the summary report summary file and saves it
with ZipFile(zippedFile, 'r') as zObject:
    zObject.extract("Report/summary.html", unZippedFile)
  zObject.close()

summaryReport = "something like unZippedFile/summary.html"
total = extractTotalTime(summaryReport)

#Populate Spreadsheet
dfTransTable = pd.read_html(summaryReport, attrs={"id" : "TransactionsTable"})

#Pull Data from table html
data_cols = ['Transaction Name', 'Average', '90 Percent', 'Pass', 'Fail']

#transaction summary table
df1 = dfTransTable[0][data_cols]

#sort table by Transaction name
df1 = df1.sort_values("Transaction Name")

#Create pass, fail list to calculate passing rate
dfPass = ['Pass']
dflist = ['Pass', 'Fail']
dfFail = ['Fail']

#Passing rate coloumn being created and added
df1['TPS'] = ((df1[dfPass].sum(axis=1) / total)).round(2)
df1['Passing Rate'] = ((1-df1[dfFail].sum(axis=1) / df1[dflist].sum(axis=1))).round(2)
df1['Failing Rate'] = ((df1[dfFail.sum(axis=1) / df1[dflist].sum(axis=1))).round(2)

#print to output
print(df1)

#saving to excel sheet. Tested on Windows.
with pd.ExcelWriter(output_file) as writer:
  df1.to_excel(writer,"Sheet1")

os.startfile(output_file)
