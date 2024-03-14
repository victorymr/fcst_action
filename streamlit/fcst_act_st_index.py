import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

from fcst_action import core

st.set_page_config(
    page_title="Fcst_act",
    page_icon="👋",
)

st.write("# Run Ad Campaign Based on Forecast")

st.sidebar.success("This is a quick demo")

## Read the campaign detals data - in future user can enter details?
company_df, campaigns_df = get_campaign_details()

## Drop downs to select company and lead time
companies = list(company_df['Company'])
company_sel = st.select(companies)
lead_days = st.slider('Forecast Lead',min_value=1,max_value=10,value=3)

if not company_sel:
    st.error("Please select a company")
else:
    @st.cache_data
    city_res_df, city_locations = get_campaign_hist(company_df, campaigns_df, company_sel = company_sel,lead_days)

    campaign_heatmap(city_res_df)
    st.pyplot(plt)

    map_campaigns_by_day(city_res_df,city_locations)
    
    duration_per_ad_per_city,percentage_per_ad_per_city = get_campaign_summary(city_res_df)

## Query the DB and export the data

## Show summary stats

## Show plots
