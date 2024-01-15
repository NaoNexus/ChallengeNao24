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
	
INSERT INTO Oggetto (titolo, 					categoria, 		prezzo, 	descrizione, 															qta_magazzino, 	qta_scaffale, 	sconto, 	eta_consigliata, 	sesso_consigliato) VALUES
	('angelic bracelet', 						'bracelet',		'155.00',	'Round cut. Pavé. Small. White. Rhodium plated', 						4, 				0, 				10, 		22, 				'F'),
	('angelic necklace', 						'necklace', 	'230.00', 	'Round cut. White. Rhodium plated',										3, 				1,				10, 		30, 				'F'),
	('constella cocktail ring', 				'ring', 		'135.00', 	'Round cut. Pavé, White, Rhodium plated', 								2, 				0, 				10,			50, 				'F'),
	('dad bracelet', 							'bracelet', 	'145.00', 	'White, Rhodium plated', 												5, 				1, 				10, 		88, 				'M'),
	('dancing swan necklace', 					'necklace', 	'155.00', 	'Swan, Blue, Rhodium plated', 											7, 				0, 				10,			20,					'F'),
	('dextera bracelet', 						'bracelet', 	'155.00', 	'Pavé, Mixed links, Black, Ruthenium plated',  							9, 				1, 				10, 		20, 				'M'),
	('dextera hoop earrings', 					'earrings', 	'115.00', 	'Small, White, Rhodium plated', 										6, 				1,				10,			20,					'F'),
	('dextera necklace', 						'necklace', 	'175.00', 	'Pavé, Mixed links, Black, Ruthenium plated', 							7, 				1, 				10,			20, 				'M'),
	('florere necklace', 						'necklace', 	'175.00', 	'Flower, Pink, Gold-tone plated', 										4, 				0,				10, 		17, 				'F'),
	('florere stud earrings', 					'earrings', 	'195.00', 	'Flower, Pink, Gold-tone plated', 										5, 				1,				10, 		56, 				'F'),
	('gema bracalet', 							'bracelet', 	'195.00', 	'Mixed cuts. Multicolored, Rhodium plated', 							8, 				1, 				10, 		65, 				'F'),
	('gema drop earrings', 						'earrings', 	'195.00', 	'Asymmetrical design, Mixed cuts, Long, Multicolored, Rhodium plated', 	5, 				0, 				10, 		77, 				'F'),
	('gema necklace', 							'necklace', 	'195.00', 	'Mixed cuts. Multicolored. Rhodium plated', 							4, 				1, 				10, 		84, 				'F'),
	('matrix tennis necklace', 					'necklace', 	'350.00', 	'Mixed cuts, Green, Rhodium plated', 									1, 				1, 				10, 		54, 				'F'),
	('matrix drop earrings', 					'earrings', 	'195.00', 	'Mixed cuts, Green, Rhodium plated', 									3, 				0, 				10, 		82, 				'F'),
	('matrix ring',								'ring', 		'125.00', 	'Baguette cut, Gray, Ruthenium plated',									7, 				0, 				10, 		34, 				'F'),
	('matrix stud earrings', 					'earrings', 	'95.00', 	'Rectangular cut, Green, Gold-tone plated',								3, 				1, 				10, 		49, 				'F'),
	('mesmera bracelet', 						'bracelet', 	'400.00', 	'Oversized crystals, White, Rhodium plated', 							6, 				0, 				10, 		38, 				'F'),
	('mesmera cocktail ring', 					'ring', 		'135.00', 	'Octagon cut, White, Rhodium plated', 									3, 				1, 				10, 		29, 				'F'),
	('mesmera necklace', 						'necklace', 	'950.00', 	'Statement, Mixed cuts, White, Rhodium plated', 						4, 				1, 				10, 		38,					'F'),
	('millenia cocktail ring', 					'ring', 		'135.00', 	'Pear cut, Pavé, White, Rhodium plated', 								8, 				0, 				10, 		47, 				'F'),
	('millenia necklace', 						'necklace', 	'700.00', 	'Square cut, Gray, Ruthenium plated', 									8, 				0, 				10, 		37, 				'M'),
	('stella drop earrings', 					'earrings',		'135.00', 	'Kite cut, Star, White, Rose gold-tone plated',							7, 				1, 				10, 		63, 				'F'),
	('stella necklace', 						'necklace', 	'175.00', 	'Star, White, Rose gold-tone plated', 									4, 				1, 				10, 		23, 				'F'),
	('stella stud earrings', 					'earrings', 	'125.00', 	'Round cut, Star, White, Rose gold-tone plated', 						7, 				0, 				10, 		62, 				'F'),
	('stone hoop earrings', 					'earrings', 	'125.00', 	'Pavé, Large, White. Rhodium plated', 									4, 				1, 				10, 		37, 				'F'),
	('swarovski iconic swan earring jackets', 	'earrings', 	'125.00', 	'Swan. Black. Rose gold-tone plated', 									9, 				0, 				10, 		39, 				'F'),
	('swarovski iconic swan pendant', 			'necklace', 	'115.00', 	'Swan. Black. Rose gold-tone plated', 									6, 				0, 				10, 		79, 				'F'),
	('swarovski swan stud earrings', 			'earrings', 	'129.00', 	'Swan. Black. Rose gold-tone plated', 									5, 				1, 				10, 		35, 				'F'),
	('vittore ring', 							'ring', 		'75', 		'Round cut. White, Gold-tone finish', 									3, 				0, 				10, 		84, 				'F');

INSERT INTO CarrelloOggetto (id_carrello, id_oggetto) VALUES
	(1, 1),
	(1, 4);

INSERT INTO Oggetto (foto) VALUES 
	(E'\\x' || encode(lo_import('C:\Users\kiade\OneDrive\Desktop\nao24-github\ChallengeNao24\coding\dataset\angelic_bracelet\angelic_bracelet_1.png'), 'hex'));

INSERT INTO Ordine (id_cliente, prezzo_totale, data_acquisto, ora_acquisto, modalita_pagamento) VALUES
	(7, 	'125.00', 	'2024-01-15', 	'12:30:00', 	'bonifico'),
	(4, 	'700.00', 	'2024-01-05', 	'11:50:44', 	'bonifico');

INSERT INTO OrdineOggetto (id_ordine, id_oggetto) VALUES
	(1, 27),
	(2, 22);

INSERT INTO Emozione (id_cliente, id_oggetto, eta, sesso, indice_gradimento	) VALUES
	(1, 	18, 	'M', 	8);
	
INSERT INTO Abbinamento (id_oggetto1, id_oggetto2) VALUES
	(1, 2),
	(4, 5);