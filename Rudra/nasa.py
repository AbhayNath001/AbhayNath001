import requests

Api_Key = "dFVeOEqeeJijlEJWyRUks6emx10P5JZfwKMiv7jU"

print("Be sure that the starting and ending date range must be under the 7 days")
start_date = input("Enter the starting date [yyyy-mm-dd]: ")
end_date = input("Enter the ending date [yyyy-mm-dd]: ")

try:
    print("Collecting Data...")
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
    r = requests.get(url)
    Data = r.json()
    Total_Astro = Data['element_count']
    neo = Data['near_earth_objects']
    print(f"\nTotal Astroids between from {start_date} to {end_date} is: {Total_Astro}")
    magnitudes = []
    for body in neo[start_date]:
        name = body['name']
        absolute = body['absolute_magnitude_h']
        magnitudes.append(absolute)
        print(f"\nName: {name} \n\tAbsolute Magnitude: {absolute}")
    if magnitudes:
        max_magnitude = max(magnitudes)
        min_magnitude = min(magnitudes)
        print(f"\nMaximum absolute magnitude: {max_magnitude}")
        print(f"Minimum absolute magnitude: {min_magnitude}")
except:
    print("Be sure the difference between starting date and ending date is not more than 7 days.")
