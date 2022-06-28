import pandas as pd
import numpy as np

# Student Functions
def read_students(_path = "data/students.json"):
    df = pd.DataFrame(pd.read_json(_path, orient='index').
                     reset_index().
                     rename(columns = {'index':'student_id', 
                                       'Fname':'f_name', 
                                       'Lname':'l_name'}))
    df = df.drop('classes', 1).assign(**pd.DataFrame.from_records(df.classes.dropna().tolist()).fillna("🙃"))
    return(df)


def student_need_search(_df, _grade):
    new = pd.DataFrame(columns = ['class_id', 'student_id', 'grade'])
    for id in _df['student_id']:
        t = _df[_df['student_id'] == id]
        p = t.drop(['student_id', 'f_name', 'l_name'], axis = 1).astype(str).apply(lambda x: x.str.contains(_grade, case=False, na=False)).any()
        t = pd.DataFrame(t.drop(['student_id', 'f_name', 'l_name'], axis = 1).
                         columns[p], columns = ['class_id']).assign(student_id = t.iloc[0, 0], grade = _grade)
        new = new.append(t, ignore_index=True)
    return(new)


def student_contact_list(_grades = ['F', 'D', 'C']):
    new = pd.DataFrame(columns = ['class_id', 'student_id', 'grade'])
    for g in _grades:
        t = student_need_search(read_students(), _grade = g)
        new = new.append(t, ignore_index=True)
    return(new)

# Example: @param you can send a list of grades you want to search for instead of the risky ones. 
yeeyee = student_contact_list()



# Tutor Functions









def save():
    """
    Save time slot to 
    student data
    """

    pass

def find():
    """
    Find classes related to 
    the student failing classes
    """
    def filter():
        """
        filter out all tutors that 
        don't match the fail classes
        """
        pass

    def search():
        """
        Select all tutors
        with related classes
        """
        pass

    def join():
        """
        Join all the tutors
        together
        """
        pass

    pass

def launch_bot():
    """
    load model and startup the 
    chat bot
    """
    pass

def populate_appt_table():
    """
    merge tutor and student info into one comprehensive table for the tutoring center
    """
    pass

def main():
    pass