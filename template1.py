#importing packages
from docxtpl import DocxTemplate
import pandas as pd #pandas used to analyse dataframe in spreadsheet
#reading file from csv format
data_frame = pd.read_csv('C:\Workings\Shivaraj\Projects\Python\Test 1\doc\Internals_1_sem_4.csv')
# taking heading of a column in as r_index , r_index is used as 
for r_index,row in data_frame.iterrows():
        S_roll = row['rollno']
        tpl = DocxTemplate('C:\Workings\Shivaraj\Projects\Python\ReportTemplate.docx')
        df_doct = data_frame.to_dict()
        x = data_frame.to_dict(orient='records')
        content = x
        #render for transformation of 
        tpl.render(content[r_index])
        tpl.save('report\\'+S_roll+".docx")