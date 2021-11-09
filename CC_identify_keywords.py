import pandas as pd
import numpy as np
import os
from rapidfuzz import fuzz
from cleantext import clean
from collections import defaultdict
import re
import sys

def clean_str(s):
    t = s.replace("\\n", " ")
    t = t.replace("\\", "")
    if len(t) == 0:
        return ""
    if t[0] == '"':
        t = t[1:-1]
    return clean(t, fix_unicode = True, no_line_breaks = True, lower = False)

def alt_keywords_from_one_call(row, keywords, clean = True):
    
    # This is an imperfect split, sometimes it breaks in the middle of a sentence
    call = str(row["Call"])
    paras_list = re.split(r"\n\s*\n+", call)
    found_keywords, found_in_paras = [], []

    report_id = row["Report"]
    for para in paras_list:
        for keyword in keywords:
            if clean == True:
                para = clean_str(para)
            if keyword in para:
                found_keywords.append(keyword)
                found_in_paras.append(para)
    
    return pd.DataFrame({"Keyword": found_keywords, "Para": found_in_paras, "Report": report_id})

def main():
    keywords_df = pd.read_csv("CriCount/keyterms.txt", sep = "\t", header = None)
    keywords = keywords_df[0]
    
    for folder_num in range(1, 51):
        folder_fp = "CriCount/group{}".format(folder_num)
        for file in os.listdir(folder_fp):
            if file == "FR5.csv":
                continue
                
            file_fp = "{}/{}".format(folder_fp, file)
            cc_df = pd.read_csv(file_fp)
            dfs_list = []
            #dfs_list = cc_df.apply(lambda row: alt_keywords_from_one_call(row, keywords, clean = False), axis = 1)
            for index, row in cc_df.iterrows():
                temp = alt_keywords_from_one_call(row, keywords, clean = False)
                dfs_list.append(temp)
            
            unclean_data = pd.concat(dfs_list).reset_index(drop = True)
            #unclean_data = unclean_data.merge(cc_df, on = "Report", how = "left")
            unclean_data["File"] = file
            #output_fp = "CriCount/Identified_Keywords/{}".format(file_fp)
            outdir = "CriCount/Identified_Keywords/group{}".format(folder_num)
            if not os.path.exists(outdir):
                os.mkdir(outdir)
            output_fp = "{}/Identified_{}.parquet.gzip".format(outdir, file)
            unclean_data.to_parquet(output_fp, compression = "gzip")
            #unclean_data.to_csv("CriCount/Identified_Keywords/group1/{}".format(file))

if __name__ == "__main__":
    main()
