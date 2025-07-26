import pandas as pd

# 注意：前面加上 ../ 回到專案根目錄
df = pd.read_csv('../data/raw/ASD_9-1_test.csv')

date_col = '收件日期'  # ←請改成你的日期欄位名稱

# 觀察前幾筆資料
print(df[date_col].head(10))

# 列出所有不同的日期格式（用 set 去重複）
unique_formats = set(df[date_col].dropna())
print(f"共有 {len(unique_formats)} 種不同的日期字串：")
for v in list(unique_formats)[:20]:  # 只印前20種，避免太多
    print(v)

# 嘗試自動解析日期格式，遇到無法解析的會變成 NaT
df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

# 檢查結果
print(df[date_col].head())