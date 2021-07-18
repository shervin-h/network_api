from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.core import serializers
from network_api.models import Network
import json
import os

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'network.json')


def index(request):
    f = open(file_path, mode='r', encoding='UTF-8')
    network_json = json.load(f)

    for item in network_json.values():
        # print(list(item.keys()))
        for network in item.keys():
            # print(item[network])
            network_info = item[network]

            n = Network()
            n.chainId = network_info['chainId']
            n.symbol = network_info['symbol']
            n.name = network_info['name']
            n.decimals = network_info['decimals']
            n.decimal = network_info['decimal']
            n.address = network_info['address']
            n.logoURI = network_info['logoURI']
            n.logo = network_info['logo']
            # n.eip2612 = network_info['eip2612'] if network_info['eip2612'] else False

            n.save()
    f.close()

    return HttpResponse('All objects inserted into db :)')


def get_networks_info(request):
    all_networks = Network.objects.all()
    serialized_all_networks = serializers.serialize('json', all_networks)
    all_networks_json = json.loads(serialized_all_networks)
    data = json.dumps(all_networks_json)
    return HttpResponse(data)
