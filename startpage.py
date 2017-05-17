import html
import glob
import os
import json


path_compare = "data/compare/nex-analysis_*.html"
path = "/Users/alex/python_project/write_csv"
path_original = "/Users/alex/nex-analysis"


file_list = glob.glob(path_compare)
html_list=[]
html_item="""
<tr>
<td style="padding:6px","text-align: center;"><a href="%s" target="_blank">%s</a></td>
<td style="padding:6px","text-align: center;"><a href="%s" target="_blank">New window</a></td>
</tr>
"""
for item in file_list:
    dpaid=item[45:-5]
    os.chdir( path )
    json_path = "outputs/DPA-Meldungen/**/**/*%s.json"%dpaid
    json_output = glob.glob(json_path)
    dpa_file = json.loads(open(json_output[0]).read())
    os.chdir( path_original )
    title=dpa_file["dpaTitle"]
    #id_pipette=dpa_file["dpaId"]
    id_pipette=item[26:-8].replace("v",'')
    id_pipette=id_pipette.replace("_",":")
    link_pipette="https://pipette.dpa-newslab.com/pipette/#/doc/%s"%id_pipette
    link="file:///Users/alex/nex-analysis/data%s"%item[4:]
    html_list.append(html_item%(link_pipette,title,link))
html_text="".join(html_list)

final_html="""
<h1>Overview NER-texts</h1>
<table width="100%%" cellspacing="2" cellpadding="0" border="1" align="center" bgcolor="aliceblue">
<tbody>
<tr>
<td style="padding:20px"><strong>Title (links to pipettte)</strong></td>
<td style="padding:20px"><strong>entity extraction</strong></td>
</tr>
</tbody>
%s
</tbody>
</table>
"""

html_file= open("data/startpage.html","w")
html_file.write(final_html%html_text)
html_file.close()