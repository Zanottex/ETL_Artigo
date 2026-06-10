CREATE TABLE Interrupcoes3 (
    IdeConjuntoUnidadeConsumidora BIGINT,
    DscConjuntoUnidadeConsumidora varchar(50),
    DscAlimentadorSubestacao varchar(50),
    DscSubestacaoDistribuicao varchar(100),
    NumOrdemInterrupcao varchar(50),
    DscTipoInterrupcao varchar(25),
    IdeMotivoInterrupcao BIGINT,
    DatInicioInterrupcao TIMESTAMP,
    DatFimInterrupcao TIMESTAMP,
    DscFatoGeradorInterrupcao varchar(255),
    NumNivelTensao BIGINT,
    NumUnidadeConsumidora varchar(100),
    NumConsumidorConjunto varchar(100),
    NumAno smallint,
    NomAgenteRegulado varchar(255),
    SigAgente varchar(100),
    NumCPFCNPJ varchar(25)
)