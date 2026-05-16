# 6. Zigzag Conversion � Post-Solve Notes

## Attempt 1 — May 16, 2026 | ~20 min | shown solution (threw in towel)

### Assessment: Did Not Complete — would be a fail
Good problem comprehension. Correct instinct that rows were the key. Could not
translate that into working code. Likely would have taken 2+ hours to arrive
independently.

---

## What Happened

**Approach tried:** Column-by-column slicing — `col1 = string[:nrows]`, then
tried to calculate how many single-character zag columns follow. Got stuck
because the column indexing math doesn't generalize cleanly.

**What was right:**
- Understood the zigzag pattern correctly after clarification
- Identified that the first column is always `string[:nrows]`
- Sensed that rows were the right framing before stopping

**What was wrong:**
- Tried to reason about columns instead of rows
- No clear path to generalizing beyond hardcoded col1, col2, col3
- Not armed with the row-accumulation pattern

---

## The Solution

```python
def acrosticker(string, nrows):
    if nrows == 1:
        return string

    rows = [""] * nrows   # one empty string per row
    current_row = 0
    going_down = False

    for char in string:
        rows[current_row] += char
        if current_row == 0 or current_row == nrows - 1:
            going_down = not going_down   # bounce at top and bottom
        current_row += 1 if going_down else -1

    return "".join(rows)
```

**Walk-through with "PAYPALISHIRING", nrows=3:**
- Start at row 0, going_down=False → first char 'P' hits row 0, toggles to going_down=True
- Walk down: A→row1, Y→row2, toggle back up
- Walk up: P→row1, A→row0, toggle back down
- ... and so on
- rows ends up as ["PAHN", "APLSIIG", "YIR"]
- "".join(rows) → "PAHNAPLSIIGYIR"

---

## Key Concepts

**The row-accumulation pattern:**
Don't think about columns. Create one bucket per row, walk the string, 
drop each character in the right bucket, join at the end.

**`"".join(rows)`:**
`rows` is a list of strings. `"".join(list)` concatenates them all with
no separator. `["ABC", "DEF", "GHI"]` → `"ABCDEFGHI"`.
Common Python pattern — worth memorizing. The `""` is the separator (empty = no gap).

**The bounce logic:**
- Track `current_row` (int) and `going_down` (bool)
- At row 0 or row nrows-1: flip `going_down`
- Move `current_row += 1` if going down, `-1` if going up
- Simple and generalizes to any nrows

**Edge case — nrows == 1:**
If there's only one row, every character goes in it and the output equals
the input. Return early. Without this, `current_row == nrows - 1` would
be `0 == 0` on the first character, toggle would fire, and
`current_row` would go to -1 → index error.

---

## Time & Space Complexity
- Time: O(n) — one pass through the string
- Space: O(n) — the rows list holds all characters

---

## What to Work On
- **`"".join(list)` pattern** — not comfortable with this yet. It's everywhere
  in Python string problems. `separator.join(list_of_strings)` → one string.
  `"".join(["a","b","c"])` → `"abc"`. `"-".join(["a","b","c"])` → `"a-b-c"`.
- **Row framing vs column framing** — when a problem has a 2D visual pattern,
  ask "can I just track which row each element belongs to?" before trying
  to slice by column. Row accumulation is almost always cleaner.
- **Going down/up boolean pattern** — useful any time you're bouncing between
  boundaries. Track direction as a bool, flip at each boundary.
