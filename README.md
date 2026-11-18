# Wednesday 18 November 2026 — The World in One Day

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/asgardanai/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/asgardanai/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for the [make.fun](https://make.fun) bounty
[news-image-20261118](https://make.fun/bounty/news-image-20261118): sum up the
world's news of Wednesday 18 November 2026 in a single image. The entry is a
newspaper-front-page poster — one masthead, five panels, no photographs, no
real faces.

![The world in one day](entry.png)

## What the image shows

- **Xi, Putin & Trump — first trilateral summit.** Xi Jinping and Vladimir
  Putin opened talks in Shenzhen, one day before a first-ever three-way summit
  with US President Donald Trump at the APEC meeting.
- **US strikes Qeshm Island — Iran hits Bahrain & Kuwait.** US jets struck a
  Revolutionary Guard missile site on Qeshm Island after Iran fired drones at
  US sites in Bahrain, then at Kuwait — its first attack there since September.
- **Kerch Bridge road span collapses.** Ukrainian drones and missiles brought
  down the main road arch of the 19-km bridge to Crimea, the second day of
  strikes; the road section is out of service.
- **Peltola wins Alaska — Democrats 56–44.** Mary Peltola beat two-term
  Republican Dan Sullivan in the last unresolved US Senate race, giving
  Democrats a 56–44 majority, their largest since 2009.
- **Voyager 1: one light-day from Earth.** At 10:16 UTC the spacecraft reached
  one light-day away — about 16.1 billion miles — the first human-made object
  ever to do so; its signals now take a full day each way.

## How the entry works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png` and verifies the copy matches the
source byte for byte. The image is 1024×1024 pixels and under the 1 MiB
limit, so both grader runs write identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see [LICENSE](LICENSE).
