CREATE TABLE Cliente (
	id			SERIAL,
	username	VARCHAR,
	nome		VARCHAR,
	cognome		VARCHAR,
	password	VARCHAR,
	
	PRIMARY KEY(id)
);

CREATE TABLE Carrello (
	id			SERIAL,
	id_cliente	INT,
	
	PRIMARY KEY(id),
	FOREIGN KEY(id_cliente) REFERENCES Cliente(id)
);

CREATE TABLE Oggetto (
	id					SERIAL,
	titolo				VARCHAR,
	categoria			VARCHAR,
	prezzo				DECIMAL,
	descrizione			VARCHAR,
	foto				BYTEA,
	qta_magazzino		INT,
	qta_scaffale		INT,
	sconto				INT,
	eta_consigliata		INT,
	sesso_consigliato	CHAR,
	
	PRIMARY KEY(id)
);

CREATE TABLE CarrelloOggetto (
	id			SERIAL,
	id_carrello	INT,
	id_oggetto 	INT,
	
	PRIMARY KEY(id),
	FOREIGN KEY(id_carrello) REFERENCES Carrello(id),
	FOREIGN KEY(id_oggetto) REFERENCES Oggetto(id)
);

CREATE TABLE Ordine (
	id					SERIAL,
	id_cliente			INT,
	prezzo_totale		DECIMAL,
	data_acquisto		DATE,
	ora_acquisto		TIME,
	modalita_pagamento	VARCHAR,
	
	PRIMARY KEY(id),
	FOREIGN KEY(id_cliente) REFERENCES Cliente(id)
);

CREATE TABLE OrdineOggetto (
	id			SERIAL,
	id_ordine	INT,
	id_oggetto	INT,
	
	PRIMARY KEY(id),
	FOREIGN KEY(id_ordine) REFERENCES Ordine(id),
	FOREIGN KEY(id_oggetto) REFERENCES Oggetto(id)
);

CREATE TABLE Emozione (
	id					SERIAL,
	id_cliente			INT,
	id_oggetto			INT,
	eta					INT,
	sesso				CHAR,
	indice_gradimento	INT,
	
	PRIMARY KEY(id),
	FOREIGN KEY(id_cliente) REFERENCES Cliente(id),
	FOREIGN KEY(id_oggetto) REFERENCES Oggetto(id)
);

CREATE TABLE Abbinamento (
	id			SERIAL,
	id_oggetto1	INT,
	id_oggetto2	INT,
	
	PRIMARY KEY(id),
	FOREIGN KEY(id_oggetto1) REFERENCES Oggetto(id),
	FOREIGN KEY(id_oggetto2) REFERENCES Oggetto(id)
);