import os
os.makedirs('output', exist_ok=True)

from src.analysis import load_data, hypothesis_1, hypothesis_2, hypothesis_3
from src.visualize import plot_hypothesis_1, plot_hypothesis_2, plot_hypothesis_3

filepath = 'data/titanic.csv'

df = load_data(filepath)

print('stats explorer — titanic dataset')
print('==================================')
print()

groups = hypothesis_1(df)
plot_hypothesis_1(groups)

male_rate, female_rate = hypothesis_2(df)
plot_hypothesis_2(male_rate, female_rate)

survived_ages, not_survived_ages = hypothesis_3(df)
plot_hypothesis_3(survived_ages, not_survived_ages)

print('all charts saved to output folder.')
