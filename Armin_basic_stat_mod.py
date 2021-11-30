'''
Created on Nov 3, 2021
A basic statistics funtion that returns the mean, std deviation and a histogram of data
@author: garmin
'''
from matplotlib.pyplot import plot,hist,show
from numpy import * 

def basic_stat(x=[]):
    sample_list=[]
    n=100
    for i in range(n):
        sample_list.append(random.randint(70,100))
    length=0     #a starting point for the loop to count the number of elements
    for i in sample_list:
        length=length+1
    sum_xi=0                   #starting point
    for i in sample_list:
        sum_xi=i+sum_xi        #add the current number to the sum calculated previously
    mu=sum_xi/length           #divide by the number of elements
    mean(sample_list) 
    sum_diffsq=0         #starting place
    for i in sample_list:
        diffsq=(i-mu)**2       #first take the difference of element and mean and square
        sum_diffsq=diffsq+sum_diffsq      #sum values
    sigma=((sum_diffsq)/(length-1))**(1/2)    #sqrt(sum/n-1)

    fig=hist(sample_list,color='lavender',edgecolor='black')         
    show()
    return (mu,sigma) 


x=[]
var=basic_stat(x)
print(var)
show()
