
# Start the Project
install docker before running below commands
 mac: 
```bash
brew install docker
docker-compose build
docker-compose up
```
# APIs
There are two GET APIs: 
```bash
GET:
API : /api/v1/fampay/youtube/videos/all
params : limit (int), offset (int), timestamp_before (int)
purpose : Returns youtube videos in paginated fashion according to previous timestamp (timestamp_before)

GET
API : /api/v1/fampay/youtube/videos/search
params : title (str), description (str), timestamp_before (int)
purpose : Returns youtube videos according to the title match and description match 
```

# Async Youtube videos fetching
We need active api_key for fetching youtube videos, which are stored in a model ApiKeyInfo, which we can access through django-admin dashboard (we will need a superuser for that) which we can create by running this command:
```bash
python manage.py createsuperuser
```
admin dashboard : 
```bash
http://0.0.0.0:8000/admin/
```
Here we can edit and save api_key_info data and make those api_key's active which are available to fetch youtube videos.

Post that cron will run and that will fetch youtube videos with a cadence of 30 seconds (configurable from celery.py, improvements we can do later)

