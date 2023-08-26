""" roadmap = []
for i in range(30):
    step = input(f"Enter step {i}: ")
    roadmap.append(step)
print (roadmap) """

from fast_youtube_search import search_youtube

youtubeurl = []
youtubetitle = []
youtubethumbnail = []
search=''
for item in data:
    results = search_youtube([data, prompt,'english']) # receives an array of search terms as argument
    print(results) #returns a list of results(dictionaries)
    print(results[0]) # a dictionary with properties name, id and img
    videoid = results[0]['id']
    thumbnail = results[0]['thumbnail']
    title = results[0]['id']
    youtubeurl.append(f"https://youtu.be/{videoid}")
    youtubetitle.append(title)
    youtubethumbnail.append(thumbnail)