# Election Poll
# (General Data Science > Descriptive Statistic > Exploratory data analysis)
#
# Each day during 2019 an agency asked a hundred randomly selected people which party they would vote
# for if elections were held that day. Results of the poll were recorded in the following file.
#  The Workers' Party asked for the report which they plan to use to improve their strategy for upcoming elections.
#
# Fill in the missing values in the report for 2019


import pandas as pd


# Read data
data_file = './files/election_poll.csv'
df = pd.read_csv(data_file, index_col='Date \ Party', parse_dates=True)

# Calculations:
workers_party_mean = round(df["Workers' Party"].mean(), 1)
workers_party_median = round(df["Workers' Party"].median(), 1)
workers_party_st_dev = round(df["Workers' Party"].std(), 1)
workers_party_max_diff = df.loc['2019-03-01':'2019-03-31']["Workers' Party"].max() - df.loc['2019-03-01':'2019-03-31']["Workers' Party"].min()
max_votes_any_day = df.max(axis=1).max()
max_date = df.max(axis=1).argmax()
max_party = df.loc[max_date, :].argmax()
party_largest_diff = (df.max(axis=0) - df.min(axis=0)).max()
party_largest_diff_name = (df.max(axis=0) - df.min(axis=0)).argmax()

print(f"Workers' Party mean: {workers_party_mean}")
print(f"Workers' Party median: {workers_party_median}")
print(f"Workers' Party St Dev: {workers_party_st_dev}")
print(f"Workers' Party diff in March: {workers_party_max_diff}")
print(f"Max votes at any date: {max_votes_any_day}")
print(f"Date with max votes: {max_date} for party {max_party}")
print(f"Party with largest diff: {party_largest_diff_name} and the difference is: {party_largest_diff}")
print('Done!')
