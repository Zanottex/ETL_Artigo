CREATE TABLE interrupcoes (
    
    IdeConjuntoUnidadeConsumidora int PRIMARY KEY ,
    DscConjuntoUnidadeConsumidora varchar(100),
    DscAlimentadorSubestacao varchar(5),
    DscSubestacaoDistribuicao varchar(3),
    NumOrdemInterrupcao int,
    DscTipoInterrupcao varchar(15),
    IdeMotivoInterrupcao int,
    DatInicioInterrupcao timestamp,
    DatFimInterrupcao timestamp,
    DscFatoGeradorInterrupcao varchar(255),
    NumNivelTensao int,
    NumUnidadeConsumidora smallint,
    NumConsumidorConjunto int,
    NumAno smallint,
    NomAgenteRegulado varchar(100),
    SigAgente varchar(50),
    NumCPFCNPJ int
);