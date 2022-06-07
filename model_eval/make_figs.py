#!/usr/bin/env python 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import ipdb

# working directory
p = Path("/usr/lusers/aultl/ThermoDrift/model_eval")

df_test = pd.read_csv(p/"datasets"/"processed_analysis_test_data.csv") 
df_train = pd.read_csv(p/"datasets"/"processed_analysis_train_data.csv")

df = pd.concat([df_test, df_train])
df["true_class"] = pd.CategoricalIndex(df["true_class"], categories=["Psychrophile", "Mesophile", "Thermophile"], ordered=True, name="True Class")




# graph distribution of classification probabilities
# fig, ax = plt.subplots(1,2, figsize=(8,6))
# # generate kde distribution plots
# for col in ["thermo_prob", "meso_prob", "psychro_prob"]:
#     df[col].plot(kind='density', label=col, ax=ax[0], legend=True)

# ax[0].set_xlabel("Probability of model classification", fontsize=13)
# ax[0].set_ylabel("Density", fontsize=13)
# plt.legend()

# generate heatmap plots
df = df.drop(columns="predicted").groupby("true_class").agg("mean")
df.index = (pd.CategoricalIndex(['Psychrophile', 'Mesophile', 'Thermophile'], 
                                categories=['Psychrophile', 'Mesophile', 'Thermophile'], 
                                ordered=True, dtype='category', name='True Class'))

df.columns = ["Thermophile", "Mesophile", "Psychrophile"]

g = sns.heatmap(df, annot=True, linewidths=.5, cmap="YlGnBu")
g.set_title("CNN Model Classification Probabilities", fontsize=14)
txt="Probability"
plt.figtext(0.5, 0.0001, txt, wrap=True, horizontalalignment='center', fontsize=11)

plt.tight_layout()
plt.savefig(p/"figs"/"220606_fig1_CNNmodel_analysis_heatmaponly.png", dpi=600)



