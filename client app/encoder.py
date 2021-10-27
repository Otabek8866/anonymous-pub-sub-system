import requests
from requests.structures import CaseInsensitiveDict
import numpy
import random


#generate an ID for message
def id_geneartor():
    id_list = []
    id_list_ascii = []

    for i in range(994):
        n = random.randint(0, 1)
        id_list_ascii.append(n)
        if n == 1:
            id_list.append(n)
        else:
            id_list.append(-1)

    wholeset = ''.join([str(x) for x in id_list_ascii])
    id_ascii_letters = []

    for i in range(0,994,7):
        id_ascii_letters.append(int(wholeset[i:i+7], 2))

    return (id_list + [1,1,1,1,1,1], id_ascii_letters)


#divide msg into chunks
def refine_msg(msg, id):
    chunk_list = []
    result_list = []

    size = len(msg)
    chunk_num = int(size/142)
    pointer = 0
    print("Number of Chunks:", chunk_num)

    for _ in range(chunk_num):
        chunk = msg[pointer:(pointer+142)]
        chunk = convert_to_bipolar(chunk) + [1 for _ in range(6)]
        chunk_list.append(chunk)
        pointer = pointer + 142

    remainder = convert_to_bipolar(msg[pointer:]) + [1 for _ in range(6)]
    fill_size = 1000 - len(remainder) - 6
    remainder = remainder + [1,1,1,1,1,1] + [-1 for _ in range(fill_size)]

    chunk_list.append(remainder)

    for item in chunk_list:
        result_list.append(encrypt_msg(item, id))

    return result_list


#converting data chunk to bipolar
def convert_to_bipolar(chunk):

    #converting to binary string
    chuck = list(chunk)
    # print(chunk)
    
    textVector = list(''.join(['{0:07b}'.format(ord(x)) for x in chunk]))
    #textVector = list(''.join(format(ord(x.encode('utf-8')), 'b') for x in chunk))
    
    #converting to int from binary
    textVectorBinary = [int(x) for x in textVector]
    
    #replacing 0s with -1
    textVectorBinary = [-1 if x == 0 else x for x in textVectorBinary]
    
    return textVectorBinary


#decrypting the data chunk
def encrypt_msg(chunk, id):
   
    prod_multip = numpy.multiply(chunk, id)
    prod_addition = prod_multip + id

    return list(prod_addition)


# Sending the data to the server
def send(url, data):

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    id, id_text = id_geneartor()
    msg = refine_msg(data, id)
    msg = str(msg)

    resp = requests.post(url, headers=headers, data="data=" + msg)

    return resp.content, id_text
