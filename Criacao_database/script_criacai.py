import os
import psycopg2
from dotenv import load_dotenv

script_dir = os.path.dirname(__file__)
env_path = os.path.abspath(os.path.join(script_dir, '..', '.env'))
load_dotenv(env_path)

def executar_script_sql(caminho_arquivo):
    conn_params = {
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASS"),
        "port": os.getenv("DB_PORT")
    }

    conn = None
    cur = None
    try:
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()

        with open(caminho_arquivo, 'r', encoding='latin-1') as f:
            sql_script = f.read()

        print(f"Executando {caminho_arquivo}...")
        cur.execute(sql_script)
        
        conn.commit()
        print("Operação realizada com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

executar_script_sql('Criacao_database/tabela.sql')