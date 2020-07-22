import pandas as pd
import numpy as np

def modify(data):
    df=pd.concat(data)
    a=df.columns
    for i in range(len(a)):
        name = a[i]
        try:
            if name[:5]=="Unnam":
                del df[a[i]]
        except:
            pass
    date_format(df)
    return df

def date_format(df):
    new_d = pd.read_excel(r"C:\Users\JRS1\Desktop\FC Model_EAST.xlsx",sheet_name="Summary_RGP",skiprows=1)
    print(new_d.columns)
    l=[]
    c=0
    for i in new_d.columns:
        c+=1
        if i[:7] != 'Unnamed':
            l.append(i)
            if c>10:
                l.append(c)
    print(l)
    for i in range(len(df.columns)):
        try:
            a = df.columns[i]
            if a != 'Plant_Name':
                b = l[0]+'_' + df.columns[i].date().strftime("%b-%y")
        except:
            if a[-2:] == '.1':
                if a[:2] == '20':
                    b = l[1]+'_' + pd.to_datetime(a.split('.')[0]).strftime("%b-%y")
                else:
                    b = l[1]+'_' + a.split('.')[0]
            else:
                b = l[0]+'_' + a
        finally:
            if a != 'Plant_Name':
                df.rename(columns = {a:b},inplace=True)
    return df


def main():
    sheetname=["Summary_RGP","Summary_KCW","Summary_BCW","Summary_JCW","Summary_DDSPL"]
    name_list=[]
    #name=["d1","d2","d3","d4","d5"]
    for i in range(len(sheetname)):
        d= pd.read_excel(r"C:\Users\JRS1\Desktop\FC Model_EAST.xlsx",sheet_name=sheetname[i],skiprows=2)
        name_list.append(d)
        d= d.insert(15 ,'Plant_Name',sheetname[i][8:],True)

    aa=modify(name_list)

    aa.to_excel('Project.xlsx',index=False,na_rep='NaN',float_format='%.1f')
    

if __name__ == "__main__":
    main()
