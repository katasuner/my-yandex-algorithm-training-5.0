songs = {}
n = int(input())

for quantity_people in range(n):
    quantity_songs = int(input())
    favorite_songs = input().split()
    for song in favorite_songs:
        songs[song] = songs.get(song, 0) + 1

list_songs_for_everybody = sorted(song for song, quantity in songs.items() if quantity == n)
print(len(list_songs_for_everybody))
print(*list_songs_for_everybody)