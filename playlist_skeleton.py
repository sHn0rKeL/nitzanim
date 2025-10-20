#liked_songs is a dictionery
#the key is the name of the song
#values are the artist, duration, genre.
liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}
Israeliplaylist = {}
#write func that let the user to see if song he like exist, and delete songs that he dosn't like

def main():
    liked_songs["labour"] = {
        "artist": "Paris Paloma",
        "duration": (4,8),
        "genre": "alternitive indie"
    }


def seedelete():
    print("search for a song you like")
    x = str(input())
    if x in liked_songs:
        print("you have this song")
        print("type delete if you want to delete him")
        xdelete = str(input())
        if xdelete == "delete":
            del liked_songs[x]
            print(f"those are your songs now:")
            songs_online = ", ".join(liked_songs.keys())
            print(songs_online)
            
    else: 
        print("you don't have this yet")
    print("type again for new song")
    xagain = input()
    if xagain == "again":
        seedelete()
    else: pass

def new_playlist():

    for songs_titel, details_dict in liked_songs.items():
        ganer = str(details_dict["genre"])
        timesong = details_dict["duration"]
        
        print(timesong)
        print(ganer)
        if ganer == "Israeli" and timesong[0] < 4 and timesong[1] < 30:
            Israeliplaylist[songs_titel] = details_dict
    print(Israeliplaylist)

   


main()
#seedelete()
new_playlist()
