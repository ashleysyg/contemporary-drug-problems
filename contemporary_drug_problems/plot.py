import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
 
df1 = pd.DataFrame({'Product': [44],
                    'Used Paraphernalia': [42.4],
                    'Drug Refuse': [13.6]},
                    index=['Sample Type'])
df2 = pd.DataFrame({'Hallucinogens': [5.6],
                    'Stimulants': [31.2],
                    'Opioids': [50.4],
                    'Benzodiazepines': [6.4],
                    'Unknown': [6.4]},
                    index=['Substance Class'])

font = {'size'   : 18}
plt.rc('font', **font)

fig, ax = plt.subplots(1, 2, figsize=(12, 10), sharey=True)
fig.suptitle('Drug Samples Collected from RI')

# sample type
df1.plot(ax=ax[0], kind='bar', stacked=True, color=sns.color_palette('gnuplot2_r'), fontsize=18).legend(loc='upper right')
ax[0].set(ylabel="Percent of Samples")

# substance class
df2.plot(ax=ax[1], kind='bar', stacked=True, color=sns.color_palette('gnuplot2_r'), fontsize=18).legend(loc='upper right')

plt.tight_layout()
plt.savefig('ri_drug_samples.png')







font = {'size'   : 14}
plt.rc('font', **font)

df3 = pd.DataFrame({'Expected': [39.2, 0],
                    'Detected': [28, 41.6]},
                    index=['Fentanyl', 'Xylazine'])

df3.plot(kind='bar', stacked=True, color=sns.color_palette('gnuplot2_r'), fontsize=12).legend(loc='upper right')

plt.ylabel('Percent of Supply')
plt.title('Drug Supply Expectation vs. Reality')
plt.tight_layout()
plt.savefig('expected_detected.png')