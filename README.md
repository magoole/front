# Magoole Frontend
The frontend of Magoole Search Engine

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
