# Assignment for the PySpark Training

# Dataset
Data contains Apache Access logs obtained from open source freely available sources.
The access logs contain a total of 6 million+ rows.
It has not been uploaded here to GitHub due to size constraints, you can see the urls in the "GetData.ipynb" notebook.

# Guide to files
<ol>
    <li>ProcessLogs.ipynb - Main notebook containing all the Transformations and plot</li>
    <li>ProcessRDDLogs.ipynb - Trying to tranform the same data using RDD, took much more time, hence abandoned</li>
    <li>iplocation/ - Contains the python code for the web crawler built on scrapy</li>
    <li>GetData.ipynb - Helper notebook to download the data and process it, also includes some RnD</li>
    <li>locations.json - contains location information based on the IP (obtained by crawling the web with a web crawler(iplocation) built on scrapy)</li>
</ol>