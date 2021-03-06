ERCOT Scraper
=============

Simple python package for archiving [ERCOT](http://www.ercot.com/gridinfo/)
data.  See related project, 
[ERCOT Sample Apps](https://github.com/oxtopus/ercot-apps), for sample 
applications using this data.

Installation
------------

    git clone git@github.com:oxtopus/ercot.git
    virtualenv ercot
    cd ercot
    source bin/activate
    pip install -r requirements.txt 
    python setup.py develop

Usage
-----

    python -m ercot.scraper "http://mis.ercot.com/misapp/GetReports.do?reportTypeId=12312&reportTitle=Seven-Day%20Load%20Forecast%20by%20Weather%20Zone&showHTMLView=&mimicKey"
    python -m ercot.scraper "http://mis.ercot.com/misapp/GetReports.do?reportTypeId=12340&reportTitle=System-Wide%20Demand&showHTMLView=&mimicKey"
    python -m ercot.scraper "http://mis.ercot.com/misapp/GetReports.do?reportTypeId=12311&reportTitle=Seven-Day%20Load%20Forecast%20by%20Forecast%20Zone&showHTMLView=&mimicKey"
    python -m ercot.scraper "http://mis.ercot.com/misapp/GetReports.do?reportTypeId=12315&reportTitle=Short%20Term%20System%20Adequacy%20Report&showHTMLView=&mimicKey"