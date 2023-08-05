from src.utils import *
from src.dbcreater import *
from src.dbmanager import *


if __name__ == '__main__':

    params = config()
    create_db('sql_course', params)

    employer_ids = [
        78638,
        1740,
        3529
    ]

    for employer_id in employer_ids:
        url = f'https://api.hh.ru/vacancies?employer_id={employer_id}&per_page=50'
        companies, vacancies = get_vacancies(url)

        db = DBManager()
        db.add_companies(companies)
        db.add_vacancies(vacancies)

# print(db.get_all_vacancies())
# print(db.get_companies_and_vacancies_count())
# print(db.get_avg_salary())
# print(db.get_vacancies_with_higher_salary())
# print(db.get_vacancies_with_keyword())





