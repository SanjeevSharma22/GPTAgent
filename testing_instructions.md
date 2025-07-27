# How to Test the Company Domain Mapper Agent

## 🧪 Testing Options Overview

You have several ways to test this agent depending on your current stage:

### 1. **Pre-Deployment Testing** (Recommended First Step)
### 2. **Local GPT Testing** (Using OpenAI's GPT Builder)
### 3. **Production Testing** (After ChatGPT Store deployment)
### 4. **API Testing** (For developers)

---

## 🔨 Option 1: Pre-Deployment Testing (Start Here!)

### Quick Knowledge Base Validation

First, verify what companies are in your database:

**Available Test Companies:**
- Microsoft, Apple, Tesla, Amazon, Google
- Tata Motors, Toyota, AT&T, Unilever, IBM
- Samsung, O'Reilly

**Quick Manual Tests:**
1. **Exact Match**: "Microsoft" → should return "microsoft.com"
2. **Special Characters**: "AT&T" → should return "att.com"
3. **Regional**: "Tata Motors + UK context" → should return "tatamotors.co.uk"

### Run Test Cases Manually

Open `test_cases.md` and manually verify the logic:

**Example Test:**
```
Input: "Find domain for Microsoft"
Expected: microsoft.com with 0.99 confidence
Logic: Should find exact match in company database
```

---

## 🏗️ Option 2: Local GPT Testing (Recommended!)

This is the **best way** to test before deployment:

### Step 1: Access GPT Builder
1. Go to https://chat.openai.com
2. Click "Explore" → "Create a GPT"
3. Create a **private test version**

### Step 2: Configure Test GPT
1. **Name**: "Company Domain Mapper - TEST"
2. **Instructions**: Copy from `gpt_instructions.txt`
3. **Knowledge**: Upload all files from `knowledge/` folder
4. **Capabilities**: Enable Web Browsing

### Step 3: Run Live Tests

#### Test Set 1: Basic Functionality
```
Test: "Find domain for Microsoft"
Expected: High confidence exact match

Test: "Map Apple to domain"
Expected: apple.com with explanation

Test: "What's AT&T's website?"
Expected: att.com (preserving &)
```

#### Test Set 2: Contextual Matching
```
Test: "Find Tata Motors domain in UK"
Expected: tatamotors.co.uk with regional context

Test: "Map Toyota for European market"
Expected: toyota-europe.com or similar with explanation
```

#### Test Set 3: Batch Processing
```
Test: "Map these: Apple, Google, Tesla"
Expected: Structured output for all three companies
```

#### Test Set 4: Edge Cases
```
Test: "Find domain for XYZ Nonexistent Company"
Expected: Graceful handling, no match found message

Test: "Map Mircosoft" (typo)
Expected: Fuzzy match to Microsoft
```

### Step 4: Validate Output Format

Each response should include:
- Company name
- Domain
- Confidence score (0.0-1.0)
- Match type (Exact/Fuzzy/Contextual/Web Search)
- Notes/reasoning
- Alternatives (when applicable)

---

## 🎯 Option 3: Quick Command Line Testing

Create a simple test script to validate the knowledge base:

### Create Test Script
```bash
# Create a simple test script
cat > test_knowledge.py << 'EOF'
import json

# Load company database
with open('knowledge/company_database.json', 'r') as f:
    data = json.load(f)

# Test basic lookups
test_companies = ['Microsoft', 'Apple', 'AT&T', 'Tata Motors']

print("=== Knowledge Base Test ===")
for company in test_companies:
    found = False
    for entry in data['companies']:
        if entry['name'].lower() == company.lower() or company in entry.get('aliases', []):
            print(f"✅ {company}: {entry['primary_domain']} (confidence: {entry['confidence']})")
            found = True
            break
    if not found:
        print(f"❌ {company}: Not found in database")

print(f"\nTotal companies in database: {len(data['companies'])}")
EOF

# Run the test
python test_knowledge.py
```

---

## 🌐 Option 4: Production Testing (After Deployment)

### Once Deployed to ChatGPT Store:

#### Access Your GPT
1. Go to ChatGPT
2. Find your "Company Domain Mapper" in the GPT store
3. Start a conversation

#### Production Test Suite

**Test 1: Exact Matches**
```
"Find domains for these major companies: Microsoft, Apple, Google"
```

**Test 2: Regional Intelligence**
```
"I need the UK website for Tata Motors"
```

**Test 3: Special Characters**
```
"What's the domain for AT&T and O'Reilly?"
```

**Test 4: Fuzzy Matching**
```
"Find domain for Mircosoft" (intentional typo)
```

**Test 5: Web Search Fallback**
```
"Map [some local business name] to domain"
```

#### Monitor Performance
- Response times
- Accuracy of results
- User feedback
- Error rates

---

## 🚀 Quick Start Testing (5 Minutes)

### Fastest Way to Test Right Now:

1. **Manual Database Check**:
   ```bash
   # Check what companies are available
   grep -A 5 -B 1 '"name"' knowledge/company_database.json
   ```

2. **Logic Validation**:
   - Microsoft → microsoft.com ✓
   - AT&T → att.com ✓ 
   - Tata Motors + UK → tatamotors.co.uk ✓

3. **Create Test GPT** (15 minutes):
   - Go to chat.openai.com
   - Create new GPT
   - Upload knowledge files
   - Test with real queries

---

## 📋 Testing Checklist

### Before Deployment:
- [ ] Knowledge base files are valid JSON/Markdown
- [ ] All major companies in database have correct domains
- [ ] Instructions file is complete and properly formatted
- [ ] Test GPT created and basic functionality verified

### During Testing:
- [ ] Exact matches work for known companies
- [ ] Special characters preserved (AT&T, O'Reilly)
- [ ] Regional context improves results appropriately
- [ ] Confidence scores make sense
- [ ] Error handling is graceful
- [ ] Output format is consistent

### Ready for Deployment:
- [ ] All test cases pass
- [ ] Performance is acceptable (<3 seconds response)
- [ ] Edge cases handled properly
- [ ] User experience is smooth

---

## 🔧 Troubleshooting Common Issues

### "No results found"
- Check if company is in `knowledge/company_database.json`
- Verify spelling and try aliases
- Test with web browsing enabled

### "Low confidence scores"
- Check company entry in database
- Verify context matching logic
- Test with additional context (country, industry)

### "Slow responses"
- Check if web browsing is enabled when not needed
- Optimize knowledge base size
- Test with exact matches first

### "Inconsistent format"
- Verify instructions are properly formatted
- Check response templates in `actions.json`
- Test with multiple queries

---

## 💡 Pro Testing Tips

1. **Start Simple**: Test exact matches first
2. **Use Known Companies**: Stick to database entries initially
3. **Check Edge Cases**: Test with typos and special characters
4. **Monitor Performance**: Track response times
5. **Collect Feedback**: Note any unexpected behavior
6. **Iterative Testing**: Test → Fix → Test again

**Ready to start testing? Begin with Option 2 (Local GPT Testing) for the best experience!** 🎯