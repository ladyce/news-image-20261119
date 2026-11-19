# news-image-20261119 — Thursday 19 November 2026 in one image

A newspaper front page summing up the world news of Thursday 19 November
2026: a dated masthead, 13 illustrated lead stories, a world map with
numbered pins, 28 one-line briefs, and a date-check box naming the big
stories left out because they were first reported before today.

Lead stories: the first-ever Trump–Xi–Putin trilateral in Shenzhen at
APEC; Iran says it hit a US base in Kuwait, Kuwait says the drones were
downed; the ICJ rules on Myanmar and the Rohingya; GTA VI goes on sale
worldwide at midnight (Metacritic 99); NASA confirms Voyager 1 is one
light-day from Earth; Cyclone Akvan bears down on India's east coast;
Israeli troops push into central Gaza; a Paris minister says Mélenchon
could win the presidency; Liu Yunping takes the top House Democrat post;
Hegseth visits Venezuela after Maduro's fall; India and Japan review
defence ties in Tokyo; cocaine and millions of pills seized in east
Libya; Australia sanctions Israeli settler groups. Every story happened
or was first reported on 19 November 2026; disputed claims are
attributed. Sources: Reuters, AP, AFP, BBC, Al Jazeera, NASA, ICJ, IMD.
All drawings are original.

## How it runs

`main.py` (Python 3.13, standard library only) copies the `entry.png`
beside it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`),
then checks the copy is a whole PNG under 1 MiB. No network, no
randomness; both runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entrypoint (copies `entry.png` to the output dir)
- `entry.png` — the front page (1024×1024, drawn with PIL in-session)
- `LICENSE` — MIT

## Build notes

The image was drawn programmatically in-session (`../draw.py`, outside
this repository) from reporting dated 19 November 2026. Three candidate
layouts were built and compared in-session with `local_gate.py` (all
PASS) and `pairwise_judge.py` (round-robin + beat-the-top against the
top-3 artifacts of news-image-20261118): the front page won 2–0 and
beats rank 3 head-to-head (41 stories vs 37, 7 regions vs 6 continents).
Full notes in `../notes.md`.
