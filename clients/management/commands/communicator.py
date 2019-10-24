import os
from clients.models import CLP


clps = CLP.objects.all()
for clp in clps:
    string = "gnome-terminal -x python3 ~/Projects/thermomix/manage.py plc_connect " + clp.name
    os.system(string)
