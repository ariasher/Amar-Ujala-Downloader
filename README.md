# Amar Ujala Downloader

A downloader for Amar Ujala Hindi newspaper. Downloads images from the website and converts them into a pdf file. Only two sections are downloaded: _Main City_ and _My City_ pages.

## Usage
There are three actions and two modes for the downloader.

### Actions
*_conf:_* This action is used to configure the downloader. 
        There are three settings:
        * path: Specifies the path where the temporary files and pdf will be saved.
        * prefix: prefix for the pdf file.
        * city_code: code of the city of which the newspaper is to be downloaded.

*_reset:_* Resets the configuration to its default settings.
           Default:
           * path: Current directory where this downloader is saved. 
           * prefix: auj
           * city: lc

*_dl_*: Used to indicate download action.
        Two modes: Single, Range. If both start and end dates are provided, it will work in range mode.
        * -s, --start: Specifies the start date in yyyy/mm/dd format. Default is current date.
        * -e, --end: Specifies the end date in yyyy/mm/dd format. Default is current date.

## Examples:
*Configuration:*
``` python auj.py conf```

*Reset Configurations:*
``` python auj.py reset```

*Download:*
Current date - ```python auj.py dl```
Particular date - ```python auj.py dl -s 2021/05/03```
Date range - ```python auj.py dl -s 2021/05/01 -e 2021/05/10```

## Disclaimer:
_Only meant for personal use and not for commercial purpose. If it violates the TnC, message me to take it down._