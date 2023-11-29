
import joblib
import streamlit as st
import pandas as pd
import sklearn

Model= joblib.load("PF_Model_Final.pkl")
Inputs= joblib.load("PF_Inputs_Final.pkl")

def Haz(Hazard):
    if Hazard == 'Light':
        return int(0)
    elif Hazard == 'Ordinary 1':
        return int(1)
    elif Hazard == 'Ordinary 2':
        return int(2)
    elif Hazard == 'Extra 1':
        return int(3)
    elif Hazard == 'Extra 2':
        return int(4)

def FHC(Hose_Cabinet):
    if Hose_Cabinet == 'No FHC':
        return int(0)
    elif Hose_Cabinet == 'inside 1':
        return int(1)
    elif Hose_Cabinet == 'inside >1':
        return int(2)
    elif Hose_Cabinet == 'Only Outside':
        return int(3)
    elif Hose_Cabinet == 'inside_and_outside':
        return int(4)   

def prediction(Hazard, Building_Height, Pipe_Length,
       D_For_Longest_Pipe, Sprinkler_Orientaion, Sprinkler_k_factor,
       Hose_Cabinet, System_Type):
    hazard=Haz(Hazard)
    fhc=FHC(Hose_Cabinet)
    test_df=pd.DataFrame(columns=Inputs)
    test_df.at[0,'Hazard']= hazard
    test_df.at[0,'Building Height (m)']= Building_Height
    test_df.at[0,'Pipe Length (m)']= Pipe_Length
    test_df.at[0,'D For Longest Pipe (in)']= D_For_Longest_Pipe
    test_df.at[0,'Sprinkler Orientaion']=  Sprinkler_Orientaion
    test_df.at[0,'Sprinkler k-factor']= Sprinkler_k_factor
    test_df.at[0,'Hose Cabinet']= fhc
    test_df.at[0,'System Type']= System_Type
    test_df.drop('System Type',axis=1,inplace=True)
    result= Model.predict(test_df)
    return result[0]

def main():
    
    ## Setting up the page title
    st.set_page_config(page_title= 'Fire Fighting Pump Flow Prediction')
    
     # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center;text-decoration: underline;color:GoldenRod'>Fire Fighting Pump Flow Prediction</h1>", unsafe_allow_html=True)
    
    Hazard=st.selectbox('Insert Hazard',  ['Light', 'Ordinary 1', 'Ordinary 2', 'Extra 1', 'Extra 2'])
    
    Building_Height=st.number_input('Insert Building Height (m)',min_value=2, max_value=120, value=30,step=5)
    
    Pipe_Length=st.number_input('Insert Pipe Length (m)',min_value=2, max_value=200, value=80,step=10)
    
    D_For_Longest_Pipe=st.slider('Choose D For Longest Pipe (in)', min_value=2, max_value=10, value=4,step=1)

    Sprinkler_Orientaion=st.radio('Sprinkler Orientaion', ['Pendent', 'Upright','SideWall'])
    
    Sprinkler_k_factor=st.selectbox('Select Sprinkler k-factor', [5.6,8,11.2,14,16.8,19.6,22.4])
    
    Hose_Cabinet =st.selectbox('Select FHC', ['No FHC', 'inside 1', 'inside >1', 'Only Outside', 'inside_and_outside'])
    
    System_Type=st.radio('Select System Type', ['Wet'])
    
   
    
    if st.button('predict'):
        results= prediction(Hazard, Building_Height, Pipe_Length,
                            D_For_Longest_Pipe, Sprinkler_Orientaion, Sprinkler_k_factor,Hose_Cabinet, System_Type)
        st.text(f"The Pump Flow is {int(results)} GPM")
    
if __name__ == '__main__':
    main()
