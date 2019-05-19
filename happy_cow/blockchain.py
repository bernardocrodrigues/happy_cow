
import datetime
import requests


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

    @staticmethod
    def create_cattle(producer_id, ):
        pass

    @staticmethod
    def transfer_cattle(origin_id, destination_id):
        pass


if __name__ == "__main__":
    pass
