---
name: gamedev-steam-publish
description: "Imported awesome-gamedev-agent-skills guidance for steam-publish workflows in game development projects."
---
# Steam Publish (Steamworks + SteamPipe)

Take a finished build to a live Steam store page. Two tracks run in parallel and both must be
approved before release: the **store page** (presence) and the **build** (SteamPipe upload +
the release checklists). This skill is the operational checklist; deep build-script,
CI/CD, and troubleshooting detail lives in `references/steampipe-build-scripts.md`.

## When to use

- Use when setting up a Steam app, building/editing the store page, configuring depots and
  packages, uploading a build via SteamPipe/steamcmd, managing beta branches, or releasing
  and updating a Steam title.
- Triggers: `steam_appid.txt`, the Steamworks SDK `tools/ContentBuilder`, `app_build_*.vdf`,
  `steamcmd`, "publish on Steam", "depot", "set build live".

**When *not* to use:** publishing on itch.io (use `itch-publish`); writing the
Steamworks **API** in-game (achievements/cloud/overlay live in engine SDK integrations, not
here); store/financial *advice* (pricing strategy, tax) — direct the user to Steamworks docs
and their own counsel.

## Prerequisites (do these once, in order)

1. **Partner account + Steam Direct fee.** Each new app requires the Steam Direct recoupable
   fee (USD $100 per app at time of writing). You receive an **App ID** — find it on your
   Steamworks homepage. Treat the App ID as the key to everything below.
2. **A dedicated build account with least privilege.** Builds require a Steam account in your
   partner group with **Edit App Metadata** and **Publish App Changes To Steam**. Create a
   *separate* build account with only those permissions (not your admin login). Releasing the
   app additionally needs **Manage pricing and discounts**.
3. **Download the Steamworks SDK** on the upload machine. The SteamPipe tools are under
   `tools/ContentBuilder/`.

> Security note: never commit account passwords or the `config.vdf` login token to the repo.
> See the CI/CD section in the reference for the supported token workflow.

## Core workflow

1. **Configure the app (App Admin).**
   - Set **launch options** (executable path + args per OS) under *Installation*. For a
     sub-folder exe, put the sub-folder in the Executable field — no leading slashes/dots.
   - Add **depots** on the *Depots* page (a depot is a bucket of files). Name each depot
     ("Base Content", "Windows Content"). Leave *[All languages]* / *[All OSes]* unless the
     depot is genuinely OS- or language-specific.
   - **Grant yourself the depots:** add them to your **Developer Comp** package on the
     *Associated Packages & DLC* page, or you won't own the content you upload.
   - **Publish** the configuration. Unpublished config is the most common cause of upload
     failures.
2. **Build the store page (presence track).** Fill graphical assets, description, tags,
   trailers, system requirements. When complete, click **Mark as ready for review**. Store
   review takes ~3-5 business days; submit at least **7 days** before you want it live. It
   must be in **Coming Soon** for at least **2 weeks** before release.
3. **Create your build scripts.** Start with the simple app-build `.vdf` in Patterns below;
   for multi-depot/multi-platform apps use depot scripts (see the reference). The script maps
   local files into depots and names where build output/logs go.
4. **Bootstrap steamcmd and upload.** Run `steamcmd` once to self-update, then run the build
   (Patterns). steamcmd chunks files (~1 MB), uploads only changed chunks, and registers a
   global **BuildID**.
5. **Set the build live on a branch.** Go to `https://partner.steamgames.com/apps/builds/<AppID>`,
   pick the build, **Preview Change**, then **Set Build Live Now** for a branch. Test on a
   beta branch first (see `references/steampipe-build-scripts.md` for branch setup).
6. **Run the Game Build checklist** and **Mark as ready for review** (store presence must be
   submitted *before* the build review). Both tracks must be approved.
7. **Release manually.** When approved and Coming Soon has run its time, use the green
   **Release App** button → **Publish Now** → **Release Now**. Approved titles do **not**
   release themselves.
8. **Update later** by uploading a new build and setting it live on `default` (manually) or
   shipping to a beta branch first. See `references/steampipe-build-scripts.md`.

## Patterns

### 1. SteamPipe ContentBuilder layout (Steamworks SDK)

```text
tools/ContentBuilder/
  builder/         steamcmd.exe (Windows)   <- run once to bootstrap
  builder_linux/   steamcmd (Linux)
  builder_osx/     steamcmd (macOS)
  content/         <- your final, runnable build goes here (the files players get)
  output/          build logs + chunk cache (safe to delete; speeds up re-uploads)
  scripts/         <- your *.vdf build scripts live here
```

### 2. Minimal app build script — `scripts/app_build_1000.vdf`

```text
// AppID 1000 with one depot (1001): upload everything under ../content recursively.
// VDF is Valve KeyValues: "key" "value", braces for nesting. Adjust IDs to your app.
"AppBuild"
{
    "AppID"       "1000"                 // your App ID
    "Desc"        "1.0.0 launch build"   // internal only; visible in Your Builds

    "ContentRoot" "..\content\"          // root of files to upload (relative to this file)
    "BuildOutput" "..\output\"           // logs + chunk cache

    "Depots"
    {
        "1001"                           // your Depot ID
        {
            "FileMapping"
            {
                "LocalPath"  "*"         // all files from ContentRoot
                "DepotPath"  "."         // mapped to the depot root
                "recursive"  "1"         // include subfolders
            }
        }
    }
}
```

### 3. Upload the build (Windows; substitute the platform builder elsewhere)

```bat
REM Run from the SDK. Bootstrap once, then build. Use a build account, not your admin login.
tools\ContentBuilder\builder\steamcmd.exe ^
  +login <build_account> <password> ^
  +run_app_build ..\scripts\app_build_1000.vdf ^
  +quit
```

```text
What happens: steamcmd self-updates -> logs in -> for each depot, hashes files into ~1 MB
chunks -> uploads only NEW chunks -> writes a depot manifest -> finishes with a global
BuildID. The build is NOT live yet; set it live per the workflow above.
```

### 4. Iterate safely with a preview build (uploads nothing)

```text
// Add to the AppBuild block to validate file mappings without uploading:
"Preview" "1"     // outputs logs + a file manifest into BuildOutput only
// And to auto-set live on a BETA branch after a successful build (never 'default'):
"SetLive" "beta-qa"
```

## Pitfalls

- **The `default` branch cannot be set live automatically.** `SetLive` only works for a
  *beta* branch; you must set the default (customer) build live by hand in App Admin. Plan
  releases around this.
- **Store page must be approved before the build.** You cannot submit the build for review
  until store presence is submitted; both must pass, and Coming Soon must run ~2 weeks.
- **Titles never auto-release.** Even after approval, a human must click **Release App** at
  the chosen moment.
- **Mac/Linux install nothing.** Almost always: the OS-specific depots aren't in the package.
  Add every depot to the package on *Associated Packages & DLC*.
- **Unpublished app config.** "Failed to get application info" / build errors usually mean
  depots, launch options, or the App ID config were never **Published**.
- **`status = 6` on build.** The build account lacks permission for the App ID, or
  `ContentRoot`/`LocalPath` points at the wrong (empty) path.
- **Committing the login token.** The `config.vdf` Steam Guard token and account password are
  secrets. Keep them out of the repo; use the CI workflow in the reference.
- **Released-app safety delay.** Changing the build account's email/phone forces a **3-day**
  wait before you can set a build live for a *released* app — don't reconfigure the account
  right before launch.

## References

- For advanced multi-depot/multi-platform build scripts, `FileExclusion`/`FileProperties`,
  beta-branch setup, the CI/CD login-token workflow, and the SteamPipe troubleshooting table,
  read `references/steampipe-build-scripts.md`.
- Primary docs: Steamworks "Uploading to Steam" (`partner.steamgames.com/doc/sdk/uploading`),
  "Release Process" (`/doc/store/releasing`), "Branches (Betas)" (`/doc/store/application/branches`),
  "Depots" (`/doc/store/application/depots`).

## Related skills

- `itch-publish` — the same game shipped on itch.io with `butler` (often done alongside Steam).
- `game-jam` / `prototype-fast` — earlier stages of the same project's lifecycle.
