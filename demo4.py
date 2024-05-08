import streamlit as st
st.header('Trà Sữa CoTAI')
col1, col2 = st.columns(2)
with col1:

    st.image('https://imgur.com/lEpdPsT.png')
    
with col2:
    size = st.radio('Kích cỡ',('Nhỏ (30k)','Vừa (40k)','Lớn (50k)'), horizontal=True)
    st.caption('Thêm')
    c1,c2 = st.columns(2)
    with c1:
        sua = st.checkbox('Sữa (5k)')
        caphe = st.checkbox('Cà phê (8k)')
    with c2:
        kem = st.checkbox('Kem (10k)')
        trung = st.checkbox('Trứng (15k)')
col3, col4 = st.columns(2)
with col3:
    topping_price = 5,5,6,7,8,10
    topping_list = ['Trân châu trắng (5k)','Trân châu đen (5k)','Thạch rau câu (6k)','Vải (7k)','Nhãn (8k)','Đào (10k)']
    topping = st.multiselect('Topping', topping_list )
with col4:  
    soluong = st.number_input('Số lượng',step=1)
ghichu = st.text_area('Ghi chú')

if st.button('Đặt hàng', use_container_width=True):
    price = 0
    if size == 'Lớn (50k)':
        co = 'Cỡ lớn'
        price = 50
    elif size == 'Nhỏ (30k)':
        co = 'Cỡ nhỏ'
        price = 30
    else:
        co = 'Cỡ vừa'
        price = 40
    add = []
    if sua == True:
        add.append('Sữa')
        giasua = 5
    if caphe == True:
        add.append('Cà phê')
    if kem == True:
        add.append('Kem')
    if trung == True:
        add.append('Trứng')
    add1 = str(add)
    dau = '''[']'''
    for ele in add1:
        if ele in dau:
            add1 = add1.replace(ele,'')
    topping1 = str(topping)
    for ele in topping1:
        if ele in dau:
            topping1 = topping1.replace(ele,'')
    topping_money = 0

    for i in  range(len(topping_list)):
        if topping_list[i] in topping:
            topping_money += topping_price[i]
    money = soluong * (price + sua*5 + caphe*8 + kem*10 + trung*15 + topping_money)
    st.success(f'''{co}  
Thêm: {add1}  
Topping: {topping1}   
{ghichu}  
Số lượng: {soluong}  
Thành tiền: {money}K''')