import streamlit as st
import pandas as pd


def main():
    st.title("Interactive Data Browser")

    # Load data
    data = load_data()

    # Display data
    st.write("### Data Preview")
    st.write(data)

    # Interactive features
    st.sidebar.header("Filters")
    add_filters(data)


def load_data():
    """
    Function to load data. Modify this function to load your data from a file or database.
    """
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        # Load data from user-uploaded CSV file
        data = pd.read_csv(uploaded_file)
    else:
        # Provide default data if no file is uploaded
        data = pd.DataFrame({"column1": [1, 2, 3], "column2": ["A", "B", "C"]})  # Example default data
    return data


def add_filters(data):
    """
    Function to add interactive filters.
    """
    # Example: Add interactive filters for categorical columns
    categorical_cols = [col for col in data.columns if data[col].dtype == "object"]
    for col in categorical_cols:
        unique_values = data[col].unique()
        selected_values = st.sidebar.multiselect(f"Select {col}", unique_values, unique_values)
        if selected_values:
            data = data[data[col].isin(selected_values)]

    # Example: Add interactive filter for numerical column
    numerical_cols = [col for col in data.columns if data[col].dtype in ["int64", "float64"]]
    for col in numerical_cols:
        min_val = int(data[col].min())
        max_val = int(data[col].max())
        default_min, default_max = min_val, max_val
        if st.sidebar.checkbox(f"Filter by {col}"):
            default_min, default_max = st.sidebar.slider(f"Select range for {col}", min_val, max_val,
                                                         (min_val, max_val))
            data = data[(data[col] >= default_min) & (data[col] <= default_max)]

    # Display filtered data
    st.write("### Filtered Data Preview")
    st.write(data)


if __name__ == "__main__":
    main()
