# butler: CI/CD, full flag reference, and the update-check API

Depth for `itch-publish`. Read this for automated uploads, the complete `butler push` flag
set, and notifying players of updates. Verify against the primary docs:
[the butler manual](https://itch.io/docs/butler) (installing, login, pushing).

## 1. Authentication for CI (`BUTLER_API_KEY`)

Interactive `butler login` opens a browser — useless in CI. Instead, set the
**`BUTLER_API_KEY`** environment variable and butler uses it automatically.

Where to get the key:
- Run `butler login` once locally, then read it from the creds file:
  - Linux: `~/.config/itch/butler_creds`
  - macOS: `~/Library/Application Support/itch/butler_creds`
  - Windows: `%USERPROFILE%\.config\itch\butler_creds`
- Or generate one on your itch.io **API keys** page (`itch.io/user/settings/api-keys`) — the
  relevant key has its source set to `wharf`.

Store it as a CI secret. **Never** print it; a key leaked into a public build log is
compromised — revoke it immediately on the API keys page.

## 2. Installing butler in CI (use `broth`, not the page link)

The `itchio.itch.io/butler` download links **expire**, so they can't be hard-coded. Use the
permanent **broth** URLs, which always serve the latest stable build of a channel:

```bash
# Example: latest stable Linux amd64 butler. Substitute the channel for your runner OS.
curl -L -o butler.zip "https://broth.itch.zone/butler/linux-amd64/LATEST/archive/default"
unzip butler.zip
chmod +x butler
./butler -V        # prints version; confirms it runs
```

Common broth channels: `linux-amd64`, `windows-amd64`, `darwin-amd64`. The `-head` channels
are bleeding-edge; the others are stable. The zip also contains two 7-zip helper libraries —
harmless, and not required for `butler push`.

## 3. GitHub Actions example

```yaml
name: Publish to itch.io
on:
  push:
    tags: ["v*"]            # publish when you tag a release
jobs:
  butler:
    runs-on: ubuntu-latest
    env:
      BUTLER_API_KEY: ${{ secrets.BUTLER_API_KEY }}   # set in repo secrets; never echoed
    steps:
      - uses: actions/checkout@v4
      # ... your build steps produce ./build/windows, ./build/linux, etc. ...
      - name: Install butler
        run: |
          curl -L -o butler.zip "https://broth.itch.zone/butler/linux-amd64/LATEST/archive/default"
          unzip butler.zip && chmod +x butler
      - name: Push builds
        run: |
          VERSION="${GITHUB_REF_NAME#v}"     # tag v1.2.0 -> 1.2.0
          ./butler push ./build/windows leafy/my-game:windows --userversion "$VERSION"
          ./butler push ./build/linux   leafy/my-game:linux   --userversion "$VERSION"
```

GitLab CI is equivalent: set `BUTLER_API_KEY` as a masked CI/CD variable and run the same
install + `butler push` commands in a job script.

## 4. `butler push` flag reference (verified)

| Flag | Purpose |
|---|---|
| `--userversion <v>` | Set an explicit version string instead of itch's auto-incrementing integer. |
| `--userversion-file <f>` | Read the version string from a file (single line, UTF-8, no BOM). |
| `--if-changed` | Skip the push if the contents are identical to the latest build (reduces no-op patches). |
| `--hidden` | Mark the upload hidden — **only** when the push creates a *new* channel; errors on an existing one. |
| `--ignore '<glob>'` | Exclude matching files; repeatable (`--ignore '*.pdb' --ignore '*.dSYM'`). Two dashes. |
| `--dry-run` | List every file that would be pushed (+ a summary); uploads nothing. |
| `--no-auto-unzip` | Push a single-`.zip` folder as one opaque file instead of unpacking it. |
| `--dereference` | Follow symlinks and upload copies of their targets (larger builds; use with care). |
| `--fix-permissions` | Normalize file permissions during the walk. |
| `--auto-wrap` | Wrap a single loose file in a folder before pushing. |

Related commands:

| Command | Purpose |
|---|---|
| `butler login` / `butler logout` | Authorize / clear local credentials (browser flow). |
| `butler version` | Print butler's version (confirms install + PATH). |
| `butler which` | Print the full path to the running butler binary. |
| `butler status <user>/<game>` | List channels and their latest builds/versions. |
| `butler push-preview <dir> <user>/<game>:<ch>` | Show `NEW/MODIFIED/DELETED/SAME` vs the last build; add `--changes-only` to hide unchanged. Uploads nothing. |
| `butler upgrade` | Update butler itself to the latest version. |

Notes:
- Processing: after a push the build is immediately live via a fast "default" patch; itch.io
  then regenerates an optimized (smaller) patch in the background. Both are transparent to
  players.
- Working from a remote/SSH host: `butler login` prints a URL; open it locally, copy the
  redirected (non-loading) page's address, and paste it back into the terminal.

## 5. Notify players of updates (no auth required)

Players who download directly (not via the itch app) don't auto-update. Query the latest
user-version for a channel and prompt them in-game:

```text
GET https://api.itch.io/wharf/latest?target=<user>/<game>&channel_name=<channel>
# or by numeric game_id (from the Edit game page URL):
GET https://api.itch.io/wharf/latest?game_id=<id>&channel_name=<channel>

Response: { "latest": "1.2.0" }   // omitted if the latest build has no user-version
```

Compare `latest` to your build's version (push with `--userversion`) and surface an
"update available" message. Private games return an "invalid game" error to avoid leaking
unreleased titles.
