import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df2015 = pd.read_csv('data_2015.csv')
df2016 = pd.read_csv('data_2016.csv')
df = pd.concat([df2015,df2016], axis = 0)
df_day = pd.read_csv('df_day.csv')

df_state = pd.read_csv('Nama File.csv')
df_clean = pd.read_csv("df_clean2.csv")
df_body = pd.read_csv("df_body.csv")

df_state = df_clean.groupby(by = 'state_name').sum()
df_state.drop(['latitude', 'longitude', 'vehicle_model_year','age' ], inplace=True, axis=1)

def app():
    st.subheader('Crash Case Visualization')
    

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)
    
    fig1,ax1 = plt.subplots(figsize = (20,10))
    df_state['Others'] = df_state.iloc[5:].sum()
    ser = df_clean.groupby('state_name')['Case_Num'].count()
    ser = ser.sort_values(ascending=False)
    ser['Others'] = ser[5:].sum()
    ser = ser.iloc[[0,1,2,3,4,-1]]

    ax1.pie(ser.values, startangle=90, autopct='%1.1f%%', pctdistance=0.8, counterclock=False)
    ax1.legend(ser.index)
    plt.axis('equal')
    plt.show()

    st.pyplot(fig1)
    st.header('Crash Case based on body')
    fig2,ax2 = plt.subplots(figsize = (12,10))
    sns.barplot(data = df_body, x = df_body.index, y = 'Case_Num',ax = ax2).set_xticklabels(['Sedan','Compact Utility','Pickup','Truck'])


    st.pyplot(fig2)
# ---------------------------------- Figure 3
    st.header('Comparing Crash Case Between States')
    fig3,ax3 = plt.subplots(figsize = (20,10))
    option1= st.multiselect("Choose Country",df_state.index)
    st.write(len(option1))
    warna = st.sidebar.color_picker("Choose Color For State Comparison","#0000FF")
    df2 = df_state.loc[option1]
    plt.bar(x=option1, height = df2['Case_Num'], color = warna)
    st.pyplot(fig3)

# ---------------------------------- Figure 4
    st.header('Crash Case Plot According to Day of Week')
    fig4,ax4 = plt.subplots(figsize = (20,10))
    sns.barplot(data = df_day, x = df_day.index, y = 'Case_Num', ax = ax4 ).set_xticklabels(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    plt.suptitle('Crash Case based on Day of the Week')
    st.pyplot(fig4)