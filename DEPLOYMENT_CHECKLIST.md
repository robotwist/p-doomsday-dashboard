# Deployment Checklist

## Pre-Deployment

- [x] 23 professions added to backend
- [x] All emojis removed (text-only design)
- [x] Error handling implemented
- [x] Social sharing enhanced (5 platforms)
- [x] Dynamic job list in sidebar
- [x] Feedback section added
- [x] Environment variables configured
- [x] Meta tags added for SEO
- [x] README updated with deployment instructions
- [x] Git repository up to date

## Netlify Deployment (Static Landing Page)

### Quick Deploy
1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Connect GitHub account
4. Select repository: `robotwist/p-doomsday-dashboard`
5. Configure build settings:
   - **Build command**: (leave empty)
   - **Publish directory**: `public`
   - **Branch**: `main`
6. Click "Deploy site"

### After Deployment
- [ ] Copy your Netlify URL (e.g., `https://your-site.netlify.app`)
- [ ] Update `public/index.html` meta tags with actual URL
- [ ] Update `README.md` with actual Netlify URL
- [ ] Test redirects: `/app` and `/calculator` should redirect to Streamlit
- [ ] Verify landing page displays correctly
- [ ] Check mobile responsiveness

## Streamlit Cloud Deployment (Main App)

1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click "New app"
4. Configure:
   - **Repository**: `robotwist/p-doomsday-dashboard`
   - **Branch**: `main`
   - **Main file path**: `frontend/app.py`
   - **App URL**: Choose your subdomain
5. Click "Deploy!"

### Environment Variables (Optional)
If you deploy the backend:
```toml
API_URL = "https://your-backend.herokuapp.com"
APP_URL = "https://p-doomsday-dashboard.streamlit.app"
```

### After Deployment
- [ ] App is live and accessible
- [ ] All 23 jobs display in sidebar
- [ ] Job search works correctly
- [ ] DOOM meter displays
- [ ] Social sharing buttons work
- [ ] Error handling displays friendly messages
- [ ] All tabs (DOOM CALCULATOR, RETRAIN ME, SURVIVAL GUIDE) work
- [ ] Resources links are clickable
- [ ] Feedback section is visible

## Backend Deployment (Optional - Currently Local)

**Note**: Backend currently runs locally. Deploy when you need production API.

### Option 1: Railway
```bash
cd backend
railway login
railway init
railway up
railway open
```

### Option 2: Render
1. Go to https://render.com
2. New → Web Service
3. Connect: `robotwist/p-doomsday-dashboard`
4. Settings:
   - Root: `backend`
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Environment: `ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app`

### After Backend Deployment
- [ ] Update `frontend/components/config.py` with API URL
- [ ] Update Streamlit Cloud environment variable `API_URL`
- [ ] Test API connectivity from frontend
- [ ] Verify CORS settings work

## Post-Deployment Testing

### Functionality Tests
- [ ] Search for all 23 jobs works
- [ ] Invalid job shows helpful error message
- [ ] DOOM meter calculates correctly
- [ ] Share buttons open correct platforms
- [ ] Copy link button works
- [ ] Email share opens mail client
- [ ] All resource links work
- [ ] Biblical resources display
- [ ] Church finder displays
- [ ] Footer links work

### Performance Tests
- [ ] Page loads in < 3 seconds
- [ ] Images load correctly
- [ ] No console errors
- [ ] Mobile responsive
- [ ] Works on Chrome, Firefox, Safari

### SEO & Social
- [ ] Meta tags present
- [ ] Social share preview looks good (use https://www.opengraph.xyz/)
- [ ] Title and description accurate
- [ ] Links work when shared

## Marketing Preparation

- [ ] Screenshot DOOM meter results
- [ ] Create social media posts
- [ ] Prepare launch tweet
- [ ] Share on relevant subreddits (r/dataisbeautiful, r/programming, r/automation)
- [ ] Post to LinkedIn
- [ ] Share in relevant Discord/Slack communities
- [ ] Consider Product Hunt launch

## Monitoring

- [ ] Check Streamlit Cloud logs for errors
- [ ] Monitor Netlify deployment status
- [ ] Set up basic analytics (Google Analytics placeholder ready)
- [ ] Watch for GitHub issues/feedback

## Quick Launch Command

```bash
# Final commit
git add -A
git commit -m "Production ready - deploy to Netlify and Streamlit Cloud"
git push origin main

# Then manually deploy via dashboards
```

## Rollback Plan

If something breaks:
1. Netlify: Click "Rollback to previous deploy" in dashboard
2. Streamlit: Revert git commit and redeploy
3. Backend: Stop dyno/service if issues arise

---

**Last Updated**: 2025-10-21  
**Status**: Ready for deployment  
**Version**: 1.0 Beta

