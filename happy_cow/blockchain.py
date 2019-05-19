
import datetime


class blockchain():

    @staticmethod
    def get_cattle(producer_id):
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


    @classmethod
    def create_cattle(producer_id, ):
        pass