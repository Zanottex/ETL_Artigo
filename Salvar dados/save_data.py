import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Configuração do banco de dados
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASS")

arquivo_csv = "dados/dados_transformados.csv"
TABELA = "interrupcoes"


def conectar_banco():
    """Conecta ao banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print(f"✓ Conectado ao banco de dados: {DB_NAME}")
        return conn
    except psycopg2.Error as e:
        print(f"✗ Erro ao conectar ao banco: {e}")
        return None


def limpar_tabela(conn):
    """Limpa a tabela antes de inserir novos dados."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABELA};")
        conn.commit()
        rows_deleted = cursor.rowcount
        print(f"✓ Tabela '{TABELA}' limpa ({rows_deleted} linhas removidas)")
        cursor.close()
    except psycopg2.Error as e:
        print(f"✗ Erro ao limpar tabela: {e}")
        conn.rollback()


def salvar_dados_no_banco():
    """Lê o CSV transformado e insere no PostgreSQL."""
    
    if not os.path.exists(arquivo_csv):
        print(f"✗ Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
        return

    print(f"\nLendo {arquivo_csv}...")
    df = pd.read_csv(arquivo_csv)
    
    print(f"✓ {len(df)} linhas lidas do CSV")
    print(f"✓ Colunas: {', '.join(df.columns.tolist())}\n")

    conn = conectar_banco()
    if conn is None:
        return

    try:
        # Limpar tabela (opcional - comentar se não quiser)
        limpar_tabela(conn)

        cursor = conn.cursor()
        
        # Preparar dados para inserção
        # Mapear valores NaN para None (NULL no PostgreSQL)
        df = df.where(pd.notna(df), None)
        
        # Criar statement SQL para insert
        colunas = ", ".join(df.columns)
        placeholders = ", ".join(["%s"] * len(df.columns))
        insert_query = f"INSERT INTO {TABELA} ({colunas}) VALUES ({placeholders})"
        
        # Converter DataFrame para lista de tuplas
        dados = [tuple(row) for row in df.values]
        
        print(f"Inserindo {len(dados)} linhas na tabela '{TABELA}'...")
        
        # Inserir dados em batch (mais eficiente)
        execute_batch(cursor, insert_query, dados, page_size=1000)
        
        conn.commit()
        print(f"✓ {len(dados)} linhas inseridas com sucesso!")
        
        # Mostrar amostra dos dados inseridos
        cursor.execute(f"SELECT COUNT(*) FROM {TABELA};")
        total = cursor.fetchone()[0]
        print(f"✓ Total de linhas na tabela: {total}")
        
        cursor.close()

    except psycopg2.Error as e:
        print(f"✗ Erro ao inserir dados: {e}")
        conn.rollback()
    finally:
        conn.close()
        print("\n✓ Conexão fechada")


if __name__ == "__main__":
    print("=" * 60)
    print("ETL - SALVAR DADOS NO POSTGRESQL")
    print("=" * 60)
    salvar_dados_no_banco()
