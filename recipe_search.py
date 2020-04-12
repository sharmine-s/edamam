import requests
from pprint import pprint

app_id = '73183a37'
app_key = '8a156cee744ffdf770e02c331cfc11ef'

ingredient = input('Which ingredient do you have? ')
print()
url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

response = requests.get(url)  # returns response e.g. 200
data = response.json()  # returns actual API content

hits_dictionary = data['hits']

count_results = data['count']
print('There are {} results'.format(count_results))
print()


def list_recipes():
    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']
        print(recipe_dictionary['label'] + ' has the following labels:')
        for healthLabel in recipe_dictionary['healthLabels']:
            print(healthLabel)
        print()


list_recipes()
print('There are {} results'.format(len(hits_dictionary)))
print()


def allergies():
    count = 0
    user_health_label = input('Which health label are you looking for? ')
    print()
    print('We recommend the following recipes: ')
    print()
    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']
        for healthLabel in recipe_dictionary['healthLabels']:
            if healthLabel == user_health_label:
                print(recipe_dictionary['label'])
                count += 1
    print()
    print('There are {} results'.format(count))


allergies()
print()

