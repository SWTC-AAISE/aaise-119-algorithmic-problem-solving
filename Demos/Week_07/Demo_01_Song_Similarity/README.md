# Song Similarity

DEM-W07D01 | Week 7, Monday

Find music for a quiet study session, then compare two ways to judge tag matches.

## Run

From this folder:

```powershell
py -3.14 main.py
```

Use `python main.py` if the Windows launcher is unavailable. Target Python 3.14.6;
verified on 3.14.7. Standard library only; no network, packages, file writes, or
sibling-demo imports. Read the short `main.py` first; `main2.py` has the same
behavior with expanded comments.

## What the Results Show

The preference profile is calm and piano. The program displays useful song names
in each order, then a small labeled score table.

| Song | Shared tags | Distinct tags in the union | Jaccard |
| --- | ---: | ---: | ---: |
| Quiet Keys | 2 | 2 | 1.000 |
| Soft Strings | 1 | 3 | 0.333 |
| Piano Focus | 1 | 2 | 0.500 |
| Unknown Track | 0 | 2 | 0.000 |
| Broad Mix | 2 | 6 | 0.333 |

Count order: Quiet Keys, Broad Mix, Soft Strings, Piano Focus, Unknown Track.

Jaccard order: Quiet Keys, Piano Focus, Soft Strings, Broad Mix, Unknown Track.

Quiet Keys and Broad Mix share the same two preference tags. Broad Mix has more
unrelated tags, so its normalized similarity is lower. The algorithm uses fictional
metadata; it does not determine whether a person will actually enjoy a song.

## Scoring Rules

- Intersection (`&`) contains tags shared by the song and profile.
- Union (`|`) contains every distinct tag in either collection.
- Shared count is the intersection size.
- Jaccard is intersection size divided by union size.
- Our policy returns zero for an empty union. Missing or None tags become empty.
- Repeated tags count once. Equal scores use ascending ID.
- The profile has no song ID; no catalog song needs self-exclusion in this example.

## Code Landmarks

`shared_count` and `jaccard` contain the core comparison logic.
`score_songs` builds descriptive result dictionaries without changing the input.
The named ordering helpers arrange the display; Tuesday develops top-k and
weighted ranking further.

`song_data.py` supplies the fixture; `song_support.py` supplies the missing-tag
policy. `song_display.py` and `console_style.py` keep presentation separate from
scoring. Colors appear on supported terminals; redirected output is plain.

## Verify

```powershell
py -3.14 test_demo.py
```

Checks cover both code versions, hand-calculated scores, duplicate/missing/empty
tags, deterministic ordering, and unchanged source data. Run without `-O`.

[All daily demos](../../README.md)
