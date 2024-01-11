-- BELLORIO GIOVANNI
-- UTENTI
-- 5 SSA
	
-- TASK 1: create table
-- creo la tabella utenti
DROP TABLE IF EXISTS utenti CASCADE;
CREATE TABLE utenti (
	id SERIAL,
	username  VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	PRIMARY KEY(id)
);

-- TASK 2: insert table
-- inserisco utenti
INSERT INTO utenti(username,password)
	VALUES 	('giovanni','giovanni'),
    		('paolo', 'paolo');