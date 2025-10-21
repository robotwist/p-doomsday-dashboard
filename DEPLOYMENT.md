# Deployment Guide

## Overview

This project uses a **hybrid deployment strategy**:
- **Static landing page** → Netlify (public/index.html)
- **Streamlit application** → Streamlit Community Cloud (frontend/)
- **Backend API** → Heroku/Railway/Render (backend/)

## Deploy Landing Page to Netlify

### Option 1: Netlify CLI (Interactive)

```bash
cd /home/robwistrand/code/solo/p-doomsday-dashboard

# Create new Netlify site
netlify sites:create --name p-doomsday-dashboard

# Select team: robify
# The CLI will create the site and link it

# Deploy to production
netlify deploy --prod --dir=public
```

### Option 2: Netlify Dashboard (Recommended)

1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Connect to GitHub and select: `robotwist/p-doomsday-dashboard`
4. Configure build settings:
   - **Build command**: `echo 'Static site'`
   - **Publish directory**: `public`
5. Click "Deploy site"
6. (Optional) Configure custom domain in Site settings

### Option 3: Drag & Drop

1. Go to https://app.netlify.com/drop
2. Drag the `public` folder from your project
3. Netlify will deploy instantly

## Deploy Streamlit App to Streamlit Community Cloud

### Prerequisites
- GitHub repository must be public or you need Streamlit Cloud Pro
- Repository must have `requirements.txt` at root or in `frontend/`

### Steps

1. Go to https://streamlit.io/cloud
2. Sign in with your GitHub account
3. Click "New app"
4. Configure:
   - **Repository**: `robotwist/p-doomsday-dashboard`
   - **Branch**: `main`
   - **Main file path**: `frontend/app.py`
   - **App URL**: `p-doomsday-dashboard` (or custom name)
   - **Python version**: 3.11
5. Advanced settings → Secrets (if needed):
   ```toml
   API_URL = "https://your-backend-api.herokuapp.com"
   ```
6. Click "Deploy!"

### Expected Result
- Your app will be live at: `https://p-doomsday-dashboard.streamlit.app`
- Streamlit Cloud handles all server management
- Auto-deploys on git push

## Deploy Backend API

### Option 1: Heroku

```bash
cd backend

# Login to Heroku
heroku login

# Create new app
heroku create p-doomsday-api

# Set environment variables
heroku config:set ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app

# Create Procfile
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile

# Deploy
git subtree push --prefix backend heroku main

# Or if you need to force push:
# git push heroku `git subtree split --prefix backend main`:main --force
```

### Option 2: Railway

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select: `robotwist/p-doomsday-dashboard`
4. Root directory: `backend`
5. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables:
   ```
   ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app
   PORT=8000
   ```
7. Deploy

### Option 3: Render

1. Go to https://render.com
2. New → Web Service
3. Connect repository: `robotwist/p-doomsday-dashboard`
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3
5. Add environment variables:
   ```
   ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app
   ```
6. Create Web Service

## Connect Everything

After deploying all components, update the URLs:

### 1. Update Frontend API URL
In `frontend/components/config.py`:
```python
API_URL = os.getenv("API_URL", "https://your-backend-api.herokuapp.com")
```

### 2. Update Backend CORS
In `backend/app/main.py` or via environment variable:
```python
ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app
```

### 3. Update Landing Page Links
In `public/index.html`:
```html
<a href="https://p-doomsday-dashboard.streamlit.app" class="cta-button">
```

### 4. Commit and Push
```bash
git add -A
git commit -m "Update production URLs"
git push origin main
```

## Quick Deploy Commands

```bash
# Netlify (static landing page)
cd /home/robwistrand/code/solo/p-doomsday-dashboard
netlify deploy --prod --dir=public

# Streamlit Cloud (frontend app)
# → Use web dashboard at https://streamlit.io/cloud

# Heroku (backend API)
cd backend
git push heroku main  # if already set up
```

## Deployment Checklist

- [ ] Backend API deployed and accessible
- [ ] Frontend Streamlit app deployed
- [ ] Static landing page on Netlify
- [ ] Environment variables configured
- [ ] CORS origins updated
- [ ] API URL updated in frontend
- [ ] Landing page links working
- [ ] GitHub repository up to date
- [ ] Custom domains configured (optional)

## Environment Variables Summary

### Backend (.env)
```bash
ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app,https://yourdomain.com
PORT=8000
```

### Frontend (Streamlit Secrets)
```toml
API_URL = "https://your-backend-api.herokuapp.com"
```

## Troubleshooting

### "CORS error" in browser console
- Check `ALLOWED_ORIGINS` in backend includes your frontend URL
- Restart backend after changing environment variables

### "Connection refused" errors
- Verify backend is running: `curl https://your-backend-api.herokuapp.com`
- Check backend logs for errors
- Ensure API_URL in frontend matches backend URL

### Streamlit app won't start
- Check `requirements.txt` includes all dependencies
- Verify Python version compatibility
- Check Streamlit Cloud logs for specific errors

### Netlify redirects not working
- Check `netlify.toml` is in root directory
- Verify redirect URLs are correct
- Clear browser cache

## Notes

- Netlify is free for static sites with generous bandwidth
- Streamlit Community Cloud is free for public GitHub repos
- Heroku free tier was discontinued - use Railway/Render instead
- Always use HTTPS in production for security
- Consider adding authentication for sensitive features

## Useful Links

- **Netlify Docs**: https://docs.netlify.com
- **Streamlit Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Railway Docs**: https://docs.railway.app
- **Render Docs**: https://render.com/docs
- **Heroku Docs**: https://devcenter.heroku.com

---

**Current Deployment Status**:
- Landing Page: Pending Netlify deployment
- Streamlit App: Ready for Streamlit Cloud
- Backend API: Ready for deployment platform of choice

