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
