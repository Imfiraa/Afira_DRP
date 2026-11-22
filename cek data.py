import pandas as pd

df = pd.read_csv("duolingo_reviews_20250410_214632.csv")

#print(df.shape)

#print(df.head())

#cek kesehatan data
df.info()
#print(df.isna().sum())

#cek duplicate
#print("jumlah data duplicate",df.duplicated().sum())

#cek id duplicate
#print("reviewId duplicate", df["reviewId"].duplicated().sum())

#cek rating
#print(df["score"].value_counts().sort_index())

#cek thumbsUp
#print(df["thumbsUpCount"].describe())

#cek tanggal
#print("Dari ",df["at"].min(),"sampai",df["at"].max())

#cek kesamaan reviewcreatedver dan appversion
sama = (df["reviewCreatedVersion"]==df["appVersion"]).sum()
#print("jumlah data",sama)

#cek versi app
#print("versi app", df["appVersion"].nunique())
#print(df["appVersion"].value_counts())

#cek isi review
#print(df["content"].head())

#Pembersihan
df = df.drop(columns=["userImage","reviewCreatedVersion","replyContent","repliedAt"])
df["appVersion"]=df["appVersion"].fillna("Tidak diketahui")
df["userName"]=df["userName"].fillna("Anonim")
df["at"]=pd.to_datetime(df["at"])

df.info()

#cek hasil pembersihan
print(df.isna().sum())
print("jumlah data duplicate",df.duplicated().sum())
print("reviewId duplicate", df["reviewId"].duplicated().sum())
print(df["userName"].head())
print(df["content"].head())
print(df["score"].value_counts().sort_index())
print(df["thumbsUpCount"].describe())
print("Dari ",df["at"].min(),"sampai",df["at"].max())
print(df["at"].head())
print("versi app", df["appVersion"].nunique())
print(df["appVersion"].value_counts())
