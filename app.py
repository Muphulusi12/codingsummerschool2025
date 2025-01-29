import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Muphulusi Nekhavhambe"
field = "Astrophysics"
institution = "University of Pretoria"
research_title = "Simulating Synthetic Data for Rare Radio Galaxies for SKA precursors"
project_description = "In the past few years MeerKAT and ASKAP have significantly changed our view of the radio sky at meter-wavelengths. Sensitive observations from these telescopes have challenged our views of traditional radio source populations and revealed new kinds of radio sources. This paradigm shift is expected to continue with the upcoming MeerKAT extension and LOFAR 2.0 facilities, which will produce an enormous amount of radio data. To deal with this flood of data and the complexity of sources we need new strategies which optimize science extraction and minimize manual effort by astronomers. To capture the underlying astrophysics of sources with complicated and rare morphologies as well as create realistic test data on which automated data analysis strategies can be tested, we need realistic synthetic image-plane data for SKA precursor facilities. The aim of this project is to use existing source models of rare radio galaxies provided by cutting-edge MHD simulations to produce realistic synthetic data for a variety of MeerKAT array configurations and observation parameters like frequency and declination. In the process we expect the student to learn about practical know-how of radio data management and assessment and the astrophysical processes giving rise to rare radio galaxies."
previous_research = "Identifying interesting AGN in DINGO continuum images"
# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f" Current research title: {research_title}")
st.write(" Current research description:")
st.write(f"{project_description}")
st.write(f"Previous research title {previous_research}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload your publications", type="None")

#if uploaded_file:
#    publications = pd.read_csv(uploaded_file)
#    st.dataframe(publications)

    # Add filtering for year or keyword
#    keyword = st.text_input("Filter by keyword", "")
#    if keyword:
#        filtered = publications[
#            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
#        ]
#        st.write(f"Filtered Results for '{keyword}':")
 #       st.dataframe(filtered)
 #   else:
  #      st.write("Showing all publications")

# Add a section for visualizing publication trends
#st.header("Publication Trends")
#if uploaded_file:
#    if "Year" in publications.columns:
#        year_counts = publications["Year"].value_counts().sort_index()
#        st.bar_chart(year_counts)
#    else:
#        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "u20450495@tuks.co.za"
st.write(f"You can reach {name} at {email}.")