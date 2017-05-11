
import os
import glob
import json
import csv
import html


tools=[
    "txtwerk",
    "dandelion",
    "ambiverse"
]
#print(os.getcwd())
path_original = "/Users/alex/nex-analysis"
path = "/Users/alex/python_project/write_csv"
os.chdir( path )
#print(os.getcwd())
dpaid="urn_newsml_dpa.com_20090101_170221-99-370286v-3"

path_output_dpa="outputs/DPA-Meldungen/**/**/%s.json"%dpaid
dpa_file_path = glob.glob(path_output_dpa)[0]
html_list=[]
for tool in tools:
    os.chdir( path )
    path_output_tool= "data/**/**/%s_%s.csv"%(tool,dpaid)

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
    length=len(entities)
    length_confidence=length
    word_count=len(text.split())
    entities_word =length / word_count
    confidence_sum = 0
    for z in entities:
        try:
            confidence_sum= confidence_sum + float(z["confidence"])
        except ValueError:
            length_confidence=length_confidence-1
    avg_confidence=confidence_sum/length_confidence
    header="""<h2>tool = %s </h2>
    <h4>Entities found = %s ---- Entities per word = %s</h4>
    <h4>Average confidence = %s</h4>
    <div>&nbsp;</div><div>"""%(tool, length, entities_word, avg_confidence)
    prefix="""<mark tool=%s><a href="%s" title="%s , %s">"""
    suffix="</a></mark>"
    text_list=[header]
    for x in range(0,length):
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


    text_html="""<td style="padding:20px">%s</td>"""%"".join(text_list)
    print("check")
    html_list.append(text_html)
    html_input="".join(html_list)
    """ 
    Html_file= open("%s_test.html"%tool,"w")
    Html_file.write(text_html)
    Html_file.close()
    """

    final_html='''<h1 style="text-align: center;">NER-Analyser</h1>
    <h3 style="text-align: center;">dpaID = %s</h3>
    <h3 style="text-align: center;">Words in text = %s </h3>
    <table min-width="800">
    </tr>
    %s
    </tr>
    </table>'''%(dpaid,word_count, html_input)

Html_file= open("test.html","w")
Html_file.write(final_html)
Html_file.close()