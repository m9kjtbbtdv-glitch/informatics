import pandas as pd

df = pd.read_csv('wild_boars.csv')

males = df[df['gender'] == 'Male']
females = df[df['gender'] == 'Female']

male_q1 = males['length_cm'].quantile(0.25)
male_q3 = males['length_cm'].quantile(0.75)
male_iqr = male_q3 - male_q1

female_q1 = females['length_cm'].quantile(0.25)
female_q3 = females['length_cm'].quantile(0.75)
female_iqr = female_q3 - female_q1

print("Male IQR:", male_iqr)
print("Female IQR:", female_iqr)

f = open('iqr.txt', 'w')
f.write("Male IQR: " + str(male_iqr) + "\n")
f.write("Female IQR: " + str(female_iqr) + "\n")
f.close()