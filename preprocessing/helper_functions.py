import unicodedata
import re
import pandas as pd
import numpy as np

def normalize(s):
    """
    Convert the required col data into ascii, stripped and lower
    to have uniformity across the entire table.
    Also strips out any text within parentheses and removes periods.
    """
    if pd.isna(s):
        return s
    s = (
        unicodedata.normalize("NFKD", str(s))
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    s = re.sub(r"\(.*?\)", "", s)   # remove anything inside parentheses
    s = s.replace(".", "")         # remove periods
    s = re.sub(r"\s+", " ", s)     # collapse any leftover double spaces
    return s.strip().lower()

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

def map_language(text, maps, default_to_self):
    """
    Splits the different data points that are all in the same row into individual ones
    to get their mappings and then rejoin them the same way.
    """
    if not isinstance(text, str):
        return np.nan

    parts = [t.strip() for t in text.split(";") if t.strip()]
    result = []
    for p in parts:
        key = p.lower()  # normalize case so lookups aren't case-sensitive
        default = key if default_to_self else "other"
        mapped = maps.get(key, default)
        if isinstance(mapped, (list, tuple, set)):
            result.extend(mapped)
        else:
            result.append(mapped)

    seen = set()
    deduped = [
        r for r in result
        if isinstance(r, str) and r != "" and not (r in seen or seen.add(r))
    ]

    if not deduped:
        return np.nan  # everything filtered out (junk-only row) -> true missing, not ""

    return ';'.join(deduped)

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

def score_encode(row, factors):
    """
    Encode positional ranking scores for given factors based on order in a semicolon-delimited string.
    Higher rank yields a higher score.
    """
    items = row.split(";")
    return {factor: len(factors) - items.index(factor) for factor in factors}