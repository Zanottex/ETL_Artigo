import os
import duckdb
import pandas as pd

arquivo_csv = "dados/tipado.csv"
arquivo_saida = "dados/dados_transformados.csv"


def transformar_dados():
    if not os.path.exists(arquivo_csv):
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
        return

    print(f"Lendo {arquivo_csv} via Pandas (contornando o encoding Latin-1)...")

    try:

        df_bruto = pd.read_csv(arquivo_csv, sep=",", encoding="latin-1", low_memory=False)
        con = duckdb.connect(database=":memory:")

        # Registrar o DataFrame como tabela no DuckDB
        con.register("df_bruto", df_bruto)

        # 3. O DuckDB consegue ler o DataFrame 'df_bruto' diretamente pelo nome da variável!
        query_transformacao = """
            SELECT 
                CAST(IdeConjuntoUnidadeConsumidora AS BIGINT) AS IdeConjuntoUnidadeConsumidora,
                CAST(DscConjuntoUnidadeConsumidora AS VARCHAR(25)) AS DscConjuntoUnidadeConsumidora,
                CAST(DscAlimentadorSubestacao AS VARCHAR(50)) AS DscAlimentadorSubestacao,
                CAST(DscSubestacaoDistribuicao AS VARCHAR(255)) AS DscSubestacaoDistribuicao,
                CAST(NumOrdemInterrupcao AS VARCHAR(50)) AS NumOrdemInterrupcao,
                CAST(DscTipoInterrupcao AS VARCHAR(25)) AS DscTipoInterrupcao,
                CAST(IdeMotivoInterrupcao AS BIGINT) AS IdeMotivoInterrupcao,
                CAST(DatInicioInterrupcao AS TIMESTAMP) AS DatInicioInterrupcao,
                CAST(DatFimInterrupcao AS TIMESTAMP) AS DatFimInterrupcao,
                CAST(DscFatoGeradorInterrupcao AS VARCHAR(255)) AS DscFatoGeradorInterrupcao,
                CAST(NumNivelTensao AS BIGINT) AS NumNivelTensao,
                CAST(NumUnidadeConsumidora AS VARCHAR(100)) AS NumUnidadeConsumidora,
                CAST(NumConsumidorConjunto AS VARCHAR(100)) AS NumConsumidorConjunto,
                CAST(NumAno AS VARCHAR(100)) AS NumAno,
                CAST(NomAgenteRegulado AS VARCHAR(150)) AS NomAgenteRegulado,
                CAST(SigAgente AS VARCHAR(5)) AS SigAgente,
                CAST(NumCPFCNPJ AS VARCHAR(100)) AS NumCPFCNPJ
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