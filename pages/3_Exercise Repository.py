import streamlit as st
import fitco
import pandas as pd
ch = fitco.connect_to_mysql()
fitco.create_users_table(ch)
fitco.create_user_exercises_table(ch)
fitco.excercise_tables(ch)

def show_everything():
    st.title(" Welcome to the Exercise Repository")
    legs, back, chest = fitco.display_excerises_all(ch)
    st.write("Back")
    backdf = pd.DataFrame(back, columns=['Exercise', "Repetitions", "Sets", "Experience Requirements", "Intensity"])
    st.dataframe(backdf, use_container_width=True)
    st.write("Chest")
    chestdf = pd.DataFrame(chest, columns=['Exercise', "Repetitions", "Sets", "Experience Requirements", "Intensity"])
    st.dataframe(chestdf, use_container_width=True)
    st.write("Legs")
    legsdf = pd.DataFrame(legs, columns=['Exercise', "Repetitions", "Sets", "Experience Requirements", "Intensity"])
    st.dataframe(legsdf, use_container_width=True)
show_everything()


st.write("# Add")
with st.form("Add Data"):
    targetA = st.text_input("Enter the Target area (Back/Chest/Legs)")
    exerciseA = st.text_input("Enter the exercise name")
    Repetitions = st.number_input("Enter number of Repetitions", step=1, min_value=0)
    Sets = st.number_input("Enter number of Sets", step=1, min_value=0)
    experience = st.selectbox("Exercise Experience", ["Beginner", "Intermediate", "Advanced"])
    intensity = st.selectbox("Intensity", ["Low", "Medium", "High"], placeholder="Choose an option")
    st.form_submit_button("Submit")

st.write("# Remove")
with st.form("Remove Data"):
    targetB = st.text_input("Enter the Target area (Back/Chest/Legs)")
    exerciseB = st.text_input("Enter the exercise name")
    st.form_submit_button("Submit")

if exerciseA:
    fitco.insert_new_exercise(ch, targetA, exerciseA, Sets, Repetitions, experience, intensity)

if exerciseB:
    fitco.remove_exercies(ch, targetB, exerciseB)