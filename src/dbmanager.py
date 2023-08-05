import psycopg2
from config import config


class DBManager:
    params = config()

    def add_companies(self, companies):
        """
        Записывает данные о компаниях
        """
        with psycopg2.connect(dbname='sql_course', **self.params)as conn:
            with conn.cursor() as cur:
                for i in companies:
                    cur.execute("INSERT INTO companies (company_id, company_name) VALUES (%s, %s)", i)
                    conn.commit()

    def add_vacancies(self, vacancies):
        """
        Записывает данные о вакансиях
        """
        with psycopg2.connect(dbname='sql_course', **self.params) as conn:
            with conn.cursor() as cur:
                for i in vacancies:
                    cur.execute("INSERT INTO vacancies (id, url, vacancy_name, salary_from, salary_to, company_name, "
                                "company_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", i)
                conn.commit()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        with psycopg2.connect(dbname='sql_course', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT DISTINCT(company_name), COUNT(*) FROM vacancies GROUP BY company_name")
                rows = cur.fetchall()
                return rows

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты
        и ссылки на вакансию.
        """
        with psycopg2.connect(dbname='sql_course', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT company_name, vacancy_name, salary_from, url FROM vacancies")
                rows = cur.fetchall()
                return rows

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """
        with psycopg2.connect(dbname='sql_course', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT AVG(salary_from) AS avg_salary FROM vacancies")
                rows = cur.fetchall()
                return rows

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        with psycopg2.connect(dbname='sql_course', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)")
                rows = cur.fetchall()
                return rows

    def get_vacancies_with_keyword(self):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
        """
        keyword = input('Введите ключевое слово')
        with psycopg2.connect(dbname='sql_course', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies WHERE vacancy_name ILIKE '%{keyword}%'")
                rows = cur.fetchall()
                return rows