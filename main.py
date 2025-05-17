import streamlit as st
from scipy.stats import (
    ttest_ind,
    mannwhitneyu
    )

from significance_tester_app.src.utils import read_csv_file

st.title("The Significance tester app")
st.header("")
st.caption("This app is for demostration purposes only!")


statistical_tests={
    "t-test": ttest_ind,
    "Mann-Whitney U": mannwhitneyu,
}


uploaded_file = st.file_uploader(
    label="Choose a CSV file", 
    accept_multiple_files=False
)

if uploaded_file is not None:
    df= read_csv_file(uploaded_file)

    st.write("Please select two columns!")
    selection= st.multiselect(
    label= "Select the columns of interest",
    options= df.columns.tolist(),
    default=None
    )

    if selection != [] and len(selection) == 2:
        st.write(df[selection].head(3))
        if len(selection) == 2 and df.isna().sum().values.sum().tolist() == 0:
            st.write("Both columns have equal lengths!")
            variance= st.selectbox(
                label= "Are you assuming equal population variance?", 
                options= ["True", "False"], 
                index=None
                )
            if variance is not None:
                distribution= st.selectbox(
                label= "Are you assuming equal population distribution?", 
                options= ["True", "False"], 
                index=None
                )
                
                if variance == "True" and distribution == "True":
                    stats= st.selectbox(
                        label= "Please select the desired statistical test", 
                        options= ["Standard t-test"], 
                        index=None
                        )
                    
                    if stats == "Standard t-test":
                        statistic, pvalue= ttest_ind(a= df[selection[0]], b= df[selection[1]], alternative='two-sided', equal_var=True)
                        st.write(f"Test: {stats}  \np-value: {pvalue}  \nNull hypothesis: {'Rejected' if pvalue<0.05 else 'Accepted'}")
                
                elif variance == "False" and distribution == "True":
                    stats= st.selectbox(
                        label= "Please select the desired statistical test", 
                        options= ["Welch's t-test"], 
                        index=None
                        )
                    if stats == "Welch's t-test":
                        statistic, pvalue= ttest_ind(a= df[selection[0]], b= df[selection[1]], alternative='two-sided', equal_var=False)
                        st.write(f"Test: {stats}  \np-value: {pvalue}  \nNull hypothesis: {'Rejected' if pvalue<0.05 else 'Accepted'}")

                elif distribution == "False":
                    stats= st.selectbox(
                        label= "Please select the desired statistical test", 
                        options= ["Mann-Whitney U"], 
                        index=None
                        )
                    if stats == "Mann-Whitney U":
                        U1, pvalue= mannwhitneyu(x= df[selection[0]], y= df[selection[1]], alternative='two-sided')
                        st.write(f"Test: {stats}  \np-value: {pvalue}  \nNull hypothesis: {'Rejected' if pvalue<0.05 else 'Accepted'}")
        
        elif len(selection) == 2 and df.isna().sum().values.sum().tolist() != 0:
            st.write("The column are unequal in lengths!")
            stats= st.selectbox(
                label= "Please select the desired statistical test", 
                options= ["Mann-Whitney U"], 
                index=None
                )
            if stats == "Mann-Whitney U":
                U1, pvalue= mannwhitneyu(x= df[selection[0]].dropna(), y= df[selection[1]].dropna(), alternative='two-sided')
                st.write(f"Test: {stats}  \np-value: {pvalue}  \nNull hypothesis: {'Rejected' if pvalue<0.05 else 'Accepted'}")