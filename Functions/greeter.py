from formatted_name import get_formatted_name

# This is an infinite loop!
while True:
    print("Please tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name")

    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello, " + formatted_name + "1")


def city_country(city_name, country):
    return "\nCity name" + city_name + "\nCountry: " + country

def make_album(artist_name, album_title, tracks=''):
    album_dict = {'Name': artist_name, "Album Name": album_title}
    if tracks:
        album_dict['Tracks': tracks]
    
    return album_dict


while True:
    print("Please enter the artist's name:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist's name: ")
    album_name = input("Album's name: ")
    tracks = input("Do yo know the number of tracks if not press enter:")
    if artist_name == 'q':
        break
    if tracks:
        asd = make_album(artist_name, album_name, tracks)
        print(asd)
    asd = make_album(artist_name, album_name)
    print(asd)




