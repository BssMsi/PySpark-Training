# Assignment for the PySpark Training
Extracting some insights by tranforming Apache access logs and visualizing through plots<br>
View the main notebook <a href="https://nbviewer.jupyter.org/github/BssMsi/PySpark-Training/blob/master/ProcessLogs.ipynb">here</a> to render the dynamic map
## Dataset
<p>
Data contains Apache Access logs obtained from open source freely available sources.<br>
The access logs contain a total of 6 million+ rows.<br>
It has not been uploaded here to GitHub due to size constraints, you can see the urls in the "GetData.ipynb" notebook.<br>
</p>
## Guide to files
<ol>
    <li>ProcessLogs.ipynb - Main notebook containing all the Transformations and plot</li>
    <li>ProcessRDDLogs.ipynb - Trying to tranform the same data using RDD, took much more time, hence abandoned</li>
    <li>iplocation/ - Contains the python code for the web crawler built on scrapy</li>
    <li>GetData.ipynb - Helper notebook to download the data and process it, also includes some RnD</li>
    <li>locations.json - contains location information based on the IP (obtained by crawling the web with a web crawler(iplocation) built on scrapy)</li>
</ol>
