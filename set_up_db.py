import sqlite3

db='sqlite:///nex-analysis.db'
database = dataset.connect(db)
database.query("select rowid from tools  where tool='%s'"%tool)

"""
CREATE TABLE `tools` (
	`tool`	TEXT NOT NULL UNIQUE
);

CREATE TABLE `dpa_text` (
	`dpa_id`	TEXT NOT NULL UNIQUE,
	`title`	TEXT,
	`ressort`	TEXT,
	`date`	TEXT,
	`text`	TEXT,
	PRIMARY KEY(`dpa_id`)
);

CREATE TABLE `entity` (
	`uri`	TEXT,
	`label`	TEXT,
	`type`	TEXT,
	`entity_id`	INTEGER NOT NULL UNIQUE
);

CREATE TABLE `found_entities` (
	`surface`	TEXT NOT NULL,
	`start`	INTEGER NOT NULL,
	`end`	INTEGER,
	`found`	TEXT,
	`confidence`	NUMERIC,
	`dpa_id`	TEXT NOT NULL,
	`tool_id`	NUMERIC,
	`entity_id`	TEXT
    FOREIGN KEY(dpa_id) REFERENCES dpa_text(dpa_id)
    FOREIGN KEY(tool) REFERENCES tools(tool_id)
    FOREIGN KEY(entity) REFERENCES entity(entity_id)
);
