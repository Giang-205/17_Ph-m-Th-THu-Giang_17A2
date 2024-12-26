import pandas as pd
#Đọc file stocks1.csv vào DataFrame stocks1.
stocks1=pd.read_csv('C:/Users/Admin/Documents/GitHub/17_Pham-Thi-Thu-Giang_17A2/baithuchanh3/DATA_lab3_pandas/stocks1.csv')
#Hiển thị 5 dòng đầu
print('2.Hiển thị 5 dòng đầu tiên của stocks :')
print(stocks1.head())
#Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1
print("\n3.Kiểu dữ liệu (dtypes) của mỗi cột trong stocks1 là :")
print(stocks1.dtypes)
#Xem tổng quan info của stocks1 
print("\n4.Thông tin tổng quan của stocks1 là :")
print(stocks1.info())