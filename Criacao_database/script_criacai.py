# coding: cp1252
import os
import psycopg2
from dotenv import load_dotenv

script_dir = os.path.dirname(__file__)
env_path = os.path.abspath(os.path.join(script_dir, '..', '.env'))
sql_path = os.path.abspath(os.path.join(script_dir, 'tabela.sql'))

load_dotenv(env_path, encoding='utf-8-sig')


def executar_script_sql(caminho_arquivo):
    print("SQL path:", sql_path)
    print("Arquivo existe?", os.path.exists(sql_path))
    conn_params = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "port": os.getenv("DB_PORT") # força UTF-8 na conexão
    }
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()

        print(f"Executando {caminho_arquivo}...")

        encodings = ['utf-8-sig', 'cp1252', 'latin-1', 'utf-8']
        sql_script = None

        for encoding in encodings:
            try:
                with open(caminho_arquivo, 'r', encoding=encoding) as f:
                    sql_script = f.read()
                print(f"Arquivo lido com encoding: {encoding}")
                break
            except (UnicodeDecodeError, LookupError):
                continue

        if sql_script is None:
            raise Exception("Nao foi possivel ler o arquivo com nenhum encoding suportado")

        cur.execute(sql_script)
        conn.commit()
        print("Operacao realizada com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


executar_script_sql(sql_path)