# Proquest-Ebook-Central-URL-Check
takes a set of URLs for Proquest Ebook Central and confirms access for the given titles and checks for the title text as well

To make this work, you'll need a CSV file
column 1: any identifier of use
column 2: the title of the record
column 3: the URL to search

save these as a CSV and then initiate the script

If you want to debug, call the main function with a parameter of "1" (eg. runCheck(1) )
