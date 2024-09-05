import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
from PIL import Image

st.set_page_config(
    page_title="Airbnb Analysis And Visualization |Sai Gaythri A",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded")

df= pd.read_csv("C:/Users/deepakgayu/OneDrive/Desktop/capstone project/Airbnb.csv")

with st.sidebar:

    options = ["Home", "Explore Stays","Geospatial View"]
    selected_option = option_menu("Option Menu", options)

if selected_option =="Home":
    st.title("Airbnb Analysis And Visualization")
    img=Image.open("C:/Users/deepakgayu/OneDrive/Desktop/capstone project/image-home.png")
    st.image(img)

    st.header('About Airbnb')
    st.write('''***Airbnb is an American company operating an online marketplace
                for short- and long-term homestays and experiences.
                The company acts as a broker and charges a commission from each booking.
                The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia.
                Airbnb is a shortened version of its original name, AirBedandBreakfast.com.***''')

    st.subheader('Airbnb services')
    st.write('''***Airbnb serves as a transformative platform that connects travelers
                    with a diverse array of accommodation options worldwide, beyond traditional hotels.
                    For guests, Airbnb offers the opportunity to discover unique stays such as entire homes,
                    private rooms, and unconventional lodgings like treehouses or castles. 
                    This variety allows travelers to tailor their accommodations to specific preferences,
                    whether seeking a local experience, privacy, or budget-friendly options.
                    Guests benefit from the flexibility to book short-term stays, extended vacations, or 
                    last-minute getaways, often at competitive prices compared to traditional lodging.***''')

elif selected_option =="Explore Stays":
    tab1,tab2,tab3,tab4=st.tabs(["BY PRICE","BY AVALIABILITY","BY LOCATION","BY CORRELATION ANALYSIS"])
    with tab1:
        st.title("**BY PRICE**")

        col1,col2=st.columns(2)

        with col1:

            country_1= st.selectbox("Select the country",(df["country"].unique()))

            # Filter df based on selected country
            dfa=df[df["country"] == country_1]
            dfa.reset_index(drop=True, inplace=True)

            room_list= st.selectbox("Select the room type",(dfa["room_type"].unique()))

            dfb=dfa[dfa["room_type"] == room_list]
            dfb.reset_index(drop=True, inplace=True)

            room_list_aggregated= pd.DataFrame(dfb.groupby("property_type")[["price","review_scores_accuracy","number_of_reviews","review_scores_rating"]].sum())
            room_list_aggregated.reset_index(inplace= True)
            
            fig_bar=px.bar(room_list_aggregated, x="property_type", y="price", title="PRICE DIFFERENCE FOR ROOM TYPE",
                        hover_data=["review_scores_accuracy","number_of_reviews","review_scores_rating"],color_discrete_sequence=px.colors.sequential.Blues)
            st.plotly_chart(fig_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")  

            property_list= st.selectbox("Select the property type",(dfb["property_type"].unique()))

            dfc=dfb[dfb["property_type"] == property_list]
            dfc.reset_index(drop=True, inplace=True)

            property_list_aggregated = pd.DataFrame(dfc.groupby("host_response_time")[["price","bedrooms","beds"]].sum())
            property_list_aggregated.reset_index(inplace= True)

            fig_pie= px.pie(property_list_aggregated, names= "host_response_time", values="price",
                            hover_data=["bedrooms","beds"],
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600)
            st.plotly_chart(fig_pie)
        
        col1,col2=st.columns(2)
        
        with col1:
                
            host_response_time= st.selectbox("Select the host_response_time",dfc["host_response_time"].unique())

            dfd=dfc[dfc["host_response_time"] == host_response_time]
            dfd.reset_index(drop=True, inplace=True)

            host_response_time_agg= pd.DataFrame(dfd.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            host_response_time_agg.reset_index(inplace= True)

            fig_bar_1= px.bar(host_response_time_agg, x="bed_type", y=["minimum_nights", "maximum_nights"], 
                            title="MINIMUM NIGHTS AND MAXIMUM NIGHTS",hover_data="price",barmode='group',
                            color_discrete_sequence=px.colors.diverging.PuOr, width=600, height=500)

            st.plotly_chart(fig_bar_1)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("") 

            host_response_time_agg= pd.DataFrame(dfd.groupby("bed_type")[["price","beds","bedrooms","accommodates"]].sum())
            host_response_time_agg.reset_index(inplace= True)

            fig_bar_2= px.bar(host_response_time_agg, x='bed_type', y=["beds","bedrooms","accommodates"], 
                            title="BEDS BEDROOMS AND ACCOMADATES",hover_data="price",barmode='group',
                            color_discrete_sequence=px.colors.diverging.Spectral, width=600, height=500)

            st.plotly_chart(fig_bar_2)
        
    with tab2:
        df_1= pd.read_csv("C:/Users/deepakgayu/OneDrive/Desktop/capstone project/Airbnb.csv")

        st.title("**BY AVALIABILITY**")

        col1,col2=st.columns(2)

        with col1:                  
            country_aa= st.selectbox("Select the country_aa",(df_1["country"].unique()))

            # Filter df based on selected country
            df_1_c=df[df["country"] == country_aa]
            df_1_c.reset_index(drop=True, inplace=True)

            property_list_avail= st.selectbox("Select the property_ty_avail",(df_1_c["property_type"].unique()))

            df2_p=df_1_c[df_1_c["property_type"] == property_list_avail]
            df2_p.reset_index(drop=True, inplace=True)

            fig_sunburst_1=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_30", 
                                    title="AVAILABILITY 30",color_discrete_sequence=px.colors.sequential.Cividis, width=600, height=500)
            
            st.plotly_chart(fig_sunburst_1)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("") 
            st.write("")
            st.write("")
            st.write("")    
            st.write("")
            st.write("")  

            fig_sunburst_2=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_60", 
                                        title="AVAILABILITY 60",color_discrete_sequence=px.colors.sequential.Purples, width=600, height=500)
                
            st.plotly_chart(fig_sunburst_2)

        col1,col2=st.columns(2)
        with col1:
            fig_sunburst_3=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_90", 
                                        title="AVAILABILITY 90",color_discrete_sequence=px.colors.sequential.Oranges, width=600, height=500)
                
            st.plotly_chart(fig_sunburst_3)
        
        with col2:
            fig_sunburst_4=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_365", 
                                        title="AVAILABILITY 365",color_discrete_sequence=px.colors.sequential.Reds, width=600, height=500)
                
            st.plotly_chart(fig_sunburst_4)  


       
        room_ty_aa= st.selectbox("Select the room_ty_aa",(dfa["room_type"].unique()))

        df3_r=dfa[dfa["room_type"] == room_ty_aa]
        df3_r.reset_index(drop=True, inplace=True)

        room_type_agg= pd.DataFrame(df3_r.groupby("host_response_time")[["price","availability_30","availability_60","availability_90","availability_365"]].sum())
        room_type_agg.reset_index(inplace= True)

        fig_bar_aa= px.bar(room_type_agg, x="host_response_time", y=["availability_30","availability_60","availability_90","availability_365"], 
                                title="AVAILABILITY BASED ON HOST RESPONSE TIME",hover_data="price",
                                color_discrete_sequence=px.colors.diverging.RdBu,width=600,height=600)

        st.plotly_chart(fig_bar_aa)

    with tab3:
        df_l= pd.read_csv("C:/Users/deepakgayu/OneDrive/Desktop/capstone project/Airbnb.csv")

        st.title("**BY LOCATION**")

        country_ac= st.selectbox("Select the country_ac",(df_l["country"].unique()))

            # Filter df based on selected country
        df_l_c=df[df["country"] == country_ac]
        df_l_c.reset_index(drop=True, inplace=True)

        property_ty_ac= st.selectbox("Select the property_ty_ac",(df_l_c["property_type"].unique()))

        df_l_p=df_1_c[df_1_c["property_type"] == property_ty_ac]
        df_l_p.reset_index(drop=True, inplace=True)

        accommodates_agg= pd.DataFrame(df_l_p.groupby("accommodates")[["bedrooms","beds","cleaning_fee","extra_people","guests_included","security_deposit"]].sum())
        accommodates_agg.reset_index(inplace= True)

        fig_bar_ac= px.bar(accommodates_agg,x="accommodates", y=["bedrooms","beds","extra_people","guests_included","security_deposit"], 
                            title="Accommodates",hover_data="cleaning_fee",
                            color_discrete_sequence=px.colors.sequential.Electric)
        
        st.plotly_chart(fig_bar_ac)

        fig_bar_2= px.bar(host_response_time_agg, x='bed_type', y=["beds","bedrooms","accommodates"], 
                                            title="BEDS BEDROOMS AND ACCOMADATES",hover_data="price",barmode='group',
                                            color_discrete_sequence=px.colors.diverging.RdYlBu, width=600, height=500)

        st.plotly_chart(fig_bar_2)

    with tab4:
            

            st.title("**BY CORRELATION ANALYSIS**")

        
            st.write("")
            st.write("")
            st.write("")

            #correlation map
            corr_df = df[["price","availability_365","minimum_nights","maximum_nights",
                        "number_of_reviews","review_scores_rating"]]
            
            #df["price"] = pd.to_numeric(df["price"], errors='coerce')
            correlation_matrix = corr_df.corr()
            
            # Create a heatmap using Seaborn
            plt.figure(figsize=(12, 8))
            sns.heatmap(correlation_matrix, annot=True)

            # Display the heatmap with Streamlit
            st.pyplot(plt)

elif selected_option =="Geospatial View":

        st.subheader("**Geospatial View**")

        df_lati= pd.read_csv("C:/Users/deepakgayu/OneDrive/Desktop/capstone project/Airbnb.csv")

        fig_scatter_geo = px.scatter_geo(df_lati,
        lat="latitude",  # specify the column for latitude
        lon="longitude", # specify the column for longitude
        color="country",  
        hover_name="country",  # column added to hover information
        size="accommodates",  # size of markers
        projection="natural earth")

        st.plotly_chart(fig_scatter_geo)