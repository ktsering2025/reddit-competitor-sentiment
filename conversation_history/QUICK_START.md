# ⚡ Quick Start - Conversation History

**Copy-paste this every time you start a new session!**

---

## 🎬 Before You Start

```bash
# Navigate to project
cd /Users/kunsang.tsering/Desktop/reddit-competitor-sentiment

# Create today's session file
touch conversation_history/$(date +%Y-%m-%d)_session.md

# Open it in your editor
open conversation_history/$(date +%Y-%m-%d)_session.md
```

---

## 📋 Copy This Template

```markdown
# 💬 Conversation - December XX, 2025

**Time:** [Start time]

---

## 🎯 Goals
- 
- 
- 

---

## 💬 Log

### [Time] - 
**Me:** 

**AI:** 

**Result:** 

---

### [Time] - 
**Me:** 

**AI:** 

**Result:** 

---

## 📝 Changes Made
- 
- 

---

## ✅ Completed
- [x] 
- [x] 

## ⏳ Next Time
- [ ] 
- [ ] 

---

**End:** [End time]
```

---

## 💡 Remember

1. **Update as you go** - Don't wait until the end!
2. **Save often** - Cmd+S / Ctrl+S
3. **Be specific** - "Fixed email spam" not "fixed stuff"
4. **Include context** - Why did you make this change?

---

## 🔍 Useful Commands

```bash
# View all sessions
ls conversation_history/

# Read latest session
cat conversation_history/$(ls -t conversation_history/*.md | head -1)

# Search for topic
grep -r "automation" conversation_history/
```

---

**That's it! Start logging! 📝**
