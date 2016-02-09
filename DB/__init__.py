__author__ = 'UriA12'

import sqlite3

conn = sqlite3.connect('cluster_db.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Color;
DROP TABLE IF EXISTS Protein;
DROP TABLE IF EXISTS Age;
DROP TABLE IF EXISTS Model;
DROP TABLE IF EXISTS Antibody;
DROP TABLE IF EXISTS Protocol;
DROP TABLE IF EXISTS Condition;
DROP TABLE IF EXISTS Point;
DROP TABLE IF EXISTS Cluster;
DROP TABLE IF EXISTS Sample;
DROP TABLE IF EXISTS Epitope;
CREATE TABLE Color (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Protein (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Epitope (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Company (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Clonal (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Species (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE WaveLength (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Age (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    age_months  INTEGER
);

CREATE TABLE Model (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Antibody (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    name TEXT  UNIQUE,
    protein_id INTEGER,
    epitope_id INTEGER,
    company_id  INTEGER,
    catalog_number INTEGER,
    clonal_id  INTEGER,
    species_id INTEGER,
    wave_length_id INTEGER
);

CREATE TABLE Protocol (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    name TEXT  UNIQUE,
    primary_antibody_id INTEGER,
    primary_antibody_dilution  INTEGER,
    secondary_antibody_id INTEGER,
    secondary_antibody_dilution  INTEGER,
    species_id INTEGER,
    model_id INTEGER,
    age_id INTEGER

);
''')

conn.commit()
