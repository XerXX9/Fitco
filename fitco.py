import mysql.connector

def connect_to_mysql():
    
    host = "localhost"
    user = "root"
    password = "Root@123"
    database = "fitco"

    
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_users_table(connection): #Creates user table
    
    cursor = connection.cursor()

    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        uid INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT,
        weight FLOAT,
        workout_experience VARCHAR(255),
        health_conditions VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)



def create_user_exercises_table(connection): #creates user excercise table
    
    cursor = connection.cursor()

   
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_exercises (
        uid INT,
        exercise_name VARCHAR(255) NOT NULL,
        sets INT,
        reps INT,
        exerciseexp VARCHAR(255),
        intensity VARCHAR(255),
        FOREIGN KEY (uid) REFERENCES users(uid)
    )
    """

    
    cursor.execute(create_table_query)


    cursor.close()
def excercise_tables(connection): #creates excericse tables


    cursor = connection.cursor()
    create_chest_table_query = """
    CREATE TABLE IF NOT EXISTS chest (
        exercise VARCHAR(255) NOT NULL,
        reps INT,
        sets INT,
        exerciseexp VARCHAR(255),
        intensity VARCHAR(255)
    )
    """

    create_back_table_query = """
    CREATE TABLE IF NOT EXISTS back (
        exercise VARCHAR(255) NOT NULL,
        reps INT,
        sets INT,
        exerciseexp VARCHAR(255),
        intensity VARCHAR(255)
    )
    """

    create_legs_table_query = """
    CREATE TABLE IF NOT EXISTS legs (
        exercise VARCHAR(255) NOT NULL,
        reps INT,
        sets INT,
        exerciseexp VARCHAR(255),
        intensity VARCHAR(255)
    )
    """

    
    cursor.execute(create_chest_table_query)
    cursor.execute(create_back_table_query)
    cursor.execute(create_legs_table_query)
    cursor.execute("select * from chest,back,legs")
    rec = cursor.fetchall()
    if not rec:
        chest_data = [
            ("Bench Press", 10, 3, "Intermediate", "Medium"),
            ("Incline Dumbbell Press", 12, 3, "Intermediate", "Medium"),
            ("Chest Flyes", 15, 3, "Intermediate", "Medium"),
            ("Push-Ups", 20, 4, "Beginner", "High"),
            ("Dips", 12, 4, "Intermediate", "High"),
            ("Machine Chest Press", 10, 3, "Intermediate", "Medium"),
            ("Pec Deck Machine", 15, 3, "Intermediate", "Medium"),
            ("Cable Crossover", 12, 3, "Intermediate", "Medium"),
            ("Decline Bench Press", 10, 3, "Intermediate", "Medium"),
            ("Pullovers", 12, 3, "Intermediate", "Medium"),
            ("Tricep Kickbacks", 8, 4, "Beginner", "Low"),
            ("Hammer Curls", 15, 3, "Advanced", "High"),
            ("Lateral Raises", 12, 3, "Beginner", "Medium"),
            ("Diamond Push-Ups", 20, 4, "Intermediate", "High"),
            ("Tricep Dips", 12, 4, "Advanced", "High"),
            ("Hammer Strength Chest Press", 15, 3, "Intermediate", "Medium"),
            ("Bicep Curls", 8, 4, "Beginner", "Low"),
            ("Russian Twists", 20, 4, "Intermediate", "High"),
            ("Front Raises", 15, 3, "Advanced", "High"),
            ("Leg Raises", 12, 3, "Beginner", "Medium")
]

        back_data = [
            ("Deadlifts", 8, 4, "Advanced", "High"),
            ("Lat Pulldowns", 12, 3, "Intermediate", "Medium"),
            ("Bent Over Rows", 10, 4, "Advanced", "High"),
            ("T-Bar Rows", 12, 3, "Intermediate", "Medium"),
            ("Chin-Ups", 15, 3, "Intermediate", "High"),
            ("Seated Cable Rows", 12, 3, "Intermediate", "Medium"),
            ("Face Pulls", 15, 3, "Intermediate", "Medium"),
            ("Hyperextensions", 12, 4, "Advanced", "High"),
            ("Pull-Ups", 10, 3, "Intermediate", "Medium"),
            ("Single-Arm Dumbbell Rows", 12, 3, "Intermediate", "Medium"),
            ("Pull-throughs", 8, 4, "Beginner", "Low"),
            ("Wide Grip Pull-Ups", 15, 3, "Advanced", "High"),
            ("Reverse Grip Rows", 12, 3, "Beginner", "Medium"),
            ("Hanging Leg Raises", 20, 4, "Intermediate", "High"),
            ("Close Grip Pull-Ups", 12, 4, "Advanced", "High"),
            ("Lat Pullovers", 15, 3, "Intermediate", "Medium"),
            ("Face Pulls", 8, 4, "Beginner", "Low"),
            ("Good Mornings", 20, 4, "Intermediate", "High"),
            ("Behind the Neck Lat Pulldowns", 15, 3, "Advanced", "High"),
            ("Wide Grip Seated Rows", 12, 3, "Beginner", "Medium")
]

        legs_data = [
            ("Squats", 10, 4, "Intermediate", "High"),
            ("Leg Press", 12, 4, "Intermediate", "High"),
            ("Lunges", 15, 3, "Intermediate", "Medium"),
            ("Leg Curls", 12, 3, "Intermediate", "Medium"),
            ("Calf Raises", 20, 3, "Beginner", "Medium"),
            ("Deadlifts", 10, 4, "Intermediate", "High"),
            ("Step-Ups", 12, 3, "Intermediate", "Medium"),
            ("Hack Squats", 10, 3, "Intermediate", "Medium"),
            ("Romanian Deadlifts", 12, 4, "Intermediate", "High"),
            ("Box Jumps", 15, 3, "Intermediate", "Medium"),
            ("Barbell Squats", 8, 4, "Beginner", "Low"),
            ("Smith Machine Leg Press", 15, 3, "Advanced", "High"),
            ("Walking Lunges", 12, 3, "Beginner", "Medium"),
            ("Seated Leg Curls", 20, 4, "Intermediate", "High"),
            ("Standing Calf Raises", 12, 4, "Advanced", "High"),
            ("Sumo Deadlifts", 15, 3, "Intermediate", "Medium"),
            ("Step-Ups", 8, 4, "Beginner", "Low"),
            ("Hack Squats", 20, 4, "Intermediate", "High"),
            ("Romanian Deadlifts", 15, 3, "Advanced", "High"),
            ("Box Jumps", 12, 3, "Beginner", "Medium")
]

        
        def insert_data(table_name, data):
            insert_query = f"INSERT INTO {table_name} (exercise, reps, sets, exerciseexp, intensity) VALUES (%s, %s, %s, %s, %s)"
            cursor.executemany(insert_query, data)

        
        insert_data("chest", chest_data)
        insert_data("back", back_data)
        insert_data("legs", legs_data)

        
        connection.commit()
        connection.close()
    else:
        pass

def find_uid(connection, name):
    cursor = connection.cursor()

    search_query = "select uid from users where name = %s"

    cursor.execute(search_query, name)

    records = cursor.fetchall()

    if not records:
            print(f"No records found in the table.")
    else:
        return records
    



def insert_user_exercise(connection, uid, exercise_name, reps, sets, exerciseexp, intensity):
    
    cursor = connection.cursor()
    
    insert_exercise_query = """
    INSERT INTO user_exercises (uid, exercise_name, reps, sets, exerciseexp, intensity)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    exercise_data = (uid, exercise_name, sets, reps, exerciseexp, intensity)

    
    cursor.execute(insert_exercise_query, exercise_data)

   
    connection.commit()

    cursor.close()

def insert_many_user_exercise(connection, uid, vals):
    for i in range(len(vals)):
        val = list(vals[i])  
        val.insert(0, uid)  
        vals[i] = tuple(val)  

    cursor = connection.cursor()

    insert_exercise_query = """
    INSERT INTO user_exercises (uid, exercise_name, reps, sets, exerciseexp, intensity)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(insert_exercise_query, vals)

    connection.commit()

    cursor.close()

def insert_new_exercise(connection, target, exercise_name, reps, sets, exerciseexp, intensity):
    cursor = connection.cursor()

    if not target:
        print("Error: Table name is empty.")
        return

    insert_exercise_query = f"""
    INSERT INTO `{target}` (exercise, reps, sets, exerciseexp, intensity)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_exercise_query, (exercise_name, sets, reps, exerciseexp, intensity))
    connection.commit()

    cursor.close()





def insert_user(connection, name, age, weight, workout_experience, health_conditions):
    
    cursor = connection.cursor()

    if name.isdigit():
        print("Error: Exercise name cannot be a number.")
        return
   
    insert_user_query = """
    INSERT INTO users (name, age, weight, workout_experience, health_conditions)
    VALUES (%s, %s, %s, %s, %s)
    """

   
    user_data = (name, age, weight, workout_experience, health_conditions)

    
    cursor.execute(insert_user_query, user_data)

    
    connection.commit()

    
    cursor.close()

def display_excerises_all(connection):
    cursor = connection.cursor()
    for i in ["back","legs","chest"]:

       
        select_query = f"SELECT * FROM back"
        cursor.execute(select_query)

        
        records = cursor.fetchall()

        
        if not records:
            print(f"No records found in the {i} table.")
        else:
            listb = []
            for record in records:
                listb.append(record)

        select_query = f"SELECT * FROM chest"
        cursor.execute(select_query)

        
        records = cursor.fetchall()

        
        if not records:
            print(f"No records found in the {i} table.")
        else:
            listc = []
            for record in records:
                listc.append(record)

        select_query = f"SELECT * FROM legs"
        cursor.execute(select_query)

        
        records = cursor.fetchall()

        
        if not records:
            print(f"No records found in the {i} table.")
        else:
            listl = []
            for record in records:
                listl.append(record)

    return listl, listb, listc
            


        
def display_user_exercises(connection,uid):
    cursor = connection.cursor()
    
    select_query = f"SELECT * FROM user_exercises WHERE uid = %s"
    cursor.execute(select_query, (uid))

    records = cursor.fetchall()

    if not records:
        print(f"No records found for uid {uid} in the user_exercise table.")
    else:
        return records

    # Close the connection
    connection.close()

ch = connect_to_mysql()

def remove_exercies(connection, target, exercise):
    cursor = connection.cursor()

    remove_query = f"DELETE FROM {target} where exercise='{exercise}'"
    cursor.execute(remove_query)

    connection.commit()

def display_exercises_specific_good(connection, exercise_experience):
    cursor = connection.cursor()

    listl, listb, listc = [], [], []

    for muscle_group in ["back", "legs", "chest"]:
        cursor.execute(f"SELECT * FROM {muscle_group} WHERE exerciseexp = %s", (exercise_experience, ))

        records = cursor.fetchall()

        if not records:
            print(f"No records found in the {muscle_group} table.")
        else:
            if muscle_group == "back":
                listb.extend(records)
            elif muscle_group == "chest":
                listc.extend(records)
            elif muscle_group == "legs":
                listl.extend(records)

    return listl, listb, listc

def display_exercises_specific_medium(connection, exercise_experience, intensity):
    cursor = connection.cursor()
    
    listl, listb, listc = [], [], []

    for muscle_group in ["back", "legs", "chest"]:
        cursor.execute(f"SELECT * FROM {muscle_group} WHERE exerciseexp = %s and intensity != %s", (exercise_experience, intensity))

        records = cursor.fetchall()

        if not records:
            print(f"No records found in the {muscle_group} table.")
        else:
            if muscle_group == "back":
                listb.extend(records)
            elif muscle_group == "chest":
                listc.extend(records)
            elif muscle_group == "legs":
                listl.extend(records)

    return listl, listb, listc


def display_exercises_specific_bad(connection, exercise_experience):
    cursor = connection.cursor()
    
    listl, listb, listc = [], [], []

    if exercise_experience == "Beginner":

        for muscle_group in ["back", "legs", "chest"]:
            cursor.execute(f"SELECT * FROM {muscle_group} WHERE exerciseexp = 'Beginner' and intensity = 'Low'")

            records = cursor.fetchall()

            if not records:
                print(f"No records found in the {muscle_group} table.")
            else:
                if muscle_group == "back":
                    listb.extend(records)
                elif muscle_group == "chest":
                    listc.extend(records)
                elif muscle_group == "legs":
                    listl.extend(records)
    
    if exercise_experience == "Intermediate":

        for muscle_group in ["back", "legs", "chest"]:
            cursor.execute(f"SELECT * FROM {muscle_group} WHERE exerciseexp = 'Intermediate' and intensity = 'Low'")
    
            records = cursor.fetchall()
            
            if not records:
                print(f"No records found in the {muscle_group} table.")
            else:
                if muscle_group == "back":
                    listb.extend(records)
                elif muscle_group == "chest":
                    listc.extend(records)
                elif muscle_group == "legs":
                    listl.extend(records)
    
    if exercise_experience == "Advanced":

        for muscle_group in ["back", "legs", "chest"]:
            cursor.execute(f"SELECT * FROM {muscle_group} WHERE exerciseexp = 'Advanced' and intensity = 'Low'")

            records = cursor.fetchall()

            if not records:
                print(f"No records found in the {muscle_group} table.")
            else:
                if muscle_group == "back":
                    listb.extend(records)
                elif muscle_group == "chest":
                    listc.extend(records)
                elif muscle_group == "legs":
                    listl.extend(records)

    return listl, listb, listc