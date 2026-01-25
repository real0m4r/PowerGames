# Django on Vercel

A complete Django project configured for deployment on Vercel with templates, static files, and URL routing fully set up.

## Features

✅ **Complete Django Setup**
- Django 4.2+ project structure
- Custom app (`core`) with views and URL routing
- Template system with base template and inheritance
- Static files (CSS & JavaScript) configuration

🚀 **Vercel Ready**
- `vercel.json` configuration
- Build script for static file collection
- WSGI configuration for serverless deployment
- SQLite database stored in `/tmp` for Vercel compatibility

🎨 **Pre-built UI**
- Responsive navigation bar
- Modern gradient design
- Feature cards and styled components
- Mobile-friendly layout

## Project Structure

```
myproject/
├── core/                    # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # App URL routing
│   └── views.py            # View functions
├── myproject/              # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI application
├── templates/              # HTML templates
│   ├── base.html
│   ├── home.html
│   └── about.html
├── static/                 # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── staticfiles/            # Collected static files (auto-generated)
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel configuration
├── build_files.sh         # Build script for Vercel
└── README.md              # This file
```

## Local Development

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone or navigate to the project directory**
   ```bash
   cd myproject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Home: http://127.0.0.1:8000/
   - About: http://127.0.0.1:8000/about/
   - API: http://127.0.0.1:8000/api/hello/
   - Admin: http://127.0.0.1:8000/admin/

## Deployment to Vercel

### Method 1: Using Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Set environment variables in Vercel**
   ```bash
   vercel env add SECRET_KEY
   ```
   Enter a strong secret key when prompted.

### Method 2: Using Vercel Dashboard

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Import project in Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration

3. **Add environment variables**
   - In project settings, add:
     - `SECRET_KEY`: A strong secret key
     - `DEBUG`: `False`

4. **Deploy**
   - Click "Deploy"
   - Your app will be live in minutes!

## Environment Variables

Create a `.env` file for local development (use `.env.example` as template):

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

For production (Vercel), set these in the Vercel dashboard:
- `SECRET_KEY`: Generate a strong secret key
- `DEBUG`: Set to `False`

## URLs

- `/` - Home page
- `/about/` - About page
- `/api/hello/` - Sample JSON API endpoint
- `/admin/` - Django admin panel

## Customization

### Adding New Views

1. Add view function in `core/views.py`
2. Add URL pattern in `core/urls.py`
3. Create template in `templates/`

### Modifying Styles

- Edit `static/css/style.css` for styling
- Edit `static/js/main.js` for JavaScript

### Database

By default, SQLite is used and stored in `/tmp/db.sqlite3` for Vercel compatibility. For production with persistent data, consider:
- Vercel Postgres
- PostgreSQL on platforms like Supabase or Railway
- Other cloud database services

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --noinput --clear
```

### Migrations not applied
```bash
python manage.py migrate
```

### Module import errors
Make sure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

## License

This project is open source and available for use.

## Support

For issues or questions, refer to:
- [Django Documentation](https://docs.djangoproject.com/)
- [Vercel Documentation](https://vercel.com/docs)
