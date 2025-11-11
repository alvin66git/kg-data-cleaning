# Jupyter Notebooks

本目錄包含專案的 Jupyter 筆記本檔案。

## 檔案說明

- `data_cleaning-2.ipynb`：主要的數據清理和處理筆記本
  - 日期格式標準化
  - 簡繁轉換處理
  - 欄位正規化
  - Excel 輸出優化
  - **新功能**: 合併正規化字典檔生成
  - **新功能**: 正規化效果評估與檢查
  - **新功能**: 基於欄位字典的智能正規化

## 今日新增功能說明

### 1. 合併正規化字典檔 (`create_merged_normalization_dictionary`)
這個功能將多個正規化欄位的唯一值合併到一個字典檔中：
- 從三個欄位收集正規化後的唯一值：
  - `Issue_Level_1_客訴故障現象_正規化`
  - `Issue_Level_2_分析看到現象_正規化`
  - `Issue_Level_7_損壞原因_正規化`
- 輸出合併後的字典檔到 CSV 和 Excel 格式
- 儲存路徑: `data/dictionary/merged_normalization_dictionary.*`

### 2. 基於字典檔的智能正規化 (`normalize_with_merged_dict`)
使用外部欄位字典進行更精確的正規化：
- 讀取 `data/raw/欄位字典_20250725.csv`
- 支援不同欄位的映射策略
- 自動處理字典對應關係

### 3. 正規化檢查與評估工具
新增兩個評估函數來分析正規化效果：
- `check_normalization()`: 檢查欄位正規化比例和變更範例
- `evaluate_normalization()`: 評估正規化後唯一值的減少程度和最常見值

### 4. 專案上傳指南
在筆記本中新增完整的 GitHub 上傳教學，包含：
- Git 初始化和設定
- .gitignore 檔案配置
- SSH 金鑰設定
- 大型檔案處理 (Git LFS)
- 常見問題解決方案

## 使用方法

```bash
# 啟動 Jupyter Notebook
jupyter notebook data_cleaning-2.ipynb
```

## 輸出檔案
- `ASD_9-1_test_cleaned_dict.csv/.xlsx`: 包含字典正規化的完整版本
- `merged_normalization_dictionary.csv/.xlsx`: 合併字典檔
- `screw_counts.csv`: 螺絲相關客訴統計結果

更多詳細資訊請參考[專案主頁 README](../../README.md)。