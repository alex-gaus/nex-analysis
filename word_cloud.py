#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud
import sqlite3
import dataset

d = path.dirname(__file__)

ressort="pl"
tool="txtwerk"
dpa_id="%"
# dpa_id="urn:newsml:dpa.com:20090101:170319-99-722478/2"


# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
text="hallo hallo hallo dies ist ein text"
# Generate a word cloud image
db='sqlite:///nex-analysis.db'
database = dataset.connect(db)
dpa_text=database["dpa_text"]
found_entities=database["found_entities"]
entity=database["entity"]
tools= database["tools"]
dpa_text= database["dpa_text"]


tool_id=list(database.query("select rowid from tools where tool=:tool",tool=tool))[0]["rowid"]
texts=list(database.query("select rowid from dpa_text where dpa_id like :dpa_id and ressort like :ressort",dpa_id=dpa_id,ressort=ressort))

text_list=[]
for dpa_id_id in texts:
    entity_list=list(database.query("select entity_id, tool_id, dpa_id from found_entities where dpa_id =:dpa_id_id and tool_id =:tool_id",dpa_id_id=dpa_id_id["rowid"],tool_id=tool_id))
    for entity in entity_list:
        entity_id=entity["entity_id"]
        tool_id=entity["tool_id"]
        dpa_id_id=entity["entity_id"]
        unique_entity=list(database.query("select label from entity where rowid like :entity_id",entity_id=entity_id))
        label=unique_entity[0]["label"]
        text_list.append(label)
        # tool_list=list(database.query("select tool from tools where rowid like :tool_id and tool like :tool",tool_id=tool_id,tool=tool,))
        # if len(tool_list)>0:
        #     text=list(database.query("select text from dpa_text where rowid like :dpa_id_id and dpa_id like :dpa_id and ressort like :ressort",dpa_id_id=dpa_id_id,dpa_id=dpa_id,ressort=ressort))
        #     if len(text)>0:
        #         text_list.append(label)
        
                

# print(text_list)

text="".join(text_list)
wordcloud = WordCloud().generate(text)

# # Display the generated image:
# # the matplotlib way:
# import matplotlib.pyplot as plt
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# # lower max_font_size
# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
image.show()