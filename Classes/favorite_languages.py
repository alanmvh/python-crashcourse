from collections import OrderedDict

# Dictionary that remembers insertion order
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'Java'

for name, language in favorite_languages.items():
    print(name.title() + " " + "'s favorite language is: " + 
    language.title() + ".")

