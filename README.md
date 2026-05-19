# Stats Explorer

I built this to practice working with real data and actually test whether things I assumed were true could be backed up by numbers.

The dataset is the Titanic passenger list. I picked three things I wanted to investigate and used Python to find out if I was right or wrong.

## The three questions I tested

1. Did richer passengers survive more?
Yes. First class survival was 63%, third class was 24%. The difference is statistically significant.

2. Did women survive more than men?
Yes, by a lot. 74% of women survived vs 19% of men. This was the strongest result.

3. Did younger passengers survive more?
Slightly. Survivors averaged 28 years old, non survivors averaged 30. It is true but age was not nearly as decisive as gender or class.

## How to run it

pip install -r requirements.txt
python main.py

Charts will be saved to the output folder automatically.

## What I used

pandas, matplotlib, seaborn, scipy