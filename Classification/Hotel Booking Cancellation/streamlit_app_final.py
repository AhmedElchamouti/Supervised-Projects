
import joblib
import streamlit as st
import category_encoders
import pandas as pd
import sklearn

Model= joblib.load("Model_Final.pkl")
Inputs= joblib.load("Inputs_Final.pkl")

def prediction(hotel,lead_time, arrival_date_year,
       arrival_date_month, arrival_date_week_number,
       arrival_date_day_of_month, stays_in_weekend_nights,
       stays_in_week_nights, adults, children, babies, meal,
       country, market_segment, distribution_channel,
       is_repeated_guest, previous_cancellations,
       previous_bookings_not_canceled, reserved_room_type,
       assigned_room_type,booking_changes, deposit_type, agent,
       days_in_waiting_list, customer_type, adr,
       required_car_parking_spaces,total_of_special_requests):
    test_df=pd.DataFrame(columns=Inputs)
    test_df.loc[0,'hotel']= hotel
    test_df.loc[0,'lead_time']= lead_time
    test_df.loc[0,'arrival_date_year']= arrival_date_year
    test_df.loc[0,'arrival_date_month']= arrival_date_month
    test_df.loc[0,'arrival_date_week_number']= arrival_date_week_number
    test_df.loc[0,'arrival_date_day_of_month']= arrival_date_day_of_month
    test_df.loc[0,'stays_in_weekend_nights']= stays_in_weekend_nights
    test_df.loc[0,'stays_in_week_nights']= stays_in_week_nights
    test_df.loc[0,'adults']= adults
    test_df.loc[0,'children']= children
    test_df.loc[0,'babies']= babies
    test_df.loc[0,'meal']= meal
    test_df.loc[0,'country']= country
    test_df.loc[0,'market_segment']= market_segment
    test_df.loc[0,'distribution_channel']= distribution_channel
    test_df.loc[0,'is_repeated_guest']= is_repeated_guest
    test_df.loc[0,'previous_cancellations']= previous_cancellations
    test_df.loc[0,'previous_bookings_not_canceled']= previous_bookings_not_canceled
    test_df.loc[0,'reserved_room_type']= reserved_room_type
    test_df.loc[0,'assigned_room_type']= assigned_room_type
    test_df.loc[0,'booking_changes']= booking_changes
    test_df.loc[0,'deposit_type']= deposit_type
    test_df.loc[0,'agent']= agent
    test_df.loc[0,'days_in_waiting_list']= days_in_waiting_list
    test_df.loc[0,'customer_type']= customer_type
    test_df.loc[0,'adr']= adr
    test_df.loc[0,'required_car_parking_spaces']= required_car_parking_spaces
    test_df.loc[0,'total_of_special_requests']= total_of_special_requests
    
    result= Model.predict(test_df)
    if result[0]== 0 :
        return st.text("This Customer won't cancel the booking")
    else:
         return st.text("This Customer will cancel the booking") 

def main():
    
    ## Setting up the page title and icon
    st.set_page_config(page_title= 'Hotel booking demand')
    
     # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center;text-decoration: underline;color:GoldenRod'>Cancelation Prediction</h1>", unsafe_allow_html=True)

    hotel=st.radio('Hotel Type', ['Resort Hotel', 'City Hotel'])
    
    lead_time=st.number_input('Insert Lead Time', min_value=0, max_value=600, value=200,step=10)
    
    arrival_date_year=st.slider('Choose the Year', min_value=2015, max_value=2023, value=2019 ,step=1)

    arrival_date_month=st.selectbox('Choose Month', ['January','February' ,'March' ,'April', 'May' ,'June','July' 
                                            ,'August', 'September', 'October', 'November' ,'December' ])
    
    arrival_date_week_number=st.slider('Choose Number of the week in the year', min_value=1, max_value=53, value=33 ,step=1)
    
    arrival_date_day_of_month=st.slider('Choose Number of the day in the month', min_value=1, max_value=31, value=15 ,step=1)
    
    stays_in_weekend_nights=st.slider('How many times stayed in weekend nights', min_value=0, max_value=30, value=15 ,step=1)
    
    stays_in_week_nights=st.slider('How many times stayed in week nights', min_value=0, max_value=50, value=20 ,step=1)
    
    adults=st.slider('How many adults', min_value=0, max_value=50, value=20 ,step=1)
    
    children=st.slider('How many children', min_value=0, max_value=15, value=10 ,step=1)

    babies=st.slider('How many babies', min_value=0, max_value=10, value=5 ,step=1)

    meal=st.selectbox('Choose Meal : 1 is no package , 2 is BB , 3 is HB , 4 is FB', ['1','2' ,'3' ,'4'])
    
    country=st.selectbox('Choose Country', ['PRT' ,'GBR', 'USA', 'ESP', 'IRL', 'FRA', 'ROU', 'NOR', 'OMN', 'ARG', 'POL', 'DEU',
 'BEL', 'CHE', 'CN' ,'GRC', 'ITA', 'NLD', 'DNK', 'RUS', 'SWE', 'AUS', 'EST', 'CZE',
 'BRA' ,'FIN' ,'MOZ' ,'BWA' ,'LUX' ,'SVN' ,'ALB' ,'IND' ,'CHN' ,'MEX' ,'MAR' ,'UKR',
 'SMR' ,'LVA' ,'PRI' ,'SRB' ,'CHL' ,'AUT' ,'BLR' ,'LTU' ,'TUR' ,'ZAF' ,'AGO' ,'ISR',
 'CYM' ,'ZMB' ,'CPV' ,'ZWE' ,'DZA' ,'KOR' ,'CRI' ,'HUN' ,'ARE' ,'TUN' ,'JAM' ,'HRV',
 'HKG' ,'IRN' ,'GEO' ,'AND' ,'GIB' ,'URY' ,'JEY' ,'CAF' ,'CYP' ,'COL' ,'GGY' ,'KWT',
 'NGA' ,'MDV' ,'VEN' ,'SVK' ,'FJI' ,'KAZ' ,'PAK' ,'IDN' ,'LBN' ,'PHL' ,'SEN' ,'SYC',
 'AZE' ,'BHR' ,'NZL' ,'THA' ,'DOM' ,'MKD' ,'MYS' ,'ARM' ,'JPN' ,'LKA' ,'CUB' ,'CMR',
 'BIH' ,'MUS' ,'COM' ,'SUR' ,'UGA' ,'BGR' ,'CIV' ,'JOR' ,'SYR' ,'SGP' ,'BDI' ,'SAU',
 'VNM' ,'PLW' ,'QAT' ,'EGY' ,'PER' ,'MLT' ,'MWI' ,'ECU' ,'MDG' ,'ISL' ,'UZB' ,'NPL',
 'BHS' ,'MAC' ,'TGO' ,'TWN' ,'DJI' ,'STP' ,'KNA' ,'ETH' ,'IRQ' ,'HND' ,'RWA' ,'KHM',
 'MCO' ,'BGD' ,'IMN' ,'TJK' ,'NIC' ,'BEN' ,'VGB' ,'TZA' ,'GAB' ,'GHA' ,'TMP' ,'GLP',
 'KEN' ,'LIE' ,'GNB' ,'MNE' ,'UMI' ,'MYT' ,'FRO' ,'MMR' ,'PAN' ,'BFA' ,'LBY' ,'MLI',
 'NAM' ,'BOL' ,'PRY' ,'BRB' ,'ABW' ,'AIA' ,'SLV' ,'DMA' ,'PYF' ,'GUY' ,'LCA' ,'ATA',
 'GTM' ,'ASM' ,'MRT' ,'NCL' ,'KIR' ,'SDN' ,'ATF' ,'SLE' ,'LAO'])
    market_segment=st.selectbox('Choose Market Segment', ['Direct' ,'Corporate', 'Online TA', 'Offline TA/TO' ,'Complementary' ,'Groups'
 ,'Undefined', 'Aviation'])
    
    distribution_channel=st.selectbox('Choose Distribution channel', ['Direct' ,'Corporate', 'TA/TO', 'Undefined' ,'GDS'])

    is_repeated_guest=st.radio('choose if the guest is repeated 1 and if not choose 0',['0','1'])
    
    previous_cancellations=st.number_input('Insert previous cancellations ', min_value=0, max_value=30, value=15,step=1)
    
    previous_bookings_not_canceled=st.number_input('Insert previous bookings not canceled ', min_value=0, max_value=100, value=30,step=1)
    
    reserved_room_type=st.selectbox('Choose reserved Room Type', ['A' ,'C' ,'D' ,'E' ,'G' ,'F' ,'H' ,'L' ,'P', 'B'])

    assigned_room_type=st.selectbox('Choose assigned Room Type', ['C' ,'A' ,'D' ,'E' ,'G' ,'F' ,'I' ,'B' ,'H' ,'P' ,'L' ,'K'])
    
    booking_changes=st.number_input('Insert booking changes times ', min_value=0, max_value=30, value=15,step=1)
    
    deposit_type=st.radio('Choose Deposit Type', ['No Deposit' ,'Refundable' ,'Non Refund'])
    
    agent=st.number_input('Insert ID travel agency that made the booking ', min_value=0, max_value=500, value=200,step=1)
    
    days_in_waiting_list=st.number_input('Insert  How many Waiting list days', min_value=0, max_value=300, value=200,step=1)
    
    customer_type=st.radio('Choose Customer Type',['Transient' ,'Contract' ,'Transient-Party' ,'Group'])
    
    adr=st.number_input('Insert  Average Daily Rate', min_value=0, max_value=400, value=200,step=1)
    
    required_car_parking_spaces=st.slider('How many parking spaces required', min_value=0, max_value=10, value=5 ,step=1)
    
    total_of_special_requests=st.slider('How many special requests ', min_value=0, max_value=10, value=5 ,step=1)
    
    
    
    if st.button('predict'):
        results= prediction(hotel,lead_time, arrival_date_year,
       arrival_date_month, arrival_date_week_number,
       arrival_date_day_of_month, stays_in_weekend_nights,
       stays_in_week_nights, adults, children, babies, meal,
       country, market_segment, distribution_channel,
       is_repeated_guest, previous_cancellations,
       previous_bookings_not_canceled, reserved_room_type,
       assigned_room_type,booking_changes, deposit_type, agent,
       days_in_waiting_list, customer_type, adr,
       required_car_parking_spaces,total_of_special_requests)
        

if __name__ == '__main__':
    main()
