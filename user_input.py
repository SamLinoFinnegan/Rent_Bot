from main import Rent_bot

person1 = {
        "MY_SEARCHES" : [ 
    "sample url, place the url you would like to search on Daft.ie, <example www.daft.ie/room/dublin>",
    "sample url, place the url you would like to search on Daft.ie, <example www.daft.ie/room/dublin>"
               ],
        "full_name": "Axxxxxx Lxxxxx",
        "your_email": "axxxxxxxfo@gmail.com", 
        "your_phone": "xxxxxxxxxx",
        "message":"Sample message, write here the message you would like to send to homeowners",
        "params":{
            "Bedrooms Available": "",
            "Single Bedroom":"",
            "Double Bedroom":"",
            "Available From": 16,
            "Lease": "",
            "Sharing with": "",
            "Furnished":"",
            "Bathroom":"",
            "Owner Occupied": "",
            "Preferences": "Male / Female",
            "max_price":1200,
            "ignore": ["Owner Occupied", "Lease","Sharing with","Bedrooms Available", "Single Bedroom", "Double Bedroom","Bathroom","Furnished"]
        }

    }

person2 = {
        "MY_SEARCHES" : [ 
    "sample url, place the url you would like to search on Daft.ie, <example www.daft.ie/room/dublin>"
               ],
        "full_name": "Lxxxxx Nxxxxxx",
        "your_email": "lxxxxx5@gmail.com", 
        "your_phone": "xxxxxxxx",
        "message":"Sample message, write here the message you would like to send to homeowners",
        "params":{
            "Bedrooms Available": "2",
            "Single Bedroom":"",
            "Double Bedroom":"",
            "Available From": 16,
            "Lease": "",
            "Sharing with": "",
            "Furnished":"",
            "Bathroom":"",
            "Owner Occupied": "No",
            "Preferences": "Male / Female",
            "max_price":2100,
            "ignore": ["Lease","Sharing with","Bedrooms Available", "Single Bedroom", "Double Bedroom","Bathroom","Furnished"]
        }

    }



list_people = [person1, person2]



def put_peaople(people):
    for person in people:
        for url in person["MY_SEARCHES"]:

            user = Rent_bot(person, url, person["params"]["max_price"])
            user.run_bot()


put_peaople(list_people)



            
  
