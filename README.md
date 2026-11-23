# One-Line Pitches — Main Chat v1

An entry for the make.fun bounty **A Day of One-Line Pitches**: a single
sentence (max 240 characters) that convinces a friend who has never coded to
let an AI agent build their first app idea on make.fun.

[![Bounty](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/haidildariell/one-line-pitches-mainchat-v1/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/haidildariell/one-line-pitches-mainchat-v1/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Bounty page: https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3

## The pitch

> You've told me about that app idea a dozen times now — you don't know a
> single line of code, and that's fine, because an AI agent on make.fun can
> build it from your plain words while you watch your dream turn real.

## How it runs

`main.py` (Python 3.13, standard library only) writes the sentence to
`entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR` if set, otherwise
`/output`).

```bash
python3 main.py
```
