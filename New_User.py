from fitco import *
import streamlit as st
from random import choice
import pandas as pd
ch = connect_to_mysql()
create_users_table(ch)
create_user_exercises_table(ch)
excercise_tables(ch)

st.set_page_config(layout="wide")

st.write("""# Welcome to Fitco
         Your AI personal trainer responsive to your every need""")

st.write("Please enter your details so that we can make you a personal training plan")



with st.form(key='columns_in_form', ):
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        name = st.text_input("Name")
    with c2:
        age = int(st.number_input("Age", min_value=14, step=1))
    with c3:
        weight = float(st.number_input("Weight", min_value=0))
    with c4:
        exercise_experience = st.selectbox("Exercise Experience", ["Beginner", "Intermediate", "Advanced"])
    with c5:
        health_conditions = st.selectbox("Health Conditions", ["None", "Diabetes", "Arthritis", "Heart Conditions", "Lung Conditions"])

    submitButton = st.form_submit_button(label='Submit')


results = False

if name:
    insert_user(ch, name, age, weight, exercise_experience, health_conditions)
    results = [age, weight, exercise_experience, health_conditions] 
    if results:
        weird_output_list = find_uid(ch, (name,))
        user_id = weird_output_list[0][0]
        if health_conditions == "None":
            legs, back, chest = display_exercises_specific_good(ch, exercise_experience)
            final_set = set()

            while len(final_set) < 6:
                chosen_leg = choice(legs)
                chosen_chest = choice(chest)
                chosen_back = choice(back)

                final_set.add(chosen_leg)
                final_set.add(chosen_chest)
                final_set.add(chosen_back)

            final = list(final_set)
            final_cpy = final.copy()
            insert_many_user_exercise(ch, user_id, final)
            finaldf = pd.DataFrame(final_cpy, columns=['Exercise', "Repetitions", "Sets", "Experience Requirements", "Intensity"])
            st.dataframe(finaldf, use_container_width=True)

        elif health_conditions == "Diabetes" or health_conditions == "Arthritis":
            legs, back, chest = display_exercises_specific_medium(ch, exercise_experience, "High")
            final_set = set()

            while len(final_set) < 6:
                chosen_leg = choice(legs)
                chosen_chest = choice(chest)
                chosen_back = choice(back)

                final_set.add(chosen_leg)
                final_set.add(chosen_chest)
                final_set.add(chosen_back)

            final = list(final_set)
            final_cpy = final.copy()
            insert_many_user_exercise(ch, user_id, final)
            finaldf = pd.DataFrame(final_cpy, columns=['Exercise', "Repetitions", "Sets", "Experience Requirements", "Intensity"])
            st.dataframe(finaldf, use_container_width=True)

        elif health_conditions == "Heart Conditions" or health_conditions == "Lung Conditions":
            legs, back, chest = display_exercises_specific_bad(ch, exercise_experience)
            final_set = set()

            while len(final_set) < 6:
                chosen_leg = choice(legs)
                chosen_chest = choice(chest)
                chosen_back = choice(back)

                final_set.add(chosen_leg)
                final_set.add(chosen_chest)
                final_set.add(chosen_back)

            final = list(final_set)
            final_cpy = final.copy()
            insert_many_user_exercise(ch, user_id, final)
            finaldf = pd.DataFrame(final_cpy, columns=['Exercise', "Repetitions", "Sets", "Experience Requirements", "Intensity"])
            st.dataframe(finaldf, use_container_width=True)
