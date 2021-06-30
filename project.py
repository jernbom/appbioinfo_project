import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns


string_h_sapiens = pd.read_csv('downloads/STRING_h_sapiens.txt', sep=' ')


network_df = string_h_sapiens[string_h_sapiens.combined_score >= 500]


network = nx.from_pandas_edgelist(network_df, source = "protein1", target = "protein2")



degree = list(network.degree())
degree_gr_100 = []
degree_leq_100 = []

for d in degree:
    if d[1] > 100:
        degree_gr_100.append(d[0])
    elif d[1] <= 100:
        degree_leq_100.append(d[0])
    else:
        print("Error")
        break


tmp1 = pd.DataFrame(list(zip(degree_gr_100, [">100"]*len(degree_gr_100))), columns=["Protein stable ID", "Node degree"])
tmp2 = pd.DataFrame(list(zip(degree_leq_100, ["<=100"]*len(degree_leq_100))), columns=["Protein stable ID", "Node degree"])

degree_dichot = tmp1.append(tmp2)
degree_dichot["Protein stable ID"] = degree_dichot.rename(columns={"Protein stable ID": "protein_id"}).apply(lambda row: row.protein_id.split(".")[1], axis=1)


protein_domains = pd.read_csv("downloads/Ensembl_protein_domain.txt", sep = "\t")
protein_domains_count = protein_domains.groupby("Protein stable ID").agg("count").rename(columns={"Pfam ID": "domain_count"})


degree_domain = protein_domains_count.join(degree_dichot.set_index("Protein stable ID"), how="outer")
degree_domain = degree_domain[degree_domain.domain_count.notnull() & degree_domain["Node degree"].notnull()]


sns.set(rc={'figure.figsize':(8.27, 11.7)})

ax = sns.boxplot(x="Node degree", y="domain_count", data = degree_domain)
fig = ax.get_figure()
fig.savefig("protein_domains_vs_string_degree.png")


