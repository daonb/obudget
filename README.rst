Open Budget of the Israeli Gov
==============================

This projects makes it easy for citizens and their serveris to access the Israeli Budget. Based on files shared by the "Accountant General"_, the system currently holds data from 1992 to 2009. 

.. _"Accountant General": http://www.ag.mof.gov.il/AccountantGeneral/Templates/BudgetExecution/PublicationFiles.aspx?NRMODE=Published&NRNODEGUID=%7b67B554DC-C476-4966-82A4-836E1201DF2B%7d&NRORIGINALURL=%2fAccountantGeneral%2fBudgetExecution%2fBudgetExecutionTopNav%2fBEHistoryData%2f&NRCACHEHINT=Guest

INSTALL
-------

$ python bootstrap.py
$ bin/buildout
$ bin/test
$ unzip budget-db.zip

If you'd like to work on the GWT based user interfce you'll have to install the GWT_ and "gwt-visualization"_ and update the path reference in src/obudget/gwt/src/build.xml.

.. _GWT: http://code.google.com/webtoolkit/download.html
.. _"visualization library": http://code.google.com/p/gwt-google-apis/downloads/list


UI
--

Point your browser at http://127.0.0.1:8000/gwt/obudget.html

API
---

Currently the system includes only a simple API to get data on a known budget row or section.

example:
--------

To get total budget for the interior ministery:
	$ curl 'http://127.0.0.1:8000/0017'  

To get the total and breakdown for the fire depatment:
	$ curl 'http://127.0.0.1:8000/000610'

