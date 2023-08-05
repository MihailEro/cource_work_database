import psycopg2

def create_db(database_name: str, params: dict):
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE companies (
                    company_id INTEGER,
                    company_name VARCHAR(255) NOT NULL,
                    CONSTRAINT companies_pkey PRIMARY KEY (company_id)                  
                )
            """)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancies (
                    id integer NOT NULL,
                    url text,
                    vacancy_name text,
                    salary_from integer,
                    salary_to integer,
                    company_name VARCHAR(255) NOT NULL,
                    company_id integer NOT NULL,
                    CONSTRAINT fk_vacancies_companies FOREIGN KEY(company_id) REFERENCES companies(company_id)
                )
            """)

    conn.commit()
    conn.close()
