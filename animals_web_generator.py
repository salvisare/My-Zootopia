import json
import requests

# def load_data(animals_data):
#   with open("animals_data.json", "r") as handle:
#     return json.load(handle)


def load_data():
  URL = 'https://api.api-ninjas.com/v1/animals'
  API_KEY = '26T6PRikVHvNSzOTqMmPTw==obAhwAgtzjq9S9bX'
  user_input = input("Enter a name of an animal: ")
  ANIMAL_NAME = user_input
  HEADERS = {
      'X-Api-Key': API_KEY
  }

  # Make a GET request to the API with the animal name as a parameter
  response = requests.get(URL, headers=HEADERS, params={'name': ANIMAL_NAME})

  # Check if the request was successful
  if response.status_code == 200 and user_input in response.json():
      # Parse the JSON response
      data = response.json()
      return data, user_input
  else:
    return None, user_input


def restructure_data(data):
    output = ""  # define an empty string
    for item in data:
        output += "<li class='cards__item'>"
        output += "<div class='card__title'>"
        if "name" in item:
            output += f"Name: {item["name"]}\n"
        else:
            # If no characteristics, add a blank line
            output += "Name: N/A\n"
        output += "</div>"
        output += "<p class='card__text'>"
        if 'characteristics' in item:
            characteristics = item["characteristics"]
            if "diet" in characteristics:
                output += f"Diet: {characteristics["diet"]}\n"
        else:
            # If no characteristics, add a blank line
            output += "Diet: N/A\n"
        output += "<br/>"
        if "locations" in item:
            locations = item['locations']
            location_string = ', '.join(locations)
            output += f"Location: {location_string}\n"
        else:
            # If no characteristics, add a blank line
            output += "Location: N/A\n"
        output += "<br/>"
        if 'characteristics' in item:
            characteristics = item["characteristics"]
            if "type" in characteristics:
                output += f"Type: {characteristics["type"]}\n\n"
            else:
                # If no characteristics, add a blank line
                output += "Type: N/A\n\n"
        output += "</p>"
        output += "</li>"

    return output


def read_and_replace_animals_html_file(string_output, user_input, data_exists):
    with open('animals_template.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    text_to_replace = "__REPLACE_ANIMALS_INFO__"

    if data_exists:
        # Replace the placeholder with the formatted string output
        html_content = html_content.replace(text_to_replace, string_output)
    else:
        # Replace with an error message if the animal doesn't exist
        error_message = f"<h2>The animal '{user_input}' doesn't exist.</h2>"
        html_content = html_content.replace(text_to_replace, error_message)

    with open('animals.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    data, user_input = load_data()
    if data:
        string_output = restructure_data(data)
        data_exists = True
    else:
        string_output = ""
        data_exists = False

    read_and_replace_animals_html_file(string_output, user_input, data_exists)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
  main()

