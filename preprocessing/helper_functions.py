import unicodedata
import re
import pandas as pd
import numpy as np

def to_ascii(s):
    """
    Convert the required col data into ascii, stripped and lower
    to have uniformity across the entire table
    """
    if pd.isna(s):
        return s
    return (
        unicodedata.normalize("NFKD", str(s))
        .encode("ascii", "ignore")
        .decode("ascii")
        .strip()
        .lower()
    )

def rename_cols(df, col_dict):
    """
    Rename all the columns to make them shorter and easy to track
    """
    return df.rename(columns={
    df.columns[idx]: new_name
    for idx, new_name in col_dict.items()
    })
    
def erase_parentheses(text):
    """
    To get rid of the extra details each option had in the initial survey data
    """
    if not isinstance(text, str):
        return text
    parts = text.split(';')
    cleaned = []
    for p in parts:
        p = re.sub(r'\([^)]*\)', '', p)
        p = re.sub(r'\s+', ' ', p).strip()
        if p:
            cleaned.append(p)
    return ';'.join(cleaned)

def map_and_categorize(text, maps, default_to_self):
    """
    Splits the different data points that are all in the same row into individual ones to get their mappings and then rejoin them the same way
    """
    parts = [t.strip() for t in text.split(";") if t.strip()]
    result = []
    for p in parts:
        default = p if default_to_self else "other"
        mapped = maps.get(p, default)
        if isinstance(mapped, (list, tuple, set)):
            result.extend(mapped)
        else:
            result.append(mapped)
    seen = set()
    deduped = [r for r in result if not (r in seen or seen.add(r))]
    return ';'.join(deduped)