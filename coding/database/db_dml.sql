INSERT INTO Cliente (username, nome, cognome, password) VALUES 
	('alberto_rubini', 			'Alberto', 	'Rubini', 			'c582dec943ff7b743aa0691df291cea6'),
	('antonio_galati', 			'Antonio', 	'Galati', 			'4e42f7dd43ecbfe104de58610557c5ba'),
	('arianna_antonelli', 		'Arianna', 	'Antonelli', 		'4124bc0a9335c27f086f24ba207a4912'),
	('aurora_savoia', 			'Aurora', 	'Savoia', 			'f970e2767d0cfe75876ea857f92e319b'),
	('chiara_demarchi', 		'Chiara', 	'De Marchi', 		'6865aeb3a9ed28f9a79ec454b259e5d0'),
	('davide_masini', 			'Davide', 	'Masini', 			'608e7dc116de7157306012b4f0be82ac'),
	('edoardo_polfranceschi', 	'Edoardo', 	'Polfranceschi', 	'6aa1e040c8b4607538970731e4040ed6'),
	('giacomo_santi', 			'Giacomo', 	'Santi', 			'1d8d5e912302108b5e88c3e77fcad378'),
	('giovanni_bellorio', 		'Giovanni',	'Bellorio', 		'7885444af42e4b30c518c5be17c8850b'),
	('laura_mascalzoni', 		'Laura', 	'Mascalzoni', 		'192292e35fbe73f6d2b8d96bd1b6697d'),
	('shenal_fernando', 		'Shenal', 	'Fernando', 		'60d31eb37595dd44584be5ef363283e3');

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
	
INSERT INTO Oggetto (titolo, 					categoria, 		prezzo, 	descrizione,															foto,																		qta_magazzino, 	qta_scaffale, 	sconto, 	eta_consigliata, 	sesso_consigliato) VALUES
	('angelic bracelet', 						'bracelet',		'155.00',	'Round cut. Pavé. Small. White. Rhodium plated', 						('../static/img/angelic_bracelet_1.png'),									4, 				0, 				10, 		22, 				'F'),
	('angelic necklace', 						'necklace', 	'230.00', 	'Round cut. White. Rhodium plated',										('../static/img/angelic_necklace_1.png'),									3, 				1,				10, 		30, 				'F'),
	('constella cocktail ring', 				'ring', 		'135.00', 	'Round cut. Pavé, White, Rhodium plated', 								('../static/img/constella_cocktail_ring_1.png'),							2, 				0, 				10,			50, 				'F'),
	('dad bracelet', 							'bracelet', 	'145.00', 	'White, Rhodium plated', 												('../static/img/dad_bracelet_1.png'),										5, 				1, 				10, 		88, 				'M'),
	('dancing swan necklace', 					'necklace', 	'155.00', 	'Swan, Blue, Rhodium plated', 											('../static/img/dancing_swan_necklace_1.png'),								7, 				0, 				10,			20,					'F'),
	('dextera bracelet', 						'bracelet', 	'155.00', 	'Pavé, Mixed links, Black, Ruthenium plated',  							('../static/img/dextera_bracelet_1.png'),									9, 				1, 				10, 		20, 				'M'),
	('dextera hoop earrings', 					'earrings', 	'115.00', 	'Small, White, Rhodium plated', 										('../static/img/dextera_hoop_earrings_1.png'),								6, 				1,				10,			20,					'F'),
	('dextera necklace', 						'necklace', 	'175.00', 	'Pavé, Mixed links, Black, Ruthenium plated', 							('../static/img/dextera_necklace_1.png'),									7, 				1, 				10,			20, 				'M'),
	('florere necklace', 						'necklace', 	'175.00', 	'Flower, Pink, Gold-tone plated', 										('../static/img/florere_necklace_1.png'),									4, 				0,				10, 		17, 				'F'),
	('florere stud earrings', 					'earrings', 	'195.00', 	'Flower, Pink, Gold-tone plated', 										('../static/img/florere_stud_earrings_1.png'),								5, 				1,				10, 		56, 				'F'),
	('gema bracalet', 							'bracelet', 	'195.00', 	'Mixed cuts. Multicolored, Rhodium plated', 							('../static/img/gema_bracelet_1.png'),										8, 				1, 				10, 		65, 				'F'),
	('gema drop earrings', 						'earrings', 	'195.00', 	'Asymmetrical design, Mixed cuts, Long, Multicolored, Rhodium plated', 	('../static/img/gema_drop_earrings_1.png'),									5, 				0, 				10, 		77, 				'F'),
	('gema necklace', 							'necklace', 	'195.00', 	'Mixed cuts. Multicolored. Rhodium plated', 							('../static/img/gema_necklace_1.png'),										4, 				1, 				10, 		84, 				'F'),
	('matrix tennis necklace', 					'necklace', 	'350.00', 	'Mixed cuts, Green, Rhodium plated', 									('../static/img/matrix _tennis_necklace_1.png'),							1, 				1, 				10, 		54, 				'F'),
	('matrix drop earrings', 					'earrings', 	'195.00', 	'Mixed cuts, Green, Rhodium plated', 									('../static/img/matrix_drop_earrings_1.png'),								3, 				0, 				10, 		82, 				'F'),
	('matrix ring',								'ring', 		'125.00', 	'Baguette cut, Gray, Ruthenium plated',									('../static/img/matrix_ring_1.png'),										7, 				0, 				10, 		34, 				'F'),
	('matrix stud earrings', 					'earrings', 	'95.00', 	'Rectangular cut, Green, Gold-tone plated',								('../static/img/matrix_stud_earrings_1.png'),								3, 				1, 				10, 		49, 				'F'),
	('mesmera bracelet', 						'bracelet', 	'400.00', 	'Oversized crystals, White, Rhodium plated', 							('../static/img/mesmera_bracelet_1.png'),									6, 				0, 				10, 		38, 				'F'),
	('mesmera cocktail ring', 					'ring', 		'135.00', 	'Octagon cut, White, Rhodium plated', 									('../static/img/mesmera_cocktail_ring_1.png'),								3, 				1, 				10, 		29, 				'F'),
	('mesmera necklace', 						'necklace', 	'950.00', 	'Statement, Mixed cuts, White, Rhodium plated', 						('../static/img/mesmera_necklace_1.png'),									4, 				1, 				10, 		38,					'F'),
	('millenia cocktail ring', 					'ring', 		'135.00', 	'Pear cut, Pavé, White, Rhodium plated', 								('../static/img/millenia_cocktail_ring_1.png'),								8, 				0, 				10, 		47, 				'F'),
	('millenia necklace', 						'necklace', 	'700.00', 	'Square cut, Gray, Ruthenium plated', 									('../static/img/millenia_necklace_1.png'),									8, 				0, 				10, 		37, 				'M'),
	('stella drop earrings', 					'earrings',		'135.00', 	'Kite cut, Star, White, Rose gold-tone plated',							('../static/img/stella_drop_earrings_1.png'),								7, 				1, 				10, 		63, 				'F'),
	('stella necklace', 						'necklace', 	'175.00', 	'Star, White, Rose gold-tone plated', 									('../static/img/stella_necklace_1.png'),									4, 				1, 				10, 		23, 				'F'),
	('stella stud earrings', 					'earrings', 	'125.00', 	'Round cut, Star, White, Rose gold-tone plated', 						('../static/img/stella_stud_earrings_1.png'),								7, 				0, 				10, 		62, 				'F'),
	('stone hoop earrings', 					'earrings', 	'125.00', 	'Pavé, Large, White. Rhodium plated', 									('../static/img/stone_hoop_earrings_1.png'),								4, 				1, 				10, 		37, 				'F'),
	('swarovski iconic swan earring jackets', 	'earrings', 	'125.00', 	'Swan. Black. Rose gold-tone plated', 									('../static/img/swarovski_iconic_swan_earring_jackets_1.png'),				9, 				0, 				10, 		39, 				'F'),
	('swarovski iconic swan pendant', 			'necklace', 	'115.00', 	'Swan. Black. Rose gold-tone plated', 									('../static/img/swarovski_iconic_swan_pendant_1.png'),						6, 				0, 				10, 		79, 				'F'),
	('swarovski swan stud earrings', 			'earrings', 	'129.00', 	'Swan. Black. Rose gold-tone plated', 									('../static/img/swarovski_swan_stud_earrings_1.png'),						5, 				1, 				10, 		35, 				'F'),
	('vittore ring', 							'ring', 		'75.00', 	'Round cut. White, Gold-tone finish', 									('../static/img/vittore_ring_1.png'),										3, 				0, 				10, 		84, 				'F');
	
INSERT INTO CarrelloOggetto (id_carrello, id_oggetto) VALUES
	(1, 1),
	(1, 4);

INSERT INTO Ordine (id_cliente, prezzo_totale, data_acquisto, ora_acquisto, modalita_pagamento) VALUES
	(7, 	'125.00', 	'2024-01-15', 	'12:30:00', 	'bonifico'),
	(4, 	'700.00', 	'2024-01-05', 	'11:50:44', 	'bonifico');

INSERT INTO OrdineOggetto (id_ordine, id_oggetto) VALUES
	(1, 27),
	(2, 22);

INSERT INTO Emozione (id_cliente, id_oggetto, eta, sesso, indice_gradimento	) VALUES
	(1, 	18, 22, 	'M', 	100);
	
INSERT INTO Abbinamento (id_oggetto1, id_oggetto2) VALUES
	(1, 2),
	(4, 5);