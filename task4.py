import csv

#as the format of the original csv file was not right, so we are filtering only those columns which are required for this comparision and storing it a new csv file
with open(r'C:\Users\Sudipt Panda\Downloads\hadoop.csv','r')as f:
    tar=open(r'C:\Users\Sudipt Panda\Downloads\hadoop_test.csv','w',newline='')
    writer=csv.writer(tar)
    reader=csv.reader(f)
    data=list(reader)
    for line in data[0:]:
        if line !=[]:
              
            buf=line[0:1]+line[4:6]+line[7:8]+line[9:15]+line[21:22]
            buf[0]=buf[0][1:]
            #print(buf)
            writer.writerow(buf)
    tar.close()
    print('Filtered hadoop_test.csv is created')

import pandas as pd
df_dup=pd.read_csv(r'C:\Users\Sudipt Panda\Downloads\hadoop_test.csv')

df_org=pd.read_csv(r'C:\Users\Sudipt Panda\Downloads\mysql.csv',sep='\t')
#df_org.drop([],axis=1)
print(df_org.columns)
df_org_copy=df_org.filter(['id','campaign_id','banner_id','userid','network','browser','os','country','state','city','server_id'],axis=1)    

#no of null value in each col

print(df_org_copy.isnull().sum())
print(df_dup.isnull().sum())

#matching column names of both files
df_dup.columns=df_org_copy.columns

#finding matching and missing columns
stemp=set(df_org_copy['id']).intersection(set(df_dup['id']))

sdiff=set(df_org_copy['id']).difference(set(df_dup['id']))

#final list of missing values

final=df_org.loc[df_org['id'].isin(sdiff)]
print(final)
############################

######search pattern of missing#############
# details = df_org.apply(lambda x : True
#             if x['userid'].startswith("62215404350526592") else False, axis = 1) 
  
# # Count number of True in the series 
# num_rows = len(details[details == True].index) 
  
# print('Number of Rows in dataframe  : ', num_rows ) 
# ########################
# pat=set(df_org['userid']).intersection(set(final['userid']))
# print(len(pat))
###########################################

#print('no of unique values in id ',df_org.id.nunique(dropna = True))



