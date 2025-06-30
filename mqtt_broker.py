import datetime
import paho.mqtt.client as mqtt
import ast
import gspread


# --------------------------------------------  Otwarcie pliku --------------------------
# wprowadzić if exist 
# to_day = str(datetime.datetime.now())
# 


# -------------------------------------------- MQTT parametr sub --------------------------
# 
localhost = '127.0.0.1' 
port = 1883
timeout = 60
topic = "/biolab"
# -------------------------------------------- MQTT parametr sub --------------------------


def on_connect(client, userdata, flags, rc):
  print("error = "+str(rc))
  client.subscribe(topic)

#  odbiera krotkę od klienta MQTT 
# - czyli od jakiegoś detektora i zapisuje ją do pliku 
# i zapisuje do bazy
def on_message(client, userdata, msg):
  
  nazwa_spreedsheet = {
    '000000003970886f': "aibree_eNOS_biolab_001",
    '10000000a47c1ec4': "aibree_eNOS_biolab_002"
  }
  slownik = {}
  received_data = msg.payload.decode("utf-8") # pojawiło sie b'xxx ' gdzie x było słownikiem {}
  slownik = ast.literal_eval(received_data) # zapisanie  stringa recived_data jako słownika
  #print("msg!")
  #print(received_data)
  to_day = slownik["Data"]
  fname = f'{to_day[0:10]}_data_backup.bck'  
  file = open(fname, "a+")
  file.write(received_data)
  file.write("\n")
  file.close
  #slownik = f'{received_data}'
  #model = slownik['model']
  #received_data[]
  print(slownik["SN"])
  print(slownik["temp"])
  sa = gspread.service_account()
  sh = sa.open(nazwa_spreedsheet[slownik["SN"]])
  to_day = slownik["Data"][0:7]
  print(to_day)
  
  temp = slownik['temp']
  hum = slownik["hum"]
  
  wks = sh.worksheet(to_day)
  wks.append_row([slownik["Data"],slownik["NH3"],slownik["CO2"], temp ,hum], value_input_option='USER_ENTERED' )
  print('rows: ', wks.row_count)


  #print(type(slownik)) #sprawdzenie
  for key, value in slownik.items(): #wyświetla w kolumnie zawartość słownika
    print(key, value)


# --------------------------------------------  Let's get party started --------------------------
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(localhost, port, timeout)
client.loop_forever()