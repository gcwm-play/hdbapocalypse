# Sprites

Pixel-art sprites for the 20 resident archetypes and 5 zombie variants.

- `atlas.png` is what the game uses. It is embedded in `play.html` as a base64 data URI (the `--atlas` CSS variable), so the game stays a single file.
  - Each cell is 18×26 px. Each row has 4 frames: idle, left step, idle, right step.
  - Rows 0–19 are residents, rows 20–39 are the same residents infected (green skin), and rows 40–44 are zombies.
  - `atlas.json` lists the row order.
- `characters/` has an 8× preview of each sprite.
- `hdbapocalypse_sprite_sheet.png` is a labelled sheet of all of them.
- `prompt_pack.html` has a full image-generation prompt for each character, for ChatGPT or Gemini.

## Regenerating

```
pip install pillow
python3 make_sprites.py out
```

Then re-embed `out/atlas.png` as the `--atlas` data URI in `play.html`.

## In the game

- Residents walk with a 4-frame cycle while they wander their flat. Elderly residents walk slower.
- The dot above the head is sanity (same colours as before). The coloured ring under the feet is the job: red guard, blue lookout, amber inventor, white medic, green gardener, brown salvage.
- A visible infection switches to the green-skinned row. Low health tints the sprite red. Below 25 sanity they pace fast and shake.
- Zombie kinds unlock by outbreak day: uncle shuffler (day 1), PMD runner (8), bloated (15), Ah Long (25), riot gear (40).
