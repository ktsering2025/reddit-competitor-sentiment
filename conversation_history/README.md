# 📚 Conversation History Directory

This directory contains detailed logs of all AI assistant conversations for the Reddit Competitor Sentiment Analysis project.

---

## 📁 File Structure

```
conversation_history/
├── README.md                    # This file - explains the system
├── 2025-12-02_session.md       # Today's conversation
├── 2025-12-XX_session.md       # Future sessions
└── [YYYY-MM-DD]_session.md     # Date-based session logs
```

---

## 📝 How to Use This System

### **For Each New Session:**

1. **Create a new file** named with today's date:
   ```
   YYYY-MM-DD_session.md
   ```
   Example: `2025-12-02_session.md`

2. **Use the template below** for consistency

3. **Update throughout the conversation** as you make progress

4. **Save at the end** with a final summary

---

## 📋 Session Template

Copy this template for each new session:

```markdown
# 💬 Conversation History - [Month Day, Year]

**Date:** [Day of week], [Month Day, Year]  
**Session Start:** [Time]  
**Participants:** Kunsang Tsering + AI Assistant (Claude Sonnet 4.5)

---

## 📝 Session Summary

### Goals for This Session
- [What you want to accomplish]
- [Any issues to fix]
- [Features to add]

### What We Accomplished
- [List achievements here as you go]

---

## 🗣️ Conversation Log

### [Time] Topic 1
**User:** "[Your question/request]"

**Assistant Response:**
- [Summary of what was done]
- [Files modified]
- [Commands run]

**Outcome:**
- [What was achieved]

---

### [Time] Topic 2
**User:** "[Your question/request]"

**Assistant Response:**
- [Summary of what was done]

**Outcome:**
- [What was achieved]

---

## 📊 Technical Changes

### Files Modified
1. `path/to/file1.py` - [What changed]
2. `path/to/file2.md` - [What changed]

### Files Created
1. `path/to/new_file.py` - [Purpose]

### Commands Run
```bash
# List important commands executed
command1
command2
```

---

## 🎯 Action Items

### Completed ✅
- [x] Task 1
- [x] Task 2

### Pending ⏳
- [ ] Task 3
- [ ] Task 4

### Future Considerations 💡
- Idea 1
- Idea 2

---

## 📌 Important Notes
- [Any key decisions made]
- [Things to remember for next time]
- [Warnings or gotchas]

---

**Session End:** [Time]  
**Duration:** [X hours/minutes]  
**Next Session:** [If planned]
```

---

## 🔍 Finding Past Conversations

### By Date
Files are named chronologically, so just look for the date:
```bash
ls conversation_history/2025-12-*
```

### Search All Conversations
```bash
grep -r "keyword" conversation_history/
```

### View Latest Session
```bash
ls -t conversation_history/*.md | head -1 | xargs cat
```

---

## 💡 Best Practices

### **Do:**
✅ Create a new file for each work session  
✅ Update the log as you go (don't wait until the end)  
✅ Include code snippets and commands for reference  
✅ Note any decisions or trade-offs made  
✅ Link to related files or documentation  
✅ Save frequently (Cmd+S / Ctrl+S)

### **Don't:**
❌ Don't overwrite old session files  
❌ Don't forget to update the summary section  
❌ Don't skip technical details (they're helpful later)  
❌ Don't delete old conversations (they're valuable history)

---

## 🗂️ Related Documentation

- **Project Summary:** `/PROJECT_SUMMARY.md`
- **Technical Docs:** `/TECHNICAL_DOCUMENTATION.md`
- **Automation Guide:** `/AUTOMATION_EXPLAINED.md`
- **Previous Session:** `/CONVERSATION_SUMMARY.md` (Nov 17, 2025)

---

## 📊 Session History

| Date | Topics Covered | Duration | Key Changes |
|------|---------------|----------|-------------|
| 2025-12-02 | Status review, conversation history setup | Ongoing | Created conversation_history system |
| 2025-11-17 | Automation fixes, email spam issue | ~2 hours | Fixed duplicate emails, updated docs |

---

## 🔄 Maintenance

### Weekly
- No action needed - just create new session files as you work

### Monthly
- Review old sessions for patterns or recurring issues
- Update this README if the template changes

### Yearly
- Archive old conversations if directory gets too large
- Create subdirectories by year if needed (e.g., `2025/`, `2026/`)

---

**Created:** December 2, 2025  
**Last Updated:** December 2, 2025  
**Maintained By:** Kunsang Tsering
