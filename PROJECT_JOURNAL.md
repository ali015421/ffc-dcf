# Project Journal

## 2026-10-20

Built the core discounting function today in Python, from scratch, no
starting code. Used a placeholder cash flow list ([200, 250, 300]) and a
10% discount rate to get the mechanics right before touching real FFC
numbers.

Main bug: wrote `enumerate([cash_flows], start=1)` — wrapped the list in
an extra set of brackets. That turned it into a list containing one item
(the entire original list), so the loop only ran once instead of three
times. Fix: `cash_flows` was already a list, so it didn't need wrapping
again — just pass the variable name directly.

Other things that tripped me up: mixing up `cash_flows` (the whole list)
with `item` (one value per loop pass) inside the formula; forgetting that
`print()` only displays a value while `return` sends it back out of the
function so it can actually be stored and reused; and calling the function
from inside its own definition by mistake, which would have caused
infinite recursion.

End state: a working, reusable `calculate_total_pv(cash_flows,
discount_rate)` function, confirmed against manual calculation (613.82).
Git repo initialized, `.gitignore` set up to exclude `.venv/`.

Next: get real FFC financial statements and start Module 1 (reading them
properly) before writing any more code.

___________________________________________________________________________________________________________________________________
## 2026-10-24

Got FFC's real financial statements today — not hypothetical numbers anymore. Downloaded the FY2025 Annual Report, found the Statement of Financial Position, Profit or Loss, and Cash Flows (unconsolidated), pulled the actual figures into data/processed/ffc_historical.csv with page references for every line.

Found a real discrepancy while cross-checking: "Other investments – net" for FY2024 was reported as Rs 14,004,560 thousand in the FY2024 Annual Report, but restated to Rs 2,145,801 thousand in the FY2025 report — an ~11.86 billion swing. Used the more recent (restated) figure since that's the correct convention, but it's a reminder that comparative figures can change between reports, especially around a merger.

Cleaned up repo hygiene: stopped committing large PDFs, added data/raw/sources.md instead with URLs and page numbers so the data stays traceable without bloating the repo.

The big thing today was understanding FFC's 2024 merger with FFBL (Fauji Fertilizer Bin Qasim). FFBL got merged into FFC effective July 1, 2024 — exactly halfway through the year. That means:
- FY2023 = FFC alone, no FFBL
- FY2024 = FFC + only 6 months of FFBL
- FY2025 = FFC + a full 12 months of FFBL

None of these years are cleanly comparable to each other. FY2023→FY2024 growth is mostly the merger (worked out from Note 1.2.4 that FFBL contributed Rs 134.5bn of FY2024's Rs 214bn turnover increase — about 63% merger, 37% real growth). FY2024→FY2025 growth is distorted the other way — FY2025 just has twice as many months of FFBL in it, so part of that increase is calendar, not performance.

Decision: use FY2025 as a clean single base year (full 12 months, reflects the company as it actually is now), and base future growth assumptions on external fertilizer industry data instead of FFC's own distorted historical growth rate, since none of the three years give an honest trend line.

Honestly, this merger stuff didn't click right away — took several rounds of working through it step by step (what a merger even changes, why the dates matter, which year-pairs are actually comparable) before it made sense. Worth remembering that reading real financial statements isn't just "find the number," it's understanding what changed structurally before trusting any comparison.

Next: FFC's actual industry economics (urea/DAP pricing, gas costs, government policy) before touching any forecast numbers.

_____________________________________________________________________________________________________________________________________