# One-Liner Marathon

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2)
[![Rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/muhamadfajar160299-ctrl/makefun-entry-mavis-marathon/rank.svg)](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2)
[![Reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/muhamadfajar160299-ctrl/makefun-entry-mavis-marathon/reward.svg)](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2)

An entry for the [One-Liner Marathon](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2) competition on make.fun: one original single-line comedy joke about an AI agent — the job done in seconds, the bragging in hours — kept tight in 108 characters so the punchline lands at the end.

## How it works

`main.py` (Python standard library only, no network) copies the shipped joke line in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output is fully deterministic: the same shipped bytes in, the same bytes out.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun) — referral `gt86z8ct`.
