from django.core.management.base import BaseCommand
from django.utils import timezone
from clients.models import Equipamento, CLP, Client, Value
from pymodbus.client.sync import ModbusTcpClient
from clients.views import is_PLC_socket_close
import time


class Command(BaseCommand):
    help = 'Recieve PLC Content'

    def add_arguments(self, parser):
        parser.add_argument('clp_name', type=str, help='Name of PLC')

    def handle(self, *args, **kwargs):
        clp_name = kwargs['clp_name']
        clp = CLP.objects.get(name=clp_name)
        connection = (ModbusTcpClient(clp.ip_ext, clp.port))
        while True:
            print(f'({timezone.now().strftime("%X")})\033[1;34mTryin to connect to {connection} ...\033[m')
            if connection.connect():
                try:
                    result = connection.read_holding_registers(0, 50)
                    equips = clp.equipamento_set.all() 
                    for equip in equips:
                        try:
                            data = clp.value_set.get(end=equip.end_modbus_leitura)
                            data.value = result.registers[equip.end_modbus_leitura]
                            data.date = timezone.now()
                            data.save()
                        except:
                            clp.value_set.create(end=equip.end_modbus_leitura,
                                                value=(result.registers[equip.end_modbus_leitura]),
                                                date=timezone.now())

                    is_PLC_socket_close(connection)
                    print(f'\033[1;32m -OK!\033[m')
                    time.sleep(1)
                except:
                    print('\033[1;31m -Error to read!\033[m')
            else:
                print('\033[1;31m -Error to connect!\033[m')


        # for equip in equip_list:
        #     if ModbusTcpClient(equip.clp.ip_ext, equip.clp.port) not in connection:
        #         connection.append(ModbusTcpClient(equip.clp.ip_ext, equip.clp.port))
        #     try:
        #         result = connection.read_holding_registers(equip.end_modbus_leitura, 1)
        #         if result.registers[0] == 0:
        #             equip.status = 'Desligado'
        #         elif result.registers[0] == 1:
        #             equip.status = 'Ligado'
        #         else:
        #             equip.status = 'Erro de leitura'
        #         equip.save()
        #     except:
        #         equip.status = 'Erro'
        #         equip.save()
        # is_PLC_socket_close(connection)

    
        # return render(request, "clients/client.html", { 'equip_list': equip_list,
        #                                             'clp_status': clp_status,
        #                                             'client_id': client_id,})
