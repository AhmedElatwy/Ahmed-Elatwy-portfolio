# 💡 Business Recommendations: Olist Retention Analysis

> *Actionable insights from analyzing 100K+ e-commerce orders*

---

## 🎯 Executive Summary

**Problem**: 96.9% of Olist customers never make a second order.  
**Opportunity**: Improving repeat rate from 3.12% → 5% = **+312K BRL/month revenue**.  
**Strategy**: Target high-potential segments with tailored retention tactics.

---

## 🔑 Key Insights

### 1. The Biggest Leak: First → Second Order

Funnel Drop-off:
• 96,096 customers make 1st order
• 2,997 make 2nd order (3.12%)
• Lost: 93,099 potential repeat customers
**Why it matters**: Acquiring a new customer costs 5-25x more than retaining an existing one. Fixing this leak has the highest ROI.

### 2. Category Matters: Essentials Retain Better

Repeat Rate by First-Purchase Category (min 500 customers):
• Furniture/Decor: 26.6% ← Highest
• Office Furniture: 22.8%
• Garden Tools: 21.6%
• ...
• Toys: 10.2% ← Lowest
• Watches/Gifts: 9.8%
• Cool Stuff: 8.4%

**Hypothesis**: Essential items drive habitual purchases; discretionary items are one-off buys.

### 3. Retention Is Declining Over Time

Cohort Trend (Jan 2017 → Aug 2018):
• Starting repeat rate: ~21%
• Ending repeat rate: ~11%
• Decline: -0.28% per month (p<0.001, R²=0.70)

**Implication**: Something changed in 2018 — product quality, competition, or customer expectations.

### 4. Geographic Variation Is Significant

Top Cities by Repeat Rate (min 100 customers):
• Petrópolis: 6.4% (2.37x average)
• Aparecida de Goiânia: 5.8%
• Pouso Alegre: 5.6%

**Opportunity**: Investigate what these cities do right — then replicate elsewhere.

---

## 🚀 Prioritized Recommendations

### 🔥 Priority 1: Launch 2nd-Order Incentive (High Impact, Low Effort)
| Component | Detail |
|-----------|--------|
| **Action** | Email 15% discount code to first-time buyers within 30 days of purchase |
| **Target** | Customers who bought non-essential categories (toys, gifts, cool stuff) |
| **Expected Impact** | +20% second-order conversion → ~600 additional repeat customers/month |
| **Revenue Impact** | 600 × 172.73 BRL = **+103K BRL/month** |
| **Owner** | Marketing Team |
| **Effort** | Low (1-week sprint: email template + automation) |
| **Timeline** | Launch in 2 weeks; measure results at 30/60/90 days |
| **Success Metric** | Second-order conversion rate for targeted segment |

### 🔥 Priority 2: Feature Home Essentials for New Buyers (High Impact, Medium Effort)
| Component | Detail |
|-----------|--------|
| **Action** | Homepage personalization: Show furniture/garden categories to first-time visitors |
| **Target** | New users with no purchase history |
| **Expected Impact** | Increase % of first orders in high-retention categories → +15% overall repeat rate |
| **Revenue Impact** | Modeled: +209K BRL/month (combined with Priority 1) |
| **Owner** | Product + Engineering |
| **Effort** | Medium (2-week sprint: recommendation logic + A/B test setup) |
| **Timeline** | Prototype in 2 weeks; full rollout after validation |
| **Success Metric** | % of first orders in high-retention categories; cohort repeat rate |

### ⚠️ Priority 3: Investigate Retention Decline (Medium Impact, Low Effort)
| Component | Detail |
|-----------|--------|
| **Action** | Survey 500 customers from 2018 cohorts who didn't return: "What nearly stopped you from buying again?" |
| **Target** | Customers with 1 order, no repeat within 60 days |
| **Expected Impact** | Identify top 3 barriers → fix highest-impact issue → +10% repeat rate |
| **Revenue Impact** | Conservative: +50K BRL/month |
| **Owner** | Customer Service + Product Research |
| **Effort** | Low (2 weeks: survey design + analysis) |
| **Timeline** | Results in 3 weeks; action plan in 4 weeks |
| **Success Metric** | Survey response rate; % of actionable insights identified |

---

## 📈 Revenue Impact Model

### Assumptions
- AOV: 172.73 BRL (calculated from dataset)
- Current repeat rate: 3.12%
- Target repeat rate: 5.0%
- Total customers: 96,096
- USD conversion: 5.0 BRL = 1 USD (for reference only)

### Calculation
Current repeat revenue:
96,096 customers × 3.12% × 172.73 BRL = 517,687 BRL
Target repeat revenue (at 5%):
96,096 customers × 5.0% × 172.73 BRL = 829,958 BRL
Upside:
829,958 - 517,687 = +312,271 BRL (~$62,454 USD)


### Scenario Planning
| Scenario | Repeat Rate | Additional Revenue | Confidence |
|----------|------------|-------------------|------------|
| Conservative | 4.0% | +156K BRL | High |
| Target | 5.0% | +312K BRL | Medium |
| Optimistic | 6.5% | +585K BRL | Low |

---

## 🧭 Next Steps Roadmap

### If We Had 2 More Weeks:
1. **A/B Test Priority 1**: Randomly assign 10% of new buyers to receive 2nd-order discount; measure lift.
2. **Seller-Level Analysis**: Do certain sellers drive higher retention? Could we promote them?
3. **Lifetime Value Modeling**: Do repeat customers spend more over time, or just buy once more?

### If We Had More Data:
1. Customer demographics (age, income) to personalize retention tactics
2. Marketing touchpoint data to attribute retention to specific campaigns
3. Post-purchase survey responses to understand "why" behind drop-offs

---

## ⚠️ Limitations & Caveats

1. **Correlation ≠ Causation**: This is observational data. Recommendations require experimental validation.
2. **Time Window Bias**: Dataset ends Aug 2018; newer customer behavior not captured.
3. **Geographic Granularity**: City-level analysis may mask neighborhood or delivery-zone patterns.
4. **AOV Stability**: 172.73 BRL is an average; actual AOV varies by category/season.
5. **One Extra Order Assumption**: Revenue model assumes each new repeat customer buys exactly 1 more order. Real LTV may be higher.

---

## 📬 Contact & Collaboration

**Author**: Ahmed A. Elatwy
🔗 [LinkedIn](https://www.linkedin.com/in/ahmed-elatwy/) || 📧 [Email Me](ahmed.abbas.elatwy@gmail.con)

**Open to**:
- Full-time Data Analyst roles (Egypt or remote)
- Freelance retention analysis for e-commerce founders
- Speaking opportunities on analytics + storytelling

*If you found this analysis helpful, let's connect! I offer free 30-minute retention consults to Egyptian e-commerce founders.*

