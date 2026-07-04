# Mobile Brand Churn Prediction

Dự đoán khả năng khách hàng rời bỏ dịch vụ di động (`brand_churn`) dựa trên hành vi sử dụng, sử dụng các mô hình học máy phân loại.

## Cấu trúc project

- `data/mobile_customers.csv` — tập dữ liệu gốc, 17.799 khách hàng, 13 thuộc tính.
- `mobile_churn_prediction.ipynb` — notebook chính, thực hiện đầy đủ:
  1. Phân tích và trực quan hóa dữ liệu (EDA)
  2. Tiền xử lý dữ liệu và lựa chọn đặc trưng
  3. Huấn luyện và so sánh 4 mô hình học máy (Logistic Regression, Decision Tree, Random Forest, Gradient Boosting) kèm cross-validation và tinh chỉnh siêu tham số
  4. Kết quả, phân tích độ quan trọng đặc trưng và khuyến nghị nghiệp vụ

## Chạy notebook

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter nbformat
jupyter notebook mobile_churn_prediction.ipynb
```
