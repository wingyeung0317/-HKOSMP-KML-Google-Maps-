# 香港骨位 KML File (Google Maps)
根據易出行製作的香港骨位的KML檔案, 可供Google map 使用. 

A KML file about Hong Kong On-Street Motocycle Parking according to the data from HKeMobility, it can be used by Google map.

[按此直接存取Google Map版](https://www.google.com/maps/d/u/0/edit?mid=1GkWOFWVW3wpZPCqI5qUltyKmbd7j2mw&usp=sharing) 

[Click Here to access Google Map](https://www.google.com/maps/d/u/0/edit?mid=1GkWOFWVW3wpZPCqI5qUltyKmbd7j2mw&usp=sharing)

![image](https://github.com/user-attachments/assets/452af4f0-9d43-49d0-813c-9e867056d9d4)


#### 注意: 由於Google Maps的上載容量有限, 沒法確保所有骨位地點齊存, 而且本人不會更新此地圖, 有需要者可跟隨以下*斜體文字教學*自行重新製作一張. 非斜體文字為解釋我的製作過程.

#### Note: Due to the limited upload file size of Google Maps, I can not ensure that all the On-Street Motocycle Parking locations are included, and I will not update this map. So if you need to, you can follow the *italicised text* below to recreate a map yourself. Non-italicised text is to explain my process when making this map.

---

## 1. 下載Postman / 其他 API 調試軟件
## 2. Header加上 
| Key | Value |
| :-- | --: |
| Origin | https://www.hkemobility.gov.hk |
| Referer | https://www.hkemobility.gov.hk/tc/toll-rate/ |
## 3. Get Method 存取 URL:
https://www.hkemobility.gov.hk/api/drss/layer/map/?typeName=DRSS%3AVW_ON_STREET_PARKING&service=WFS&version=1.0.0&request=GetFeature&outputFormat=application%2Fjson&styles=OSP_Type_ALL&cql_filter=(VEHICLE_TYPE%20%3D%20'Motor%20Cycles')%20AND%20BBOX(SHAPE%2C%20113.7715210770302%2C22.09149645255427%2C114.56486620617868%2C22.58284043586623)
## 4. 存下取得的json file命名為data.json
## 5. 在同一資料夾運行toKML.py
## 6. 在google map匯入生成的output.kml

<!--
## 1. Access to HKeMobility Web
[https://www.hkemobility.gov.hk/en/toll-rate/](https://www.hkemobility.gov.hk/en/toll-rate/)
![[https://www.hkemobility.gov.hk/en/toll-rate/](https://www.hkemobility.gov.hk/en/toll-rate/)](https://github.com/user-attachments/assets/5bb85684-7062-4b6e-a3e7-adcb14f6868f)

## 2. Open DevTools by pressing F12 or Ctrl+Shift+I and Navigate to Network
![image](https://github.com/user-attachments/assets/e72301e9-94dc-4713-8658-f8861291b643)

## 3. Turn On the Layer for On Street Motocycle Parking
![image](https://github.com/user-attachments/assets/1e66f3da-d23f-4c9d-95cd-aba736dbc0ed)

![image](https://github.com/user-attachments/assets/0c9cf0ab-21b7-4090-81c8-f731b999efa4)

## 4. Zoom in until the numbers become a spot
![image](https://github.com/user-attachments/assets/364e098f-37d1-451c-9df5-fc3797f23730)

## 5. Click on "Clear Network Log" for a better view
![image](https://github.com/user-attachments/assets/cb146698-4af3-4ff8-8b4e-5fe73e34dc7e)

## 6. Zoom in one more time and you find out the datas are from chunk-vendors.98785fe8.js:378, Click on it.
![image](https://github.com/user-attachments/assets/9a3534d6-05f1-4e5d-a282-7fa9a12695f5)

## 7. You will find a json file here
![image](https://github.com/user-attachments/assets/49009f61-d16f-4469-8899-7c2a317e5995)

-->
