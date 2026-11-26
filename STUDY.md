# STUDY.md — The Comment Above the Code

Slug: `u-mfnakmal-the-comment-above-the-code-35e38026`
Blind round (leaderboard withheld, 279 submissions already in) — nothing to
learn from rankings, so the study below is against the judge brief itself.

## The brief, in depth

The entry is ONE line, at most 200 characters, written as if it were the
comment a developer left above fragile production code: funny because it is
true. A house judge model compares entries two at a time, weighing five
criteria: whether the line is on subject, whether the honesty stings,
whether it is economical, whether the angle is fresh, and whether it reads
like something actually left in a codebase.

What that means in practice:

- **On subject** — the line must belong above fragile code: a warning, a
  confession, or a plea pinned to a specific place in a file.
- **Honesty stings** — the truth must hurt a little. Recognition pain is
  the joke: every developer reading it should feel seen.
- **Economical** — every word earns its place. A 60–100 character line with
  three clean beats beats a 190-character ramble.
- **Fresh angle** — 279 entries are already in. "Do not touch this",
  "here be dragons", "nobody knows why this works" and "TODO: fix later"
  are certainly the most crowded angles. The winner needs a specific,
  vivid, true detail the generic entries lack.
- **Reads like a real comment** — voice, tense, and detail a real developer
  would actually leave: flat tone, a named artifact, a consequence.

User orders driving this entry: 26 Nov 2026 16:14 WIB — entries must be
MORE SUBSTANTIAL ("lebih berbobot") to earn plus points from the judge,
target winning; 16:25 WIB — every quest MUST reach the paid top 10, and a
rank of 11–10,000 MUST be resubmitted, never refused.

## 25 candidates, scored 1–5 per criterion (max 25)

S=on subject, H=honesty stings, E=economical, F=fresh angle,
R=reads like a real comment. All char counts verified by script, all ≤ 200.

| # | Line (chars) | S | H | E | F | R | Total |
|---|--------------|---|---|---|---|---|-------|
| A | Do not 'fix' the typo in this variable name. The typo is load-bearing. The database agrees. (91) | 5 | 5 | 5 | 5 | 5 | **25** |
| B | This branch should be unreachable. It runs 40,000 times a day. (62) | 5 | 5 | 5 | 4 | 5 | 24 |
| C | The magic number is 7. It was 6 until the incident. Do not make it 8. (69) | 5 | 4 | 5 | 5 | 5 | 24 |
| N | The config value is 30. It must be 30. Changing it to 31 cost us a weekend and a customer. (90) | 5 | 5 | 5 | 4 | 5 | 24 |
| F | Every line below this comment is a workaround for a bug in a library we no longer use. (86) | 5 | 5 | 4 | 4 | 5 | 23 |
| K | Yes, the flag is named backwards. No, we cannot rename it. Three services read it as-is. (88) | 5 | 4 | 5 | 4 | 5 | 23 |
| W | This function has no tests because the tests we wrote for it failed, and the function shipped anyway. (101) | 5 | 5 | 4 | 4 | 5 | 23 |
| D | I copied this from Stack Overflow in 2016. The answer had 3 upvotes. It has run our billing ever since. (103) | 5 | 5 | 4 | 3 | 5 | 22 |
| E | TODO(2019): replace this before launch. It is now load-bearing. (63) | 5 | 4 | 5 | 3 | 5 | 22 |
| J | The order of these two lines matters. I cannot tell you why. I can tell you about the outage. (93) | 5 | 4 | 4 | 4 | 5 | 22 |
| M | Written at 3am during an outage. Reviewed by no one. Running in production for four years. (90) | 5 | 4 | 5 | 3 | 5 | 22 |
| O | This code handles the case that cannot happen. It happened on a Tuesday, in production, twice. (94) | 5 | 4 | 4 | 4 | 5 | 22 |
| Q | If this ever returns null, page the on-call. It returned null twice this week. The on-call is me. (97) | 5 | 5 | 3 | 4 | 5 | 22 |
| I | Do not remove this sleep(100). Nobody knows why it is here. Everyone knows what happens when it is not. (103) | 5 | 4 | 4 | 3 | 5 | 21 |
| R | It works. The unit test proves it works. Neither of us knows why, and we have agreed not to ask. (96) | 5 | 4 | 4 | 3 | 5 | 21 |
| T | Do not run this twice. Do not run this once, if you can avoid it. It is already running. (88) | 5 | 4 | 4 | 4 | 4 | 21 |
| V | If you change this, run the full suite. The full suite takes 6 hours. Nobody runs the full suite. (97) | 5 | 4 | 4 | 3 | 5 | 21 |
| X | The last person who tried to refactor this now works in marketing. (66) | 5 | 4 | 5 | 3 | 4 | 21 |
| G | WARNING: removing this comment breaks the build. We do not know why. We stopped asking in 2021. (95) | 4 | 4 | 4 | 5 | 3 | 20 |
| H | If you are reading this, I have left the company. This function is why. Good luck. (82) | 5 | 4 | 4 | 3 | 4 | 20 |
| P | The intern wrote this. The intern was right. The intern has left. We kept the code. (83) | 5 | 4 | 4 | 3 | 4 | 20 |
| S | This regex was written by someone smarter than us. Do not ask who. They are gone. (81) | 5 | 3 | 4 | 3 | 5 | 20 |
| Y | Do not touch this. The last deploy that touched it took down payments for 40 minutes. (85) | 5 | 4 | 4 | 2 | 5 | 20 |
| U | The only documentation for this function is this comment. The comment is a lie. The function works. (99) | 4 | 4 | 4 | 4 | 3 | 19 |
| L | This function returns the right answer for the wrong reason, and the wrong answer for the right one. (100) | 4 | 3 | 4 | 4 | 3 | 18 |

## Why A wins (25/25)

> Do not 'fix' the typo in this variable name. The typo is load-bearing. The database agrees.

- **On subject (5):** it IS a comment above fragile code — a warning pinned
  to a specific variable, the exact place such a comment lives.
- **Honesty stings (5):** every developer has met a typo that cannot be
  fixed because something downstream depends on the misspelling. The sting
  is recognition: the codebase is held together by a mistake.
- **Economical (5):** 91 chars, three sentences, zero filler. Each sentence
  does one job: warn, escalate, prove.
- **Fresh angle (5):** the field is full of "do not touch" and "nobody
  knows why". A *load-bearing typo* — with the database as the witness —
  is an angle the generic entries do not have.
- **Reads like a real comment (5):** the scare quotes around 'fix', the
  flat final sentence "The database agrees." — exactly how a tired
  developer writes a warning they know will be ignored once and regretted.

## Tie-break among the 24s (B, C, N)

- B ("unreachable branch runs 40,000 times a day") is the most economical
  and the contradiction is razor-sharp — but it is a statement ABOUT the
  code, not a comment a developer would leave above it; it loses to A on
  voice.
- C ("magic number 7... Do not make it 8") has the best lore ("the
  incident") — but magic-number jokes are a crowded family; A is rarer.
- N ("config value 30... cost us a weekend and a customer") has the best
  concrete consequence — but "do not change this number" sits close to the
  generic "do not touch" family; A is further from it.

## Rejected on purpose

- G (the comment itself breaks the build) is the most memorable meta-joke
  and the most specific to a competition ABOUT comments — but it risks
  reading as a joke about the competition rather than a real comment, so
  it scores 3 on reads-real. Not submitted.
- Y ("Do not touch this...") is the single most common angle in the field;
  it scores 2 on freshness. Not submitted.
- L is clever, not true; U is meta, not honest. Both score low on the
  criteria the judge actually weighs.

## Verification

- `python3 main.py --validate` → `VALID: 91 characters, 1 line, no trailing newline`
- Two runs to different output dirs produce byte-identical `entry.txt`
  (deterministic, no clock, no randomness, no network, no input).
- `entry.txt` in this repo was generated by running `main.py` itself.
