# Schema for saving

CREATE DATABASE IF NOT EXISTS Chrono ;
USE Chrono;
#[66,'SCHAFER',"Alain","Fribourg","Honda"],

DROP TABLE IF EXISTS T_Concurents;
CREATE TABLE T_Concurents
(
	id				BIGINT UNSIGNED			NOT NULL PRIMARY KEY AUTO_INCREMENT,
	numero		INT UNSIGNED 				NOT NULL,
	nom			VARCHAR(80)				NOT NULL,
	prenom		VARCHAR(80)				NOT NULL,
	moto			INT UNSIGNED				,
	npa			VARCHAR(10)				,
	ville			VARCHAR(80)				,
	adresse		TINYTEXT						,
	pays			CHAR(3)						,
	telephone	VARCHAR(20)				,
	urgence		TINYTEXT						,
	bithday		DATE							,
	licences		TINYTEXT						,
	remarques	TEXT
);

# Liste pays iso
#DROP TABLE IF EXISTS T_Pays;
CREATE TABLE IF NOT EXISTS   T_Pays
(
	id				CHAR(3)						NOT NULL PRIMARY KEY,
	numero		INT							,
	nom			VARCHAR(100)
);
