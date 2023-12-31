import fitco
import streamlit as st
import pandas as pd
ch = fitco.connect_to_mysql()
fitco.create_users_table(ch)
fitco.create_user_exercises_table(ch)
fitco.excercise_tables(ch)

st.write(""" # Welcome back to Fitco
         Please enter your unique user id to see your program""")

uid = st.number_input("Enter your ID here", step=1, min_value=0)
l = []
l.append(uid)


if uid:
    f = fitco.display_user_exercises(ch, l)
    fdf = pd.DataFrame(f, columns=['ID','Exercise', "Repetitions", "Sets", "Experience Requirements", "Intensity"])
    st.dataframe(fdf, use_container_width=True)