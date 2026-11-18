---
type: handout-index
unit: 3
topic: 3.6.D.3 / 3.6.D.4
last_updated: 2026-11-18
---

# 3.6.D — How real companies estimate next year's revenue and cost

**Purpose:** source material for 3.6.D.3 (future revenue) and 3.6.D.4 (future COGS and operating expenses), plus a full set of question sheets for 3.6 practice. Every page here is a **verified excerpt** from a real filing (Chinese A-share annual reports as single-page PDFs; US 10-Ks as one-page text-reproduced PDFs plus a Markdown note).

## 1. What is in this folder

### A-share annual reports (single-page PDFs, Chinese source pages)

| File | Company / period | Page | Topic | Why it is here |
|---|---|---|---|---|
| `Yili 2025 - Business plan, capex and risks p31-32.pdf` | Yili 600887, FY2025 | 31–32 | **D.3 + D.4** | 2026 target: revenue **121.5bn**, pretax profit **13.6bn**, "based on industry development conditions"; capex plan **6.4bn** |
| `Yili 2024 - Business plan (2025 targets) p29.pdf` | Yili, FY2024 | 29 | **D.3** | The same sentence one year earlier: 2025 target **119.0bn / 12.6bn** — you can check what was delivered |
| `Yili 2025 - Revenue, cost and volume by product p18.pdf` | Yili, FY2025 | 18 | **D.3** | Revenue, cost and gross margin by product line, plus production and sales volume |
| `Shuanghui 2025 - Revenue, cost and volume p26.pdf` | Shuanghui 000895, FY2025 | 26 | **D.3** | "Volume +7.81%, revenue −0.43% because hog and meat prices fell" |
| `Shuanghui 2025 - Business plan, capex and risks p42.pdf` | Shuanghui, FY2025 | 42 | **D.4** | COGS driver = live-hog prices; opex driver = labour, food safety, environmental rules; 2026 capex 1.3bn |
| `Haitian 2025 - Raw material and procurement risk p45.pdf` | Haitian 603288, FY2025 | 45 | **D.4** | "Procurement plans are set from the **sales forecast** and **expected price movements**" |

### US 10-Ks (one-page PDFs + Markdown notes)

| File | Company | Topic | Why it is here |
|---|---|---|---|
| `Pure Storage 10-K FY2025 - RPO revenue estimate.pdf` | PSTG, FY2025 | **D.3** | 48% of RPO expected to be recognised within 12 months |
| `Colgate 10-K FY2024 - Outlook.pdf` | CL, FY2024 | **D.3 + D.4** | Raw material cost → pricing → demand, one chain across three lines |
| `Delta 10-K FY2024 - Fuel share of opex.pdf` | DAL, FY2024 | **D.4** | Fuel = 19–24% of operating expense; $2.29–$4.25 per gallon |
| `Nike 10-K FY2026 - Consolidated Statements of Income.pdf` | NKE, FY2026 | **whole 3.6** | Textbook ladder; marketing and overhead split |
| `Apple 10-K FY2026 - Consolidated Statements of Operations.pdf` | AAPL, FY2026 | **whole 3.6** | Same table cut by business line (products / services) |
| `Chipotle 10-K FY2025 - Consolidated Statements of Income.pdf` | CMG, FY2025 | **whole 3.6** | No gross profit line at all |

### Comparable pairs — full income statements for paired analysis (added 2026-11-19)

Seven fresh statements pulled from EDGAR by `fetch_income_statements.py`, grouped into **same-industry pairs** so students compare business models, not just numbers. All are the latest fiscal year, as reported.

| Group | Statements | The comparison question |
|---|---|---|
| **Restaurants** | `McDonalds 10-K FY2025 - Consolidated Statement of Income.pdf` (pairs with the Chipotle statement above) | Same industry, opposite models: 100% company-operated vs 62% franchised — where does each draw the COGS line? |
| **Airlines** | `Delta 10-K FY2025 - Consolidated Statements of Operations.pdf` · `United 10-K FY2025 - Consolidated Statements of Operations.pdf` | Fuel as the dominant variable cost, salaries as the fixed base, interest as the price of the fleet |
| **Big-box retail** | `Walmart 10-K FY2026 - Consolidated Statements of Income.pdf` · `Target 10-K FY2026 - Consolidated Statements of Operations.pdf` | Everyday-low-price vs differentiated merchandise: Target wins gross margin, Walmart wins opex — they meet at the same operating margin |
| **Banks** | `JPMorgan 10-K FY2025 - Consolidated Statements of Income.pdf` · `Bank of America 10-K FY2025 - Consolidated Statement of Income.pdf` | No COGS at all: interest paid is netted *inside* revenue, provision for credit losses is the COGS-equivalent — the textbook ladder has to be rebuilt |

> Fiscal years differ by retailer convention (WMT/TGT years ended 31 Jan 2026); everything else is calendar-year. Each PDF carries the accession number and source URL on its face.
>
> **Ready to hand out:** `* - Student Handout.pdf` — one self-contained file per pair (both statements + the questions + answer space, no answers), built by `build_student_handouts.py`. Print or upload these four; the separate statement PDFs and Student/ sheets are the working pieces behind them.

### Question sheets (teacher version, with answers)

| Sheet | Pairs with | Time / marks | Focus |
|---|---|---|---|
| `Nike 10-K FY2026 - Income Statement Question Sheet (with answers).md` | Nike statement | 25 min · 35 | Flat revenue, profit −3.4% — all of it the tax line |
| `Apple 10-K FY2026 - Income Statement Question Sheet (with answers).md` | Apple statement | 25 min · 35 | Two businesses, one table; three growth rates that disagree |
| `Chipotle 10-K FY2025 - Income Statement Question Sheet (with answers).md` | Chipotle statement | 25 min · 35 | Draw the COGS boundary yourself; which costs outgrew revenue |
| `Yili 2025 Annual Report - Question Sheet (with answers).md` | Yili pages | 30 min · 40 | Two revenue measures; profit +36.8% is mostly a smaller impairment |
| `Shuanghui 2025 Annual Report - Question Sheet (with answers).md` | Shuanghui pages | 30 min · 40 | Volume +7.8% with revenue −0.4%; slaughtering vs processed meat |
| `Haitian 2025 Annual Report - Question Sheet (with answers).md` | Haitian page | 30 min · 40 | Gross margin 37.0% → 40.2%; a plan with no numbers |
| `Three-Company Comparison - Question Sheet (with answers).md` | all three | 35 min · 40 | Which revenue estimate is verifiable; a 5% input shock in each |
| `Restaurant Pair (CMG vs MCD) - Comparison Question Sheet (with answers).md` | CMG + MCD statements | 35 min · 40 | Draw the COGS boundary twice; why a franchisor's margins are structurally higher |
| `Airline Pair (DAL vs UAL) - Comparison Question Sheet (with answers).md` | DAL + UAL statements | 35 min · 40 | Fuel/salary ratios; interest below operating profit; a profit jump that came from non-operating |
| `Retail Pair (WMT vs TGT) - Comparison Question Sheet (with answers).md` | WMT + TGT statements | 35 min · 40 | Two margin strategies meeting at one operating margin; growth ≠ operations (other gains/losses) |
| `Bank Pair (JPM vs BAC) - Comparison Question Sheet (with answers).md` | JPM + BAC statements | 35 min · 40 | Why banks have no COGS; interest with two opposite jobs; provision as the COGS-equivalent |

### Student versions (`Student/`)

Eleven English worksheets with the answers removed, name/class/date lines and a total at the foot:

`Yili 2025 Annual Report - Question Sheet.md` · `Shuanghui 2025 Annual Report - Question Sheet.md` · `Haitian 2025 Annual Report - Question Sheet.md` · `Three-Company Comparison - Question Sheet.md` · `Nike 10-K FY2026 - Income Statement Question Sheet.md` · `Apple 10-K FY2026 - Income Statement Question Sheet.md` · `Chipotle 10-K FY2025 - Income Statement Question Sheet.md` · `Restaurant Pair (CMG vs MCD) - Comparison Question Sheet.md` · `Airline Pair (DAL vs UAL) - Comparison Question Sheet.md` · `Retail Pair (WMT vs TGT) - Comparison Question Sheet.md` · `Bank Pair (JPM vs BAC) - Comparison Question Sheet.md`

> The student sheets use the same numbers as the teacher sheets, so the teacher answers grade them directly. **Change a number and you must change both.**

## 2. Three ways to estimate revenue (board-ready)

| Route | Basis | Example |
|---|---|---|
| **Industry trend → total target** | supply, demand, policy, per-capita consumption | Yili: "based on industry development conditions, target revenue 121.5bn" |
| **Volume × price** | units forecast × price assumption | Shuanghui: volume +7.81%, revenue −0.43% |
| **Contract backlog × conversion** | RPO / order book | Pure Storage: 48% of RPO within 12 months |

## 3. Three ways to estimate cost (board-ready)

| Route | Basis | Example |
|---|---|---|
| **One dominant input** | live hog, crude, raw milk | Shuanghui (hogs), Delta (fuel, 19–24% of opex) |
| **Forecast → procurement plan** | sales forecast, then purchase plan | Haitian: "procurement plans from the sales forecast and expected price movements" |
| **Planned spend** | capex, labour, compliance | Yili (6.4bn capex), Shuanghui (rising social costs) |

## 4. Five-minute classroom sequence

1. **Yili p.31** — which of the three D.3 sources is "industry development conditions"? Why does the paragraph end with a disclaimer?
2. **Shuanghui p.26** — if this were next year's budget, which two numbers must you assume first? (volume, price)
3. **Shuanghui p.42 + Delta MD&A** — which line of the income statement does each hit: COGS or operating expense?
4. **Haitian p.45** — why must the procurement plan follow the sales forecast? (Because COGS is a function of output, and output follows sales.)
5. Close: **revenue ≈ volume × price × trend; cost ≈ input price × quantity + planned spend. In an annual report this is called the business plan.**

## 5. Sources (downloaded 2026-11-18; paired statements 2026-11-19)

| File | Link |
|---|---|
| Yili FY2025 | `http://static.cninfo.com.cn/finalpage/2026-04-30/1225259562.PDF` |
| Yili FY2024 | `http://static.cninfo.com.cn/finalpage/2025-04-30/1223421123.PDF` |
| Shuanghui FY2025 | `http://static.cninfo.com.cn/finalpage/2026-03-25/1225028113.PDF` |
| Haitian FY2025 | `http://static.cninfo.com.cn/finalpage/2026-03-27/1225038237.PDF` |
| Pure Storage FY2025 10-K | `https://www.sec.gov/Archives/edgar/data/1474432/000162828025015044/pstg-20250202.htm` |
| Colgate FY2024 10-K | `https://www.sec.gov/Archives/edgar/data/21665/000002166525000008/cl-20241231.htm` |
| Delta FY2024 10-K | `https://www.sec.gov/Archives/edgar/data/27904/000002790425000004/dal-20241231.htm` |
| Nike FY2026 10-K | `https://www.sec.gov/Archives/edgar/data/320187/000032018726000007/nke-20260531.htm` |
| Apple FY2026 10-K | `https://www.sec.gov/Archives/edgar/data/320193/000032019326000008/aapl-20260926.htm` |
| Chipotle FY2025 10-K | `https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm` |
| McDonald's FY2025 10-K | `https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm` |
| Delta FY2025 10-K | `https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm` |
| United FY2025 10-K | `https://www.sec.gov/Archives/edgar/data/100517/000010051726000023/ual-20251231.htm` |
| Walmart FY2026 10-K | `https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm` |
| Target FY2026 10-K | `https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm` |
| JPMorgan FY2025 10-K | `https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm` |
| Bank of America FY2025 10-K | `https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm` |

> The seven paired statements were extracted from the filings' rendered R-files (the same XBRL viewer EDGAR serves in the browser) and re-rendered as one-page PDFs; re-run `python3 fetch_income_statements.py` in this folder to refresh them when next year's 10-Ks land. Every figure on the comparison sheets was checked against the statement on its face.

> The A-share PDFs contain only the cited pages (the originals run 215–272 pages). Page numbers are the **printed** page numbers: for Yili the printed number is 4 lower than the PDF page (PDF 35 = p.31); for Shuanghui and Haitian they match.
> Classroom use: keep the company name, the accession number and the page reference visible on screen.