from django.http import HttpResponse
from django.shortcuts import render
from .blockchain import blockchain

def produtor_view(request, id_produtor):

    if request.method == "GET":
        context = {}
        context['bois'] = blockchain.get_cattle(id_produtor)
        return render(request, 'happy_cow/produtor_view.html', context)

    # elif request.method == "POST":
    #     # functionality 2
    # elif request.method == "PUT":
    #     # functionality 3
    # elif request.method == "DELETE":
    #     # functionality 4

def produtor_criar(request):

    if request.method == "POST":
        pass


