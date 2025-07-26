#!/bin/bash

# 建立資料夾結構
mkdir -p data/raw data/cleaned notebooks src

# 建立 .gitignore
cat > .gitignore <<EOL
# Python virtual environments
.venv/
env/
venv/

# Python cache files
__pycache__/
*.pyc

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Local data files (ignore everything in data/ except raw/ and cleaned/)
data/*
!data/raw/
!data/cleaned/
EOL

# 建立 README.md
cat > README.md <<EOL
# Python Data Cleaning Project

## 結構說明

- data/raw/：原始資料
- data/cleaned/：清理後資料
- notebooks/：Jupyter Notebooks
- src/：Python 腳本
EOL

# 建立 notebooks 目錄下的說明檔
cat > notebooks/README.md <<EOL
This directory will hold Jupyter notebooks for exploratory data analysis and visualization.
EOL

echo "資料夾結構與說明檔案已建立完成。"
echo "請手動建立虛擬環境並安裝所需套件："
echo "  python3 -m venv .venv"
echo "  source .venv/bin/activate"
echo "  pip install --upgrade pip"
echo "  pip install pandas numpy seaborn jupyter"