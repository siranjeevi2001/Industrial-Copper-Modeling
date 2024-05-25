import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('trained_model.pkl')



def option_exract(option):
    
    df = pd.read_csv('Copper_Set.csv')
    df1 = pd.read_csv('cleandata.csv')
    
    test = df[option].value_counts()
    # Convert to DataFrame
    test = test.reset_index()
    test.columns = [option, 'count']



    en_code = df1[option].value_counts()
    en_code = en_code.reset_index()
    en_code.columns = [option, 'count']


    # Create a dictionary from the two lists
    status_dict = {j: i for i, j in zip(en_code[option], test[option])}

    return status_dict
# Print the resulting dictionary

col1, col2 = st.columns([5,5])

with col1:
    # pass
    # Streamlit app
    st.title("Selling Price Prediction")

    st.write("Please input the details for the Status prediction:")

    # Get user input for the sample data
    quantity_tons = st.number_input('Quantity (tons)', min_value=0.0, value=13.0)
    thickness = st.number_input('Thickness', min_value=0.0, value=5.0)
    width = st.number_input('Width', min_value=0, value=1500)


    product_ref_option = option_exract('product_ref')
    selected_option_pr = st.selectbox("choose a product_ref Code:", list(product_ref_option.keys()))
    product_ref = product_ref_option[selected_option_pr]

    # product_ref = st.number_input('Product Reference', min_value=0, value=2)

    customer = st.number_input('Enter Customer Code', min_value=0, value=84)

    country_option = option_exract('country')
    selected_option_cc = st.selectbox("choose a country code:", list(country_option.keys()))
    country = country_option[selected_option_cc]

    # country = st.number_input('Country', min_value=0, value=10)


    status_option= option_exract('status')
    # Create a dropdown with the text  status_option
    selected_option_ss = st.selectbox("Choose an Status:", list( status_option.keys()))

    # Get the numeric value corresponding to the selected option
    status =  status_option[selected_option_ss]
    # status = st.number_input('Status', min_value=0, value=7)


    item_option = option_exract('item type')
    selected_option_it = st.selectbox("Choose an Item type:", list( item_option.keys()),index=2)
    item_type = item_option[selected_option_it]



    application_option = option_exract('application')
    selected_option_a = st.selectbox("Choose an Application Code:", list( application_option.keys()),index=2)
    application = application_option[selected_option_a]

    # application = st.number_input('Application', min_value=0, value=17)


    item_year = st.number_input('Item order Year', min_value=2020, max_value=2100, value=2021)
    item_month = st.number_input('Item order Month', min_value=1, max_value=12, value=9)
    item_day = st.number_input('Item order Day', min_value=1, max_value=31, value=14)

    # Create a sample input data for testing based on user input
    sample_data = {
        'quantity tons': [quantity_tons],
        'thickness': [thickness],
        'width': [width],
        'product_ref': [product_ref],
        'customer': [customer],
        'country': [country],
        'status': [status],  
        'item type': [item_type],
        'application': [application],
        'item_year': [item_year],
        'item_month': [item_month],
        'item_day': [item_day]
    }

    sample_df = pd.DataFrame(sample_data)

    # Apply the same preprocessing steps to the sample data
    # (e.g., encoding, scaling, etc.)

    # Predict the selling price using the sample data
    prediction = model.predict(sample_df)


    st.write("Sample Data:")
    st.write(sample_df)

    st.write(f"The predicted selling price is: {prediction[0]}")


with col2:
    st.title("Selling copper status Predication")

    st.write("Please input the details for the prediction:")

    # Get user input for the sample data
    quantity_tons = st.number_input('Quantity(tons)', min_value=0.0, value=8.71)
    thickness = st.number_input('Thickness copper', min_value=0.0, value=1.0)
    width = st.number_input('Width copper', min_value=0, value=1500)
    selling = st.number_input('selling price', min_value=0, value=1253)


    product_ref_option = option_exract('product_ref')
    selected_option_pr = st.selectbox("choose a product_ref Code", list(product_ref_option.keys()))
    product_ref = product_ref_option[selected_option_pr]

    # product_ref = st.number_input('Product Reference', min_value=0, value=2)
    customer_option = option_exract('customer')

    selected_option_pr = st.selectbox("customer Code", list(customer_option.keys()))
    customer = customer_option[selected_option_pr]

    # customer = st.number_input('Customer Code', min_value=0, value=78)

    country_option = option_exract('country')
    selected_option_cc = st.selectbox("country code:", list(country_option.keys()))
    country = country_option[selected_option_cc]

    # country = st.number_input('Country', min_value=0, value=10)


    item_option = option_exract('item type')
    selected_option_it = st.selectbox("Item type:", list( item_option.keys()),index=2)
    item_type = item_option[selected_option_it]



    application_option = option_exract('application')
    selected_option_a = st.selectbox("Application Code:", list( application_option.keys()),index=2)
    application = application_option[selected_option_a]

    # application = st.number_input('Application', min_value=0, value=17)


    item_year = st.number_input('Item order year', min_value=2020, max_value=2100, value=2021)
    item_month = st.number_input('Item order month', min_value=1, max_value=12, value=4)
    item_day = st.number_input('Item order day', min_value=1, max_value=31, value=1)
    
    delivery_year = st.number_input('delivery order Year', min_value=2020, max_value=2100, value=2021)
    delivery_month = st.number_input('delivery order Month', min_value=1, max_value=12, value=7)
    delivery_day = st.number_input('delivery order Day', min_value=1, max_value=31, value=1)

    # Create a sample input data for testing based on user input
    status_data = {
        'quantity tons': [quantity_tons],
        'thickness': [thickness],
        'width': [width],
        'selling_price': [selling],
        'product_ref': [product_ref],
        'customer': [customer],
        'country': [country],
        'item type': [item_type],
        'application': [application],
        'item_year': [item_year],
        'item_month': [item_month],
        'item_day': [item_day],
        'delivery year': [delivery_year],
        'delivery month': [delivery_month],
        'delivery day': [delivery_day]
    }

    status_df = pd.DataFrame(status_data)

    # Apply the same preprocessing steps to the sample data
    # (e.g., encoding, scaling, etc.)
    import pickle

    # Load the model from file
    with open('xgboost_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    # Predict the selling price using the sample data
    prediction = loaded_model.predict(status_df)

    result = {7: 'Won',
                1: 'Lost',
                2: 'Not lost for AM',
                5: 'Revised',
                6: 'To be approved',
                0: 'Draft',
                4: 'Offered',
                3: 'Offerable',
                9: 'Wonderful'}
   
    

    st.write("Status Data:")
    st.write(status_df)

    st.write(f"The predicted selling price is: {result[prediction[0]]}")
