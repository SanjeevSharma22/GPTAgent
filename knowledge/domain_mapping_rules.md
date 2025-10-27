# Domain Mapping Rules and Logic

## Matching Algorithm

### 1. Exact Match (Confidence: 0.95-0.99)
- Direct string match with company name or known aliases
- Case-insensitive comparison
- Preserves special characters (AT&T, O'Reilly, A+B)
- Highest priority matching method

### 2. Fuzzy Match (Confidence: 0.80-0.94)
- String similarity using Levenshtein distance
- Threshold: >90% similarity
- Accounts for:
  - Minor spelling variations
  - Abbreviations vs full names
  - Common typos

### 3. Contextual Match (Confidence: 0.70-0.93)
- Considers additional context factors:
  - **Country**: Boosts regional domains (+0.1-0.15)
  - **Industry**: Validates business sector alignment (+0.05-0.10)
  - **Size**: Matches company scale expectations (+0.02-0.05)
  - **Keywords**: Relevant business terms (+0.03-0.08)

### 4. Web Search Fallback (Confidence: 0.60-0.85)
- Triggered when internal matches < 0.80 confidence
- Uses targeted search queries
- Validates results through domain analysis

## Scoring Formula

```
Final_Score = Base_Match_Score + Country_Weight + Industry_Weight + Size_Weight + Keyword_Weight + Historical_Reputation

Where:
- Base_Match_Score: 0.60-0.99 (exact/fuzzy match quality)
- Country_Weight: 0.0-0.15 (geographic relevance)
- Industry_Weight: 0.0-0.10 (sector alignment)
- Size_Weight: 0.0-0.05 (scale appropriateness)
- Keyword_Weight: 0.0-0.08 (content relevance)
- Historical_Reputation: 0.0-0.05 (known accuracy)
```

## Special Handling Rules

### Legal Suffixes
Remove only at end of string:
- Ltd, Inc, Corp, LLC, Pvt Ltd, GmbH, SA, PLC
- Preserve if part of brand (e.g., "3M Corp" → keep "Corp")

### Special Characters
Always preserve:
- Ampersands: AT&T, H&M, P&G
- Apostrophes: O'Reilly, McDonald's
- Hyphens: Jean-Claude, T-Mobile
- Plus signs: A+B Engineering, C++
- Numbers: 3M, 7-Eleven

### Regional Domain Selection
1. **Country-specific TLD**: .co.uk, .de, .jp
2. **Country path**: /en-gb, /de-de
3. **Subdomain**: uk.company.com
4. **Default to global**: company.com

### Multinational Company Logic
- **No country context**: Return global domain
- **Country specified**: Prefer regional variant
- **Multiple regions**: Show alternatives
- **Subsidiary context**: Use business unit domain

## Confidence Thresholds

| Range | Action | User Communication |
|-------|--------|--------------------|
| 0.95-1.0 | Auto-return result | High confidence statement |
| 0.80-0.94 | Return with note | Medium confidence + reasoning |
| 0.60-0.79 | Return with warning | Low confidence + alternatives |
| <0.60 | Web search fallback | Uncertainty acknowledgment |

## Quality Validation

### Domain Verification Checks
1. **DNS Resolution**: Domain must resolve
2. **HTTP Response**: Returns valid web page
3. **Brand Indicators**: Logo, copyright, company name present
4. **Content Relevance**: Industry-appropriate content
5. **Official Markers**: About Us, Contact, Legal pages

### False Positive Prevention
- Filter out: News sites, directories, social media
- Validate: Domain ownership, brand consistency
- Cross-check: Multiple source confirmation

## Ambiguity Resolution

### Multiple Strong Matches
- Present top 2-3 options
- Explain differences (geography, business unit)
- Ask for clarification
- Default to most global/primary

### Parent/Subsidiary Disambiguation
- Use industry context
- Consider company size
- Check keyword relevance
- Prefer specific business unit if context clear

## Error Handling

### No Match Found
- Acknowledge uncertainty
- Suggest web search approach
- Request additional context
- Provide similar company examples

### Low Confidence Results
- Clearly state uncertainty level
- Explain reasoning process
- Offer verification suggestions
- Provide multiple alternatives

## Continuous Learning

### Feedback Integration
- User corrections update confidence scores
- Track successful vs failed mappings
- Adjust algorithm weights based on performance
- Maintain audit log of decisions

### Knowledge Base Updates
- Regular refresh from authoritative sources
- Incorporate new company formations
- Update domain changes and acquisitions
- Validate and clean existing entries