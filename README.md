# Notes
Code and data supporting my publications. This is a file listing organized by publication, with a short description of each file.

Submission to CMCL Feb 2025:
CollectedAnnotations

Publication: 
None, August, 2021

Files:

collectMetaData.py -- cycles through a directory containing customer reviews from AWS arranged in files by customer ID, collects and stores information about the data set.

DirOps.py -- Differentiates single-category and multi-category customers and creates a batch file for moving one group to a new directory.

BeautSoupAndTokens.py--includes:

-a function to detect html, and create text entry with html stripped and also a non-stripped version
  
-basic NLP over a set of files; tokenizing, finding the most common token, calculating lexical diversity
  
-comments

WordFrequencyGraph.py -- cycles through a directory containing customer reviews from AWS arranged in files by customer ID, tokenizes reivew and review header, agglomerates all tokens, counts word frequency, plots word frequency, forms list of all tokens used, forms list of all tokens that appear only once in entire data set.

