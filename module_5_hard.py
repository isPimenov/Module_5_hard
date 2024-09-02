import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __repr__(self):
        return f"<User {self.nickname}>"

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}"

    def __contains__(self, keyword):
        return keyword.lower in self.title.lower

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(password) == user.password:
                self.current_user = user
                return
            '''else: #логично было бы добавить такую ветку, но в ТЗ ее нет
                 print("Такого пользователя не существует")'''

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
            return
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            return

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not self.videos:  #проверяю пустой ли self.videos
                self.videos.append(video)
            else:
                for v in self.videos:
                    if not v.title == video.title:
                        self.videos.append(video)

    def get_videos(self, keyword):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            for video in self.videos:
                if video.title == title:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        return
                    else:
                        while video.time_now < video.duration:
                            video.time_now += 1
                            print(video.time_now)
                            time.sleep(1)
                        print('конец видео')
                        video.time_now = 0
                        return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
