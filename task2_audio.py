from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=q0xKow-E4Ws'

try:
    yt_obj = YouTube(youtube_video_url)

    yt_obj.streams.get_audio_only().download(output_path='E:\Обучение на гик брейнс\Разработчик-Программист\Знакомство с Пайтон\dz9\dz9piton\Dounloads1', filename='audio')
    print('Звук из этого видео успешно загружен')
except Exception as e:
    print(e)