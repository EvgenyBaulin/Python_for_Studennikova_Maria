playlist = input()

search_string = input().lower()

tracks = [track.strip() for track in playlist.split(',')]

matching_tracks_count = 0

for track in tracks:
	artist_name, song_name = map(str.strip, track.split('|'))

	if search_string in artist_name.lower():
		matching_tracks_count += 1

print(matching_tracks_count)
