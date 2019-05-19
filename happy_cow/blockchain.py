
import datetime
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
            {'raca': 'Angus',
             'pai': 123,
             'mae': 345,
             'peso': 300,
             'nascimento': datetime.datetime.now()},
            {'raca': 'Angus',
             'pai': 123,
             'mae': 345,
             'peso': 300,
             'nascimento': datetime.datetime.now()},
            {'raca': 'Angus',
             'pai': 123,
             'mae': 345,
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
    def create_cattle(producer_id, race, father, mother, weight):
        
        payload_dict = {'producer_id' : producer_id,
                        'race'        : race, 
                        'father'      : father,
                        'mother'      : mother,
                        'weight'      : weight}

        response = requests.post(bc_address, data = payload_dict)

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