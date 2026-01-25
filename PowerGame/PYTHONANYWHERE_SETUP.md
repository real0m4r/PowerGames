# PythonAnywhere Deployment Guide for PowerGame

## Prerequisites
- PythonAnywhere account (free or paid)
- Your repository pushed to GitHub

## Step-by-Step Setup

### 1. Clone Your Repository on PythonAnywhere

Open the Bash console on PythonAnywhere and run:

```bash
cd ~
git clone https://github.com/real0m4r/PowerGames.git
cd PowerGames/PowerGame
```

### 2. Create a Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.12 powergame
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a Web App

1. Go to the **Web** tab in PythonAnywhere
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Select **Python 3.12**
5. This creates a WSGI file at `/var/www/yourusername_pythonanywhere_com_wsgi.py`

### 5. Update the WSGI File

Edit the WSGI file (`/var/www/yourusername_pythonanywhere_com_wsgi.py`) and replace its content with:

```python
import os
import sys

project_home = '/home/yourusername/PowerGames/PowerGame'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'PowerGame.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Important:** Replace `yourusername` with your actual PythonAnywhere username!

### 6. Configure Virtual Environment in PythonAnywhere

1. In the **Web** tab, scroll down to **Virtualenv**
2. Enter the path: `/home/yourusername/.virtualenvs/powergame`

### 7. Configure Static Files

1. In the **Web** tab, scroll to **Static files**
2. Add a static files mapping:
   - URL: `/static/`
   - Directory: `/home/yourusername/PowerGames/PowerGame/staticfiles`

### 8. Set Environment Variables

1. Go to **Web** → **Web app settings**
2. Scroll to **Environment variables**
3. Add:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: `False` (for production)

### 9. Collect Static Files

In the Bash console:

```bash
cd ~/PowerGames/PowerGame
python manage.py collectstatic --noinput
```

### 10. Run Migrations

```bash
python manage.py migrate --noinput
```

### 11. Reload Your Web App

Go to the **Web** tab and click the **Reload** button for your web app.

## Database Configuration

By default, PythonAnywhere uses SQLite (stored in your home directory). For production, you can:

### Option 1: Keep SQLite (Simple)
Default configuration will work with SQLite.

### Option 2: Use PostgreSQL (Recommended)
1. PythonAnywhere offers PostgreSQL. Set it up in the **Databases** section
2. Update `PowerGame/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'yourusername$yourdatabase',
           'USER': 'yourusername',
           'PASSWORD': 'your_postgres_password',
           'HOST': 'yourusername.postgres.pythonanywhere-services.com',
           'PORT': '5432',
       }
   }
   ```

## Accessing Your App

Once deployed, your app will be available at:
```
https://yourusername.pythonanywhere.com
```

## Troubleshooting

### Error: Module not found
- Ensure virtual environment path is correct in Web settings
- Check that `sys.path` in WSGI file is correct

### Static files not loading
- Run: `python manage.py collectstatic --noinput` again
- Verify the static files URL mapping in Web settings
- Check file permissions

### Database errors
- Ensure migrations have run: `python manage.py migrate`
- Check database credentials in settings.py

### 500 errors
- Check the error log: **Web** → **Error log** (tail)
- Look for Django error messages in the logfile

## Updating Your App

To pull the latest changes from GitHub:

```bash
cd ~/PowerGames/PowerGame
git pull origin main
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
```

Then reload your web app from the **Web** tab.

## Additional Resources

- [PythonAnywhere Django Documentation](https://help.pythonanywhere.com/pages/Django/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
