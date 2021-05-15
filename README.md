# Amar Ujala Downloader

A downloader for Amar Ujala Hindi newspaper. Downloads images from the website and converts them into a pdf file. Only two sections are downloaded: _**Main City**_ and _**My City**_ pages.

## Requirements
* Python pillow library.

## Usage
There are three actions and two modes for the downloader.

### Actions
**_conf:_** This action is used to configure the downloader. There are three settings: <br />
- _path_: Specifies the path where the temporary files and pdf will be saved.
- _prefix_: prefix for the pdf file.
- *city_code*: code of the city of which the newspaper is to be downloaded.

**_reset:_** Resets the configuration to its default settings.
Default:
* _path:_ Current directory where this downloader is saved. 
* _prefix:_ auj
* *city_code:* lc

**_dl_**: Used to indicate download action. There are two modes: **Single** and **Range**. If both _start_ and _end_ dates are provided, it will work in range mode.
* _-s, --start:_ Specifies the start date in yyyy/mm/dd format. Default is current date.
* _-e, --end:_ Specifies the end date in yyyy/mm/dd format. Default is start date.

# City Codes
City | Code
------ | -------
Agra | ac
Aligarh | ct
Ayodhya | fz
Chandigarh | cc
Dehradun | dc
Delhi | dl
Gurugram | gr
Jammu | cj
Kanpur | kc
Lucknow | lc
Meerut | cm
Noida | nd

*More will be added later.*

## Examples
*Configuration:* <br/>
``` python auj.py conf```

*Reset Configuration:* <br/>
``` python auj.py reset```

*Download:* <br/>
**Current date -** ```python auj.py dl``` <br/>
**Particular date -** ```python auj.py dl -s 2021/05/03``` <br/>
**Date range -** ```python auj.py dl -s 2021/05/01 -e 2021/05/10``` <br/>

## Disclaimer
_Only meant for personal use and not for commercial purpose. If it violates any TnC, message me to take it down._