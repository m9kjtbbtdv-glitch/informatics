import pandas as pd
df = pd.read_csv('wild_boars.csv')
print(df['tusk_length_cm'])
print("максимальная длина клыков - ", max(df['tusk_length_cm']))
print("минимальная длина клыков - ", min(df['tusk_length_cm']))