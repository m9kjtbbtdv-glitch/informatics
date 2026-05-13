import pandas as pd

df = pd.read_csv('wild_boars.csv')

cols = ['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

f = open('percentiles.txt', 'w')

for col in cols:
    print(col + ":")
    print("Percentile 25 (Q1):", df[col].quantile(0.25))
    print("Median 50 (Q2):", df[col].quantile(0.50))
    print("Percentile 75 (Q3):", df[col].quantile(0.75))
    print("Percentile 90:", df[col].quantile(0.90))
    print("Percentile 95:", df[col].quantile(0.95))
    print("Max:", df[col].max(), "\n")

    f.write(col + ":\n")
    f.write("Percentile 25 (Q1): " + str(df[col].quantile(0.25)) + "\n")
    f.write("Median 50 (Q2): " + str(df[col].quantile(0.50)) + "\n")
    f.write("Percentile 75 (Q3): " + str(df[col].quantile(0.75)) + "\n")
    f.write("Percentile 90: " + str(df[col].quantile(0.90)) + "\n")
    f.write("Percentile 95: " + str(df[col].quantile(0.95)) + "\n")
    f.write("Max: " + str(df[col].max()) + "\n")
    f.write("\n")

f.close()