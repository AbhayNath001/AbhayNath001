import requests                 #pip install requests

def Astro():
    Api_Key = "dFVeOEqeeJijlEJWyRUks6emx10P5JZfwKMiv7jU"
    start_date = input("Enter the starting date [yyyy-mm-dd]: ")
    end_date = input("Enter the ending date [yyyy-mm-dd]: ")
    try:
        print("Collecting Data...")
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
        r = requests.get(url)
        Data = r.json()
        Total_Astro = Data['element_count']
        neo = Data['near_earth_objects']
        print(f"\nTotal Astroid between from {start_date} to {end_date} is: {Total_Astro}")
        for body in neo[start_date]:
            name = body['name']
            absolute = body['absolute_magnitude_h']
            print(f"\nName: {name} \n\tAbsolute Magnitude: {absolute}")
    except:
        print("Be sure the difference between starting date and ending date is not more than 7 days.")
    
Astro()