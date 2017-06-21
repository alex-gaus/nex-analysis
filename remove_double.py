import sqlite3
import dataset
import json
import glob
import csv
import datetime
import os
import os.path

db='sqlite:///nex-analysis.db'
database = dataset.connect(db)
dpa_text=database["dpa_text"]
found_entities=database["found_entities"]
entity=database["entity"]
tools= database["tools"]
dpa_text= database["dpa_text"]

entity_list=list(database.query("select rowid, surface, start, entity_id, dpa_id from found_entities where tool_id=:tool_id",tool_id=3))
x=0
for entity in entity_list:
    surface=entity["surface"]
    start=entity["start"]
    entity_id=entity["entity_id"]
    dpa_id=entity["dpa_id"]
    rowid=entity["rowid"]
    
    for entity_2 in entity_list:
        rowid_2=entity_2["rowid"]
        surface_2=entity_2["surface"]
        start_2=entity_2["start"]
        entity_id_2=entity_2["entity_id"]
        dpa_id_2=entity_2["dpa_id"]
        if rowid==rowid_2:
            print("same entity")
        else:
            if surface==surface_2 and start==start_2 and entity_id==entity_id_2 and dpa_id==dpa_id_2:
                print(x)
                x=x+1
                database.query("delete from found_entities where rowid=:rowid",rowid=rowid_2)

