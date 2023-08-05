* Курсовой проект на тему "Работа с базами данных"
   - Проект получает данные о компаниях и их вакансиях с сайта "HH.RU"
   - Проектирует таблицы в БД PostgresSQL 
   - Загружает полученные данные в созданные таблицы

*** 

- В проекте есть класс DBManager, который может обрабатывать полученные данные
   - получает список всех компаний и количество вакансий у каждой компании.
   - получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
   - получает среднюю зарплату по вакансиям.
   - получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
   - получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.