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

# print(yeeyee)

# Tutor Functions
def read_tutor(_path = "data/tutors.json"):
    df = pd.DataFrame(pd.read_json(_path, orient='index').
                     reset_index().
                     rename(columns = {'index':'student_id', 
                                       'Fname':'f_name', 
                                       'Lname':'l_name',
                                       'class':'class'}))
    df = df.drop('availability', 1).assign(**pd.DataFrame.from_records(df.availability.dropna().tolist()).fillna("🙃"))
    return(df)

tutors = read_tutor()












def save():
    """
    Save time slot to 
    student data
    """

    pass

def find(student, tutors, time):
    """
    Find classes related to 
    the student failing classes
    """
    


def launch_bot():
    """
    load model and startup the 
    chat bot
    """
    import tflearn
    import pickle
    import random
    import nltk
    from nltk.stem.lancaster import LancasterStemmer
    import json
    stemmer = LancasterStemmer()
    
    def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words if word not in "?"]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
                
        return np.array(bag)

    

    # Loading saved data
    with open(f'training\\data\\data.pickel', 'rb') as f:
            words, labels, training, output = pickle.load(f)

    with open(f"training\\data\\time_intents.json") as file:
        data = json.load(file)

    def make_model():
            #Input layer trying to get the length from none on
            net = tflearn.input_data(shape= [None, len(training[0])])
            net = tflearn.fully_connected(net, 16, activation="relu") #hidden layer
            net = tflearn.fully_connected(net, 16, activation="relu") #hidden layer
            #Output layer solfmax 
            net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
            net = tflearn.regression(net)
            return tflearn.DNN(net)
            
    #Loading model
    model = make_model()
    model.load(f"training\\data\\model.tflearn")
    #Starting up the chatbot
    print("Start talking with bot!(type 'quit' to stop)")

    time = {
        'day':'',
        'time':'',
        'month':''
    }


    times = ['1', '2','3','4','5','6','7','8','9','10','11','12']
    days = ["monday", "tuesday", "wendsay", "thursday", "friday", "saturday", "sunday", "mon", "tues", "wed", "thur", " fri", "sat", "sun"]
    months = ["january","jan", "february","feb", "march","mar", "may", "june","jun", "july", "august","aug", "september","sept", "october","oct", "november","nov", "december","dec"]
    
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        
        #All this is going to give us a matrix of numbers where the numbers are probabilities of each class
        results = model.predict([bag_of_words(inp, words)])
        #Argmax will grab the index of highest probability in the matrix
        results_index = np.argmax(results)
        tag = labels[results_index]
        
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        choice = random.choice(responses)  
        
        
        if choice == 'day':
            print('day')
            '''
            take out the day
            save the info in a dictionary
            '''
            inpu = nltk.word_tokenize(inp)
            inpu = [stemmer.stem(word.lower()) for word in inpu if word not in "?"]
            act_day = ''
            for i in inpu:
                if i.lower() in days:
                    act_day = i
                    break
            print(inpu)
            act_day = act_day.title()
            print(act_day[:3])

        elif choice == 'time':
            print('time')
            '''
            take out the time
            '''
            inpu = nltk.word_tokenize(inp)
            inpu = [stemmer.stem(word.lower()) for word in inpu if word not in "?"]
            act_time = []
            for i in inpu:
                if i in times:
                    act_time.append(i)
            print(inpu)
            print(act_time)

        elif choice == 'date':
            print('date')
            '''
            take out the month
            '''
            inpu = nltk.word_tokenize(inp)
            inpu = [stemmer.stem(word.lower()) for word in inpu if word not in "?"]
            act_date = ''
            for i in inpu:
                if i.lower() in months:
                    act_date = i
                    break
            print(inpu)
            print(act_date)
            


# launch_bot()


def populate_appt_table():
    """
    merge tutor and student info 
    into one comprehensive table 
    for the tutoring center
    """
    pass

def main():
    pass