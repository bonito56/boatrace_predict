# 必要なライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd
import requests

# タイトルとテキストを記入
st.title('ボートレース予測🚤')
st.write('レースの条件を入力して着順を予測できます。')
# race_no



# tabs = st.tabs(['レース情報','選手情報'])

with st.expander("See explanation",True):
    st.subheader('レース情報')

    st.write('#レース詳細')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        yyyymmdd = st.date_input('レース開催日')
        race_name = st.selectbox('レース名',["優勝戦","その他"])



    with col2:
        pool_code = st.selectbox('場コード',list(range(1, 25)))
        race_no = st.selectbox('レースNo',list(range(1, 13)))


    with col3:
        grade = st.selectbox('グレード',['一般・若手', '一般・女子', '一般',  'Ｇ１・女子',  'Ｇ２・女子', 'Ｇ３・女子', 'ＳＧ', 'Ｇ１',  'Ｇ２', 'Ｇ３'])
        stabilizer = st.radio("安定版",["あり", "なし"])

    st.write('#環境情報')    
    col1, col2 = st.columns(2)
    with col1:
        weather =st.selectbox('天気',['晴', '曇り', '雨'])
        temperature = st.slider('気温', 0.0, 40.0, 20.0, 0.1)
        water_tempreture = st.slider('水温', 0, 30, 15, 1)
        kiatu = st.slider('気圧', 900.0, 1100.0, 1013.0, 0.1)

    with col2:

        wind = st.selectbox('風向き',list(range(0, 17)))
        wind_speed = st.slider('風速', 0, 10, 0, 1)
        wave_height = st.slider('波高', 0.0, 40.0, 0.0, 1.0)  
        situdo = st.slider('湿度', 0.00, 100.00, 60.00, 0.1)

with st.expander("See explanation",True):
    st.subheader('枠番情報・直前情報') 


    tab_titles = ['1号艇', '2号艇', '3号艇', '4号艇', '5号艇', '6号艇']
    tabs = st.tabs(tab_titles)

    with tabs[0]:
        st.write('#枠番情報')
        col1, col2, col3 = st.columns(3)

        with col1:
            class1 =st.selectbox(
                '選手クラス①',
                ['A1', 'A2', 'B1',  'B2']
            )
        with col2:
            flying_count1 = st.selectbox(
                'フライング回数①',
                list(range(0, 4))
            )
        with col3:
            lost_count1= st.selectbox(
                '出遅れ回数①',
                list(range(0, 4))
            )

        col1, col2 = st.columns(2)
        with col1:
            st1 = st.slider('平均ST①', 0.00, 0.15, 0.30, 0.01)
            nationwide_double_rate1 = st.slider('全国二連率①', 0.00, 100.00, 50.00, 0.01)
            local_win_rate1 = st.slider('当地勝率①', 0.00, 10.00, 5.00, 0.01)
            local_triple_rate1 = st.slider('当地三連率①', 0.00, 100.00, 50.00, 0.01)
            motor_triple_rate1 = st.slider('モーター三連率①', 0.00, 100.00, 50.00, 0.01)
            adjusted_weight1 = st.slider('選手調整体重①', 0.00, 5.00, 0.00, 0.5)


        with col2:
            nationwide_win_rate1 = st.slider('全国勝率①', 0.00, 10.00, 5.00, 0.01)
            nationwide_triple_rate1 = st.slider('全国三連率①', 0.00, 100.00, 50.00, 0.01)
            local_double_rate1 = st.slider('当地二連率①', 0.00, 100.00, 50.00, 0.01)
            motor_double_rate1 = st.slider('モーター二連率①', 0.00, 100.00, 50.00, 0.01)            
            body_weight1= st.slider('選手体重①', 30.00, 70.00, 50.00, 0.1)


        st.write('#直前情報')
        col1, col2 = st.columns(2)
        with col1:
            tilt1 = st.slider('チルト①', -0.5, 3.00, 0.00, 0.5)            
            start_time1 = st.slider('スタート展示タイム①', -1.0, 1.0, 0.2, 0.01)
        with col2:       
            rehearsal_time1 = st.slider('展示タイム①', 5.00, 10.00, 7.00, 0.01)     

    with tabs[1]:
        st.write('#枠番情報')
        col1, col2, col3 = st.columns(3)

        with col1:
            class2 =st.selectbox(
                '選手クラス②',
                ['A1', 'A2', 'B1',  'B2']
            )
        with col2:
            flying_count2 = st.selectbox(
                'フライング回数②',
                list(range(0, 4))
            )
        with col3:
            lost_count2= st.selectbox(
                '出遅れ回数②',
                list(range(0, 4))
            )

        col1, col2 = st.columns(2)
        with col1:
            st2 = st.slider('平均ST②', 0.00, 0.15, 0.30, 0.01)
            nationwide_double_rate2 = st.slider('全国二連率②', 0.00, 100.00, 50.00, 0.01)
            local_win_rate2 = st.slider('当地勝率②', 0.00, 10.00, 5.00, 0.01)
            local_triple_rate2 = st.slider('当地三連率②', 0.00, 100.00, 50.00, 0.01)
            motor_triple_rate2 = st.slider('モーター三連率②', 0.00, 100.00, 50.00, 0.01)
            adjusted_weight2 = st.slider('選手調整体重②', 0.00, 5.00, 0.00, 0.5)


        with col2:
            nationwide_win_rate2 = st.slider('全国勝率②', 0.00, 10.00, 5.00, 0.01)
            nationwide_triple_rate2 = st.slider('全国三連率②', 0.00, 100.00, 50.00, 0.01)
            local_double_rate2 = st.slider('当地二連率②', 0.00, 100.00, 50.00, 0.01)
            motor_double_rate2 = st.slider('モーター二連率②', 0.00, 100.00, 50.00, 0.01)            
            body_weight2 = st.slider('選手体重②', 30.00, 70.00, 50.00, 0.1)


        st.write('#直前情報')
        col1, col2 = st.columns(2)
        with col1:
            tilt2 = st.slider('チルト②', -0.5, 3.00, 0.00, 0.5)            
            start_time2 = st.slider('スタート展示タイム②', -1.0, 1.0, 0.2, 0.01)
        with col2:       
            rehearsal_time2 = st.slider('展示タイム②', 5.00, 10.00, 7.00, 0.01) 

        
    with tabs[2]:
        st.write('#枠番情報')
        col1, col2, col3 = st.columns(3)

        with col1:
            class3 = st.selectbox(
                '選手クラス③',
                ['A1', 'A2', 'B1',  'B2']
            )
        with col2:
            flying_count3 = st.selectbox(
                'フライング回数③',
                list(range(0, 4))
            )
        with col3:
            lost_count3 = st.selectbox(
                '出遅れ回数③',
                list(range(0, 4))
            )

        col1, col2 = st.columns(2)
        with col1:
            st3 = st.slider('平均ST③', 0.00, 0.15, 0.30, 0.01)
            nationwide_double_rate3 = st.slider('全国二連率③', 0.00, 100.00, 50.00, 0.01)
            local_win_rate3 = st.slider('当地勝率③', 0.00, 10.00, 5.00, 0.01)
            local_triple_rate3 = st.slider('当地三連率③', 0.00, 100.00, 50.00, 0.01)
            motor_triple_rate3 = st.slider('モーター三連率③', 0.00, 100.00, 50.00, 0.01)
            adjusted_weight3 = st.slider('選手調整体重③', 0.00, 5.00, 0.00, 0.5)

        with col2:
            nationwide_win_rate3 = st.slider('全国勝率③', 0.00, 10.00, 5.00, 0.01)
            nationwide_triple_rate3 = st.slider('全国三連率③', 0.00, 100.00, 50.00, 0.01)
            local_double_rate3 = st.slider('当地二連率③', 0.00, 100.00, 50.00, 0.01)
            motor_double_rate3 = st.slider('モーター二連率③', 0.00, 100.00, 50.00, 0.01)            
            body_weight3 = st.slider('選手体重③', 30.00, 70.00, 50.00, 0.1)


        st.write('#直前情報')
        col1, col2 = st.columns(2)
        with col1:
            tilt3 = st.slider('チルト③', -0.5, 3.00, 0.00, 0.5)            
            start_time3 = st.slider('スタート展示タイム③', -1.0, 1.0, 0.2, 0.01)
        with col2:       
            rehearsal_time3 = st.slider('展示タイム③', 5.00, 10.00, 7.00, 0.01) 



    with tabs[3]:
        st.write('#枠番情報')
        col1, col2, col3 = st.columns(3)

        with col1:
            class4 =st.selectbox(
                '選手クラス④',
                ['A1', 'A2', 'B1',  'B2']
            )
        with col2:
            flying_count4 = st.selectbox(
                'フライング回数④',
                list(range(0, 4))
            )
        with col3:
            lost_count4 = st.selectbox(
                '出遅れ回数④',
                list(range(0, 4))
            )

        col1, col2 = st.columns(2)
        with col1:
            st4 = st.slider('平均ST④', 0.00, 0.15, 0.30, 0.01)
            nationwide_double_rate4 = st.slider('全国二連率④', 0.00, 100.00, 50.00, 0.01)
            local_win_rate4 = st.slider('当地勝率④', 0.00, 10.00, 5.00, 0.01)
            local_triple_rate4 = st.slider('当地三連率④', 0.00, 100.00, 50.00, 0.01)
            motor_triple_rate4 = st.slider('モーター三連率④', 0.00, 100.00, 50.00, 0.01)
            adjusted_weight4 = st.slider('選手調整体重④', 0.00, 5.00, 0.00, 0.5)


        with col2:
            nationwide_win_rate4 = st.slider('全国勝率④', 0.00, 10.00, 5.00, 0.01)
            nationwide_triple_rate4 = st.slider('全国三連率④', 0.00, 100.00, 50.00, 0.01)
            local_double_rate4 = st.slider('当地二連率④', 0.00, 100.00, 50.00, 0.01)
            motor_double_rate4 = st.slider('モーター二連率④', 0.00, 100.00, 50.00, 0.01)            
            body_weight4 = st.slider('選手体重④', 30.00, 70.00, 50.00, 0.1)


        st.write('#直前情報')
        col1, col2 = st.columns(2)
        with col1:
            tilt4 = st.slider('チルト④', -0.5, 3.00, 0.00, 0.5)            
            start_time4 = st.slider('スタート展示タイム④', -1.0, 1.0, 0.2, 0.01)
        with col2:       
            rehearsal_time4 = st.slider('展示タイム④', 5.00, 10.00, 7.00, 0.01)      

    with tabs[4]:
        st.write('#枠番情報')
        col1, col2, col3 = st.columns(3)

        with col1:
            class5 =st.selectbox(
                '選手クラス⑤',
                ['A1', 'A2', 'B1',  'B2']
            )
        with col2:
            flying_count5 = st.selectbox(
                'フライング回数⑤',
                list(range(0, 4))
            )
        with col3:
            lost_count5 = st.selectbox(
                '出遅れ回数⑤',
                list(range(0, 4))
            )

        col1, col2 = st.columns(2)
        with col1:
            st5 = st.slider('平均ST⑤', 0.00, 0.15, 0.30, 0.01)
            nationwide_double_rate5 = st.slider('全国二連率⑤', 0.00, 100.00, 50.00, 0.01)
            local_win_rate5 = st.slider('当地勝率⑤', 0.00, 10.00, 5.00, 0.01)
            local_triple_rate5 = st.slider('当地三連率⑤', 0.00, 100.00, 50.00, 0.01)
            motor_triple_rate5 = st.slider('モーター三連率⑤', 0.00, 100.00, 50.00, 0.01)
            adjusted_weight5 = st.slider('選手調整体重⑤', 0.00, 5.00, 0.00, 0.5)


        with col2:
            nationwide_win_rate5 = st.slider('全国勝率⑤', 0.00, 10.00, 5.00, 0.01)
            nationwide_triple_rate5 = st.slider('全国三連率⑤', 0.00, 100.00, 50.00, 0.01)
            local_double_rate5 = st.slider('当地二連率⑤', 0.00, 100.00, 50.00, 0.01)
            motor_double_rate5 = st.slider('モーター二連率⑤', 0.00, 100.00, 50.00, 0.01)            
            body_weight5 = st.slider('選手体重⑤', 30.00, 70.00, 50.00, 0.1)


        st.write('#直前情報')
        col1, col2 = st.columns(2)
        with col1:
            tilt5 = st.slider('チルト⑤', -0.5, 3.00, 0.00, 0.5)            
            start_time5 = st.slider('スタート展示タイム⑤', -1.0, 1.0, 0.2, 0.01)
        with col2:       
            rehearsal_time5 = st.slider('展示タイム⑤', 5.00, 10.00, 7.00, 0.01)    
        
    with tabs[5]:
        st.write('#枠番情報')
        col1, col2, col3 = st.columns(3)

        with col1:
            class6 =st.selectbox(
                '選手クラス⑥',
                ['A1', 'A2', 'B1',  'B2']
            )
        with col2:
            flying_count6 = st.selectbox(
                'フライング回数⑥',
                list(range(0, 4))
            )
        with col3:
            lost_count6 = st.selectbox(
                '出遅れ回数⑥',
                list(range(0, 4))
            )

        col1, col2 = st.columns(2)
        with col1:
            st6 = st.slider('平均ST⑥', 0.00, 0.15, 0.30, 0.01)
            nationwide_double_rate6 = st.slider('全国二連率⑥', 0.00, 100.00, 50.00, 0.01)
            local_win_rate6 = st.slider('当地勝率⑥', 0.00, 10.00, 5.00, 0.01)
            local_triple_rate6 = st.slider('当地三連率⑥', 0.00, 100.00, 50.00, 0.01)
            motor_triple_rate6 = st.slider('モーター三連率⑥', 0.00, 100.00, 50.00, 0.01)
            adjusted_weight6 = st.slider('選手調整体重⑥', 0.00, 5.00, 0.00, 0.5)


        with col2:
            nationwide_win_rate6 = st.slider('全国勝率⑥', 0.00, 10.00, 5.00, 0.01)
            nationwide_triple_rate6 = st.slider('全国三連率⑥', 0.00, 100.00, 50.00, 0.01)
            local_double_rate6 = st.slider('当地二連率⑥', 0.00, 100.00, 50.00, 0.01)
            motor_double_rate6 = st.slider('モーター二連率⑥', 0.00, 100.00, 50.00, 0.01)            
            body_weight6 = st.slider('選手体重⑥', 30.00, 70.00, 50.00, 0.1)


        st.write('#直前情報')
        col1, col2 = st.columns(2)
        with col1:
            tilt6 = st.slider('チルト⑥', -0.5, 3.00, 0.00, 0.5)            
            start_time6 = st.slider('スタート展示タイム⑥', -1.0, 1.0, 0.2, 0.01)
        with col2:       
            rehearsal_time6 = st.slider('展示タイム⑥', 5.00, 10.00, 7.00, 0.01)  
    

class_list = {
    'A1': 0,
    'A2': 1,
    'B1': 2,
    'B2': 3,
}

sin_list = [0, 1.0, 0.92, 0.71, 0.38, 0.0, -0.38, -0.71, -0.92, -1.0, -0.92, -0.71, -0.38, -0.0, 0.38, 0.71, 0.92]
cos_list = [0, -0.0, 0.38, 0.71, 0.92, 1.0, 0.92, 0.71, 0.38, 0.0, -0.38, -0.71, -0.92, -1.0, -0.92, -0.71, -0.38]

wind_y = wind_speed*sin_list[wind]
wind_x = wind_speed*cos_list[wind]

# grade_replacement_rules = {
#     '一般・若手': '一般など',
#     '一般・女子': '一般など',
#     '一般': '一般など',
#     'Ｇ３・女子': '一般など',
#     'Ｇ３': '一般など',
#     'Ｇ２・女子': 'G2',
#     'Ｇ２': 'G2',
#     'Ｇ１・女子': 'G1など',
#     'Ｇ１': 'G1など',
#     'ＳＧ': 'G1など',
# }
# grade_cat = grade_replacement_rules[grade]
# grade_cat_G2 =0
# grade_cat_一般など =0

# if grade_cat == '一般など':
#     grade_cat_一般など = 1
#     grade_cat_G2 =0
# elif grade_cat == 'G2':
#     grade_cat_一般など = 0
#     grade_cat_G2 =1
# else:
#     grade_cat_一般など = 0
#     grade_cat_G2 =0  

# weather_曇り=0 
# weather_雨=0 
# weather_雪=0 
# weather_霧=0 

# if weather == '曇り':
#     weather_曇り=1 
#     weather_雨=0 
#     weather_雪=0 
#     weather_霧=0 
# elif grade_cat == '雨':
#     weather_曇り=0 
#     weather_雨=1 
#     weather_雪=0 
#     weather_霧=0 
# elif grade_cat == '雪':
#     weather_曇り=0 
#     weather_雨=0 
#     weather_雪=1 
#     weather_霧=0 
# elif grade_cat == '霧':
#     weather_曇り=0 
#     weather_雨=0 
#     weather_雪=0 
#     weather_霧=1 
# else:
#     weather_曇り=0 
#     weather_雨=0 
#     weather_雪=0 
#     weather_霧=0 

# stabilizer_flg = 0
# if stabilizer=='あり':
#     stabilizer_flg = 1
# else:
#     stabilizer_flg = 0

# race_name_flg = 0
# if race_name_flg=='優勝戦':
#     race_name_flg = 1
# else:
#     race_name_flg = 0

race = {
"race_no" : race_no,
"class1" : class_list[class1],
"flying_count1" : flying_count1,
"lost_count1" : lost_count1,
"st1" : st1,
"nationwide_win_rate1" : nationwide_win_rate1,
"nationwide_double_rate1" : nationwide_double_rate1,
"nationwide_triple_rate1" : nationwide_triple_rate1,
"local_win_rate1" : local_win_rate1,
"local_double_rate1" : local_double_rate1,
"local_triple_rate1" : local_triple_rate1,
"motor_double_rate1" : motor_double_rate1,
"motor_triple_rate1" : motor_triple_rate1,
"class2" : class_list[class2],
"flying_count2" : flying_count2,
"lost_count2" : lost_count2,
"st2" : st2,
"nationwide_win_rate2" : nationwide_win_rate2,
"nationwide_double_rate2" : nationwide_double_rate2,
"nationwide_triple_rate2" : nationwide_triple_rate2,
"local_win_rate2" : local_win_rate2,
"local_double_rate2" : local_double_rate2,
"local_triple_rate2" : local_triple_rate2,
"motor_double_rate2" : motor_double_rate2,
"motor_triple_rate2" : motor_triple_rate2,
"class3" : class_list[class3],
"flying_count3" : flying_count3,
"lost_count3" : lost_count3,
"st3" : st3,
"nationwide_win_rate3" : nationwide_win_rate3,
"nationwide_double_rate3" : nationwide_double_rate3,
"nationwide_triple_rate3" : nationwide_triple_rate3,
"local_win_rate3" : local_win_rate3,
"local_double_rate3" : local_double_rate3,
"local_triple_rate3" : local_triple_rate3,
"motor_double_rate3" : motor_double_rate3,
"motor_triple_rate3" : motor_triple_rate3,
"class4" : class_list[class4],
"flying_count4" : flying_count4,
"lost_count4" : lost_count4,
"st4" : st4,
"nationwide_win_rate4" : nationwide_win_rate4,
"nationwide_double_rate4" : nationwide_double_rate4,
"nationwide_triple_rate4" : nationwide_triple_rate4,
"local_win_rate4" : local_win_rate4,
"local_double_rate4" : local_double_rate4,
"local_triple_rate4" : local_triple_rate4,
"motor_double_rate4" : motor_double_rate4,
"motor_triple_rate4" : motor_triple_rate4,
"class5" : class_list[class5],
"flying_count5" : flying_count5,
"lost_count5" : lost_count5,
"st5" : st5,
"nationwide_win_rate5" : nationwide_win_rate5,
"nationwide_double_rate5" : nationwide_double_rate5,
"nationwide_triple_rate5" : nationwide_triple_rate5,
"local_win_rate5" : local_win_rate5,
"local_double_rate5" : local_double_rate5,
"local_triple_rate5" : local_triple_rate5,
"motor_double_rate5" : motor_double_rate5,
"motor_triple_rate5" : motor_triple_rate5,
"class6" : class_list[class6],
"flying_count6" : flying_count6,
"lost_count6" : lost_count6,
"st6" : st6,
"nationwide_win_rate6" : nationwide_win_rate6,
"nationwide_double_rate6" : nationwide_double_rate6,
"nationwide_triple_rate6" : nationwide_triple_rate6,
"local_win_rate6" : local_win_rate6,
"local_double_rate6" : local_double_rate6,
"local_triple_rate6" : local_triple_rate6,
"motor_double_rate6" : motor_double_rate6,
"motor_triple_rate6" : motor_triple_rate6,
"body_weight1" : body_weight1,
"adjusted_weight1" : adjusted_weight1,
"rehearsal_time1" : rehearsal_time1,
"tilt1" : tilt1,
"start_time1" : start_time1,
"body_weight2" : body_weight2,
"adjusted_weight2" : adjusted_weight2,
"rehearsal_time2" : rehearsal_time2,
"tilt2" : tilt2,
"start_time2" : start_time2,
"body_weight3" : body_weight3,
"adjusted_weight3" : adjusted_weight3,
"rehearsal_time3" : rehearsal_time3,
"tilt3" : tilt3,
"start_time3" : start_time3,
"body_weight4" : body_weight4,
"adjusted_weight4" : adjusted_weight4,
"rehearsal_time4" : rehearsal_time4,
"tilt4" : tilt4,
"start_time4" : start_time4,
"body_weight5" : body_weight5,
"adjusted_weight5" : adjusted_weight5,
"rehearsal_time5" : rehearsal_time5,
"tilt5" : tilt5,
"start_time5" : start_time5,
"body_weight6" : body_weight6,
"adjusted_weight6" : adjusted_weight6,
"rehearsal_time6" : rehearsal_time6,
"tilt6" : tilt6,
"start_time6" : start_time6,
"temperature" : temperature,
"water_tempreture" : water_tempreture,
"wave_height" : wave_height,
"kiatu" : kiatu,
"situdo" : situdo,
"pool_code_02" : 1 if pool_code == 2 else 0,
"pool_code_03" : 1 if pool_code == 3 else 0,
"pool_code_04" : 1 if pool_code == 4 else 0,
"pool_code_05" : 1 if pool_code == 5 else 0,
"pool_code_06" : 1 if pool_code == 6 else 0,
"pool_code_07" : 1 if pool_code == 7 else 0,
"pool_code_08" : 1 if pool_code == 8 else 0,
"pool_code_09" : 1 if pool_code == 9 else 0,
"pool_code_10" : 1 if pool_code == 10 else 0,
"pool_code_11" : 1 if pool_code == 11 else 0,
"pool_code_12" : 1 if pool_code == 12 else 0,
"pool_code_13" : 1 if pool_code == 13 else 0,
"pool_code_14" : 1 if pool_code == 14 else 0,
"pool_code_15" : 1 if pool_code == 15 else 0,
"pool_code_16" : 1 if pool_code == 16 else 0,
"pool_code_17" : 1 if pool_code == 17 else 0,
"pool_code_18" : 1 if pool_code == 18 else 0,
"pool_code_19" : 1 if pool_code == 19 else 0,
"pool_code_20" : 1 if pool_code == 20 else 0,
"pool_code_21" : 1 if pool_code == 21 else 0,
"pool_code_22" : 1 if pool_code == 22 else 0,
"pool_code_23" : 1 if pool_code == 23 else 0,
"pool_code_24" : 1 if pool_code == 24 else 0,
"grade_cat_G2" : 1 if grade in ['Ｇ２・女子', 'Ｇ２'] else 0,
"grade_cat_一般など" : 1 if grade in ['一般・若手', '一般・女子', '一般', 'Ｇ３・女子', 'Ｇ３'] else 0,
"weather_曇り" : 1 if weather=='曇り' else 0,
"weather_雨" : 1 if weather=='雨' else 0,
"weather_雪" : 1 if weather=='雪' else 0,
"weather_霧" : 1 if weather=='霧' else 0,
"stabilizer" : 1 if stabilizer=='あり' else 0,
"race_name" : 1 if race_name == '優勝戦' else 0,
"wind_x" : wind_x,
"wind_y" : wind_y,
"year" : int(yyyymmdd.strftime("%Y%m%d")[:4]),
"month" : int(yyyymmdd.strftime("%Y%m%d")[4:6])
}


if st.button("Predict"):
    # 予測の実行
    response = requests.post("https://boatrace-predict.onrender.com/predict", json=race)
    # レスポンスの確認とエラーハンドリング
    if response.status_code == 200:
        # 正常なレスポンスの処理
        prediction= response.json()["prediction"]
        st.write(f'一着は{prediction}かも、、、')

    else:
        # エラーの処理
        st.error("エラーが発生しました: " + response.text)
