## Дипломная работа по теме: Анализ и сравнение написания web-приложений с использованием разных фреймворков.

Целью работы является проведение сравнительного анализа фреймворков Django, Aiogram и FastAPI с целью определения наиболее подходящего для конкретных задач веб-приложений на Python.

Выбор данной темы обусловлен её актуальностью, высокому спросу на рынке ит-услуг, моей личной заинтересованности и желании углубленно изучить данную тему.<br>
В процессе принятия решения какими фреймворками воспользоваться для работы, мой выбор пал на aiogram, FastAPI, и конечно Django.<br>
Целью работы было создание приложения для работы с товарами, в частности демонстрация товара, описание, цена и краткий экскурс в деятельность компании.
При выполнении работы приобретен навык подключения к встраиваемой СУБД  - SQLite, отработана практика по созданию и поддержке таблиц и содержащихся в них данных.
В процессе работы приобретены навыки по работе с сторонними библиотеками, такими как sqlalchemy, pydantic, os, pillow, numpy и др.
Применена на практике работа с шаблонизатором Jinja2, Django HTML, опробован в работе язык программирования для работы с реляционными базами данных - SQL.<br>
В целом пройден значительный путь к дальнейшей самостоятельной деятельности с намечен ряд задач для дальнейшего обучения и развития в качестве Python разработчика.

## Обзор фреймворков для разработки ВЭБ-приложений

## Фреймворк 
Фреймворк — это надстройка над языком программирования, которая упрощает разработку. Внутри фреймворка собрано много готовых конструкций, которые программисту не нужно делать самому — вместо этого он использует команды фреймворка и сразу получает результат. Можно представить, что фреймворк — это набор полуфабрикатов, из которых можно приготовить блюдо.

### Aiogram

Aiogram — это высокоуровневая асинхронная библиотека для Telegram Bot API. Она позволяет реализовывать ботов, которые могут работать параллельно с несколькими пользователями, не ожидая ответа от каждого из них.
Некоторые преимущества библиотеки:
<li>интуитивно понятный интерфейс</li>
<li>минимизация необходимости глубокого погружения в детали реализации Telegram API</li>
<li>сосредоточенность на логике взаимодействия бота с пользователем.</li>
Aiogram предлагает множество инструментов и полный доступ к Telegram API для работы с сообщениями, клавиатурой, медиафайлами и другими функциями.
Библиотека написана на Python с использованием asyncio и aiohttp. Последняя версия, выпущенная 18 сентября 2024 года, — 3.13.1.
В своей работе я пользовался версией 2.25

### FastAPI

FastAPI — это современный и высокопроизводительный веб-фреймворк для создания API на языке программирования Python. Он был запущен в 2018 году и разрабатывался как простой и удобный инструмент для ускорения разработки и уменьшения количества шаблонного кода. Еще стоит упомянуть, что FastAPI — это микрофреймворк, в котором акцентирование идет на простоту использования и производительность.
Некоторые особенности FastAPI:
<li>высокая производительность. Достигается путём использования асинхронных функций — обрабатывается сразу несколько запросов.</li>
<li>атоматическая документация для API. Упрощает разработку, тестирование, взаимодействие с клиентами и другими разработчиками.</li>
<li>встроенная валидация. Позволяет избежать ошибок и писать код более компактно.</li>
<li>поддержка популярных библиотек. Например, SQLAlchemy, JWT, pytest и многие другие.</li>

### Django

Django — это фреймворк для быстрой разработки сайтов и приложений на Python. Это набор готовых инструментов и функций, который позволяет реализовывать на Python сайты и приложения, работающие в браузере, быстрее и проще, чем писать весь код с нуля. Ну и конечно тут стоит отметить, Django — это мега-фреймворк, у которого большое количество возможностей.
Основные возможности Django:
<li>Встроенный веб-сервер для обработки запросов от пользователей к веб-сервису.</li>
<li>Механизмы авторизации пользователей.</li> 
<li>Подключение и работа с базами данных. </li>
<li>Шаблоны страниц и простых веб-интерфейсов. </li>
<li>Система кэширования для увеличения скорости загрузки и открытия страниц через браузеры, внешние клиенты или приложения.</li> 
<li>Административный интерфейс для управления контентом сервиса — наполнения, изменения, обновления используемых данных. </li>
Django работает по модели MVT — Model-View-Template, она разделяет логику работы сайта, внешний вид страниц и реакции на действия пользователей.<br>
Сейчас на Django работает много популярных проектов, например:
<li>YouTube;</li>
<li>Google (для вывода результатов по шаблону);</li>
<li>Dropbox;</li>
<li>Quora;</li>
<li>Mozilla;</li>
<li>Spotify;</li>
<li>Reddit.</li>
Django можно использовать везде, где есть большая база данных и много пользователей.

## Проектирование приложения.

Первый шаг в разработке дипломной работы — это четкое определение целей и задач. 

Задачи:
1. Провести обзор литературы и интернет-ресурсов по фреймворкам Django, Aiogram и FastAPI. 
2. Подготовить методику для сравнительного анализа фреймворков. 
3. Разработать простые веб-приложения с использованием каждого фреймворка. 
4. Провести тестирование и сравнение производительности разработанных приложений. 
5. Оценить результаты и сделать выводы.

<p>Работа была основана, в первую очередь на изучении учебного курса Urban university, выполнение практических работ, получение знаний из материалов лекций и детальный разбор темы на вебинарах.</p>
Использованные модули курса:
<li>Модуль 13. Основы асинхронного программирования на базе фреймворка aiogram</li>
<li>Модуль 14. Библиотека для работы с данными</li>
<li>Модуль 16. Библиотеки для работы с ресурсами 1.1</li>
<li>Модуль 17. Библиотека для работы с ресурсами 2.1</li>
<li>Модуль 18. Django. Представления и Шаблоны</li>
<li>Модуль 19. Django в Python. Дополнительный модуль</li><br>

Использованные материалы интернет ресурсов:
<li>[habr.com](https://habr.com/ru</li>
<li>[YouTube-канал «Про Python»](https://www.youtube.com/user/zaemiel)</li>
<li>[docs-python.ru](https://docs-python.ru/)</li><br>
Использованная документация:
<li>https://fastapi.tiangolo.com/ru/</li>
<li>https://docs.aiogram.dev/</li>
<li>https://djangodoc.ru</li><br>
Использованная литература:
<li>Изучаем Python Марк_Лутц.</li>
<li>Программирование на Python для абсолютных новичков. Кевин Уилсон</li>

### Разработка в соответствии с созданной документацией.

FastAPI. При создании приложения использованы следующие технологии (стэк технологий).
<li>FastAPI: Сердце приложения</li>
<li>SQLAlchemy [asyncio]: Асинхронная работа с базой данных</li>
<li>Pydantic: Валидация и аннотации типов</li>
<li>Alembic: Миграции базы данных</li><br>
Определение структуры приложения:
<li>routers/: Здесь находятся файлы с маршрутизаторами для различных частей проекта (категории и продукты).</li>
<li>schemas/: Здесь описаны модели данных (schemas) с использованием Pydantic.</li>
<li>models/: Модели представляют структуру таблиц в базе данных.</li>  
<li>backend/: Для связи объектов приложения с таблицами базы данных.</li>  
<li>main.py: Главный файл, в котором запускается приложение и подключаются маршруты.</li><br>

![fastapi_structura](https://github.com/user-attachments/assets/703f0436-ecac-4105-982f-37f380fffd2e)



### Анализ и интерпретация результатов.

В результате был создан простейший API на базе FastAPI, создана база данных и таблицы внутри нее при помощи SQLAlchemy, описаны схемы данных и их валидация при помощи Pydantic.<br>
![fastapi_swagger](https://github.com/user-attachments/assets/ebdd3346-0a73-43ec-9cad-9ae50e8addcd)

Интеграция базы данных:
![fastapi_db](https://github.com/user-attachments/assets/7a1f284e-af7c-48b7-9485-3755f6e6cedc)
Приложение доступно по IP-адресу сервера, на него могут зайти другие пользователи и использовать готовые API.






















### Дипломную работу выполнил Аллабергенов Вячеслав











