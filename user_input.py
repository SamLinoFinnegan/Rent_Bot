from main import Rent_bot

antonio = {
        "MY_SEARCHES" : [ 
    "https://www.daft.ie/property-for-rent/rathmines-dublin?rentalPrice_to=1200&radius=3000",
    "https://www.daft.ie/property-for-rent/dublin-city?radius=3000&rentalPrice_to=1200&firstPublishDate_from=now-1d%2Fd"
               ],
        "full_name": "Antonio Landolfo",
        "your_email": "anto.landolfo@gmail.com", 
        "your_phone": "",
        "message":"Hello, I am writing to express my strong interest in viewing the apartment that you have advertised for rent. The apartment sounds like it would be the perfect fit for me and I would love the opportunity to see it in person. I am a responsible, reliable and tidy tenant with a steady income. I have been searching for a new place and your apartment appears to meet all my needs. The location is convenient for me, and the apartment's features, make it very appealing. I would appreciate it if you could arrange a viewing for me at your earliest convenience. I am available to view the apartment at any time that is convenient for you, and I am happy to work around your schedule. If there is any additional information or documentation that you require from me, please do not hesitate to let me know. I am more than happy to provide you with any information necessary to help facilitate the rental process. Thank you for considering my interest in your apartment. I look forward to hearing back from you soon. Sincerely, Antonio",
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

leo = {
        "MY_SEARCHES" : [ 
    "https://www.daft.ie/property-for-rent/dublin-city?radius=10000&rentalPrice_to=2100&numBeds_from=2&firstPublishDate_from=now-1d%2Fd&leaseLength_from=6"
               ],
        "full_name": "Leonardo Nogueira",
        "your_email": "leolima2705@gmail.com", 
        "your_phone": "0830582735",
        "message":"Hi, my name is Leonardo, I am Brazilian, 27 years old. I have been living in Dublin for the past 5 years. I am married but my partner is living in the UK for work, I work at a tech company in Central Park. I am easy going, a really chill person, I like enjoying my free time mostly relaxing at home, but I am always open for a pint. I also have a cat, but he is the most adorable pet, really chill and friendly. I hope I can get a viewing and just let me know if you need any more information. The house would be shared between me and my colleague from work, we are all around the same age and have all the references ready to go. Looking forward to hearing something back. Thank you, Leonardo Nogueira.",
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



list_people = [leo, antonio]



def put_peaople(people):
    for person in people:
        for url in person["MY_SEARCHES"]:

            user = Rent_bot(person, url, person["params"]["max_price"])
            user.run_bot()


put_peaople(list_people)



            
  
