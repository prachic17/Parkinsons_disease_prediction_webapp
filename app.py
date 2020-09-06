# -*- coding: utf-8 -*-
import streamlit as st
import pickle
import numpy as np
pks= pickle.load(open('model.pkl','rb'))


def predict_disease(*args):
    input=np.array([args]).astype(np.float64)
    prediction=pks.predict(input)
    
    return int(prediction)

def main():
    st.title("Are You Suffering from Parkinsons Disease?")
    html_temp="""
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Check Out Now! </h2>
    </div>
    """    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    a = st.text_input("MDVP:Fo(Hz)","Type Here")
    b = st.text_input("MDVP:Fhi(Hz)","Type Here")
    c = st.text_input("MDVP:Flo(Hz)","Type Here")
    d = st.text_input("MDVP:Jitter(%)","Type Here")
    e = st.text_input("MDVP:Jitter(Abs)","Type Here")
    f = st.text_input("MDVP:RAP","Type Here")
    g = st.text_input("MDVP:PPQ","Type Here")
    h = st.text_input("Jitter:DDP","Type Here")
    i = st.text_input("MDVP:Shimmer","Type Here")
    j = st.text_input("MDVP:Shimmer(dB)","Type Here")
    k = st.text_input("Shimmer:APQ3","Type Here")
    l = st.text_input("Shimmer:APQ5","Type Here")
    m = st.text_input("MDVP:APQ","Type Here")
    n = st.text_input("Shimmer:DDA","Type Here")
    o = st.text_input("NHR","Type Here")
    p = st.text_input("HNR","Type Here")
    q = st.text_input("RPDE","Type Here")
    r = st.text_input("DFA","Type Here")
    s = st.text_input("spread1","Type Here")
    t = st.text_input("spread2","Type Here")
    u = st.text_input("D2","Type Here")
    v = st.text_input("PPE","Type Here")
          
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;">Relax! You are not suffering from Parkinsons Disease! </h2>
       </div>
    """
    
    
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;">You are suffering from Parkinsons Disease!! Consult the doctor soon!</h2>
       </div>
    """
    
    if st.button("Predict"):
        output=predict_disease(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v)
        st.success('The probability of suffering is {}'.format(output))
        
        
        if output == 0:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
     
            
if __name__=='__main__':
   main()
        
    