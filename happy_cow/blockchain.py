
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime, json
import requests

bc_address = 'http://127.0.0.1/anything'
url = "http://10.0.1.244:4000/channels/canal-contrato/chaincodes/contratoCC"
jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTgyNzY0ODMsIm5vbWUiOiJOYWRpbmUiLCJvcmciOiJQcm9kdXRvciIsImlhdCI6MTU1ODI0MDQ4M30.AlhEzcR-SF7BMP4YbzQVVkh-DtJWibq9VVYO8hPBe5Y"

class blockchain():    

    @staticmethod
    def hello_json():

        response = requests.post('http://127.0.0.1/anything', data={'key':'value'})
        print (response.content)
    
# Uncomment
    @staticmethod
    def get_all_cattle(producer_id):

        clean = {            
            'dono': producer_id
        }
       
        clean = json.dumps(clean)

        payload = {
            "peers": ["peer0.produtor.dominio.com"],
            "fcn": "queryBois",
            "args": [clean]
        }

        response = requests.post(
        url, headers={"Authorization": "Bearer " + jwt}, json=payload)                

        if response.status_code == 200:
            print('Success!')
        else:
            print('Error!')
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
    #     clean = {            
    #         'dono': producer_id
    #     }
       
    #    clean = json.dumps(clean)

    #     payload = {
    #         "peers": ["peer0.produtor.dominio.com"],
    #         "fcn": "criarBoi",
    #         "args": [clean]
    #     }

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

        clean = {
            'raca':  race,
            'pai' :  father,
            'mae' :  mother,
            'peso':  weight,
            'timestamp': datetime.datetime.now(),
            'dono': producer_id,
            'vivo': True
        }

        clean = json.dumps(clean)

        payload = {
            "peers": ["peer0.produtor.dominio.com"],
            "fcn": "criarBoi",
            "args": [clean]
        }

        response = requests.post(
            url, headers={"Authorization": "Bearer " + jwt}, json=payload)                

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
