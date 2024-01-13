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
	
	
INSERT INTO Oggetto (titolo, categoria, prezzo, descrizione, qta_magazzino, qta_scaffale, sconto, eta_consigliata, sesso_consigliato) VALUES
	('angelic bracelet', 			'bracelet',		'155.00',		'Round cut. Pavé. Small. White. Rhodium plated', 	4, 		0, 	'T', 		22, 	'F'),
	('angelic necklace', 			'necklace', 	'230.00', 	'Round cut. White. Rhodium plated',					3, 		1,	'F', 		30, 	'M'),
	('constella cocktail ring', 	'ring', 		'135.00', 	'Round cut. Pavé, White, Rhodium plated', 			2, 		0, 	'F',		50, 	'M'),
	('florere necklace', 			'necklace', 	'175.00', 	'Flower, Pink, Gold-tone plated', 					4, 		0,	'T', 		17, 	'F'),
	('florere stud earrings', 		'earrings', 	'195.00', 	'Flower, Pink, Gold-tone plated', 					5, 		1,	'F', 		56, 	'M');

INSERT INTO CarrelloOggetto (id_carrello, id_oggetto) VALUES
	(1, 1),
	(1, 4);
	
INSERT INTO Abbinamento (id_oggetto1, id_oggetto2) VALUES
	(1, 2),
	(4, 5);
	
	
	
	
