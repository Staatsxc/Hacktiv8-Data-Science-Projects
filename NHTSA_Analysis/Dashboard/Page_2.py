import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

df_table = pd.read_csv('contingency.csv')

df2015 = pd.read_csv('data_2015.csv')
df2016 = pd.read_csv('data_2016.csv')
df = pd.concat([df2015,df2016], axis = 0)

col ='age'
    



def app():
    st.write('For this Analysis, Data Scientist will do hypothesis testing of correlation between gender of the driver and the Fatal injury caused, the data scientist choose fatal injury because fatal injury case is the most dangerous injury out of all and it is also the most happened injury compared to any other injury, the method used is going to be Chi - Square Analysis')
    st.header('Chi - Square Analysis')
    
    if st.checkbox('Show Table'):
        st.subheader('Table')
        st.table(df_table)

    st.header('Explanation')
    st.subheader('H0:  Gender is a factor related to the fatal injury caused by the accident')
    st.subheader('H1:  Gender is not factor related to the fatal injury caused by the accident')

    st.write('After Calculating Data we have 0.440 P-Value, this means that alternate hypothesis is rejected and it means that both data are not related')
    st.text('This means that no matter who is driving the car, a car crash accident can lead to fatal injury')

    st.header('Descriptive Statistics')



    fig, axes = plt.subplots(ncols = 2, figsize = (15, 5))
    
    # histogram
    sns.histplot(df[col],ax = axes[0], kde=True,line_kws={'linewidth': 3},color = 'k', bins = 20)
    axes[0].set_title(f"Histogram '{col}'")
    axes[0].axvline(df[col].mean(), color = 'red', linestyle = 'dashed', label = 'mean')
    axes[0].axvline(df[col].median(), color = 'green', linestyle = 'dashed', label = 'median')
    axes[0].legend()
    axes[0].xaxis.set_major_locator(MultipleLocator(5))
    
    # boxplot
    sns.boxplot(y=df[col], ax =  axes[1])
    axes[1].set_title(f"Boxplot '{col}'")
    
    plt.show()
    
    # skewness
    print(df[col].name + ' Kurtosis: ' + str(df[col].kurt()))
    print(df[col].name + ' Skewness: ' + str(df[col].skew()))
    if -0.5 <= df[col].skew() <= 0.5:
        print("Columns '{}' normal distribution".format(col))
    elif df[col].skew() > 0.5:
        print("Columns '{}' right skewed".format(col))
    elif df[col].skew() < -0.5:
        print("Columns '{}' left skewed".format(col))
    
    st.pyplot(fig)

    st.write('From the descriptive statistics it can be seen that age is a normal distribution. There is a jump of crash case from age 15 to 16. There are also people as old as 95+ years old that is in a crash case. The line is decreasing from age group of 25 years old meaning that after 25 years it is more unlikely to be in a crash accident than when we are younger.')
    
    