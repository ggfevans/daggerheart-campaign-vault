# Rapid SaaS Validation Framework

## The 7-Day Validation Sprint

This framework helps you validate SaaS ideas quickly and cheaply before writing any code.

---

## Day 1-2: Market Research Sprint

### Competitor Analysis (4 hours)
1. **Search Queries to Run:**
   - "[Your solution] software"
   - "[Your solution] tools"
   - "[Your solution] SaaS"
   - "[Your solution] for [target industry]"
   - "[Problem statement] solutions"

2. **Document for Each Competitor:**
   - Pricing tiers and model
   - Core features offered
   - Target customer size
   - User reviews/complaints
   - Marketing messaging

3. **Sweet Spot Indicators:**
   - ✅ 3-5 competitors = market validated but not saturated
   - ✅ Prices $50-500/month = SMB willingness to pay
   - ✅ 3+ star average reviews = room for improvement
   - ✅ Common complaints = differentiation opportunities

### TAM Calculation (2 hours)
```
TAM = [# of target companies] × [% who have problem] × [average price point] × 12 months

Example:
- 50,000 dental practices in US
- 80% need better scheduling (40,000)
- Would pay $200/month average
- TAM = 40,000 × $200 × 12 = $96M annually
```

### Willingness to Pay Research (2 hours)
- **LinkedIn Posts:** "What do you currently spend on [problem]?"
- **Reddit Threads:** Search r/[industry] for budget discussions
- **Facebook Groups:** Join industry groups, observe pain discussions
- **Industry Reports:** Search "[industry] software spending"

**Document:** Current spending methods (consultants, tools, time)

---

## Day 3-4: Landing Page Creation & Testing

### Landing Page Components (4 hours to build)

1. **Headline Formula:**
   - "[Achieve desired outcome] without [current pain point]"
   - "The [industry] software that [specific benefit]"
   - "Finally, [solution] that actually [works/is affordable/is simple]"

2. **Essential Sections:**
   ```
   Hero: Headline + Subheadline + CTA
   Problem: 3 bullet points of current pains
   Solution: Your approach in 1 paragraph
   Benefits: 3-5 specific outcomes
   Pricing: 3 tiers with clear value
   CTA: Start free trial / Get early access
   ```

3. **Pricing Display:**
   - **Starter:** $X/month (individual)
   - **Professional:** $Y/month (small team) ← Make this most attractive
   - **Business:** $Z/month (larger team)

### Quick Landing Page Tools
- **Carrd.co:** $19/year, 2-hour setup
- **Webflow:** Free plan, 4-hour setup
- **Unicorn Platform:** $8/month, 2-hour setup
- **ConvertKit Commerce:** Built-in payments

### Testing Channels (2 days, $100 budget)

1. **Reddit Strategy:**
   - Find 3 relevant subreddits
   - Provide value first (answer questions)
   - Soft launch: "I'm building X, would this help?"
   - Target: 50-100 targeted visitors

2. **LinkedIn Outreach:**
   - Connect with 50 target customers
   - Message: "I noticed you work in [industry]. I'm researching how teams handle [problem]. Could I ask you 2 quick questions?"
   - Follow up with landing page link

3. **Facebook Groups:**
   - Join 5 industry groups
   - Engage genuinely for 2 days
   - Share as: "Getting feedback on a tool I'm building"

4. **Google Ads (Optional):**
   - $50 budget, targeted keywords
   - Expected: 100-200 visits
   - Focus on high-intent searches

### Success Metrics
- **Email Signups:** 5-15% = good, >15% = excellent
- **Pre-orders:** 2-5% = good, >5% = excellent
- **Survey Completions:** >20% indicates high interest

---

## Day 5-6: Customer Development Interviews

### Finding Interviewees
1. **From Landing Page:** Email all signups
2. **LinkedIn:** Direct outreach to titles
3. **Warm Intros:** Ask your network
4. **Communities:** Slack groups, forums
5. **Calendly:** Offer 15-min slots

**Goal:** 15-20 interviews scheduled

### Interview Script (Keep to 15 minutes)

**Opening (1 min):**
"Thanks for your time. I'm researching how [role] handles [problem area]. There's no sales pitch - I'm just trying to understand the current state of things."

**Current State Questions (5 min):**
1. "Walk me through how you currently handle [process]"
2. "How much time does this take per [week/month]?"
3. "What's most frustrating about the current approach?"
4. "Have you tried any tools/solutions? What happened?"

**Value Questions (5 min):**
1. "If you could wave a magic wand, what would the ideal solution do?"
2. "How would you measure if a solution was working?"
3. "What would it be worth to solve this problem?"
4. "Who makes the decision to buy tools like this?"

**Validation Questions (4 min):**
1. "If a tool did [proposed solution], would you use it?"
2. "What would you expect to pay monthly?"
3. "What would stop you from buying/using this?"
4. [Show pricing] "Does this seem reasonable?"

**Closing:**
"Would you like early access when we launch?" [If yes, this is validation]

### Analysis Framework
Track responses in spreadsheet:
- Pain severity (1-10)
- Current solution satisfaction (1-10)
- Willingness to pay ($X/month)
- Blocker concerns
- "Very disappointed" test result

**Green lights:**
- Average pain severity >7
- Current satisfaction <5
- WTP within 20% of your target price
- >40% would be "very disappointed" without solution

---

## Day 7: Go/No-Go Decision

### Validation Scorecard

**Market Signals (40 points max):**
- [ ] Competitors exist but have obvious gaps (10 pts)
- [ ] TAM calculation >$10M (10 pts)
- [ ] Current solutions cost >$100/month (10 pts)
- [ ] Growing industry/trend (10 pts)

**Landing Page Results (30 points max):**
- [ ] >10% email conversion (10 pts)
- [ ] >2% pre-order conversion (10 pts)
- [ ] >100 qualified visitors (10 pts)

**Interview Results (30 points max):**
- [ ] >40% "very disappointed" test (10 pts)
- [ ] Clear willingness to pay at target price (10 pts)
- [ ] Consistent feature requests (not scattered) (10 pts)

**Total Score: ___/100**

### Decision Matrix

**80+ Points: "BUILD NOW"**
- You have clear validation
- Start MVP immediately
- Focus on most requested features
- Launch to interview participants first

**60-79 Points: "PIVOT & RETEST"**
- Validation mixed but promising
- Adjust positioning/pricing
- Run another 3-day test
- Focus on biggest objections

**40-59 Points: "MAJOR CONCERNS"**
- Validation is weak
- Consider different market
- May need different solution
- Don't build yet

**<40 Points: "KILL IT"**
- No clear validation
- Move to next idea
- Save lessons learned
- Don't waste more time

---

## Concierge MVP Option (If Score 60+)

Instead of building software, manually deliver the service:

1. **Offer to 5 customers:** "I'll personally do [service] for $X/month"
2. **Deliver manually:** Use existing tools, spreadsheets, your time
3. **Learn the workflow:** Document every step and pain point
4. **Charge real money:** This validates true willingness to pay
5. **Build only proven features:** After 1 month of manual delivery

**Success metrics:**
- 3+ paying customers in week 1
- Retention after month 1
- Clear feature requirements from usage
- Positive testimonials

---

## Common Validation Mistakes to Avoid

1. **Asking hypotheticals:** "Would you use..." vs "Show me how you currently..."
2. **Friends & family feedback:** They're biased, find real customers
3. **Feature obsession:** Validate problem/price before features
4. **Analysis paralysis:** 7 days max, then decide
5. **Free feedback only:** Charging validates real interest
6. **Building first:** Always validate before coding
7. **Broad targeting:** Narrow ICP gets clearer signals

---

## Post-Validation Next Steps

### If Validated (GO):
1. **Week 1:** Choose tech stack, setup development environment
2. **Week 2-3:** Build core feature only (ignore nice-to-haves)
3. **Week 4:** Add payment processing and basic onboarding
4. **Week 5:** Launch to beta users from validation
5. **Week 6+:** Iterate based on usage data

### If Not Validated (NO-GO):
1. **Document learnings:** What assumptions were wrong?
2. **Interview analysis:** What problem did they actually want solved?
3. **Pivot options:** Adjacent problems with more pain?
4. **Next idea:** Apply learnings to new opportunity
5. **Speed:** Start next validation within 48 hours

---

## Tools & Resources

### Landing Pages
- Carrd.co (simplest)
- Unicorn Platform (SaaS focused)
- Webflow (most flexible)

### Email Collection
- ConvertKit (free <1000)
- EmailOctopus (cheapest)
- Buttondown (developer-friendly)

### Payment Testing
- Stripe Payment Links
- Gumroad (quick setup)
- Lemon Squeezy (SaaS-friendly)

### Interview Scheduling
- Calendly (free tier)
- Cal.com (open source)
- Google Calendar appointments

### Analytics
- Plausible (privacy-friendly)
- SimpleAnalytics (easy setup)
- Google Analytics (free)

---

*Remember: The goal is to fail fast and cheap. Every NO saves you months of wasted effort and gets you closer to your YES.*