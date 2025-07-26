This directory will hold Jupyter notebooks for exploratory data analysis and visualization.

# 知識圖譜數據清理專案

## 專案簡介
本專案針對 ASD 數據進行清理和正規化處理，包含簡繁轉換、欄位正規化、日期格式統一等功能。透過系統化的數據處理流程，提升數據品質並為後續分析做準備。

## 功能特色
- 📊 **數據清理與正規化**：統一欄位格式，處理異常值
- 🔄 **簡體轉繁體中文處理**：使用 OpenCC 進行全欄位繁體轉換
- 📅 **日期格式標準化**：將日期統一為 YYYY-MM-DD 格式
- 📋 **Excel 格式輸出優化**：清理特殊字元，確保 Excel 相容性
- 🗂️ **欄位字典對應處理**：基於字典檔案進行欄位值正規化
- 🔍 **數據統計分析**：提供螺絲相關客訴統計等專項分析

## 檔案結構
```
python-data-cleaning/
├── notebooks/                      # Jupyter 筆記本
│   ├── data_cleaning-2.ipynb      # 主要數據清理筆記本
│   └── README.md                   # 筆記本說明文件
├── data/
│   ├── raw/                        # 原始數據
│   │   ├── ASD_9-1_test.csv       # 原始測試數據
│   │   ├── 欄位字典_20250725.csv   # 原始欄位字典
│   │   └── 欄位字典_20250725_TC.csv # 繁體轉換後的欄位字典
│   └── cleaned/                    # 清理後的數據
│       ├── ASD_9-1_test_cleaned.csv
│       ├── ASD_9-1_test_cleaned_dict.csv
│       ├── ASD_9-1_test_cleaned_dict.xlsx
│       └── screw_counts.csv        # 螺絲相關統計
├── src/                            # 源代碼目錄
├── .gitignore                      # Git 忽略檔案設定
├── .venv/                          # Python 虛擬環境
├── init_project.sh                 # 專案初始化腳本
└── README.md                       # 專案說明文件
```

## 數據處理流程

### 1. 日期格式標準化
- 將收件日期統一轉換為 `YYYY-MM-DD` 格式
- 處理多種輸入日期格式

### 2. 欄位正規化
- **Issue_Level_6_故障零件位置**：統一分隔符號，排序零件名稱
- **Issue_Level_1_客訴故障現象**：基於字典檔案進行正規化
- **Issue_Level_2_分析看到現象**：對應標準術語
- **Issue_Level_7_損壞原因**：統一損壞原因描述

### 3. 簡繁轉換
- 使用 OpenCC 將所有中文欄位從簡體轉換為繁體
- 保留原始資料以供對比

### 4. Excel 輸出優化
- 清理控制字元和特殊符號
- 確保 Excel 開啟時的中文顯示正確
- 同時提供 CSV 和 Excel 兩種格式

## 使用方法

### 環境設定
```bash
# 1. 建立虛擬環境
python -m venv .venv

# 2. 啟動虛擬環境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows

# 3. 安裝依賴套件
pip install pandas opencc-python-reimplemented openpyxl
```

### 執行數據清理
1. 將原始數據檔案放入 `data/raw/` 目錄
2. 開啟 Jupyter Notebook：
   ```bash
   jupyter notebook notebooks/data_cleaning-2.ipynb
   ```
3. 依序執行筆記本中的程式碼區塊
4. 查看處理結果於 `data/cleaned/` 目錄

### 輸出檔案說明
- `ASD_9-1_test_cleaned.csv`：基礎清理版本
- `ASD_9-1_test_cleaned_dict.csv/.xlsx`：包含字典正規化的完整版本
- `screw_counts.csv`：螺絲相關客訴統計結果

## 依賴套件
```requirements.txt
pandas>=1.5.0
opencc-python-reimplemented>=1.1.0
openpyxl>=3.0.0
jupyter>=1.0.0
```

## 安裝指令
```bash
pip install pandas opencc-python-reimplemented openpyxl jupyter
```

## 數據品質檢查

專案包含數據品質評估功能：
- 正規化效果統計
- 唯一值減少比例分析
- 變更內容對比展示

## 注意事項

1. **大型檔案處理**：如果數據檔案超過 100MB，建議使用 Git LFS
2. **敏感資料**：請確保不要將包含個人隱私的原始數據上傳到公開倉庫
3. **編碼問題**：輸出檔案使用 UTF-8-sig 編碼，確保中文在 Excel 中正確顯示

## 版本歷史
- v1.0：基礎數據清理功能
- v1.1：新增簡繁轉換功能
- v1.2：新增欄位字典正規化功能
- v1.3：新增 Excel 輸出優化和數據品質檢查

## 貢獻指南
歡迎提交 Issue 或 Pull Request 來改善本專案。

## 授權條款
MIT License

## 聯絡資訊
如有問題或建議，請聯絡：alvinliu66@gmail.com