
# coding: utf-8

# In[28]:

import pandas as pd

table=pd.read_csv("data/20170508-entities.csv")
table.head()


# # Tool-Vergleich

# In[61]:

tooltable=table.groupby("tool").count()
tooltable.head(100)


# # Verschiedene Surfaceforms

# In[62]:

print("Disctinct Surfaceforms:",len(set(table["surface"])))


# # Ueberschneidungen zwischen den tools

# In[63]:

# eine Funktion, die fuer jede Zeile ausgefuehrt wird und eine neue Spalte zurueckliefert 

func=lambda a: a["dpaid"]+":"+str(a["start"])

table["startpos"]=table.apply(func, axis=1)

startpostable=table.groupby("startpos").aggregate({ "start"   : "count", 
                                                    "tool"    : lambda a: ",".join(sorted(a)), 
                                                    "surface" : lambda a: ",".join(set(a))
                                                  })



# In[66]:

from itertools import combinations

tools_list=sorted(set(table["tool"]))

for n in range(1,1+len(tools_list)) :
    for c in combinations(tools_list,n) :
        tools=",".join(c) 
        print(tools,":",len(startpostable.query("tool=='%s'" % tools)))


# In[ ]:




# In[ ]:



