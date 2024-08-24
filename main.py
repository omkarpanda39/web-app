import streamlit as st
import pandas as pd 

st.title("This is a sample code ")
st.header("Header")
st.subheader("Sub Heading")
st.caption("This is a caption")

arr = pd.DataFrame({
    'one':[1,2,3,4],
    'two':[6,7,8,9]
})
st.write(arr)

st.metric(label="Temperature",value="31 ° C",delta="1.2 ° C")
st.metric(label="Population",value="123 Billions",delta="1 Million")
st.bar_chart(arr)
st.line_chart(arr)
st.area_chart(arr)