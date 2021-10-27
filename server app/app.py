from flask import Flask, request, render_template
import json
import pickle
import numpy as np
import os

# from __future__ import print_function
# import sys
app = Flask(__name__)

#Creating python dictionary as database
database = {}

#Creating indexes for msgs
msg_count = 1
Path = os.getcwd()


#Default web page response
@app.route('/')
def index():
    return render_template('index.html')


#Method to publish data
@app.route('/pub', methods=['POST'])
def my_form_post():
    global database
    global msg_count
    global Path

    #getting the data from client
    data = request.form['data']

    #Converting string to list
    data_list = json.loads(data)

    #taking the key to store
    key = str(data_list[0])
    print("Received data size:", len(data_list))

    #Storing the data in a pickle file
    temp_db = open(Path + "\database\msg_" + str(msg_count) + ".pkl", "wb")
    pickle.dump({key: str(data_list)}, temp_db)
    temp_db.close()
    msg_count = msg_count + 1

    #inserting the data into dictionary
    database.update({key: str(data_list)})
    print("Database size:", len(database))

    return "data received"


#Method to send the data back to client
@app.route('/sub', methods=['GET'])
def get_id():
   
    global database

    # getting the ID and converting to list 
    id_string = request.args.get('ID')
    print("Size of the received ID:", id_string)
    id_int_list = json.loads(id_string)
    
    #Converting the ID to bipolar format
    ID = refine_id(id_int_list)

    #getting all keys as a matrix (from string to list)
    final_list = []
    for item in database.keys():
        final_list.append(json.loads(item))

    #Calculating the dot product
    dot_prod = list(np.dot(final_list, ID))
    my_list = []
    for i in final_list:
        my_list.append(str(i))

    #Finding the index of max
    my_index = dot_prod.index(max(dot_prod))
    print("Dot product:", dot_prod)
    print("Index of max:", my_index)

    #Retrieving the data and sending back to client
    target_data_key = my_list[my_index]
    print("Size of the retrieved data:", len(database.get(target_data_key)))

    return database.get(target_data_key)


#Converting the ID to bipolar format
def refine_id(retrieved_id):
    id_string = ''.join(['{0:07b}'.format(x) for x in retrieved_id])
    
    #converting to int from binary
    idVectorBinary = [int(x) for x in id_string]
    
    #replacing 0s with -1
    idVectorBinary = [-1 if x == 0 else x for x in idVectorBinary] + [1,1,1,1,1,1]
    
    return idVectorBinary



#Starting the web server

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)