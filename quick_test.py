#!/usr/bin/env python3
import json
import os

print("🧪 Company Domain Mapper - Quick Test")
print("=" * 40)

# Check files exist
files = ['gpt_instructions.txt', 'knowledge/company_database.json']
for f in files:
    if os.path.exists(f):
        print(f"✅ {f}")
    else:
        print(f"❌ {f} - MISSING!")

# Test database
try:
    with open('knowledge/company_database.json', 'r') as f:
        data = json.load(f)
    
    print(f"\n📊 Loaded {len(data['companies'])} companies")
    
    # Test some companies
    test_companies = ['Microsoft', 'Apple', 'AT&T']
    for company in test_companies:
        for entry in data['companies']:
            if entry['name'] == company:
                print(f"✅ {company}: {entry['primary_domain']}")
                break
        else:
            print(f"❌ {company}: Not found")
            
except Exception as e:
    print(f"❌ Error: {e}")

print("\n🚀 Ready for GPT Builder testing!")
