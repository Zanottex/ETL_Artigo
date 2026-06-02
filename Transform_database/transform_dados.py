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

        df_bruto = pd.read_csv(arquivo_csv, sep=";", encoding="utf-8-sig", low_memory=False)
        con = duckdb.connect(database=":memory:")

        # Registrar o DataFrame como tabela no DuckDB
        con.register("df_bruto", df_bruto)

        # 3. O DuckDB consegue ler o DataFrame 'df_bruto' diretamente pelo nome da variável!
        query_transformacao = """
            SELECT 
                CAST(IdeConjuntoUnidadeConsumidora AS VARCHAR(100)) AS IdeConjuntoUnidadeConsumidora,
                CAST(DscConjuntoUnidadeConsumidora AS VARCHAR(100)) AS DscConjuntoUnidadeConsumidora,
                CAST(DscAlimentadorSubestacao AS VARCHAR(20)) AS DscAlimentadorSubestacao,
                CAST(DscSubestacaoDistribuicao AS VARCHAR(20)) AS DscSubestacaoDistribuicao,
                CAST(NumOrdemInterrupcao AS VARCHAR(50)) AS NumOrdemInterrupcao,
                CAST(DscTipoInterrupcao AS VARCHAR(15)) AS DscTipoInterrupcao,
                CAST(IdeMotivoInterrupcao AS VARCHAR(100)) AS IdeMotivoInterrupcao,
                CAST(DatInicioInterrupcao AS VARCHAR(20)) AS DatInicioInterrupcao,
                CAST(DatFimInterrupcao AS VARCHAR(20)) AS DatFimInterrupcao,
                CAST(DscFatoGeradorInterrupcao AS VARCHAR(255)) AS DscFatoGeradorInterrupcao,
                CAST(NumNivelTensao AS VARCHAR(100)) AS NumNivelTensao,
                CAST(NumUnidadeConsumidora AS VARCHAR(100)) AS NumUnidadeConsumidora,
                CAST(NumConsumidorConjunto AS VARCHAR(100)) AS NumConsumidorConjunto,
                CAST(NumAno AS SMALLINT) AS NumAno,
                CAST(NomAgenteRegulado AS VARCHAR(100)) AS NomAgenteRegulado,
                CAST(SigAgente AS VARCHAR(10)) AS SigAgente,
                CAST(NumCPFCNPJ AS VARCHAR(14)) AS NumCPFCNPJ
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