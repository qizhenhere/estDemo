import numpy as np
import pandas as pd
import pickle
import streamlit as st

#导入模型
model_st = pickle.load(open('D:\\edu\\app_streamlit\\gs_xgb2.pkl', 'rb'))

st.title('智能评价系统')

st.subheader('下载Excel模板')
with open('D:\\edu\\app_streamlit\\模板.xlsx', 'rb') as file:
    btn = st.download_button(label='下载', data=file, file_name='模板.xlsx')

st.subheader('上传Excel数据')
uploaded_file = st.file_uploader(label='')

#数据处理
def predict_b(uploaded_file='sj.xlsx'):
    data=pd.read_excel(uploaded_file)
    prediction = model_st.predict(data)
    return prediction

#评价
def main():
    result = ""
    if st.button('评价'):
        try:
            result = predict_b(uploaded_file=uploaded_file)
        except:
            return
    st.success('评价结果:{}'.format(result))
    st.write("1:达标，2：合格，3：相对薄弱")

if __name__ == '__main__':
    main()