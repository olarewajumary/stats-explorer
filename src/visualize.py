import matplotlib.pyplot as plt
import seaborn as sns

def plot_hypothesis_1(groups):
    plt.figure(figsize=(8, 5))
    groups.plot(kind='bar', color=['steelblue', 'coral', 'green'], edgecolor='black')
    plt.title('survival rate by passenger class')
    plt.xlabel('passenger class')
    plt.ylabel('survival rate')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('output/hypothesis_1.png')
    plt.close()
    print('hypothesis 1 chart saved to output/hypothesis_1.png')

def plot_hypothesis_2(male_rate, female_rate):
    plt.figure(figsize=(8, 5))
    plt.bar(['male', 'female'], [male_rate, female_rate], color=['steelblue', 'coral'], edgecolor='black')
    plt.title('survival rate by gender')
    plt.xlabel('gender')
    plt.ylabel('survival rate')
    plt.tight_layout()
    plt.savefig('output/hypothesis_2.png')
    plt.close()
    print('hypothesis 2 chart saved to output/hypothesis_2.png')

def plot_hypothesis_3(survived_ages, not_survived_ages):
    plt.figure(figsize=(8, 5))
    sns.kdeplot(survived_ages, label='survived', color='steelblue')
    sns.kdeplot(not_survived_ages, label='not survived', color='coral')
    plt.title('age distribution by survival')
    plt.xlabel('age')
    plt.ylabel('density')
    plt.legend()
    plt.tight_layout()
    plt.savefig('output/hypothesis_3.png')
    plt.close()
    print('hypothesis 3 chart saved to output/hypothesis_3.png')