# nearest-pharmacy

**Используемые технологии**

* [API Яндекс Карт](https://yandex.ru/dev/maps/)

Для запуска проекта - вам понадобится python 3.10 +  
Скачать его можно [тут](https://www.python.org/downloads/)

**Запуск проекта**


| Windows:                                                                                                                                                            | Linux:                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1** Клонируем себе репозиторий:  <br/>  ```git clone https://github.com/mge410/nearest-pharmacy.git ```                                                           | **1** Клонируем себе репозиторий:  <br/>  ```git clone https://github.com/mge410/nearest-pharmacy.git ```                                                                                          |
| **2** Заводим виртуальное окружение и активируем его: <br> ```python -m venv venv ``` <br> ```.\venv\Scripts\activate ```                                           | **2** Заводим виртуальное окружение и активируем его: <br> ```python3 -m venv venv ``` <br> ```source venv/bin/activate ```                                                                        |
| **3** Обновляем pip и качаем туда все что есть в requirements.txt: <br>```python -m pip install --upgrade pip``` <br> ```pip install -r .\requirements\prod.txt ``` | **3** Обновляем pip и качаем туда все что есть в requirements.txt: <br> ```pip install -U pip``` или    ```python3 -m pip install --upgrade pip``` <br> ```pip install -r requirements/prod.txt``` |
| **4** Запускаем проект: <br> ``` python .\main\main.py ```                                                                                                          | **4** Запускаем проект: <br> ``` python .\main\main.py	```                                                                                                                                         |

---

**Настройка проекта**  
В репозитории есть пример файла с настройками проекта __example_config.env__
копируем его файл с названием .env  
__Для Windows__   
```cp example_config.env .env```   
__Для linux__   
```cp -r example_config.env .env```

После чего его можно настроить под себя. Хоть в тестовом файле уже вбиты ключи для API, просим вас не использовать в камерческих целях. Ключи используются только для тестовой демонстрации проекта.


***Установка зависимостей***  
```cd requirements```  

Основные зависимости:  
```python -m pip install --upgrade pip```   
```pip install -r prod.txt ```  

Зависимости для разработки  
``` pip install -r dev.txt```  
