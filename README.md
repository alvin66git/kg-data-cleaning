This directory will hold Jupyter notebooks for exploratory data analysis and visualization.

# 知識圖譜數據清理專案

## 專案簡介
本專案針對 ASD 數據進行清理和正規化處理，包含簡繁轉換、欄位正規化、日期格式統一等功能。透過系統化的數據處理流程，提升數據品質並為後續分析做準備。

## 功能特色
- 📊 數據清理與正規化：統一欄位格式，處理異常值
- 🔄 簡體轉繁體中文處理：使用 OpenCC 進行全欄位繁體轉換
- 📅 日期格式標準化：將日期統一為 YYYY-MM-DD 格式
- 📋 Excel 格式輸出優化：清理特殊字元，確保 Excel 相容性
- 🗂️ 欄位字典對應處理：基於字典檔案進行欄位值正規化
- 🔍 數據統計分析：提供螺絲相關客訴統計等專項分析

## 檔案結構
```
python-data-cleaning/
├── notebooks/                          # Jupyter 筆記本
│   ├── data_cleaning-2.ipynb          # 主要數據清理筆記本
│   └── README.md                       # 筆記本說明文件
├── data/
│   ├── raw/                            # 原始數據（完整納入版控，僅新增不覆寫）
│   │   ├── ASD_9-1_test.csv
│   │   ├── 欄位字典_20250725.csv
│   │   └── 欄位字典_20250725_TC.csv
│   └── cleaned/                        # 清理後數據（僅保留關鍵成果）
│       ├── ASD_9-1_test_cleaned.csv
│       ├── ASD_9-1_test_cleaned_dict.csv
│       ├── ASD_9-1_test_cleaned_dict.xlsx
│       └── screw_counts.csv
├── scripts/
│   └── gen_manifest.py                 # 產生資料清單（manifest）
├── src/                                # 源碼（如有）
├── data_manifest.csv                   # 資料清單（自動產生）
├── requirements.txt                    # 依賴套件清單
├── .gitignore
├── .venv/                              # Python 虛擬環境（不建議提交）
└── README.md                           # 專案說明文件（本檔）
```

## 數據處理流程
### 1. 日期格式標準化
- 將收件日期統一轉換為 `YYYY-MM-DD` 格式
- 處理多種輸入日期格式

### 2. 欄位正規化
- Issue_Level_6_故障零件位置：統一分隔符號，排序零件名稱
- Issue_Level_1_客訴故障現象：基於字典檔案進行正規化
- Issue_Level_2_分析看到現象：對應標準術語
- Issue_Level_7_損壞原因：統一損壞原因描述

### 3. 簡繁轉換
- 使用 OpenCC 將所有中文欄位從簡體轉為繁體
- 保留原始資料以供對比

### 4. Excel 輸出優化
- 清理控制字元和特殊符號
- 確保 Excel 開啟時的中文顯示正確
- 同時提供 CSV 與 Excel 兩種格式

## 使用方法
### 環境設定
```bash
# 建立並啟用虛擬環境（macOS/Linux）
python -m venv .venv
source .venv/bin/activate

# 安裝依賴
pip install -r python-data-cleaning/requirements.txt
```

### 執行數據清理
1. 將原始數據放入 `python-data-cleaning/data/raw/`
2. 開啟 Notebook：
   ```bash
   jupyter notebook python-data-cleaning/notebooks/data_cleaning-2.ipynb
   ```
3. 依序執行程式碼區塊
4. 查看結果於 `python-data-cleaning/data/cleaned/`

### 輸出檔案說明
- ASD_9-1_test_cleaned.csv：基礎清理版本
- ASD_9-1_test_cleaned_dict.csv/.xlsx：包含字典正規化的完整版本
- screw_counts.csv：螺絲相關客訴統計結果

## 資料版本策略
- raw/ 完整納入版控，原始檔「只新增不覆寫」；修正版以 `_fixed`、`_v2` 後綴保留歷史
- 若單檔超過 100MB 或未來常更新，建議使用 Git LFS（選用）
- 重要資料批次建立標籤（例如：`v-data-YYYYMMDD`）以便回溯

## 資料清單（manifest）
- 使用 `scripts/gen_manifest.py` 掃描 `data/`，產生 `data_manifest.csv`
- 內容包含：相對路徑、大小位元組、檔案指紋（sha256），以及 CSV 欄位樣本
- 目的：完整性驗證、快照比對、稽核與資料治理

產生方式：
```bash
cd python-data-cleaning
python scripts/gen_manifest.py
git add data_manifest.csv
git commit -m "chore(data): add/refresh manifest"
```

## 釋出（完成版）
```bash
# 確認工作樹乾淨並同步
git pull --ff-only
git status

# 產生/更新 manifest
cd python-data-cleaning && python scripts/gen_manifest.py && cd ..

# 提交與打標籤（若 v1.0.0 已存在，改用 v1.0.1）
git add .
git commit -m "chore(release): final dataset + notebooks snapshot"
git tag v1.0.0
git push && git push --tags
```

## 協作與同步指引
- 分支命名：`feature/<功能>`、`fix/<問題>`、`docs/<文檔>`
- 推送前檢查：
  - `git pull --ff-only`
  - `git status`
  - `git diff --name-only`
- 環境再現：`pip install -r python-data-cleaning/requirements.txt`
- 新增資料批次可建立資料標籤：`git tag v-data-YYYYMMDD && git push --tags`

## 依賴套件
```requirements.txt
pandas>=1.5.0
opencc-python-reimplemented>=1.1.0
openpyxl>=3.0.0
jupyter>=1.0.0
```

## 安裝指令（快速）
```bash
pip install pandas opencc-python-reimplemented openpyxl jupyter
```

## 數據品質檢查
- 正規化效果統計
- 唯一值減少比例分析
- 變更內容對比展示

## 注意事項
1. 大型檔案處理：>100MB 檔案建議使用 Git LFS
2. 敏感資料：避免將個資上傳至公開倉庫
3. 編碼：輸出使用 UTF-8-sig，確保 Excel 正確顯示中文

## 版本歷史
- v1.0：基礎數據清理功能
- v1.1：新增簡繁轉換功能
- v1.2：新增欄位字典正規化功能
- v1.3：新增 Excel 輸出優化和數據品質檢查
- v1.4：最終資料快照與 manifest（完成版）

## 貢獻指南
歡迎提交 Issue 或 Pull Request 改善本專案。

## 授權條款
MIT License

## 聯絡資訊
如有問題或建議，請聯絡：alvinliu66@gmail.com