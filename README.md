![Banner](https://repository-images.githubusercontent.com/421525017/daa6f4d1-249b-4a52-a681-a8dbf69cd940)
<div align="center">

# Magoole frontend
The privacy first and fully open source search engine.

</div>
This repository contains the frontend of Magoole

## Table of content
- [Credits](#credits-and-acknowledgement)
- [What's that ?](#what-is-magoole-)
- [Try it locally](#try-locally-)

## Credits and acknowledgement
- Source code under [CeCLL Licence V2.1](https://github.com/magoole/front/tree/main/LICENSE?raw=true) by [@camarm](https://github.com/camarm-dev).
- Brand and logos under [CC BY-NC-ND 3.0 FR](https://creativecommons.org/licenses/by-nc-nd/3.0/fr/) by [@camarm](https://github.com/camarm-dev).
- Icon from [Fontawesome V5.15.4](https://fontawesome.com/v5/icons/brain?f=classic&s=solid).
- Font "League Spartan".

## What is Magoole ?
Magoole is a privacy first fully open source search engine.
Magoole has its own bot that scans internet and a free API.

You can self-host your own Magoole instance.

# Try locally:
1. Install requirements
```shell
pip install -r requirements.txt
```
2. Set a backend url in `.backendurl` file<br>
   - Default to  *http://api.magoole.org*, you can change it with your own
   ```shell
      echo "http://mybackend.mymagoole.com" > .backendurl
   ```
3. Run python file (with your magoole url in argument)
```shell
cd /path/to/front && python3 routes.py http://mymagoole.com
```
4. Happy searching !
