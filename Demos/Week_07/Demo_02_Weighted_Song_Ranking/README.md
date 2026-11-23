# Weighted Song Ranking

DEM-W07D02 | Week 7, Tuesday

Help a listener find a short list of songs for studying. Filter the available
songs, rank the matches, and see how giving a preference more importance changes
the suggestions.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

Use `python main.py` if the Windows launcher is unavailable. Target Python 3.14.6;
verified locally on 3.14.7. Standard library only; no network, installed packages,
or imports from sibling demos. The program does not write files.

Read `main.py` first. `main2.py` runs the same logic with expanded teaching comments.

## Optional Filter and Result Limit

```powershell
py -3.14 main.py --tag calm --limit 3
py -3.14 main.py --tag calm --limit 4
py -3.14 main.py --emphasis piano
```

- `--tag` keeps songs with that exact tag. Omit it to consider the whole catalog.
- `--limit` selects the maximum number displayed in each list; default 3.
- `--emphasis` gives calm or piano weight 4; default calm. Other tags weigh 1.

The filter selects eligible songs. It does not change the listener's preference
profile, which stays calm and piano. The sequence is **filter, score, sort, limit**.
Limit after sorting; choosing the first three catalog records is a different task.

## See Top-k and a Tie

With `--tag calm --limit 3`, four of the six songs match, but only three appear:

| Position | Equal weights | Calm emphasized |
| --- | --- | --- |
| 1 | Quiet Keys (S01), 1.000 | Quiet Keys (S01), 1.000 |
| 2 | Evening Keys (S06), 0.667 | Evening Keys (S06), 0.833 |
| 3 | Soft Strings (S02), 0.333 | Soft Strings (S02), 0.667 |
| Outside top 3 | Gentle Guitar (S05), 0.333 | Gentle Guitar (S05), 0.667 |

Soft Strings and Gentle Guitar have identical tags, so they receive identical
scores. S05 deliberately appears before S02 in the supplied catalog. Sorting by
descending score and then ascending ID still puts S02 first. The displayed tie
explanation identifies why S02 receives the last place in the top three.

Change to `--limit 4` to reveal both tied songs. The tie is exact, not a rounding
artifact. An ID tie-break makes the order repeatable; it does not imply higher
musical quality.

## See a Changed Recommendation

Without a filter, the baseline top three are Quiet Keys, Evening Keys, and Piano
Focus. Emphasizing calm replaces Piano Focus with Soft Strings. The output names
matched tags and their contributions so the change can be explained.

Try `--tag not-a-tag` for a friendly no-match message. A limit of zero intentionally
displays no recommendations; negative limits are rejected.

## Scoring Contract

Score = total matched tag weight / total weight of all distinct union tags.

Weights must be finite and nonnegative; unspecified weights are 1. Missing or
None tags are treated as empty. An empty or all-zero-weight union scores 0.
Duplicates do not add extra weight. Scores sort descending; exact ties use
ascending ID. Fictional metadata illustrates the algorithm, not musical truth
or trained machine learning.

## Code Landmarks

- `filter_songs`: optional exact-tag selection.
- `weighted_similarity`: explicit loops for matched and union weights.
- `ranking_key`: named score/ID ordering rule.
- `rank_songs`: named result records, sorting, and top-k slicing.

`song_data.py` holds the small fixture. `song_support.py` supplies input checks.
`song_display.py` handles readable results and the cutoff/tie explanation;
`console_style.py` handles reusable terminal colors. Redirected output is plain.
The CLI requests the full ranking so the display can report hidden matches and
explain a cutoff tie; `rank_songs` itself also supports a smaller k.

## Verify

```powershell
py -3.14 test_demo.py
```

Checks cover both code versions, score changes, exact ties across the cutoff,
reversed input order, optional filtering, empty/missing data, result limits,
invalid weights, and unchanged source data. Run without `-O`.

[All daily demos](../../README.md)
