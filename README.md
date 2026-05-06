# LeetCode Interview Prep

## Bank Rationale

Bank curated based on frequency analysis across recent interview reports:
- Cross-referenced a large set of interview experience reports (2025-2026) against a global frequency ranking of commonly asked problems.
- Filters applied: recent rounds, two-interview compressed format, senior IC-adjacent roles.
- Result: design problems are slightly over-represented in this format vs. the global average. "Initial question + follow-up extension" is the dominant structure.

Each problem should be drilled with awareness of likely follow-up extensions (tracked in each `notes.md`).

## Problem Bank (16 problems)
#### Tier 0?
 - parking-lot-oop-design
 - 146-lru-cache
 - 362-design-hit-counter
 - 380-insert-delete-getrandom-o1

### Tier 1 — Highest priority, drill heavily (6 problems)
- 146 - LRU Cache
- 380 - Insert Delete GetRandom O(1)
- 359 - Logger Rate Limiter
- 1 - Two Sum
- 3 - Longest Substring Without Repeating Characters
- 56 - Merge Intervals

### Tier 2 — Pattern fundamentals, drill moderately (5 problems)
- 347 - Top K Frequent Elements
- 207 - Course Schedule
- 139 - Word Break
- 11 - Container With Most Water
- 20 - Valid Parentheses

### Tier 3 — Familiarize, single rep each (4 problems)
- 15 - 3Sum
- 162 - Find Peak Element
- 362 - Design Hit Counter
- 981 - Time Based Key-Value Store

### Tier 4 — Stretch / novel design muscle (1 problem)
- Parking Lot OOP Design (no LeetCode number — original system design problem)

Fine practice problems, but not where interview focus lands for this format. Revisit if time permits after core bank is solid.

## Scoring Rubric

- **Frame before solving** — clarifying questions and requirements first, code second
- **Class design** — sensible boundaries, good naming, no cryptic abbreviations
- **Tradeoff articulation** — every design choice explained with "why this, what the cost is, when I'd reconsider"
- **Edge case handling** — mentioned out loud or coded explicitly
- **Code cleanliness** — 30-50 lines, no fluff, production-quality
- **Talk out loud** — silent coding = bad signal, walk through reasoning continuously
- **Scope and impact framing** — own the problem, don't just implement the task

## Interview Format Constraints

- 30-50 lines of Python OOP
- Static interview platform (syntax highlighting only, no autocomplete, no AI, no execution)
- LeetCode mediums likely, with initial question + follow-up extension structure
- Pseudocode discouraged unless interviewer requests it
- Talk through approach before coding

## Practice Loop

1. Switch to `interview-prep` VS Code profile (no Copilot, no autocomplete beyond syntax)
2. Open the problem folder, read `problem.md`
3. Set 45-min timer
4. Talk out loud while solving in `solution.py`
5. Write `notes.md` after: Approach, Tradeoffs, Edge Cases, Complexity, Likely Follow-up Extensions, What I'd Do Differently
6. Paste solution + notes into Claude chat for evaluation

## Session Log
<!-- Format: YYYY-MM-DD (Day) - Problem - attempt # - one-line takeaway -->
_(Real entries added after each rep)_