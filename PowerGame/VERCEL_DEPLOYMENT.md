# Vercel Deployment Guide

Your Django PowerGame project is now configured for Vercel deployment!

## Setup Steps

1. **Install Vercel CLI** (optional):
   ```bash
   npm install -g vercel
   ```

2. **Configure Environment Variables**:
   - Go to your Vercel project settings
   - Add the following environment variables:
     - `SECRET_KEY`: Set a secure Django secret key
     - `DEBUG`: Set to `False` for production
     - Any other required environment variables

3. **Deploy**:
   ```bash
   vercel --prod
   ```
   Or push to your Git repository connected to Vercel for automatic deployments.

## Files Created/Modified

- **vercel.json**: Vercel configuration file
- **requirements.txt**: Python dependencies
- **.vercelignore**: Files to exclude from deployment
- **build.sh**: Build script for Vercel
- **PowerGame/settings.py**: Updated for production and Vercel compatibility

## Key Configuration Changes

1. **WhiteNoise Middleware**: Added for efficient static file serving
2. **Environment Variables**: `SECRET_KEY` and `DEBUG` now use environment variables
3. **ALLOWED_HOSTS**: Set to '*' for Vercel deployment
4. **Security Settings**: SSL/HTTPS, secure cookies enabled on production
5. **Static Files**: Configured with compression and manifest

## Important Notes

- **Database**: Currently using SQLite. For production, consider using:
  - PostgreSQL (via Vercel Postgres)
  - MongoDB (via MongoDB Atlas)
  - Neon
  
  Update `DATABASES` setting in `PowerGame/settings.py` accordingly.

- **Media Files**: If you need user uploads, use cloud storage like:
  - AWS S3
  - Vercel Blob Storage
  - Cloudinary

- **Build Time**: Migrations run automatically during build via `build.sh`

## Troubleshooting

- Check Vercel build logs if deployment fails
- Ensure all dependencies in `requirements.txt` are correct
- Verify environment variables are set in Vercel project settings
- For local testing: `python manage.py runserver` (ensure `DEBUG = True` locally)

## Additional Resources

- [Vercel Django Deployment Guide](https://vercel.com/docs/concepts/frameworks/django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
