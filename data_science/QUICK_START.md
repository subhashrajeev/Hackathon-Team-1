# 🚀 Quick Start Guide

## Get the Dashboard Running in 3 Minutes

### Step 1: Open Terminal/Command Prompt

**Windows:** Press `Win + R`, type `cmd`, press Enter
**Mac/Linux:** Press `Cmd + Space`, type "terminal", press Enter

### Step 2: Navigate to Project

```bash
cd /path/to/Hackathon-Team-1/data_science
```

### Step 3: Install Requirements (First Time Only)

```bash
pip install -r requirements.txt
```

**Note:** This will take 2-3 minutes. Only needs to be done once.

### Step 4: Run the Dashboard

#### Option A: Using the Script (Recommended)

**Windows:**
```bash
run_dashboard.bat
```

**Mac/Linux:**
```bash
./run_dashboard.sh
```

#### Option B: Direct Command

```bash
streamlit run app/dashboard.py
```

### Step 5: View in Browser

The dashboard will automatically open at: **http://localhost:8501**

If it doesn't open automatically, manually navigate to that URL in your browser.

---

## 🎨 What You'll See

The dashboard has 4 main sections:

1. **🌫️ AQI Monitoring** - Air quality predictions and health alerts
2. **⚡ Outage Prediction** - Utility restoration time estimates
3. **📸 Civic Reporting** - AI image classification for civic issues
4. **🚗 Traffic Analysis** - Route optimization and congestion analysis

---

## 🛠️ Troubleshooting

### "Command not found: streamlit"

**Solution:** Make sure you installed the requirements:
```bash
pip install -r requirements.txt
```

### "No module named 'pandas'" (or other modules)

**Solution:** Install requirements with:
```bash
pip install --upgrade -r requirements.txt
```

### "Port 8501 already in use"

**Solution:** Either:
1. Close any other Streamlit apps running
2. Or use a different port:
```bash
streamlit run app/dashboard.py --server.port 8502
```

### "Permission denied" (Mac/Linux)

**Solution:** Make the script executable:
```bash
chmod +x run_dashboard.sh
```

---

## 🔍 Exploring the Project

### View the Notebooks

1. Install Jupyter (if not already installed):
   ```bash
   pip install jupyter
   ```

2. Launch Jupyter:
   ```bash
   jupyter notebook notebooks/
   ```

3. Open:
   - `01_exploratory_data_analysis.ipynb` - Data analysis and insights
   - `02_model_training_evaluation.ipynb` - Model development and evaluation

### Check the Code

- `app/dashboard.py` - Main dashboard application
- `utils/predictors.py` - ML model prediction logic
- `utils/data_generator.py` - Data generation utilities

---

## 📱 Sharing with Others

### Option 1: Screen Share
Simply share your screen during a video call

### Option 2: Local Network Access
Others on your network can access at: `http://YOUR_IP:8501`

To find your IP:
- **Windows:** `ipconfig` (look for IPv4 Address)
- **Mac/Linux:** `ifconfig` (look for inet address)

### Option 3: Deploy to Cloud (Advanced)
- Deploy to Streamlit Cloud (free)
- Deploy to Heroku, AWS, or Azure

---

## ⏹️ Stopping the Dashboard

Press `Ctrl + C` in the terminal where the dashboard is running.

---

## 📞 Need Help?

Check the full README.md for:
- Detailed documentation
- Technical explanations
- Advanced configuration
- Troubleshooting guide

---

**That's it! You should now have a working dashboard. Enjoy exploring!** 🎉
