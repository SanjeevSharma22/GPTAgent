# Test Cases for Company Domain Mapper Agent

## Overview
This document contains comprehensive test cases to validate the Company Domain Mapper agent's functionality before deployment to the ChatGPT store.

## 🧪 Test Categories

### 1. Exact Match Tests

#### Test 1.1: Major Technology Companies
**Input**: "Find domain for Microsoft"
**Expected Output**:
```
**Company**: Microsoft
**Domain**: microsoft.com
**Confidence**: 0.99
**Match Type**: Exact
**Notes**: Major US technology company, primary global domain
```

#### Test 1.2: Companies with Special Characters
**Input**: "What's the domain for AT&T?"
**Expected Output**:
```
**Company**: AT&T
**Domain**: att.com
**Confidence**: 0.98
**Match Type**: Exact
**Notes**: Major US telecommunications company, preserves ampersand
```

#### Test 1.3: Company with Apostrophe
**Input**: "Find domain for O'Reilly"
**Expected Output**:
```
**Company**: O'Reilly
**Domain**: oreilly.com
**Confidence**: 0.96
**Match Type**: Exact
**Notes**: Technology publishing company, preserves apostrophe
```

### 2. Fuzzy Matching Tests

#### Test 2.1: Minor Spelling Variation
**Input**: "Find domain for Mircosoft"
**Expected Output**:
```
**Company**: Microsoft (corrected from Mircosoft)
**Domain**: microsoft.com
**Confidence**: 0.91
**Match Type**: Fuzzy
**Notes**: Corrected spelling variation, high confidence match
```

#### Test 2.2: Abbreviation vs Full Name
**Input**: "Map IBM to domain"
**Expected Output**:
```
**Company**: IBM
**Domain**: ibm.com
**Confidence**: 0.99
**Match Type**: Exact
**Notes**: Matches both IBM and International Business Machines
```

### 3. Contextual Matching Tests

#### Test 3.1: Regional Context
**Input**: "Find domain for Tata Motors in the UK"
**Expected Output**:
```
**Company**: Tata Motors
**Domain**: tatamotors.co.uk
**Confidence**: 0.88
**Match Type**: Contextual
**Notes**: UK-specific automotive division of Tata Group
**Alternatives**: tatamotors.com (global), tata.com (parent company)
```

#### Test 3.2: Industry Context
**Input**: "Map Toyota automotive company"
**Expected Output**:
```
**Company**: Toyota
**Domain**: toyota.com
**Confidence**: 0.98
**Match Type**: Contextual
**Notes**: Major Japanese automotive manufacturer
**Alternatives**: toyota.co.uk (UK), toyota.de (Germany)
```

#### Test 3.3: Country and Industry Context
**Input**: "Find domain for Unilever consumer goods in Germany"
**Expected Output**:
```
**Company**: Unilever
**Domain**: unilever.de
**Confidence**: 0.92
**Match Type**: Contextual
**Notes**: German regional site for multinational consumer goods company
**Alternatives**: unilever.com (global)
```

### 4. Batch Processing Tests

#### Test 4.1: Multiple Major Companies
**Input**: "Map these companies to domains: Apple, Google, Tesla"
**Expected Output**:
```
**Company**: Apple
**Domain**: apple.com
**Confidence**: 0.99
**Match Type**: Exact
**Notes**: Major US consumer electronics company

**Company**: Google
**Domain**: google.com
**Confidence**: 0.99
**Match Type**: Exact
**Notes**: Major US internet services company

**Company**: Tesla
**Domain**: tesla.com
**Confidence**: 0.98
**Match Type**: Exact
**Notes**: US electric vehicle manufacturer
```

#### Test 4.2: Mixed Confidence Levels
**Input**: "Map these companies: Microsoft, Obscure Local Company, Samsung"
**Expected Output**: Should handle mix of high-confidence and low-confidence matches appropriately.

### 5. Ambiguous Cases Tests

#### Test 5.1: Parent Company Ambiguity
**Input**: "Find domain for Tata"
**Expected Output**:
```
**Company**: Tata
**Domain**: tata.com
**Confidence**: 0.85
**Match Type**: Contextual
**Notes**: Tata Group parent company - multiple business units available
**Alternatives**: tatamotors.com (automotive), tatasteel.com (steel), tataconsultancy.com (IT services)
```

#### Test 5.2: Common Company Name
**Input**: "Map Delta to domain"
**Expected Output**: Should present multiple options (Delta Airlines, Delta Faucet, etc.) with explanations.

### 6. Regional Variations Tests

#### Test 6.1: European Focus
**Input**: "Find Toyota's European domain"
**Expected Output**:
```
**Company**: Toyota
**Domain**: toyota-europe.com
**Confidence**: 0.94
**Match Type**: Contextual
**Notes**: Toyota's European operations site
**Alternatives**: toyota.com (global), toyota.co.uk (UK specific)
```

#### Test 6.2: Asian Market
**Input**: "Map Samsung domain for South Korea"
**Expected Output**:
```
**Company**: Samsung
**Domain**: samsung.com
**Confidence**: 0.98
**Match Type**: Contextual
**Notes**: Global domain, Samsung is South Korean company
**Alternatives**: samsung.com/kr (Korean language)
```

### 7. Edge Cases Tests

#### Test 7.1: Non-existent Company
**Input**: "Find domain for XYZ123 Nonexistent Corp"
**Expected Output**:
```
**Company**: XYZ123 Nonexistent Corp
**Status**: No confident match found
**Suggestions**: Verify company name spelling, provide additional context
**Next Steps**: Try providing additional context (country, industry) or verify spelling
```

#### Test 7.2: Very New Company
**Input**: "Map StartupABC to domain"
**Expected Output**: Should acknowledge uncertainty and suggest web search fallback.

#### Test 7.3: Legal Suffix Handling
**Input**: "Find domain for Microsoft Corporation"
**Expected Output**:
```
**Company**: Microsoft Corporation
**Domain**: microsoft.com
**Confidence**: 0.99
**Match Type**: Exact
**Notes**: Strips 'Corporation' suffix for matching, same as Microsoft
```

### 8. Web Search Fallback Tests

#### Test 8.1: Unknown Company
**Input**: "Find domain for Regional Local Business Inc"
**Expected Process**:
1. Internal database search fails
2. Triggers web search fallback
3. Returns result with lower confidence and "Web Search" match type

#### Test 8.2: Recently Founded Company
**Input**: "Map newly founded tech startup to domain"
**Expected**: Should use web search and provide appropriate confidence level.

### 9. Error Handling Tests

#### Test 9.1: Empty Input
**Input**: ""
**Expected Output**:
```
Please provide a valid company name for domain mapping.
```

#### Test 9.2: Invalid Characters
**Input**: "Find domain for @@##$$"
**Expected Output**: Should handle gracefully and request valid company name.

#### Test 9.3: Very Long Input
**Input**: [Very long string]
**Expected**: Should truncate appropriately and attempt matching.

### 10. Performance Tests

#### Test 10.1: Response Time
**Metric**: Response time for exact matches should be < 2 seconds

#### Test 10.2: Large Batch Processing
**Input**: List of 20+ companies
**Expected**: Should handle efficiently with appropriate performance

#### Test 10.3: Concurrent Requests
**Test**: Multiple users querying simultaneously
**Expected**: Consistent performance and accuracy

## 🎯 Success Criteria

### Accuracy Thresholds
- **Exact Matches**: ≥99% accuracy for Fortune 500 companies
- **Fuzzy Matches**: ≥95% accuracy with common variations
- **Contextual Matches**: ≥90% accuracy with proper context
- **Web Fallback**: ≥85% accuracy for findable companies

### Performance Benchmarks
- **Response Time**: <3 seconds for internal database matches
- **Web Search**: <10 seconds for fallback searches
- **Batch Processing**: Linear scaling with input size
- **Error Rate**: <5% for well-formed queries

### User Experience Standards
- **Clear Confidence Indicators**: Always present
- **Helpful Error Messages**: Actionable guidance
- **Alternative Suggestions**: When applicable
- **Consistent Format**: Standardized output structure

## 🔍 Test Execution Protocol

### Pre-Deployment Testing
1. **Smoke Tests**: Run basic functionality tests
2. **Regression Tests**: Verify all test cases pass
3. **Performance Tests**: Validate response times
4. **Edge Case Tests**: Handle error conditions gracefully

### Post-Deployment Monitoring
1. **User Feedback**: Track user corrections and complaints
2. **Accuracy Metrics**: Monitor confidence vs actual accuracy
3. **Performance Metrics**: Response time and error rate tracking
4. **Usage Patterns**: Identify common query types

### Continuous Improvement
1. **Weekly Reviews**: Analyze failed test cases
2. **Monthly Updates**: Refresh knowledge base
3. **Quarterly Assessments**: Full test suite execution
4. **Annual Overhauls**: Major algorithm improvements

## 📊 Test Results Template

### Test Execution Record
```
Test Date: [Date]
Test Environment: [Production/Staging]
Tester: [Name]
Test Suite Version: [Version]

Results Summary:
- Total Tests: [Number]
- Passed: [Number]
- Failed: [Number]
- Success Rate: [Percentage]

Failed Tests:
[List of failed test cases with details]

Performance Metrics:
- Average Response Time: [Seconds]
- 95th Percentile Response Time: [Seconds]
- Error Rate: [Percentage]

Recommendations:
[List of improvements needed]
```

## 🚀 Deployment Readiness Checklist

### Functional Requirements
- [ ] All exact match tests pass (≥99% accuracy)
- [ ] Fuzzy matching works for common variations
- [ ] Contextual matching improves results appropriately
- [ ] Batch processing handles multiple companies
- [ ] Regional variations work correctly
- [ ] Web search fallback functions properly

### Non-Functional Requirements
- [ ] Response times meet performance benchmarks
- [ ] Error handling is graceful and helpful
- [ ] Output format is consistent and clear
- [ ] Confidence scores correlate with accuracy
- [ ] Special character handling works correctly

### Integration Requirements
- [ ] Web browsing capability enabled
- [ ] Knowledge base files uploaded correctly
- [ ] Instructions configured properly
- [ ] Privacy settings configured
- [ ] Store listing content prepared

---

**Ready for deployment when all test cases pass and checklist items are completed!** ✅