
# coding: utf-8

# In[1]:

from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles

plt.figure(figsize=(4,4))
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels = ('A', 'B', 'C'))
v.get_patch_by_id('100').set_alpha(1.0)
v.get_patch_by_id('100').set_color('white')
v.get_label_by_id('100').set_text('Unknown')
v.get_label_by_id('A').set_text('Set "A"')
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='dashed')
c[0].set_lw(1.0)
c[0].set_ls('dotted')
plt.title("Sample Venn diagram")
plt.annotate('Unknown set', xy=v.get_label_by_id('100').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
             ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))
plt.show()


# In[2]:

import pandas as pd

table=pd.read_csv("data/20170508-entities.csv")

ambiverse = []
txtwerk = []
dandelion = []

for i in table.index:
    if table.ix[i]["tool"] == "ambiverse":
        ambiverse.append(table.ix[i]["surface"])
    elif table.ix[i]["tool"] == "txtwerk":
        txtwerk.append(table.ix[i]["surface"])
    elif table.ix[i]["tool"] == "dandelion":
        dandelion.append(table.ix[i]["surface"])
print("D",len(dandelion))
print("T",len(txtwerk))
print("A",len(ambiverse))
print("Ds",len(set(dandelion)))
print("Ts",len(set(txtwerk)))
print("As",len(set(ambiverse)))
type(dandelion)


# In[3]:

set1 = set(dandelion)
set2 = set(txtwerk)
set3 = set(ambiverse)
print("D",len(set1))
print("T",len(set2))
print("A",len(set3))

venn3([set1, set2, set3], ('Dandelion', 'Txtwerk', 'Ambiverse'))
plt.show()


# In[4]:

import pandas as pd

table=pd.read_csv("data/20170508-entities.csv")

ambiverse = []
txtwerk = []
dandelion = []

for i in table.index:
    if table.ix[i]["tool"] == "ambiverse":
        ambiverse.append(table.ix[i]["uri"])
    elif table.ix[i]["tool"] == "txtwerk":
        txtwerk.append(table.ix[i]["uri"])
    elif table.ix[i]["tool"] == "dandelion":
        dandelion.append(table.ix[i]["uri"])
print("D",len(dandelion))
print("T",len(txtwerk))
print("A",len(ambiverse))
type(dandelion)


# In[5]:

set1 = set(dandelion)
set2 = set(txtwerk)
set3 = set(ambiverse)

venn3([set1, set2, set3], ('Dandelion', 'Txtwerk', 'Ambiverse'))
plt.show()


# In[9]:

import pandas as pd

table=pd.read_csv("data/20170508-entities.csv")

ambiverse = []
txtwerk = []
dandelion = []

for i in table.index:
    if table.ix[i]["tool"] == "ambiverse":
        uri=str(table.ix[i]["uri"])
        uri=uri.replace("entity","wiki")
        uri=uri.replace("http","https")
        ambiverse.append(uri)
    elif table.ix[i]["tool"] == "txtwerk":
        txtwerk.append(str(table.ix[i]["uri"]))
    elif table.ix[i]["tool"] == "dandelion":
        dandelion.append(str(table.ix[i]["uri"]))

set1_uri = set(dandelion)
set2_uri = set(txtwerk)
set3_uri = set(ambiverse)

venn3([set1_uri, set2_uri, set3_uri], ('Dandelion', 'Txtwerk', 'Ambiverse'))
plt.title("URI")
plt.show()


ambiverse = []
txtwerk = []
dandelion = []

for i in table.index:
    if table.ix[i]["tool"] == "ambiverse":
        ambiverse.append(table.ix[i]["surface"])
    elif table.ix[i]["tool"] == "txtwerk":
        txtwerk.append(table.ix[i]["surface"])
    elif table.ix[i]["tool"] == "dandelion":
        dandelion.append(table.ix[i]["surface"])
        
set1_surface = set(dandelion)
set2_surface = set(txtwerk)
set3_surface = set(ambiverse)

venn3([set1_surface, set2_surface, set3_surface], ('Dandelion', 'Txtwerk', 'Ambiverse'))
plt.title("Surface")
plt.show()


ambiverse = []
txtwerk = []
dandelion = []

for i in table.index:
    if table.ix[i]["tool"] == "ambiverse":
        val="".join([str(table.ix[i]["start"]),str(table.ix[i]["dpaid"])])
        ambiverse.append(val)
    elif table.ix[i]["tool"] == "txtwerk":
        val="".join([str(table.ix[i]["start"]),str(table.ix[i]["dpaid"])])
        txtwerk.append(val)
    elif table.ix[i]["tool"] == "dandelion":
        val="".join([str(table.ix[i]["start"]),str(table.ix[i]["dpaid"])])
        dandelion.append(val)
        
set1_start = set(dandelion)
set2_start = set(txtwerk)
set3_start = set(ambiverse)

venn3([set1_start, set2_start, set3_start], ('Dandelion', 'Txtwerk', 'Ambiverse'))
plt.title("Start")
plt.show()


ambiverse = []
txtwerk = []
dandelion = []

for i in table.index:
    if table.ix[i]["tool"] == "ambiverse":
        val="".join([str(table.ix[i]["end"]),str(table.ix[i]["dpaid"])])
        ambiverse.append(val)
    elif table.ix[i]["tool"] == "txtwerk":
        val="".join([str(table.ix[i]["end"]),str(table.ix[i]["dpaid"])])
        txtwerk.append(val)
    elif table.ix[i]["tool"] == "dandelion":
        val="".join([str(table.ix[i]["end"]),str(table.ix[i]["dpaid"])])
        dandelion.append(val)
        
set1_end = set(dandelion)
set2_end = set(txtwerk)
set3_end = set(ambiverse)

venn3([set1_end, set2_end, set3_end], ('Dandelion', 'Txtwerk', 'Ambiverse'))
plt.title("End")
plt.show()




# In[ ]:




# In[ ]:




# In[ ]:



