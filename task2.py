from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=DkU9WFj8sYo'

yt_obj = YouTube(youtube_video_url)

# for stream in yt_obj.streams:
#     print(stream)


filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

for mp4_filter in filters:
    print(mp4_filter)

filters.get_highest_resolution().download('E:\Обучение на гик брейнс\Разработчик-Программист\Знакомство с Пайтон\dz9\dz9piton\Dounloads2')
print('Видео успешно загружено')
# try:
#     yt_obj = YouTube('https://www.youtube.com/watch?v=DkU9WFj8sYo')

#     print(f'Video Title is {yt_obj.title}')
#     print(f'Video Length is {yt_obj.length} seconds')
#     print(f'Video Description is {yt_obj.description}')
#     print(f'Video Rating is {yt_obj.rating}')
#     print(f'Video Views Count is {yt_obj.views}')
#     print(f'Video Author is {yt_obj.author}')

# except Exception as e:
#     print(e)