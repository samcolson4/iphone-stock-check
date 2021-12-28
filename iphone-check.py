import requests
import time
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getiPhoneData():
    postcode = os.getenv('POSTCODE')

    r = requests.get('https://www.apple.com/uk/shop/pickup-message-recommendations?location=' + postcode + '&product=MLLA3B/A')

    json_data = r.json()

    if r.status_code != 200:
        print(r.status_code)

    stores = json_data['body']['PickupMessage']['stores']

    models = {
        "MLLK3B/A": "1tb Graphite Pro Max",
        "MLVE3B/A": "256gb Graphite Pro Max",
        "MLLE3B/A": "Pro Max 256GB Sierra Blue",
        "MLL93B/A": "Pro Max 128gb Sierra Blue"
    }

    models_array = ["MLLK3B/A", "MLVE3B/A", "MLLE3B/A", "MLL93B/A", "MLVP3B/A", "MLVF3B/A", "MLLN3B/A", "MLLL3B/A", "MLVK3B/A"]

    for store in stores:
        counter = 0
        print("\033[1m" + store['storeName'] + "\033[0m")

        if store['partsAvailability'] != {}:
            for model in models_array:
                try:
                    # print(store['partsAvailability'])

                    if "Max" in store['partsAvailability'][model]['storePickupProductTitle']:
                        print(bcolors.OKGREEN + store['partsAvailability'][model]['storePickupProductTitle'] + bcolors.ENDC)
                    else:
                        print(bcolors.WARNING + store['partsAvailability'][model]['storePickupProductTitle'] + bcolors.ENDC)
                        counter += 1
                except:
                    counter += 1
    
        if counter >= 0:
            print("No max models in stock.")
            
        print("\n")

while True:
    print("Getting data at: " + str(time.strftime("%I:%M:%S %p")))
    getiPhoneData()
    print("-------")
    time.sleep(5)
    