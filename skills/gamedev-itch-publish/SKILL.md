---
name: gamedev-itch-publish
description: "Imported awesome-gamedev-agent-skills guidance for itch-publish workflows in game development projects."
---
# itch.io Publish (butler)

Get a build onto an itch.io page and keep it updated. The page is created in the browser; all
uploads go through **butler**, itch.io's command-line tool, with one command you'll use
forever: `butler push`. butler diffs against the previous build and uploads only what
changed. Deep CI/CD and flag detail lives in `references/butler-ci.md`.

## When to use

- Use when creating/updating an itch.io project page, installing or logging in to butler,
  uploading a build with `butler push`, choosing channel names, versioning uploads, or
  shipping a jam/demo/release build to itch.io.
- Triggers: `butler push`, `butler login`, channels, `.itch.toml`, "publish on itch",
  "upload to itch".

**When *not* to use:** publishing on Steam (use `steam-publish`); jam *scope/planning* (use
`game-jam` — this skill is only the upload mechanics); building the game itself (engine
skills).

## Core workflow

1. **Create the project page** at `itch.io/game/new`. Set the **Kind of project**: keep
   *Downloadable* for native builds, or choose **HTML** for a browser-playable game (this is
   required for web builds — see Pitfalls). Set pricing/visibility (Draft until ready).
2. **Install butler and log in.** Download from `itchio.itch.io/butler`, add it to `PATH`,
   then `butler login` (opens a browser to authorize). Verify with `butler version`. For
   CI, use `BUTLER_API_KEY` instead — see the reference.
3. **Prepare a portable build folder** — the exact files a player runs, nothing extra. Push a
   **folder** (or a single `.zip` *of* that folder), **not an installer** and **not a
   pre-compressed archive of archives** (hurts patching; see Pitfalls).
4. **Push to a channel:** `butler push <dir> <user>/<game>:<channel>`. The channel name
   determines the platform tag (see Patterns). The first push uploads everything; later
   pushes to the same channel upload only the diff.
5. **Set platform/HTML tags** on the *Edit game* page if a channel wasn't auto-tagged
   correctly, then **Save**. For browser games also flip the page to **HTML** and tag the
   channel *playable in browser*.
6. **Version your builds** (optional but recommended): `--userversion 1.2.0` or
   `--userversion-file build.txt` so you control the version string players and the update
   API see.
7. **Update later** by pushing to the *same* channel again. Use `butler status <user>/<game>`
   to see channels/builds and `butler push-preview` to see what a push would change before
   sending it.

## Patterns

### 1. The one command you need — `butler push`

```bash
# butler push <directory-or-zip> <user>/<game>:<channel>
butler push ./build/windows leafy/my-game:windows
butler push ./build/mac     leafy/my-game:osx
butler push ./build/linux   leafy/my-game:linux
butler push ./web           leafy/my-game:html   # browser build (also set page Kind = HTML)
```

### 2. Channel naming controls the platform tag (kebab-case, lowercase)

```text
Substring in channel name -> auto-applied tag:
  win / windows  -> Windows        linux -> Linux
  mac / osx      -> macOS          android -> Android
Multiple platforms in one channel are allowed: e.g. a Java jar:
  butler push ./jar leafy/my-game:win-linux-mac
Convention: lowercase words separated by dashes (windows-beta, osx-demo, soundtrack).
Tags are only the INITIAL guess — fix them anytime on the Edit game page (then Save).
```

### 3. Version, verify, and preview

```bash
butler version                              # print version; confirms install + PATH
butler login                                # authorize this machine (opens browser)

# Set an explicit version string instead of itch's auto-incrementing integer:
butler push ./build leafy/my-game:windows --userversion 1.2.0
butler push ./build leafy/my-game:windows --userversion-file build_number.txt

butler status leafy/my-game                 # list channels + latest builds/versions
butler push-preview ./build leafy/my-game:windows   # NEW/MODIFIED/DELETED/SAME, uploads nothing
```

### 4. First-time, hidden, and filtered pushes

```bash
# Hide a brand-new channel from the page until you're ready (NEW channels only):
butler push ./build leafy/my-game:windows-beta --hidden

# Exclude files from the upload without copying the folder (--ignore is repeatable):
butler push ./build leafy/my-game:windows --ignore '*.pdb' --ignore '*.dSYM'

# Preview exactly what would be sent, without sending it:
butler push ./build leafy/my-game:windows --dry-run
```

## Pitfalls

- **Pushing an installer.** itch.io patches *portable* builds; an installer (`.exe`/`.msi`)
  defeats patching and the itch app's auto-update, and may need admin rights players don't
  have. Push the extracted, runnable folder instead.
- **Pre-compressed builds.** Pushing a heavily compressed archive (or an archive of archives)
  makes patches huge — a tiny change rewrites the whole compressed blob. Push uncompressed
  files; itch.io compresses on its side.
- **A folder containing only one `.zip`.** butler auto-unzips it and pushes the contents
  (to avoid a "zip in a zip"). Pass `--no-auto-unzip` only if you truly want the zip uploaded
  as one opaque file.
- **HTML5 game shows as a download.** Two switches are required: set the page **Kind** to
  *HTML* and tag the channel *playable in browser* on the *Edit game* page after the first
  push — neither happens automatically from the channel name.
- **`--hidden` on an existing channel errors.** It only applies when the push *creates* a new
  channel. Unhide later from *Edit game*.
- **Channel typos make duplicate slots.** `windows` and `win-final` are different channels and
  create separate downloads. Decide your channel names up front and reuse them.
- **30 GB cap.** itch.io rejects builds whose total *uncompressed* size exceeds 30 GB.
- **Secrets in CI logs.** A `BUTLER_API_KEY` printed in a public log is compromised — revoke
  it immediately on the API keys page. See the reference for safe CI usage.

## References

- For CI/CD (GitHub Actions/GitLab) with `BUTLER_API_KEY`, automated install via `broth`, the
  full flag list, and the update-check API, read `references/butler-ci.md`.
- Primary docs: the butler manual — `itch.io/docs/butler` (installing, login, pushing).

## Related skills

- `steam-publish` — the same game on Steam via SteamPipe (often shipped alongside itch.io).
- `game-jam` — most jams are hosted on itch.io; this skill handles the upload step.
- `prototype-fast` — share an early prototype on a Draft/restricted itch page for playtesting.
