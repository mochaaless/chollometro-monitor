from datetime import datetime
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from bs4 import BeautifulSoup
import re
import json
import colorama
from colorama import Fore, Back, Style

colorama.init()


naranja = "\033[38;5;208m"
url_nuevos = 'https://www.chollometro.com/nuevos'
url_populares = 'https://www.chollometro.com/populares'
url_destacados = 'https://www.chollometro.com'
newtitle1=""
newtitle2=""
newtitle3=""

def send_wh(enlace, titulo, precio_antiguo, precio_actual,foto, timestamp):
    embed = DiscordEmbed(title='Nuevo chollo: ', url=enlace, description=titulo + "\n" + "\n" +  "~~" + precio_antiguo + "~~ \n" + precio_actual, color=242424)
    embed.set_image(url=foto)
    embed.set_footer(text=f"Chollometro by Mochaalesss#1538 | "+ timestamp)
    webhook.add_embed(embed)
    response = webhook.execute()

    
print(naranja+      "   ________  ______  __    __    ____  __  ___________________  ____     __  _______  _   ________________  ____   \n"+
                    "  / ____/ / / / __ \/ /   / /   / __ \/  |/  / ____/_  __/ __ \/ __ \   /  |/  / __ \/ | / /  _/_  __/ __ \/ __ \  \n"+
                    " / /   / /_/ / / / / /   / /   / / / / /|_/ / __/   / / / /_/ / / / /  / /|_/ / / / /  |/ // /  / / / / / / /_/ /  \n"+
                    "/ /___/ __  / /_/ / /___/ /___/ /_/ / /  / / /___  / / / _, _/ /_/ /  / /  / / /_/ / /|  // /  / / / /_/ / _, _/   \n"+
                    "\____/_/ /_/\____/_____/_____/\____/_/  /_/_____/ /_/ /_/ |_|\____/  /_/  /_/\____/_/ |_/___/ /_/  \____/_/ |_|  by Mochaaless  \n")

# Cargar los datos desde el archivo JSON existente
try:
    with open("config.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}

# Verificar si el campo "webhook" ya está llenado
if "webhook" in data and data["webhook"]:
    print(Fore.WHITE+" - Inicializando..."+Style.RESET_ALL)
else:
    # Solicitar al usuario que ingrese el enlace del webhook
    enlace_webhook = input(Fore.BLUE+" - Ingrese el enlace del webhook: "+Style.RESET_ALL)

    # Actualizar el campo "webhook" en el diccionario
    data["webhook"] = enlace_webhook

    # Guardar los datos en el archivo JSON
    with open("config.json", "w") as file:
        json.dump(data, file)
    
    print(Fore.GREEN+" - Se ha configurado el enlace del webhook con éxito."+Style.RESET_ALL)

webhook = DiscordWebhook(url=data["webhook"])

# Verificar si el campo "delay" ya está llenado
if "delay" in data and data["delay"]:
    pass
else:
    # Solicitar al usuario que ingrese el delay
    delay = input(Fore.BLUE+" - Ingrese el delay: "+Style.RESET_ALL)

    # Actualizar el campo "webhook" en el diccionario
    data["delay"] = delay

    # Guardar los datos en el archivo JSON
    with open("config.json", "w") as file:
        json.dump(data, file)
    
    print(Fore.GREEN+" - Se ha configurado el delay con éxito."+Style.RESET_ALL)

delay = int(data["delay"])

# Verificar si el campo "discount" ya está llenado
if "discount" in data and data["discount"]:
    pass
else:
    # Solicitar al usuario que ingrese el delay
    discount = input(Fore.BLUE+" - Ingrese el discount minimo: "+Style.RESET_ALL)

    # Actualizar el campo "webhook" en el diccionario
    data["discount"] = discount

    # Guardar los datos en el archivo JSON
    with open("config.json", "w") as file:
        json.dump(data, file)
    
    print(Fore.GREEN+" - Se ha configurado el discount del delay con éxito."+Style.RESET_ALL)

discount = int(data["discount"])


while True:
    timestamp = datetime.now().strftime("%H:%M:%S")

    archivo = open("Chollometro_KW.txt", "r")
    contenido = archivo.read()
    archivo.close()
    keywords = contenido.split(",")
    response_nuevos = requests.get(url_nuevos)
    response_populares = requests.get(url_populares)
    response_destacados = requests.get(url_destacados)
    soup_nuevos = BeautifulSoup(response_nuevos.content, 'html.parser')
    soup_populares = BeautifulSoup(response_populares.content, 'html.parser')
    soup_destacados = BeautifulSoup(response_destacados.content, 'html.parser')

    #nuevos
    titulo1 = soup_nuevos.find('a', {'class': 'cept-tt thread-link linkPlain thread-title--list js-thread-title'}).text #title="Roscon de reyes"
    enlace1 = soup_nuevos.find('a', {'class': 'cept-tt thread-link linkPlain thread-title--list js-thread-title'})['href']
    foto1 = src = soup_nuevos.find('img')['src']
    precio_actual1 = soup_nuevos.find('span', {'class': 'thread-price text--b cept-tp size--all-l size--fromW3-xl'}).text
    precio_antiguo1 = soup_nuevos.find('span', {'class': 'mute--text text--lineThrough size--all-l size--fromW3-xl'}).text
    discount1=soup_nuevos.find('span', {'class': 'space--ml-1 size--all-l size--fromW3-xl'}).text
    discount1_value = int(re.sub("[^0-9]", "", discount1))
    if precio_actual1=="GRATIS":
        precio_actual1="0"
    precio_antiguo1 = precio_antiguo1.replace(",", ".").replace("€", "")
    num1_antiguo = float(precio_antiguo1)
    precio_actual1 = precio_actual1.replace(",", ".").replace("€", "")
    num1_actual = float(precio_actual1)

    #populares
    titulo2 = soup_populares.find('a', {'class': 'cept-tt thread-link linkPlain thread-title--list js-thread-title'}).text #title="Roscon de reyes"
    enlace2 = soup_populares.find('a', {'class': 'cept-tt thread-link linkPlain thread-title--list js-thread-title'})['href']
    foto2 = src = soup_populares.find('img')['src']
    precio_actual2 = soup_populares.find('span', {'class': 'thread-price text--b cept-tp size--all-l size--fromW3-xl'}).text
    precio_antiguo2 = soup_populares.find('span', {'class': 'mute--text text--lineThrough size--all-l size--fromW3-xl'}).text
    discount2=soup_populares.find('span', {'class': 'space--ml-1 size--all-l size--fromW3-xl'}).text
    discount2_value = int(re.sub("[^0-9]", "", discount2))
    if precio_actual2=="GRATIS":
        precio_actual2="0"
    precio_antiguo2 = precio_antiguo2.replace(",", ".").replace("€", "")
    num2_antiguo = float(precio_antiguo2)
    precio_actual2 = precio_actual1.replace(",", ".").replace("€", "")
    num2_actual = float(precio_actual2)

    #destacados
    titulo3 = soup_destacados.find('a', {'class': 'cept-tt thread-link linkPlain thread-title--list js-thread-title'}).text #title="Roscon de reyes"
    enlace3 = soup_destacados.find('a', {'class': 'cept-tt thread-link linkPlain thread-title--list js-thread-title'})['href']
    foto3 = src = soup_destacados.find('img')['src']
    precio_actual3 = soup_destacados.find('span', {'class': 'thread-price text--b cept-tp size--all-l size--fromW3-xl'}).text
    precio_antiguo3 = soup_destacados.find('span', {'class': 'mute--text text--lineThrough size--all-l size--fromW3-xl'}).text
    discount3=soup_destacados.find('span', {'class': 'space--ml-1 size--all-l size--fromW3-xl'}).text
    discount3_value = int(re.sub("[^0-9]", "", discount3))
    if precio_actual3=="GRATIS":
        precio_actual3="0"
    precio_antiguo3 = precio_antiguo3.replace(",", ".").replace("€", "")
    num3_antiguo = float(precio_antiguo3)
    precio_actual3 = precio_actual3.replace(",", ".").replace("€", "")
    num3_actual = float(precio_actual3)

    #monitor por descuento mayor del discount
    if discount1_value>=discount:
        if titulo1!=newtitle1:
            embed = DiscordEmbed(title=f'Nuevo chollo con rebaja de +{discount}% : ', url=enlace1, description=titulo1 + "\n" + "\n" +  "~~" + precio_antiguo1 + "~~ \n" + precio_actual1, color=242424)
            embed.set_image(url=foto1)
            embed.set_footer(text=f"Chollometro by Mochaalesss#1538 | "+ timestamp)
            webhook.add_embed(embed)
            response = webhook.execute()
            print(f"{naranja}[{timestamp}]"+f'- Nuevo chollo con rebaja de +{discount}%'+Style.RESET_ALL)
            newtitle1=titulo1 
    
    if discount2_value>=discount:
        if titulo2!=newtitle2:
            embed = DiscordEmbed(title=f'Nuevo chollo con rebaja de +{discount}% : ', url=enlace2, description=titulo2 + "\n" + "\n" +  "~~" + precio_antiguo1 + "~~ \n" + precio_actual1, color=242424)
            embed.set_image(url=foto2)
            embed.set_footer(text=f"Chollometro by Mochaalesss#1538 | "+timestamp)
            webhook.add_embed(embed)
            response = webhook.execute()
            print(f"{naranja}[{timestamp}]"+f' - Nuevo chollo con rebaja de +{discount}%'+Style.RESET_ALL)
            newtitle2=titulo2
    
    if discount3_value>=discount:
        if titulo3!=newtitle3:
            embed = DiscordEmbed(title=f'Nuevo chollo con rebaja de +{discount}% : ', url=enlace3, description=titulo3 + "\n" + "\n" +  "~~" + precio_antiguo1 + "~~ \n" + precio_actual1, color=242424)
            embed.set_image(url=foto3)
            embed.set_footer(text=f"Chollometro by Mochaalesss#1538 | "+ timestamp)
            webhook.add_embed(embed)
            response = webhook.execute()
            print(f"{naranja}[{timestamp}]"+f' - Nuevo chollo con rebaja de +{discount}%'+Style.RESET_ALL)
            newtitle3=titulo3

    else:
        #monitor keywords
        encontrado = False
        for keyword in keywords:
            if keyword in titulo1:
                if titulo1!=newtitle1:
                    send_wh(enlace1, titulo1, precio_antiguo1, precio_actual1,foto1, timestamp)
                    print(f"{naranja}[{timestamp}]"+' - Nuevo chollo con la keyword: '+ keyword+Style.RESET_ALL)
                    newtitle1=titulo1

            if keyword in titulo2:
                encontrado2 = True
                if titulo2!=newtitle2:
                    send_wh(enlace2, titulo2, precio_antiguo2, precio_actual2, foto2, timestamp)
                    print(f"{naranja}[{timestamp}]"+' - Nuevo chollo con la keyword: '+ keyword+Style.RESET_ALL)
                    newtitle2=titulo2

            if keyword in titulo3:
                encontrado3 = True
                if titulo3!=newtitle3:
                    send_wh(enlace3, titulo3, precio_antiguo3, precio_actual3, foto3, timestamp)
                    print(f"{naranja}[{timestamp}]"+' - Nuevo chollo con la keyword: '+ keyword+Style.RESET_ALL)
                    newtitle3=titulo3

            else:
                continue


    print(f"{Fore.WHITE}[{timestamp}]"+" - Running..."+Style.RESET_ALL)         
    time.sleep(delay)
    pass