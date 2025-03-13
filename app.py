import streamlit as st
import pandas as pd
!pip install seaboard
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Set page title and description
# st.set_page_config(page_title="Iris Dataset Visualization", page_icon=":bar_chart:", layout="wide")
# st.title("Iris Dataset Visualization")
# st.write("This application visualizes the Iris dataset using Seaborn.")

# Scatter plot
# st.subheader("Scatter Plot")
fig, ax = plt.subplots()
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", ax=ax)
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
st.pyplot(fig)

# Histogram
# st.subheader("Histogram - Sepal Length")
# fig, ax = plt.subplots()
# sns.histplot(data=iris, x="sepal_length", bins=20, ax=ax)
# ax.set_xlabel("Sepal Length (cm)")
# ax.set_ylabel("Frequency")
# st.pyplot(fig)

# Box plot
# st.subheader("Box Plot")
# fig, ax = plt.subplots()
# sns.boxplot(data=iris, x="species", y="petal_length", ax=ax)
# ax.set_xlabel("Species")
# ax.set_ylabel("Petal Length (cm)")
# st.pyplot(fig)

# Display dataset
# st.subheader("Dataset")
# st.write(iris)

# Acknowledgements
# st.subheader("Acknowledgements")
# st.write("Built with [Streamlit](https://streamlit.io). Iris dataset from [Fisher's 1936 paper](https://archive.ics.uci.edu/ml/datasets/iris).")
