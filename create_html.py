
import os
import glob
import json
import csv
import html


tool="txtwerk"
#print(os.getcwd())
path_original = "/Users/alex/nex-analysis"
path = "/Users/alex/python_project/write_csv"
os.chdir( path )
#print(os.getcwd())
dpaid="urn_newsml_dpa.com_20090101_170221-99-370286v-3"

path_output_dpa="outputs/DPA-Meldungen/**/**/%s.json"%dpaid

path_output_tool= "data/**/**/%s_%s.csv"%(tool,dpaid)
#path_output="*.ipynb"




dpa_file_path = glob.glob(path_output_dpa)[0]
#print(file_list)
dpa_file= json.loads(open(dpa_file_path).read())
text=dpa_file["text"]
output_file_path=glob.glob(path_output_tool)[0]
output = csv.DictReader(open(output_file_path))
os.chdir( path_original )
#print(os.getcwd())
entities=[]
for entity in output:
    entities.append(entity)
start_list=[]
end_list=[]
for position in entities:
    start_list.append(position["start"])
    end_list.append(position["end"])
y=0
header="""<h1>NER-Analyser</h1>
<h2>dpaID= %s</h2>
<h2>tool= %s</h2>
<div>&nbsp;</div><div>"""%(dpaid,tool)
prefix="""<mark tool=%s><a href="%s" title="%s , %s">"""
suffix="</a></mark>"
text_list=[header]
for x in range(0,len(entities)):
    part=text[y:int(entities[x]["start"])]
    entity=text[int(entities[x]["start"]):int(entities[x]["end"])]
    uri=entities[x]["uri"]
    label=entities[x]["label"]
    confidence=entities[x]["confidence"]
    text_list.append(part)
    text_list.append(prefix%(tool,uri,label,confidence))
    text_list.append(entity)
    text_list.append(suffix)
    y=int(entities[x]["end"])
end=text[y:len(text)]
text_list.append(end)
text_list.append("</div>")
text_html="".join(text_list)



Html_file= open("test.html","w")
Html_file.write(text_html)
Html_file.close()