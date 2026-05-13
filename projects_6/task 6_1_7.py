import pandas as pd

df = pd.read_csv('wild_boars.csv')

cols = ['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

f = open('dispersion.txt', 'w')

for col in cols:
    var = df[col].var()
    std = df[col].std()
    cv = (std / df[col].mean()) * 100

    print(col + ":")
    print("  Variance:", var)
    print("  Std:", std)
    print("  CV:", cv, "% \n")

    f.write(col + ":\n")
    f.write("  Variance: " + str(var) + "\n")
    f.write("  Std: " + str(std) + "\n")
    f.write("  CV: " + str(cv) + " %\n")
    f.write("\n")

f.close()