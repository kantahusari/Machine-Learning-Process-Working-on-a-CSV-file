# Kanta Husari: 101217294 , Data Science Assignemnt 01
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#import CSV file
file = pd.read_csv (r'biostats.csv')

ds=file

#Fetch age column
age=ds.loc[:,"Age"]


#print age column
for value in age:
    print(value)

# average, standard deviation, minimum, maximum
average=np.average(age)
std=np.std(age)
min=np.min(age)
max=np.max(age)

print('Average: ',average,'\n',
      'Standard Deviation: ',std,'\n',
      'Minimum: ',min,'\n',
      'Maximum: ',max,'\n')
# 30th percentile, median, 70th percentile
thirtyp=np.percentile(age,30)
median=np.median(age)
seventyp=np.percentile(age,70)

print('30th Percentile: ',thirtyp,'\n',
      'Median: ',median,'\n',
      '70th Percentile: ',seventyp,'\n',)

# Plot the results
plt.hist(age, bins = [25,30,35,40,45,50])
plt.title("Age Distribution – Kanta Husari")
plt.ylabel('Number')
plt.xlabel('Age')
plt.show()
