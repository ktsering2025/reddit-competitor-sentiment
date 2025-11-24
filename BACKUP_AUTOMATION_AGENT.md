# 🤖 Backup Automation Agent - Local Cron Setup

**Purpose:** Automatic weekly reports even if GitHub Actions fails  
**Runs:** Every Sunday at 8:00 PM EST automatically  
**Location:** Your Mac (must be on and awake)

---

## 🎯 **Why You Need This:**

GitHub Actions cron is **unreliable** (industry-wide issue). This backup ensures reports always send on time.

**Primary:** GitHub Actions (cloud-based, no laptop needed)  
**Backup:** Local cron agent (runs on your Mac)

If GitHub Actions fails, your Mac will send the reports automatically.

---

## ⚡ **One-Time Setup (5 Minutes):**

### **Step 1: Install the Cron Job**

Open Terminal and run:

```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
./setup_local_cron.sh
```

This installs a background agent that runs every Sunday at 8 PM.

---

### **Step 2: Verify Installation**

Check if it's installed:

```bash
crontab -l
```

You should see:

```
0 20 * * 0 cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment && /usr/bin/python3 complete_automation.py >> automation.log 2>&1
```

✅ **If you see this, the agent is installed!**

---

### **Step 3: Keep Mac Awake on Sundays**

The cron job only runs if your Mac is:
- ✅ Powered on
- ✅ Awake (not sleeping)

**Option A: Plug in your Mac**
- Plugged-in Macs don't sleep automatically

**Option B: Change Energy Settings**
1. System Settings → Energy Saver
2. Check "Prevent automatic sleeping when display is off"

**Option C: Use Caffeinate (Temporary)**
Run this before 8 PM on Sundays:
```bash
caffeinate -u -t 7200  # Keeps Mac awake for 2 hours
```

---

## 🔄 **How It Works:**

### **Every Sunday at 8:00 PM EST:**

```
1. Cron agent wakes up
2. Checks if it's Sunday 8 PM
3. Runs: complete_automation.py
   ├─ Scrapes Reddit
   ├─ Generates reports
   ├─ Updates website
   └─ Sends emails to all 5 recipients
4. Logs everything to automation.log
5. Goes back to sleep
```

**Total time:** ~3 minutes  
**Your involvement:** None (fully automatic)

---

## ✅ **Verification:**

### **Check 1: Cron Job Exists**
```bash
crontab -l
```
Should show the cron job.

---

### **Check 2: Test Run (Without Email)**
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
python3 complete_automation.py --no-send
```

This runs the full pipeline without sending emails (for testing).

---

### **Check 3: View Logs**
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
tail -50 automation.log
```

Shows recent automation activity.

---

### **Check 4: Next Sunday**
After 8 PM on Sunday, check:

```bash
tail -100 automation.log | grep "Email"
```

Should show email send confirmations.

---

## 🚨 **Troubleshooting:**

### **"Cron didn't run on Sunday"**

**Possible reasons:**
1. Mac was asleep/off at 8 PM
2. Mac was restarting
3. Cron service was disabled

**Solution:**
```bash
# Check if cron is running
ps aux | grep cron

# Restart cron (if needed)
sudo launchctl stop com.vix.cron
sudo launchctl start com.vix.cron
```

---

### **"Emails didn't send"**

**Check logs:**
```bash
tail -100 automation.log
```

Look for errors like:
- "GMAIL_APP_PASSWORD not found"
- "SMTP authentication failed"
- "Reddit API error"

**Solution:** Environment variables might not be loaded. Run manually:
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
python3 complete_automation.py
```

---

### **"I want to disable the cron job"**

```bash
crontab -r
```

This removes the cron job. You can always reinstall it later.

---

## 🔧 **Advanced: Dual-Agent Setup (Maximum Reliability)**

### **How It Works:**

```
Sunday 8:00 PM EST:
├─ GitHub Actions tries to run (primary)
│  └─ If succeeds: ✅ Emails sent
│  └─ If fails: ❌ Nothing happens
│
└─ Local Cron runs 5 minutes later (backup)
   └─ Checks if GitHub Actions succeeded
   └─ If not: Sends emails as backup
```

### **Setup:**

Modify the cron job to run at 8:05 PM (5 minutes after GitHub Actions):

```bash
crontab -e
```

Change:
```
0 20 * * 0 ...
```

To:
```
5 20 * * 0 ...
```

Now the local agent runs 5 minutes after GitHub Actions as a safety net.

---

## 📊 **Monitoring:**

### **Weekly Checklist (Every Monday Morning):**

- [ ] Check email: Did you receive Sunday's report?
- [ ] Check GitHub Actions: Did it run successfully?
- [ ] Check automation.log: Any errors?

If all 3 are ✅, everything is working!

---

## 🎯 **Recommended Setup:**

**For Maximum Reliability:**

1. ✅ Keep GitHub Actions enabled (primary)
2. ✅ Install local cron agent (backup)
3. ✅ Set calendar reminder to verify emails arrived
4. ✅ Check logs weekly for issues

**This gives you 2 layers of protection:**
- GitHub Actions (cloud, no laptop needed)
- Local cron (backup, requires laptop on)

---

## 📝 **Quick Commands:**

### **View cron jobs:**
```bash
crontab -l
```

### **Edit cron jobs:**
```bash
crontab -e
```

### **Remove all cron jobs:**
```bash
crontab -r
```

### **Test automation (no email):**
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
python3 complete_automation.py --no-send
```

### **Test automation (with email):**
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
python3 complete_automation.py
```

### **View recent logs:**
```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment
tail -50 automation.log
```

---

## ✅ **Status Check:**

To verify everything is set up correctly:

```bash
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment

echo "=== BACKUP AUTOMATION STATUS ==="
echo ""
echo "1. Cron Job:"
crontab -l 2>&1 | grep reddit || echo "❌ Not installed"
echo ""
echo "2. Python Script:"
test -f complete_automation.py && echo "✅ Found" || echo "❌ Missing"
echo ""
echo "3. Environment Variables:"
test -f .env && echo "✅ Found" || echo "❌ Missing"
echo ""
echo "4. Recent Logs:"
test -f automation.log && tail -5 automation.log || echo "❌ No logs yet"
```

---

**With this backup agent, you'll never miss a weekly report!** 🚀
