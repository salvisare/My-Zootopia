import json

def load_data(animals_data):
  with open("animals_data.json", "r") as handle:
    return json.load(handle)


def restructure_data(data):
  output = ""  # define an empty string
  for item in data:
    output += "<li class='cards__item'>"
    if "name" in item:
      output += f"Name: {item["name"]}\n"
    else:
      # If no characteristics, add a blank line
      output += "Name: N/A\n"
    output += "<br/>"
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
    output += "</li>"

    print("")

  return output


animals_data = load_data("animals_data.json")

string_output = restructure_data(animals_data)


def read_and_replace_animals_html_file(string_output):
  with open('animals_template.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    text_to_replace = "__REPLACE_ANIMALS_INFO__"
    if text_to_replace in html_content:
      html_content = html_content.replace(text_to_replace, string_output)
    with open('animals.html', 'w') as file:
      file.write(html_content)


read_and_replace_animals_html_file(string_output)