import pandas as pd

df = pd.read_csv('wild_boars.csv')

males = df[df['gender'] == 'Male']
females = df[df['gender'] == 'Female']

male_cv = (males['tusk_length_cm'].std() / males['tusk_length_cm'].mean()) * 100
female_cv = (females['tusk_length_cm'].std() / females['tusk_length_cm'].mean()) * 100

print("Male CV:", male_cv, "%")
print("Female CV:", female_cv, "%")

f = open('tusk_cv.txt', 'w')
f.write("Male CV: " + str(male_cv) + " %\n")
f.write("Female CV: " + str(female_cv) + " %\n")
f.close()