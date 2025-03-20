import requests
import json


BASE_URL = "https://rickandmortyapi.com/api/character/"

def fetch_characters(name=None, status=None):

    params = {}
    if name:
        params['name'] = name
    if status:
        params['status'] = status


    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        display_characters(data['results'])
    else:
        print(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")


def display_characters(characters):
    for character in characters:
        print(f"ID: {character['id']}")
        print(f"Name: {character['name']}")
        print(f"Status: {character['status']}")
        print(f"Species: {character['species']}")
        print(f"Gender: {character['gender']}")
        print(f"Origin: {character['origin']['name']}")
        print(f"Location: {character['location']['name']}")
        print(f"Image: {character['image']}")
        print(f"First Episode URL: {character['episode'][0] if character['episode'] else 'N/A'}")
        print(f"Created At: {character['created']}")
        print("-" * 40)


fetch_characters(name="Rick", status="alive")