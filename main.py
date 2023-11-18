from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import lightgbm as lgb
import numpy as np

# インスタンス化
app = FastAPI()

# 入力するデータ型の定義
class race(BaseModel):
    race_no : int
    class1 : int
    flying_count1 : int
    lost_count1 : int
    st1 : float
    nationwide_win_rate1 : float
    nationwide_double_rate1 : float
    nationwide_triple_rate1 : float
    local_win_rate1 : float
    local_double_rate1 : float
    local_triple_rate1 : float
    motor_double_rate1 : float
    motor_triple_rate1 : float
    class2 : int
    flying_count2 : int
    lost_count2 : int
    st2 : float
    nationwide_win_rate2 : float
    nationwide_double_rate2 : float
    nationwide_triple_rate2 : float
    local_win_rate2 : float
    local_double_rate2 : float
    local_triple_rate2 : float
    motor_double_rate2 : float
    motor_triple_rate2 : float
    class3 : int
    flying_count3 : int
    lost_count3 : int
    st3 : float
    nationwide_win_rate3 : float
    nationwide_double_rate3 : float
    nationwide_triple_rate3 : float
    local_win_rate3 : float
    local_double_rate3 : float
    local_triple_rate3 : float
    motor_double_rate3 : float
    motor_triple_rate3 : float
    class4 : int
    flying_count4 : int
    lost_count4 : int
    st4 : float
    nationwide_win_rate4 : float
    nationwide_double_rate4 : float
    nationwide_triple_rate4 : float
    local_win_rate4 : float
    local_double_rate4 : float
    local_triple_rate4 : float
    motor_double_rate4 : float
    motor_triple_rate4 : float
    class5 : int
    flying_count5 : int
    lost_count5 : int
    st5 : float
    nationwide_win_rate5 : float
    nationwide_double_rate5 : float
    nationwide_triple_rate5 : float
    local_win_rate5 : float
    local_double_rate5 : float
    local_triple_rate5 : float
    motor_double_rate5 : float
    motor_triple_rate5 : float
    class6 : int
    flying_count6 : int
    lost_count6 : int
    st6 : float
    nationwide_win_rate6 : float
    nationwide_double_rate6 : float
    nationwide_triple_rate6 : float
    local_win_rate6 : float
    local_double_rate6 : float
    local_triple_rate6 : float
    motor_double_rate6 : float
    motor_triple_rate6 : float
    body_weight1 : float
    adjusted_weight1 : float
    rehearsal_time1 : float
    tilt1 : float
    start_time1 : float
    body_weight2 : float
    adjusted_weight2 : float
    rehearsal_time2 : float
    tilt2 : float
    start_time2 : float
    body_weight3 : float
    adjusted_weight3 : float
    rehearsal_time3 : float
    tilt3 : float
    start_time3 : float
    body_weight4 : float
    adjusted_weight4 : float
    rehearsal_time4 : float
    tilt4 : float
    start_time4 : float
    body_weight5 : float
    adjusted_weight5 : float
    rehearsal_time5 : float
    tilt5 : float
    start_time5 : float
    body_weight6 : float
    adjusted_weight6 : float
    rehearsal_time6 : float
    tilt6 : float
    start_time6 : float
    temperature : float
    water_tempreture : float
    wave_height : float
    kiatu : float
    situdo : float
    pool_code_02 : int
    pool_code_03 : int
    pool_code_04 : int
    pool_code_05 : int
    pool_code_06 : int
    pool_code_07 : int
    pool_code_08 : int
    pool_code_09 : int
    pool_code_10 : int
    pool_code_11 : int
    pool_code_12 : int
    pool_code_13 : int
    pool_code_14 : int
    pool_code_15 : int
    pool_code_16 : int
    pool_code_17 : int
    pool_code_18 : int
    pool_code_19 : int
    pool_code_20 : int
    pool_code_21 : int
    pool_code_22 : int
    pool_code_23 : int
    pool_code_24 : int
    grade_cat_G2 : int
    grade_cat_一般など : int
    weather_曇り : int
    weather_雨 : int
    weather_雪 : int
    weather_霧 : int
    stabilizer : int
    race_name : int
    wind_x : float
    wind_y : float
    year : int
    month : int

# モデル読み込み
model = lgb.Booster(model_file='multiclass_model.txt')

# トップページ
@app.get('/')
def index():
    return {"race": 'race_prediction'}

# POST が送信された時（入力）と予測値（出力）の定義
# POST が送信された時（入力）と予測値（出力）の定義
@app.post('/predict')
def make_predictions(features: race):
    print(features)
    data = jsonable_encoder(features)
    print(list(data.values()))
    predict = np.argmax(model.predict([list(data.values())])[0])
    return {"prediction": str(predict+1)}
    # return {"race": 'race_prediction'}