import requests

URL = 'https://api.api-ninjas.com/v1/animals'
API_KEY = '26T6PRikVHvNSzOTqMmPTw==obAhwAgtzjq9S9bX'  # Replace this with your actual API key
ANIMAL_NAME = 'fox'  # Example: Tiger
HEADERS = {
    'X-Api-Key': API_KEY
}

# Make a GET request to the API with the animal name as a parameter
response = requests.get(URL, headers=HEADERS, params={'name': ANIMAL_NAME})

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Output the results
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
