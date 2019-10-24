from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from clients.models import Equipamento, CLP, Client
from pymodbus.client.sync import ModbusTcpClient
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import time

def index(request):
	client_dict = {}
	for client in Client.objects.all():
		if request.user.has_perm('clients.' + str(client.id)):
			client_dict[str(client.id)] = [client.name, client.client_img]

	return render(request, "clients/index.html", { 'client_dict': client_dict })

def clp_view(request,client_id):
	client = get_object_or_404(Client, pk=client_id)
	equip_list = client.equipamento_set.order_by('name')
	clp_status = []
	if request.user.is_authenticated and request.user.has_perm('clients.' + str(client_id)):
		connection = ModbusTcpClient('0.0.0.0', 0)
		for equip in equip_list:
			if ModbusTcpClient(equip.clp.ip_ext, equip.clp.port) != connection:
				is_PLC_socket_close(connection)
				connection = ModbusTcpClient(equip.clp.ip_ext, equip.clp.port)
			if connection.connect():
				clp_status = []
			else:
				clp_status.append(f'Erro ao conectar no CLP: {equip.clp.name}')
				clp_status = list(set(clp_status))

			try:
				data = equip.clp.value_set.get(end=equip.end_modbus_leitura)
				if data.value == 0:
					equip.status = 'Desligado'
				elif data.value == 1:
					equip.status = 'Ligado'
				else:
					equip.status = 'Erro de leitura'
				equip.save()
			except:
				equip.status = 'Erro'
				equip.save()
		is_PLC_socket_close(connection)

	
		return render(request, "clients/client.html", { 'equip_list': equip_list,
													'clp_status': clp_status,
													'client_id': client_id,})
	else:
		return render(request, "clients/permission_error.html")

def EquipOn(request, client_id, equipamento_id):
	equip = get_object_or_404(Equipamento, pk=equipamento_id)
	connection = ModbusTcpClient(equip.clp.ip_ext, equip.clp.port)
	if request.user.is_authenticated and request.user.has_perm('clients.' + str(client_id)):
		try:
			connection.write_register(equip.end_modbus_escrita, 1)
			equip.status = 'Ligando ...'
			equip.save()
		except:
			equip.status = 'Erro!'
			equip.save()

		is_PLC_socket_close(connection)

	response = redirect('clp_view', equip.client.id)
	return response

def EquipOff(request, client_id, equipamento_id):
	equip = get_object_or_404(Equipamento, pk=equipamento_id)
	connection = ModbusTcpClient(equip.clp.ip_ext, equip.clp.port)
	if request.user.is_authenticated and request.user.has_perm('clients.' + str(client_id)):
		try:
			connection.write_register(equip.end_modbus_escrita, 0)
			equip.status = 'Desligando ...'
			equip.save()
		except:
			equip.status = 'Erro!'
			equip.save()

		is_PLC_socket_close(connection)

	response = redirect('clp_view', equip.client.id)
	return response

def is_PLC_socket_close(connection):
	while connection.is_socket_open() == True:
		connection.close()
		time.sleep(0.3)
