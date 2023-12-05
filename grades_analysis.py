# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:04:16 2023

@author: mozea
"""

import numpy as np
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
length = grades.size #Returns the total no of elements in the array
mean = np.mean(grades, axis=None, dtype=float)
median = np.median(grades)
SD = np.std(grades)
maximum = np.max(grades)
minimum = np.min(grades)
ascendingOrder = np.sort(grades) #Arranging the elements of the array in ascending order
descendingOrder = np.sort(grades)[::-1] #Arranging the elements of the array in descending order
HighestGradeIndex = np.where(grades == maximum)
IndexOfNumbersGreaterThan_90 = np.where(grades > 90) #Returns the index of the particular condition inside the bracket and returns it as a tuple ie array([3, 4, 7])
IndexOfNumbersGreaterThan_90_array = IndexOfNumbersGreaterThan_90[0] #Collects the first element of the tuple '[3, 4, 7]' thereby returning it as a numpy array
NoOfStudentsWithScoresAbove_90 = np.count_nonzero(np.where(grades > 90)) #Counts all the indexes where the condition is True
NoOfStudentsWithScoresBelow_90 = np.count_nonzero(grades[grades < 90])
#Another method of counting the indexes
PercentageOfStudentsWithScoresAbove_90 = (NoOfStudentsWithScoresAbove_90/length) * 100 
OtherPercentage = np.mean(grades > 90) * 100 #Another way of finding the percentage
PercentageOfStudentsWithScoresBelow_75 = (np.count_nonzero(np.where(grades < 75))/length) * 100 
high_performers = grades[grades > 90]
passing_grades = grades[grades < 75]


print(grades)
print(mean)
print(median)
print(SD)
print(maximum)
print(minimum)
print(ascendingOrder)
print(descendingOrder)
print(HighestGradeIndex)
print(IndexOfNumbersGreaterThan_90_array)
print(NoOfStudentsWithScoresAbove_90)
print(PercentageOfStudentsWithScoresAbove_90)
print(PercentageOfStudentsWithScoresBelow_75)
print(high_performers)
print(passing_grades)
