import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

# Gets the names of the available data sets in seaborn
sns.get_dataset_names()

titanic.head()

titanic['class'].value_counts()

sns.countplot(x="class", data=titanic)

sns.countplot(y="class", hue="who", data=titanic)

sns.countplot(x="class", hue="survived", data=titanic, orient="v")
