<<<<<<< HEAD
CREATE TABLE Interrupcoes (
    IdeConjuntoUnidadeConsumidora varchar(100),
    DscConjuntoUnidadeConsumidora varchar(100),
    DscAlimentadorSubestacao varchar(100),
    DscSubestacaoDistribuicao varchar(100),
    NumOrdemInterrupcao varchar(100),
    DscTipoInterrupcao varchar(100),
    IdeMotivoInterrupcao varchar(100),
    DatInicioInterrupcao varchar(255),
    DatFimInterrupcao varchar(255),
    DscFatoGeradorInterrupcao varchar(255),
    NumNivelTensao varchar(100),
    NumUnidadeConsumidora varchar(100),
    NumConsumidorConjunto varchar(100),
    NumAno varchar(100),
    NomAgenteRegulado varchar(150),
=======
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
>>>>>>> b77dcb8c27c3f1a13d3471403b66584a5be76fff
    SigAgente varchar(100),
    NumCPFCNPJ varchar(100)
)