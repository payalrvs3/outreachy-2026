# Outreachy Contribution - WikiMovimento Brasil

Contributions for the Outreachy internship project:
**Addressing the Lusophone Technological Wishlist Proposals**
(Wish #3 and Wish #8 - T418285, T418286)

---

## Task 1 - JavaScript date formatting

Formats a list of Wikipedia article objects, displaying each article's
title, page ID, and creation date in human-readable form.
Uses `toLocaleDateString` with timezone-safe date parsing.

---

## Task 2 - URL status checker

Reads URLs from a CSV file and checks their HTTP status codes.
Uses HEAD requests with a GET fallback for 405 responses, specific
error handling for timeouts and connection errors, and threading via
`ThreadPoolExecutor` for concurrent URL checking.

Updated based on mentor feedback - switched to threading and removed
unnecessary encoding.

---

## Prototype - Wish #8: Wikidata support for WikiScore

An interactive prototype demonstrating how WikiScore could be extended
to count Wikidata edits in contests and edit-a-thons. Built based on
the real WikiScore codebase structure, using actual model names,
the real scoring formula from `CounterHandler`, and real Wikibase
action types.

Features shown:
- Leaderboard with separate Wikipedia and Wikidata point columns
- Live contributions feed showing real Wikibase action types
- Per-contest configuration: enable/disable Wikidata scoring,
  exclude bot edits, set points per edit type
- **Live API lookup tab** - calls the real Wikidata `usercontribs`
  API, parses Wikibase action types from edit comments using regex,
  and scores edits in real time. Try it with any Wikidata username.

**Live preview:** [Wish #8 - Wikidata support for WikiScore](https://payalrvs3.github.io/outreachy-2026/Prototype/wishlist8_prototype.html)

---

## Phabricator proposal

[T423406](https://phabricator.wikimedia.org/T423406#11842628) - Proposal: Addressing the Lusophone Technological Wishlist Proposals - payalrvs3
