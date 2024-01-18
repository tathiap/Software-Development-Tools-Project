import os
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

csv_file_path = os.path.abspath('vehicles_us.csv')
df = pd.read_csv(csv_file_path)

st.header("US Vehicles")
st.write('Explore the current listings of US Vehicles below and get the right car for you') # setting the tone for users to explore the dataset of US Vehicle's car listings 

type_choice = df['type'].unique()
options_menu = st.selectbox('Select the type of car', type_choice)

# df_filter = df[df.type==type_choice]

# min_price, max_price = int(df['price'].min()), int(df['price'].max())
# price_range = st.slider("Price Range",value=(min_price, max_price), min_value=min_price, max_value=max_price)
# actual_pricerange = list(range(price_range[0], price_range[1]+1))

# df_filter = df [(df.type==options_menu) & (df.price.isin(list(actual_pricerange)))]

# st.header("Price Analysis")
# st.write("""
#          ###### Let's examine the factors that have the most significant impact on the price. We will explore how the distribution of prices varies based on factors such as transmission type, make & model of the car, and condition of the car.
#          """)

# list_priceanalysis = ['transmission', 'model', 'condition']
# options_dropdown = st.selectbox('Select the type of car',list_priceanalysis)

# fig1 = px.histogram(df, x="price", color=options_dropdown)
# fig1.update_layout(title= "<b> Select Price By{}</b>".format(options_dropdown))
# st.plotly_chart(fig1)

# st.write("""
#          ###### Let's investigate how the price is influenced by odometer readings, the number of cylinders, and the presence of 4-wheel drive.
#          """)


# use_is_4wd_category = st.checkbox("Use is_4wd Category to see if 4 Wheel Drive is avaliable")

# if use_is_4wd_category:
#     def is_4wd_category(x):
#         if x == 1:
#             return '4WD'
#         else:
#             return 'Non-4WD'

#     df['is_4wd_category'] = df['is_4wd'].apply(is_4wd_category)
#     color_column = 'is_4wd_category'
# else:
#     color_column = None


# list_priceengineanalysis = ['odometer', 'cylinders']
# scatter_choice = st.selectbox("Price dependency on", list_priceengineanalysis)

# fig2 = px.scatter(df, x="price", y=scatter_choice, color=color_column, hover_data=['cylinders'])
# fig2.update_layout(title="<b>Price vs {}</b>".format(scatter_choice))
# st.plotly_chart(fig2)