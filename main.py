import pandas as pd
#import numpy as np

data = pd.read_csv('olympics.csv', skiprows=4)
print(data.columns)

#value_counts represent values in descending order
#find the year with most medals presented
edition_vc = data.Edition.value_counts()
print(edition_vc)
#find the medals in gender
gender_vc = data.Gender.value_counts()

#sort_values sorts the values in a series in ascending order of a single col. NAN is always at the end we can sort multiple columns

filter_data = data[['Edition', 'NOC', 'Gender', 'Event', 'Medal', 'Athlete']]
test = filter_data.sort_values(by=['Edition', 'Medal'])


#retreive all data with gold for women#sort the result by player names
women_gold = data[(data.Medal == 'Gold')
                  & (data.Gender == "Women")].sort_values('Athlete')
#in which event did jesse owens win a medal
jow = filter_data[filter_data.Athlete.str.contains("OWENS, Jesse")]
#which country has won the most medals in single badminton over the years
#print("badmintion singles as follows")

badminton_single = data[(data.Sport.str.contains("Badminton"))
                        & (data.Event == "singles")].NOC.value_counts()
#print(badminton_single)
#which three countries have won the most medals in 1984 - 2008

most_meds = data[(data.Edition >= 1984)
                 & (data.Edition <= 2008)].NOC.value_counts().head(3)

#display the gold medal winners for 100m track and field sprint event.
td = filter_data[(filter_data.Medal == 'Gold') & (filter_data.Gender == "Men")
                 & (filter_data.Event == "100m")].sort_values("NOC")

#set_index it makes the desired column the first column so that we can refer the rows using the name in that column.here we are making the first column the athlete name so that we can get all data of athlete using the name itself

data.set_index('Athlete', inplace=True)
#using loc we can call data using the index column
#print(data.loc['BOLT, Usain'])
#we can also reset the index using reset_index
data.reset_index(inplace=True)

#GROUP BY function groups data wrt columns
group_edition = list(data.groupby('Edition'))
#print(group_edition)

#use groupby dictionary to group by on one itself
dic_edition = data.groupby(['Edition', 'NOC',
                            'Medal']).agg({'Edition': ['count']})
#print(dic_edition.head(20))

lewis = data[data.Athlete.str.contains('LEWIS, Carl')].groupby(
    ['Athlete', 'Medal', 'Edition']).agg({'Edition': ['count']})

print("total medals as follows")
total_medal = data.groupby(['Edition', 'Medal']).agg({'Edition': ['count']})
#print(total_medal)

sum_medal = data.groupby('Edition').size()
#print(sum_medal)

print("country medals as follows")
country_medals = data.groupby(['Edition', 'NOC', 'Medal'
                               ]).agg({'Edition': ['min', 'max', 'count']})
#print(country_medals)
#Athletes winning medals in the 2008 for 100 and 200
tokyo = data[(data.Edition == 2008)
             & ((data.Event == '100m') | (data.Event == '200m'))]
#print("tokyo medals as follows")
tokyo = tokyo.groupby(['NOC', 'Gender', 'Discipline', 'Event']).size()
#print(tokyo)

#####################################################################
#event gender analysis
#1)getting data with event gender =x only
x_event = data[(data.Event_gender == 'X')]

#2)now grouping data wrt to edition and athlete
x_event_medals = x_event.groupby(['Athlete', 'Edition', 'Event',
                                  'Medal']).agg({'Edition': ['count']})

#3)men vs women in x_event
x_event_gender = x_event.Gender.value_counts()

#4)how many medals of each gold silver and bronze have men and women won seperately
x_event_vs = x_event.groupby(['Event_gender', 'Gender',
                              'Medal']).agg({'Medal': ['count']})

#5)in event gender x which country has won the highest number of medal
x_country = x_event.groupby(['NOC']).size().sort_values(ascending=False)

#6)what is the name of the athlete with the most medals in x_event

x_athlete = x_event.groupby(['Athlete']).size().sort_values(ascending=False)
