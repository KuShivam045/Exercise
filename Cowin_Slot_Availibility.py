# from email import header
# from urllib import response
import requests 

District_Id = ''

while len(District_Id) != 3:
    District_Id = input("Please enter the district code (length should be 3 digits) ==> \t")
    if len(District_Id) < 3:
        print(f"{District_Id} is shorter than the actual length")
    elif len(District_Id) > 3:
        print(f"{District_Id} is larger than the actual length")

# Request_Date = '25-08-2022'
Request_Date = input("Enter the date to get the status (Date Format: DD-MM-YYYY)  ==> \t")

Request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={District_Id}&date={Request_Date}"
header = {'User-Agent' : 'Chrome/84.0.4147.105 Safari/537.36'}
response = requests.get(Request_link, headers = header)
raw_JSON = response.json()

Total_Centers = len(raw_JSON['centers'])
print()
print("                    *>>>>>>>> RESULTS <<<<<<<<<<*                    ")
print("_________________________________________________________________________________________________")
print(f"Date: {Request_Date} | District_ID: {District_Id} ")

if Total_Centers != 0:
    print(f"Total Centers in your area is {Total_Centers}")

else:
    print(f"Unfortunately !! Seems like no centers in this area / Kindly recheck the District_ID")

print("_________________________________________________________________________________________________")
print()

for center in range(len(raw_JSON['centers'])):
    print()
    print(f"[{center+1}] Center Name: ", raw_JSON['centers'][center]['name'])
    print("_________________________________________________________________________________________________")
    print("       Date         Vaccine Type       Vaccination Fee         Minimum Age         Available Slot")
    print("    ----------    ---------------    -------------------     ---------------     ----------------")
    this_session = raw_JSON['centers'][center]['sessions']
    for session in range(len(this_session)):
        print("{0:^12} {1:^12} {3:^12} {4:^16}".format(this_session[session]['date'], this_session[session]['vaccine'],
        this_session['min_age_limit'], this_session[session]['available_capacity']))