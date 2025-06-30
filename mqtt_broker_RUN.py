import datetime
import paho.mqtt.client as mqtt
import ast
#from daemonize import Daemonize

# --------------------------------------------  Otwarcie pliku --------------------------
# wprowadzić if exist 
# to_day = str(datetime.datetime.now())
# fname = f'{to_day[0:10]}_data_backup.bck'


# -------------------------------------------- MQTT parametr sub --------------------------
# 
localhost = '127.0.0.1' 
port = 1883
timeout = 60
topic = "/biolab"


def on_connect(client, userdata, flags, rc):
  print("error = "+str(rc))
  client.subscribe(topic)

#  odbiera krotkę od klienta MQTT 
# - czyli od jakiegoś detektora i zapisuje ją do pliku 
# i zapisuje do bazy
def on_message(client, userdata, msg):
  to_day = str(datetime.datetime.now())
  fname = f'{to_day[0:10]}_data_backup.bck'
  slownik = {}
  received_data = msg.payload.decode("utf-8") # pojawiło sie b'xxx ' gdzie x było słownikiem {}
  slownik = ast.literal_eval(received_data) # zapisanie  stringa recived_data jako słownika
  #print("msg!")
  #print(received_data)
  file = open(fname, "a+")
  file.write(received_data)
  file.write("\n")
  file.close
  #slownik = f'{received_data}'
  #model = slownik['model']
  #print(type(slownik)) #sprawdzenie
  for key, value in slownik.items(): #wyświetla w kolumnie zawartość słownika
    print(key, value)


# --------------------------------------------  Let's get party started --------------------------
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(localhost, port, timeout)
client.loop_forever()