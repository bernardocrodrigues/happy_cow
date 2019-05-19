
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime, json
import requests

bc_address = 'http://127.0.0.1/anything'

class blockchain():    

    @staticmethod
    def hello_json():

        response = requests.post('http://127.0.0.1/anything', data={'key':'value'})
        print (response.content)
    
# Uncomment
    @staticmethod
    def get_all_cattle(producer_id):

        return [
            {
             'id'  : 0x5F67,
             'raca': 'Angus',
             'pai' : 0XA123,
             'mae' : 345,
             'peso': 300,
             'nascimento': datetime.datetime.now()},
            {
             'id'  : 0x5A56,
             'raca': 'Mimosa',
             'pai' : 0XE123,
             'mae' : 345,
             'peso': 300,
             'nascimento': datetime.datetime.now()},
            {
             'id'  : 0xE45F,
             'raca': 'De Lorean',
             'pai' : 0XC123,
             'mae' : 0XB345,
             'peso': 300,
             'nascimento': datetime.datetime.now()},
        ]

        # response = requests.get(
        # bc_address, 
        # headers={'Producer_id': producer_id}
        # )
        # if response.status_code == 200:
            # print('Success!')
        # else:
            # print('Error!')

    @staticmethod
    def get_all_producers():

        response = requests.get(
                                bc_address
        #                        headers={'Token': token}
        )
        if response.status_code == 200:
            print('Success!')
            return response.content
        else:
            print('Error!')
            return {}

    @staticmethod
    def create_cattle(producer_id, race, father, mother, weight):

        url = "http://10.0.1.244:4000/channels/canal-contrato/chaincodes/contratoCC"
        jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTgyNzY0ODMsIm5vbWUiOiJOYWRpbmUiLCJvcmciOiJQcm9kdXRvciIsImlhdCI6MTU1ODI0MDQ4M30.AlhEzcR-SF7BMP4YbzQVVkh-DtJWibq9VVYO8hPBe5Y"

        clean = {
            'raca':  race,
            'pai' :  father,
            'mae' :  mother,
            'peso':  weight,
            'timestamp': datetime.datetime.now(),
            'dono': producer_id,
            'vivo': True
        }

        # clean = json.dumps(clean).replace("\"", "\\\"").replace(" ", "").replace("\n", "")
        clean = json.dumps(clean)

        #print(clean)

        payload = {
            "peers": ["peer0.produtor.dominio.com"],
            "fcn": "criarBoi",
            "args": [clean]
        }

        # print(request.POST)

        response = requests.post(
            url, headers={"Authorization": "Bearer " + jwt}, json=payload)                

        # response = requests.post(bc_address,
        #                          data = payload_dict
        #                         headers={'Token': token}
        #)

        if response.status_code == 200:
            print('Success!')
        else:
            print('Error!')

            

    @staticmethod
    def transfer_cattle(origin_id, cattle_id, weight, destination_id):
        payload_dict = {'origin_id'      : origin_id,
                        'cattle_id'      : cattle_id, 
                        'weight'         : weight,
                        'destination_id' : destination_id,
                        }

        response = requests.post(bc_address, data = payload_dict)

        if response.status_code == 200:
            print('Success!')
        else:
            print('Error!')


if __name__ == "__main__":
    # blockchain.hello_json()
    blockchain.create_cattle("jao", "nova", "joo", "jaa", "86")
