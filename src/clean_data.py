import pandas as pd
from opencc import OpenCC
import unicodedata
from pathlib import Path

cc = OpenCC('s2t')

def normalize_width(text: str) -> str:
    return unicodedata.normalize("NFKC", str(text))

def normalize_part_list(raw_parts: str) -> str:
    parts = [p.strip() for p in str(raw_parts).split(',') if p.strip()]
    parts.sort()
    return ', '.join(parts)

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    if 'description' in df.columns:
        df['description'] = df['description'].apply(normalize_width).apply(cc.convert)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime("%Y-%m-%d")
    if 'parts' in df.columns:
        df['parts'] = df['parts'].apply(normalize_part_list)
    return df

def main(infile: Path, outfile: Path):
    df_raw = pd.read_excel(infile)
    df_clean = clean_dataframe(df_raw)
    outfile.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_excel(outfile, index=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Clean Excel data")
    parser.add_argument('input', type=Path, help='Path to input Excel file')
    parser.add_argument('output', type=Path, nargs='?', default=Path('data/processed/cleaned.xlsx'),
                        help='Path to output Excel file')
    args = parser.parse_args()
    main(args.input, args.output)
