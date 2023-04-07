# adspower-import-metamask-rework
![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue?style=flat-square)
![Supports](https://img.shields.io/badge/Python-Windows%20%7C%20MacOS%20%7C%20Linux-brightgreen?style=flat-square)
![Metamask](https://img.shields.io/badge/Metamask-10.26.2-orange?style=flat-square)
___
#### Изменения 07.04 commit:

* Изменена структура скрипта
* Добавлен обход защиты LavaMoat
* Добавлена функция смены кошелька через forgot pass
* Добавлена функция подготовки профилей для ручного управления
___



#### Описание режимов работы:
1. Скрипт импортирует созданные метамаски в готовые профили в Adspower.
После импорта он добавляет сети Optimism, BSC, Polygon и Arbitrum в кошелек.  
Заменяет уже добавленые метамаски на новые. Сети сохраняются.
2. Режим подготовки профилей к работе. Открывает профили и разблокирует метамаски.

___
#### Для установки необходимых библиотек пропиши в терминал:
```
pip install -r requirements.txt
```
___
### LavaMoat Fixed :white_check_mark:

Этот фикс отключает LavaMoat путем изменения переменной **scuttleGlobalThis** в файле run-time.js


В фиксе присутствуют 2 основных файла:
* LavaMoatExtFix.py
* LavaMoatProfileCacheFix.py



**LavaMoatExtFix.py** - предназначен для изменения файла run-time.js в условном "корневом" каталоге расширения Metamask, скаченным Adspower. Позваляет создавать профили с **отключенным** LavaMoat.


**LavaMoatProfileCacheFix.py** - предназначен для изменения файла run-time.js в уже созданном профиле.
<br></br>

Для корректного запуска фалов измените путь в переменной:

    path_from_ads_settings = r"YOUR_PATH"
Для **Windows**:

    path_from_ads_settings = r"С:\.ADSPOWER_GLOBAL"     # Возжможна другая буква диска

Для **MacOS**:
    
    # Вместо YOUR_NICKNAME ваша персональная папка

    path_from_ads_settings = r"/Users/YOUR_NICKNAME/Library/Application Support/adspower_global/cwd_global/source"


В файле LavaMoatProfileCacheFix.py обязательно измените переменную user_ID:
* Зайдите в Adspower -> Перейдите в настройки -> Мой Аккаунт -> Скопируйте ID пользователя

```
user_ID = 'YOUR_USER_ID'
```

###

**Запуск LavaMoatExtFix.py**
1. Измените путь до папки
2. Запустить скрипт.
* При успешном применении вы увидите:

```
Фикс применен/fix applied.
```


**Запуск LavaMoatProfileCacheFix.py**
1. Измените путь до папки
2. Измените переменную user_ID
3. Добавить id профилей в файл id_users.txt (каждый с новой строки)
4. Запустить скрипт.

* При успешном применении вы увидите:

```
1. < {ads_id} >  fixed              # Изменения применены 

2. < {ads_id} >  already fixed'     # Изменения уже были применены 
```

___



### Исктрукция для скрипта импорта :rocket:
1. Экспортируй ids из adspower со своих профилей
2. Добавь эти ids в файл id_users.txt (каждый с новой строки)
3. Добавь сид-фразы от заранее созданных кошельков в файл seeds.txt (каждый с новой строки)
4. По желанию в файле main.py измени переменную password (по умолчанию=password123)
5. Запусти Adspower
6. Запусти файл main.py


**Возможные режимы работы:**

|  Переменная   |  Значение  | Режим работы                                                                                                                                                                              |        
|:-------------:|:----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  unlock_mode  |     0      | Импортирует сид-фразы в созданные профиля, если в профиле уже имеется авторизованный метамаск, он будет заменен на новый через fargot password.                                           |
|  unlock_mode  |     1      | Режим предназначен для подготовки профилей к работе.   <br>Запускает профиль и входит в метамаск, при этом окно профиля закрываться не будет.   <br>Не требует заполнения файла seeds.txt |        


###

### Rework by *[Desti](https://t.me/ddest1)*
#### Автор оригинального скрипта ***[Zaivanza](https://t.me/zaivanza)***
#### При поддержке канала *[hodlmod.eth](https://t.me/hodlmodeth)*
