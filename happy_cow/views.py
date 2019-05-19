from django.http import HttpResponse
from django.shortcuts import render, redirect
from .blockchain import blockchain
import requests
import json, datetime


def produtor_view(request, id_produtor):

    if request.method == "GET":
        context = {'id': id_produtor}
        # context['bois'] = blockchain.get_allcattle(id_produtor)
        return render(request, 'happy_cow/producer_home.html', context)

    # elif request.method == "POST":
    #     # functionality 2
    # elif request.method == "PUT":
    #     # functionality 3
    # elif request.method == "DELETE":
    #     # functionality 4


def produtor_criar(request, id_produtor):

    context = {'id': id_produtor}

    if request.method == "POST":

        print(request.POST)

        url = "http://10.0.1.244:4000/channels/canal-contrato/chaincodes/contratoCC"
        jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTgyNzY0ODMsIm5vbWUiOiJOYWRpbmUiLCJvcmciOiJQcm9kdXRvciIsImlhdCI6MTU1ODI0MDQ4M30.AlhEzcR-SF7BMP4YbzQVVkh-DtJWibq9VVYO8hPBe5Y"

        clean = {
            'raca': request.POST['raca'],
            'pai': request.POST['father'],
            'mae':  request.POST['mother'],
            'peso':  request.POST['weight'],
            'timestamp': str(datetime.datetime.now()),
            'dono': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTgyNzY0ODMsIm5vbWUiOiJOYWRpbmUiLCJvcmciOiJQcm9kdXRvciIsImlhdCI6MTU1ODI0MDQ4M30.AlhEzcR-SF7BMP4YbzQVVkh-DtJWibq9VVYO8hPBe5Y",
            'vivo': True
        }

        # clean = json.dumps(clean).replace("\"", "\\\"").replace(" ", "").replace("\n", "")
        clean = json.dumps(clean)

        print(clean)

        payload = {
            "peers": ["peer0.produtor.dominio.com"],
            "fcn": "criarBoi",
            "args": [clean]
        }

        # print(request.POST)

        requests.post(
            url, headers={"Authorization": "Bearer " + jwt}, json=payload)

        return redirect('produtor_view', id_produtor=id_produtor)
    elif request.method == "GET":
        return render(request, 'happy_cow/producer_add.html', context)
    else:
        return redirect('produtor_view')


def produtor_cattle(request, id_produtor):

    if request.method == "GET":
        context = {'id': id_produtor}
        context['bois'] = blockchain.get_all_cattle(id_produtor)
        return render(request, 'happy_cow/producer_view.html', context)


def transfer2producer(request, id_produtor, id_boi):

    if request.method == "GET":
        context = {'id': id_produtor}
        context['producers'] = blockchain.get_all_cattle()
        return render(request, 'happy_cow/producer_transfer_producer.html', context)


def transfer2frigo(request, id_produtor):
    pass
