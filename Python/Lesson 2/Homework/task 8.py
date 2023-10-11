art = {"Starry Night": "Vincent Van Gogh", "Last Supper": "Leonardo da Vinci",
	   "Mona Lisa": "Leonardo da Vinci", "Anatomy Lesson": "Rembrandt",
	   "Spring": "Sandro Botticelli", "The Creation of Adam": "Michelangelo",
	   "Venus and Mars": "Sandro Botticelli",
	   "The Birth of Venus": "Sandro Botticelli", "Polenov": "Vasily Polenov",
	   "Dance of the Young": "Pierre-Auguste Renoir"}

artist = input()

result = []

for art_0, artist_0 in art.items():
	if artist_0 == artist:
		result.append(art_0)

if len(result) != 0:
	for i in sorted(result):
		print(i)
else:
	print(f'{artist} not found')




