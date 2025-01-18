import streamlit as st

with st.expander('Cat'):
    st.write('Meow' + ' meow'*1000)

css='''
<style>
    [data-testid="stExpander"] div:has(>.streamlit-expanderContent) {
        overflow: scroll;
        height: 400px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)



