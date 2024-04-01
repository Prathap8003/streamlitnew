import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import time
st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")
selected_x_var = st.selectbox("What do you want the x variable to be?",["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],)
selected_y_var = st.selectbox("What about the y?",["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],)
selected_gender = st.selectbox("What gender do you want to filter for?", ['all penguins', 'male penguins', 'female penguins'])
#File uploader - if no file uploaded use default file - if uploaded use their file
penguins_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")
def load_file(penguins_file):
    time.sleep(3)
    if penguins_file is not None:
        df = pd.read_csv(penguins_file)
    else:
        df = pd.read_csv('penguins.csv')
    return(df)
penguins_df = load_file(penguins_file)
#penguin gender filter app
if selected_gender == "male penguins":
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == "female penguins":
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass
sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
alt_chart = (
alt.Chart(penguins_df, title="Scatterplot of Palmer's Penguins")
.mark_circle()
.encode(x= selected_x_var, y=selected_y_var, color="species",)
.interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
