# LRE_Results_Extractor
Short Script to pull out essential report

Personally I got tired of copying and pasting high level reports from the LRE generated reports to send out.
So I worked on a personal solution to save some time and not have to deal with manually creating this part of the report.

# How it works
Download the Export.zip file from LRE.
Put the directory for the files you're going to be working with in the script.
Export.zip, 'Export.zip directory', 'unziped file directory',' directory of the output/excel file as well as the file'

Now the script unzips the summary.html file and using BeautifulSoup extracts the Elapsed time of the test (at the moment, test should be at least and hour)
Then it extracts the table data using pandas.
We then do some simple math to calculate the TPS using the Pass count and the Elapsed time previously calculated, as well as the Passing and Failing rate.
Finally creates a table, adds it to the excel sheet created earlier
prints it out in the console and opens the excel using OS.

Always room for improvements :) <sub>(except to automate myself out of a job)</sub>
