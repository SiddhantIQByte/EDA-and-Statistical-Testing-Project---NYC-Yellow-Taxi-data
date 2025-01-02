import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Upload the file (CSV or Parquet)
uploaded_file = st.file_uploader("Upload your CSV or Parquet file for EDA", type=["csv", "parquet"])

if uploaded_file is not None:
    # Check the file extension and read the file accordingly
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".parquet"):
        data = pd.read_parquet(uploaded_file,engine='pyarrow')
    
    st.write("Dataset:", data)

    # Identify numeric and categorical columns
    numeric_columns = data.select_dtypes(include=['number']).columns
    categorical_columns = data.select_dtypes(exclude=['number']).columns

    # Descriptive statistics
    st.write("### Descriptive Statistics")
    st.write(data.describe(include='all'))

    # Numeric column analysis
    st.write("### Numeric Column Analysis")
    for col in numeric_columns:
        st.write(f"#### Analysis for {col}")

        # Histogram for distribution
        st.write("Distribution:")
        fig, ax = plt.subplots()
        sns.histplot(data[col], kde=True, ax=ax)
        st.pyplot(fig)

        # Boxplot for outliers
        st.write("Boxplot:")
        fig, ax = plt.subplots()
        sns.boxplot(x=data[col], ax=ax)
        st.pyplot(fig)

        # Trends over index (if applicable)
        st.write("Trend over rows:")
        fig, ax = plt.subplots()
        plt.plot(data.index, data[col])
        ax.set_title(f"Trend for {col}")
        ax.set_xlabel("Index")
        ax.set_ylabel(col)
        st.pyplot(fig)

    # Categorical column analysis
    st.write("### Categorical Column Analysis")
    for col in categorical_columns:
        st.write(f"#### Analysis for {col}")

        # Count plot
        st.write("Count Plot:")
        fig, ax = plt.subplots()
        sns.countplot(y=data[col], order=data[col].value_counts().index, ax=ax)
        st.pyplot(fig)

    # Correlation Heatmap
    st.write("### Correlation Analysis")
    if len(numeric_columns) > 1:
        corr_matrix = data[numeric_columns].corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Pairplot for multivariate analysis
    st.write("### Pairplot")
    if len(numeric_columns) > 1:
        pairplot_fig = sns.pairplot(data[numeric_columns])
        st.pyplot(pairplot_fig.fig)
