# Playlist Integrity and Limits

DEM-W07D03 | Week 7 topic-family Demo 03; delivered Week 8 Monday, November 30

The Thursday, November 26 class is canceled for the holiday. The existing folder
and demo ID are retained so code and links remain stable.

Check whether saved playlist metadata changed, and distinguish that result from
the quality of a song recommendation.

## Run

From this folder:

```powershell
py -3.14 main.py
```

Use `python main.py` if the Windows launcher is unavailable. Target Python 3.14.6;
verified on 3.14.7. Standard library only; no network, installed packages, file
writes, audio files, or sibling-demo imports.

Read `main.py` first. `main2.py` runs the same logic with expanded explanations.

## Two Independent Changes

Both scenarios start from an independent copy of the original playlist.

| Scenario | What changes? | Recommendation result | Fingerprint |
| --- | --- | --- | --- |
| Original | Nothing | Quiet Keys 1.000; Soft Strings 0.333 | Reference |
| Remove Quiet Keys tags | Tag metadata | Soft Strings becomes first; Quiet Keys scores 0 | Would change; checked separately in tests |
| Edit only Quiet Keys title | Title metadata | Same IDs, order, and scores | Changes; shown in the application |

The missing-tag example shows how incomplete metadata can hide a good match.
The title-only example shows why a changed fingerprint does not necessarily mean
a changed recommendation.

The console uses readable names and explicit CHANGED/UNCHANGED results. Full
SHA-256 values are retained as labeled technical evidence rather than the only
explanation.

## Snapshot Contract

The supplied `snapshot_support.py` helper turns selected metadata into consistent
bytes before hashing:

1. Include only ID, title, and unique sorted tags.
2. Sort records by ID and JSON keys by name.
3. Use the declared compact JSON formatting and UTF-8 encoding.

Record and tag order do not change the fingerprint. A title change does.
Missing or None tags are treated as empty. Duplicate record IDs are rejected.
Fields outside this declared contract are not checked by this fingerprint.

Canonical means consistent under these rules; it is not a promise that every
program serializes the same data this way. The helper contains a short optional
AI explanation prompt about JSON text, encoding, and bytes.

`digest` passes those bytes to the standard library SHA-256 implementation.
Students do not implement a cryptographic algorithm.

## What the Evidence Means

A changed digest detects a change in this serialized snapshot. Comparison needs
a trustworthy reference value. A matching digest alone does not prove authenticity,
fairness, accurate tags, or recommendation quality.

This digest is distinct from Python's lookup `hash()`, similarity scoring, and
encryption. It covers metadata, not the music audio.

## Code Landmarks

- `rank`: reuses Jaccard scoring; returns ID/score dictionaries without titles.
- `digest`: names the serialization, hashing, and printable-digest steps.
- `deepcopy`: isolates nested dictionaries/tag lists so scenarios preserve the original.
- `playlist_display.py`: uses each snapshot's titles to display its results.
- `console_style.py`: reusable terminal colors; redirected output stays plain.
- `playlist_data.py`: the small fictional fixture.

## Verify

```powershell
py -3.14 test_demo.py
```

Checks cover both code versions, the preserved reference digest, reordered and
duplicate tags, title-only changes, missing tags, empty inputs, exact ties,
duplicate-ID rejection, selected-field boundaries, and unchanged original data.
Run without `-O`.

[All daily demos](../../README.md)
