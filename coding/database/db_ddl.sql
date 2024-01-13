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
	--foto				BLOB,
	qta_magazzino		INT,
	qta_scaffale		INT,
	sconto				CHAR,
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




INSERT INTO Cliente (username, nome, cognome, password) VALUES 
	('alberto_rubini', 			'Alberto', 	'Rubini', 			'ar'),
	('antonio_galati', 			'Antonio', 	'Galati', 			'ag'),
	('arianna_antonelli', 		'Arianna', 	'Antonelli', 		'aa'),
	('aurora_savoia', 			'Aurora', 	'Savoia', 			'as'),
	('chiara_demarchi', 		'Chiara', 	'De Marchi', 		'cd'),
	('davide_masini', 			'Davide', 	'Masini', 			'dm'),
	('edoardo_polfranceschi', 	'Edoardo', 	'Polfranceschi', 	'ep'),
	('giacomo_santi', 			'Giacomo', 	'Santi', 			'gs'),
	('giovanni_bellorio', 		'Giovanni',	'Bellorio', 		'gb'),
	('laura_mascalzoni', 		'Laura', 	'Mascalzoni', 		'lm'),
	('shenal_fernando', 		'Shenal', 	'Fernando', 		'sf');

INSERT INTO Carrello (id_cliente) VALUES
	(1),
	(2),
	(3),
	(4),
	(5),
	(6),
	(7),
	(8),
	(9),
	(10),
	(11);
	
INSERT INTO CarrelloOggetto (id_carrello, id_oggetto) VALUES
	(1),
	(2),
	(3),
	(4),
	(5),
	(6),
	(7),
	(8),
	(9),
	(10),
	(11);
	
INSERT INTO Oggetto (titolo, categoria, prezzo, descrizione, foto, qta_magazzino, qta_scaffale, sconto, eta_consigliata, sesso_consigliato) VALUES
	('angelic bracelet', 			),
	('angelic necklace', 			),
	('constella cocktail ring', 	'ring'),
	('florere necklace', 			),
	('florere stud earrings', 		),
	('gema bracelet', 				),
	('gema drop earrings', 			),
	('gema necklace', 			),
	('matrix tennis necklace'),
	('matrix drop earrings'),
	(11);





