import pandas as pd

df = pd.read_csv('wild_boars.csv')

cols = ['gender', 'age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

f = open('modes.txt', 'w')

for col in cols:
    print(col + ":", df[col].mode().iloc[0])
    f.write(col + ": " + str(df[col].mode().iloc[0]) + "\n")

f.close()