import random
from typing import Literal

user : dict[Literal['name'] | Literal['second_name'] | Literal['username'], str] = {}
user['nama'] = ' mele'

def say_somethin(number:int, word:str,bebra: tuple[int, ...] = (1, 2),var_4: list = (1, 2) ) -> str:  # Takes in int and str, outputs exactly string
    word = word.capitalize()                                                    # word:str <-- doesn't do anything really, just for IDE to show u stuff
    print(bebra.count(1))
    return word * number

def get_tuple(lst: list[float | bool]) -> tuple[int, ...]:
    return tuple(int(num) for num in lst)
def do_something(arg: dict[int, str | bool]) -> None:
    pass
print(get_tuple([1.0,2.0,0.0]))

 #______________________self.something is GAY, you can do better________________________
class User:
    def __init__(self, user_id, name, age, email):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email
#______________________do this instead________________________
from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str
#______________________________Examples_____________________________________
@dataclass
class DatabaseConfig:
    host: str  # URL-адрес базы данных
    user: str  # Username пользователя базы данных
    password: str  # Пароль к базе данных
    database: str  # Название базы данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    bot: TgBot
    db: DatabaseConfig

# config = Config(
#     bot=TgBot(token=BOT_TOKEN, admin_ids=ADMIN_IDS),
#     db=DatabaseConfig(
#         host=DB_HOST,
#         user=DB_USER,
#         password=DB_PASSWORD,     |То, например, получить токен бота можно, будет так:
#         database=DATABASE         |token = config.bot.token
#     )
# )
#_____________________________ lookatisshit ______________________________________
drops = [[random.randint(0, 800), random.randint(-700, 0)] for _ in range(10)]
print(drops)