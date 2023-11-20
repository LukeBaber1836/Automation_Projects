import streamlit as st
import pandas

# Access online at: https://lukebaber-test-app.streamlit.app/

#Through a graph on streamlit
data = {
    'Series_1':[1,3,4,5,7],
    'Series_2':[10,30,40,100,250]
}
df = pandas.DataFrame(data)

st.title("My first project")
st.subheader("Automating things with Python!")
st.write('''This is my first app.
Enjoy it!
''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

my_slider = st.slider('Celsius')
st.write(my_slider, 'in Fahrenheit is', my_slider * 9/5 + 32)