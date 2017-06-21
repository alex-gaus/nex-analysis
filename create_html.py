
import os
import glob
import json
import csv
import html
from set_color import set_color



csv_list="data/list_100.csv"

tools=[
    "txtwerk",
    "dandelion",
    "ambiverse"
]
path_original = "/Users/alex/nex-analysis"
path = "/Users/alex/python_project/write_csv"


with open(csv_list) as f:
    file_list=csv.reader(f)
    os.chdir( path )
    for row in file_list:
        html_list = []
        os.chdir( path )
        dpa_file_path = row[0]
        #path_output_dpa = "outputs/DPA-Meldungen/**/**/%s"%dpaid
        #dpa_file_path = glob.glob(path_output_dpa)[0]
        dpa_file = json.loads(open(dpa_file_path).read())
        text = dpa_file["text"]
        urn = dpa_file["dpaId"]
        dpaid = urn.replace(":","_")
        dpaid = dpaid.replace('/', 'v-')
        urn = urn[:-2]
        title = dpa_file["dpaTitle"]
        pipette="https://pipette.dpa-newslab.com/pipette/#/doc/%s"%urn

        for tool in tools:
            os.chdir(path)
            path_output_tool = "data/**/**/%s_%s.csv"%(tool,dpaid)
            output_file_path=glob.glob(path_output_tool)[0]
            output = csv.DictReader(open(output_file_path))
            os.chdir(path_original)
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
            try:
                words_entity = word_count/length
            except ZeroDivisionError:
                words_entity = 0
            confidence_sum = 0
            
            for z in entities:
                try:
                    confidence_sum= confidence_sum + float(z["confidence"])
                except ValueError:
                    length_confidence=length_confidence-1
                except KeyError:
                    length_confidence=length_confidence-1
            try:
                avg_confidence=confidence_sum/length_confidence
            except ZeroDivisionError:
                avg_confidence= "Error"


            header="""
            <script src="https://hypothes.is/embed.js" async></script>
            <h2 style="text-align: center;">tool = %s </h2>
            <h4 style="text-align: center;">Entities found = %s ---- Words per entity = %s</h4>
            <h4 style="text-align: center;">Average confidence = %s</h4>
            <div>&nbsp;</div><div>
            """%(tool, length, words_entity, avg_confidence)

            prefix="""
            <mark tool="%s"
            confidence="%s"
            label="%s"
            uri="%s"
            ><a href="%s" 
            title="%s , %s" 
            style="background-color: %s;">
            """
            suffix="""
            </a></mark>
            """
            color=set_color(tool,tools)
            text_list=[header]

            for x in range(0,length):
                part=text[y:int(entities[x]["start"])]
                entity=text[int(entities[x]["start"]):int(entities[x]["end"])]
                try:
                    uri=entities[x]["uri"]
                except KeyError:
                    uri="Error"
                label=entities[x]["label"]
                try:
                    confidence=entities[x]["confidence"]
                except KeyError:
                    confidence = "Error"
                text_list.append(part)
                text_list.append(prefix%(tool,confidence,label,uri,uri,label,confidence,color))
                # text_list.append(prefix % locals())
                # prefix=" %(tool)s"
                text_list.append(entity)
                text_list.append(suffix)
                # ... in Python
                # { "type" : "text" , "content" : "....."}
                # { "type" : "entity" , "text": "...", "link" : ... }
                # ... in Jinja
                # {% for item in liste %}
                #  {% if item.type == "text" %}{{ item.text }}
                #  {% else %}
                #  <mark data-tool="{{ item.tool }}" data-confidence="{{ item.confidence }}"
                #  data-label="{{ item.label }}" ... ><a ...>{{ item.text }}</a></mark> 
                #  {% endif %}
                # {% endfor %}
                # 
                #  
                y=int(entities[x]["end"])
            end=text[y:len(text)]
            text_list.append(end)
            text_list.append("</div>")


            text_html="""
            <td style="padding:20px">%s</td>
            """%"".join(text_list)

            html_list.append(text_html)
            html_input="".join(html_list)

            final_html="""
            <h1 style="text-align: center;">NER-Analyser</h1>
            <h3 style="text-align: center;">%s </h3>
            <h3 style="text-align: center;"<td style="padding:6px","text-align: center;"><a href="%s" target="_blank">%s</a></td>
            **** Words in text = %s</h3>
            <table min-width="800">
            </tr>
            %s
            </tr>
            </table>
            """%(title,pipette, dpaid,word_count, html_input)

        html_file= open("data/compare/nex-analysis_%s.html"%dpaid,"w")
        html_file.write(final_html)
        html_file.close()