import os
import duckdb
import pandas as pd

arquivo_csv = "dados/base.csv"
arquivo_saida = "dados/dados_transformados.csv"


def transformar_dados():
    if not os.path.exists(arquivo_csv):
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
        return

    print(f"Lendo {arquivo_csv} via Pandas (contornando o encoding Latin-1)...")

    try:

        df_bruto = pd.read_csv(arquivo_csv, sep=",", encoding="utf-8-sig")
        con = duckdb.connect(database=":memory:")

        # Registrar o DataFrame como tabela no DuckDB
        con.register("df_bruto", df_bruto)

        # 3. O DuckDB consegue ler o DataFrame 'df_bruto' diretamente pelo nome da variável!
        query_transformacao = """
            SELECT 
                CAST(id AS INTEGER) AS id,
                CAST(IdeConjuntoUnidadeConsumidora AS INTEGER) AS IdeConjuntoUnidadeConsumidora,
                CAST(DscConjuntoUnidadeConsumidora AS TEXT) AS DscConjuntoUnidadeConsumidora,
                CAST(DscAlimentadorSubestacao AS TEXT) AS DscAlimentadorSubestacao,
                CAST(DscSubestacaoDistribuicao AS TEXT) AS DscSubestacaoDistribuicao,
                CAST(NumOrdemInterrupcao AS TEXT) AS NumOrdemInterrupcao,
                CAST(DscTipoInterrupcao AS TEXT) AS DscTipoInterrupcao,
                CAST(IdeMotivoInterrupcao AS INTEGER) AS IdeMotivoInterrupcao,
                CAST(DatInicioInterrupcao AS DATE) AS DatInicioInterrupcao,
                CAST(DatFimInterrupcao AS DATE) AS DatFimInterrupcao,
                CAST(DscFatoGeradorInterrupcao AS TEXT) AS DscFatoGeradorInterrupcao,
                CAST(NumNivelTensao AS INTEGER) AS NumNivelTensao,
                CAST(NumUnidadeConsumidora AS INTEGER) AS NumUnidadeConsumidora,
                CAST(NumConsumidorConjunto AS INTEGER) AS NumConsumidorConjunto,
                CAST(NumAno AS SMALLINT) AS NumAno,
                CAST(NomAgenteRegulado AS TEXT) AS NomAgenteRegulado,
                CAST(SigAgente AS TEXT) AS SigAgente,
                CAST(NumCPFCNPJ AS BIGINT) AS NumCPFCNPJ
            FROM df_bruto
        """

        print("\n--- Prévia dos Dados Transformados (Top 5 linhas) ---")
        con.sql(query_transformacao).limit(5).show()

        print(f"\nExportando dados para {arquivo_saida}...")
        con.execute(
            f"COPY ({query_transformacao}) TO '{arquivo_saida}' (FORMAT CSV, HEADER TRUE, DELIMITER ',');"
        )
        print("Transformação concluída com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante a transformação:\n{e}")
    finally:
        if "con" in locals():
            con.close()


if __name__ == "__main__":
    transformar_dados()