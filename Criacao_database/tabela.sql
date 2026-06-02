CREATE TABLE Interrupcoes (
    IdeConjuntoUnidadeConsumidora VARCHAR(100),
    DscConjuntoUnidadeConsumidora varchar(100),
    DscAlimentadorSubestacao varchar(100),
    DscSubestacaoDistribuicao varchar(100),
    NumOrdemInterrupcao varchar(100),
    DscTipoInterrupcao varchar(100),
    IdeMotivoInterrupcao VARCHAR(100),
    DatInicioInterrupcao varchar(100),
    DatFimInterrupcao varchar(100),
    DscFatoGeradorInterrupcao varchar(255),
    NumNivelTensao VARCHAR(100),
    NumUnidadeConsumidora VARCHAR(100),
    NumConsumidorConjunto VARCHAR(100),
    NumAno VARCHAR(100),
    NomAgenteRegulado varchar(100),
    SigAgente varchar(100),
    NumCPFCNPJ varchar(14)
)