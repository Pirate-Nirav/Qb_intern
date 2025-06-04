import requests
class IRCTC:
    def __init__(self):
        user_input = input("""
        How would you like to proceed ?
        1.Enter 1 to check the live train status
        2.Enter 2 to check PNR
        3. Enter 3 to check train schedule
        :-""")

        if user_input == 1:
            print("Live train status")
        elif user_input == 2:
            print("PNR")
        else:
            self.train_schedule()



    def train_schedule(self):
        train_no = input("Enter train no: ")
        print("StationName|ArrivalTime|DepartureTime|Distance|")
        self.fetch_data(train_no)

    def fetch_data(self, train_no):
        data = requests.get("http://indianrailapi.com/api/v2/TrainSchedule/apikey/879274cdbe8a236077ed70621b9f0bc7/TrainNumber/{}".format(train_no))

        data = data.json()

        for i in data['Route']:
            print(i['StationName'],"|", i['ArrivalTime'],"|",i['DepartureTime'],"|",i['Distance'],"km")


obj = IRCTC()
