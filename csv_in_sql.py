import sqlite3
import dataset
import json
import glob
import csv
import datetime
import os
import os.path

path_original = "/Users/alex/nex-analysis"
path = "/Users/alex/python_project/write_csv"
db='sqlite:///nex-analysis.db'

database = dataset.connect(db)
dpa_text=database["dpa_text"]
found_entities=database["found_entities"]
entity=database["entity"]
tools= database["tools"]
dpa_text= database["dpa_text"]

os.chdir(path)
file_list_tool=glob.glob("data/*/*/*.csv")

for tool_file in file_list_tool:
    with open (tool_file, "r") as f:
        t=os.path.getmtime(tool_file)
        entities = list(csv.DictReader(f))
        if len(entities) > 0:
            tool=entities[0]["tool"]
            value_tool=tools.find_one(tool=tool)
            if  value_tool == None:
                tools.insert({"tool":tool})
                print("Tool ",tool," angelegt")
            else:
                print("Tool ",tool," ist bereits angelegt")
            tool_id=list(database.query("select rowid from tools  where tool=:tool",tool=tool))[0]["rowid"]
            dpa_id_edited=entities[0]["dpaid"]
            dpa_id_original=dpa_id_edited.replace("_",":")
            dpa_id_original=dpa_id_original.replace('v-', '/')
            value_dpaid=dpa_text.find_one(dpa_id=dpa_id_original)
            if value_dpaid == None:
                file_list_dpa=glob.glob("outputs/*/*/*/%s.json"%dpa_id_edited)
                dpa_file=file_list_dpa[0]
                with open (dpa_file, "r") as f:
                    dpa = json.load(f)
                    dpa_id = dpa["dpaId"]
                    title = dpa["dpaTitle"]
                    ressort = dpa["dpaRessort"]
                    text = dpa["text"]
                    date = dpa["createdAt"] 
                    dpa_text.insert(dict(
                        dpa_id=dpa_id,
                        title=title,
                        ressort=ressort,
                        text=text,
                        date=date
                        ))
                print("dpaID ",dpa_id_original,"  angelegt")
            else:
                print("dpaID ",dpa_id_original," ist bereits angelegt")
            dpa_id_id=list(database.query("select rowid from dpa_text  where dpa_id=:dpa_id",dpa_id=dpa_id_original))[0]["rowid"]
            for entity_dic in entities:
                try:
                    uri=entity_dic["uri"]
                    uri=uri.replace("https://www.wikidata.org/wiki/","")
                    uri=uri.replace("http://www.wikidata.org/entity/","")
                except KeyError:
                    uri=""
                surface=entity_dic["surface"]
                if len(uri)>1:
                    entity_id=uri
                else:
                    entity_id=surface
                if len(entity_dic["label"])>0:
                    label=entity_dic["label"]
                    labelfromsurface=False
                else:
                    label=entity_dic["surface"]
                    labelfromsurface=True
                value_entity=entity.find_one(entity_id=entity_id)
                extra={
                    "txtwerk":"None",
                    "dandelion":"None",
                    "ambiverse":"None"}
                if value_entity == None:
                    entity.insert(dict(
                        uri=uri,
                        label=label,
                        entity_id=entity_id,
                        labelfromsurface=labelfromsurface,
                        extra=str(extra)
                        
                    ))
                    print("Entity ",entity_dic["surface"]," wurde angelegt")
                else:
                    print("Entity ",entity_dic["surface"]," bereits angelegt")
                    entity_id_id=list(database.query("select rowid from entity  where entity_id=:entity_id",entity_id=entity_id))[0]["rowid"]
                    value_label=list(database.query("select labelfromsurface from entity where rowid=:entity_id_id",entity_id_id=entity_id_id))[0]["labelfromsurface"]
                    if value_label == 1:
                        entity.upsert(dict(
                            label=label,
                            labelfromsurface=labelfromsurface,
                            entity_id=entity_id
                            ),["entity_id"])
                entity_id_id=list(database.query("select rowid from entity  where entity_id=:entity_id",entity_id=entity_id))[0]["rowid"]
                value_extra=found_entities.find_one(entity_id=entity_id_id,tool_id=tool_id)
                value_extra=None                   
                if value_extra == None:
                    try:
                        confidence=float(entity_dic["confidence"])
                    except ValueError:
                        confidence = None
                    except KeyError:
                        confidence = None
                    found_entities.insert(dict(
                        surface=surface,
                        start=int(entity_dic["start"]),
                        end=int(entity_dic["end"]),
                        confidence=confidence,
                        found='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t)) ,
                        dpa_id=dpa_id_id,
                        tool_id=tool_id,
                        entity_id=entity_id_id
                    ))

        """else:
            extra={tool:"None"}
            found_entities.insert(dict(surface="",
                    label="",
                    start=0,
                    end=0,
                    confidence=0,
                    uri="q0",
                    timestamp='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t)),
                    extra=str(extra)))
"""
print("DONE")
os.chdir(path_original)