# FFC DCF Valuation

A discounted cash flow (DCF) valuation of Fauji Fertilizer Company Limited
(FFC), built from scratch in Python, with a parallel Excel/Artcraft model
planned.

## Why FFC

FFC is a large, established, PSX-listed fertilizer producer. Fertilizer
demand in Pakistan is tied to agriculture, which is relatively stable and
less cyclical than many other sectors, and urea pricing has historically
been influenced by government policy — making cash flows more predictable
to forecast than a high-growth or early-stage company. Pakistan-specific
companies also reflect real local market context rather than a generic,
widely-modeled US company.

## Status (as of Oct 2026)

- Python: core discounting logic complete. A reusable `calculate_total_pv()`
  function takes any list of cash flows and a discount rate, and returns
  the total present value.
- Excel/Artcraft model: not started yet.
- Real FFC financial data: not yet collected. Current numbers are
  placeholder/hypothetical, used only to build and test the calculation
  logic.

## Tech stack

- Python 3.14.4, run in a local `venv`
- Artcraft (MS Office-compatible spreadsheet suite) planned for the
  parallel spreadsheet implementation
- Git/GitHub for version control

## Not done yet

- Real FFC historical financials (FY2023–FY2025)
- Revenue/FCF forecasting logic
- WACC calculation
- Terminal value and enterprise-to-equity bridge
- Excel/Artcraft model
- Tests
