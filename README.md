# extractparasfromcc

Extract remaining paragraphs containing keywords from conference calls

Some info that might be helpful:

Repo structure (not ideal, but wanted to get this out asap)"
1. Code - contains the main .py file
2. Output
- ConferenceCall
  - Csv: contains 1 csv file, the csv of one bunch of conference calls.
- KeywordIdentification
  - keyterms: contains a .txt file containing the list of keywords
  - Test Set of 50 Group Folders: contains 50 folders (group1, ..., group50) in the same way as the format on Mercury (by previous RP). Only the first folder, group1 contains files.
    - group 1: contains a FR5.csv file (named by previous RP), containing a list of keywords that matched conference calls for that 1 csv file.

Change your directory on the python file, namely the following code (may be mac rather than windows for you): 

```
if r"C:\Users" in homepath:
    windows = True
    print("Detected Windows home path - using Jason's Dropbox folders")
    os.chdir(r"C:\Users\jasonjia\Dropbox\Projects\extractparasfromcc\Output\KeywordIdentification\Test Set of 50 Group Folders")
    csv_dir1 = r"C:\Users\jasonjia\Dropbox\Projects\extractparasfromcc\Output\ConferenceCall\Csv"
    keyterms_filepath = r"C:\Users\jasonjia\Dropbox\Projects\extractparasfromcc\Output\KeywordIdentification\keyterms\keyterms.txt"
```

Hopefully the code should run!

The output will be TotalCircnew.xlsx in \extractparasfromcc\Output\KeywordIdentification\Test Set of 50 Group Folders. I've named mine as TotalCircnew_myoutput.xlsx as comparison.
