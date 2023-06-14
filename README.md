
# ***"Pereval"***
### **Данный проект является backend-приложением для проекта по сбору данных о горных перевалах.**
**Приложение создано по заказу от Федерации Спортивного Туризма России [ФСТР](https://tssr.ru/)** 

![logo tssr.ru](https://tssr.ru/files/materials/1879/logo.png)
___
## *Задача, решаемая данным приложением*

На сайте https://pereval.online/ ФСТР ведёт базу горных перевалов, которая пополняется туристами.

После преодоления очередного перевала, турист заполняет отчёт в формате PDF и отправляет его на электронную 
почту федерации. Экспертная группа ФСТР получает эту информацию, верифицирует, а затем вносит её в базу, которая 
ведётся в Google-таблице.

Весь процесс очень неудобный и долгий и занимает в среднем ***от 3 до 6 месяцев***.

ФСТР заказала разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке 
данных о перевале и сократило время обработки запроса ***до трёх дней***.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять
их в ФСТР, как только появится доступ в Интернет.
___
## *Что было реализованно в проекте*

В данном проекте было создано **Rest API** для беспроблемной работы приложения на базе Android и IOS с сервером.

### Методы реализованные в Rest API

> #### Метод POST submitData
> URL метода `/pereval/new/`
>> Когда турист поднимется на перевал, он сфотографирует его и внесёт нужную информацию с помощью мобильного приложения:
>>+ координаты объекта и его высоту;
>>+ название объекта;
>>+ несколько фотографий;
>>+ информацию о пользователе, который передал данные о перевале:
>>  + имя пользователя (ФИО строкой);
>>  + почта;
>>  + телефон.
>>  
>> После этого турист нажмёт кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод submitData твоего REST API.
>>
>>Метод submitData принимает JSON в теле запроса с информацией о перевале. Ниже находится пример такого JSON-а:
```json
{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "",
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин", 
        "name": "Василий",
        "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
  "coords":{
        "latitude": "45.3842",
        "longitude": "7.1525",
        "height": "1200"},
 
 
  "level":{"winter": "", 
        "summer": "1А",
        "autumn": "1А",
        "spring": ""},
 
   "image": [{"data":"<картинка1>", "title_data":"Седловина"}, 
        {"data":"<картинка>", "title_data":"Подъём"}]
}
```

> #### Метод GET /submitData /id
> URL метода `/pereval/int:pk/`
>> Возвращает одну запись (перевал) по её id.
>> Выводит всю информацию об объекте, в том числе статус модерации.

> #### Метод PATCH /submitData/id
> URL метода `/pereval/edit/int:pk/`
>> Редактирует существующую запись, если она в статусе new.
>> Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. Метод принимает тот
>> же самый json, который принимал метод submitData.

> #### Метод GET /submitData/?user__email = email
> URL метода `/pereval/filter/`
>> Cписок данных обо всех объектах, которые пользователь с почтой *email* отправил на сервер.

Данное приложение доступно адресу http://arteml87.pythonanywhere.com

## Авторы

1. Артем Л

