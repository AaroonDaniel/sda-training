#ver la fecha y la hora actual de mi computadora

import datetime

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
