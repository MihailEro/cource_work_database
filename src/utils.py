import requests

def get_vacancies(url: str):
    """Получает и возвращает данные о вакансиях и компаниях"""
    vacancies = []
    companies = {}
    response = requests.get(url)
    data = response.json()
    for i in data['items']:
        vacancy_id = i['id']
        vacancy_url = i['alternate_url']
        vacancy_name = i['name']
        try:
            if not((i['salary'] is None) or (i['salary']['from'] is None)):
                salary_from = i['salary']['from']
                salary_to = i['salary']['to']
            else:
                salary_from = 0
                salary_to = 0
            company_id = i['employer']['id']
        except KeyError:
            continue
        company_name = i['employer']['name']
        vacancy = (vacancy_id, vacancy_url, vacancy_name, salary_from, salary_to, company_name, company_id)
        company = (company_id, company_name)
        companies[company_id] = company[1]
        vacancies.append(vacancy)
    return list(companies.items()), vacancies