import sqlite3

db='sqlite:///nex-analysis.db'
database = dataset.connect(db)
database.query("select rowid from tools  where tool='%s'"%tool)

# DROP TABLE IF EXISTS `tools`
"""
CREATE TABLE `tools` (
	`tool`	TEXT NOT NULL UNIQUE
);

CREATE TABLE 'dpa_text' (
	'dpa_id'	TEXT NOT NULL UNIQUE,
	'title'	TEXT,
	'ressort'	TEXT,
	'date'	TEXT,
	'text'	TEXT,
	PRIMARY KEY('dpa_id')
);

CREATE TABLE 'entity' (
	'uri'	TEXT,
	'label'	TEXT,
	'labelfromsurface' INTEGER,
	'entity_id'	TEXT NOT NULL UNIQUE,
	'extra' TEXT
);

CREATE TABLE 'found_entities' (
	'surface'	TEXT NOT NULL,
	'start'	INTEGER NOT NULL,
	'end'	INTEGER NOT NULL,
	'found'	TEXT,
	'confidence'	NUMERIC,
	'dpa_id'	INTEGER NOT NULL,
	'tool_id'	INTEGER NOT NULL,
	'entity_id'	INTEGER NOT NULL,
    FOREIGN KEY(dpa_id) REFERENCES dpa_text(rowid),
    FOREIGN KEY(tool_id) REFERENCES tools(rowid),
    FOREIGN KEY(entity_id) REFERENCES entity(rowid)
);
"""


database.engine.execute("select * from entity where label like :suchbegriff",suchbegriff="%’%").fetchall()
list(database.query("select * from entity where label like :suchbegriff",suchbegriff="%’%"))
 #tool_id=list(database.query("select rowid from tools  where tool=?", tool)[0]["rowid"]


DELETE FROM found_entities;
DELETE FROM entity;
DELETE FROM dpa_text;
DELETE FROM tools;
