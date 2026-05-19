import pandas as pd
from scipy import stats

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def hypothesis_1(df):
    groups = df.groupby('Pclass')['Survived'].mean()
    class1 = df[df['Pclass'] == 1]['Survived']
    class3 = df[df['Pclass'] == 3]['Survived']
    t_stat, p_value = stats.ttest_ind(class1, class3)
    result = 'supported' if p_value < 0.05 else 'not supported'
    print(f'hypothesis 1: higher class passengers survived more')
    print(f'class 1 survival rate: {class1.mean():.2f}')
    print(f'class 3 survival rate: {class3.mean():.2f}')
    print(f'p-value: {p_value:.4f} — hypothesis {result}')
    print()
    return groups

def hypothesis_2(df):
    male = df[df['Sex'] == 'male']['Survived']
    female = df[df['Sex'] == 'female']['Survived']
    t_stat, p_value = stats.ttest_ind(male, female)
    result = 'supported' if p_value < 0.05 else 'not supported'
    print(f'hypothesis 2: women survived more than men')
    print(f'male survival rate: {male.mean():.2f}')
    print(f'female survival rate: {female.mean():.2f}')
    print(f'p-value: {p_value:.4f} — hypothesis {result}')
    print()
    return male.mean(), female.mean()

def hypothesis_3(df):
    df = df.dropna(subset=['Age'])
    survived = df[df['Survived'] == 1]['Age']
    not_survived = df[df['Survived'] == 0]['Age']
    t_stat, p_value = stats.ttest_ind(survived, not_survived)
    result = 'supported' if p_value < 0.05 else 'not supported'
    print(f'hypothesis 3: younger passengers survived more')
    print(f'average age survived: {survived.mean():.2f}')
    print(f'average age not survived: {not_survived.mean():.2f}')
    print(f'p-value: {p_value:.4f} — hypothesis {result}')
    print()
    return survived, not_survived