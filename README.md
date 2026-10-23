# PR Radar

A Mac app that tracks your GitHub pull requests via the [`gh`](https://cli.github.com) CLI and tells you when something changes.

- **Needs my review**: open PRs with a review requested from you or your teams.
- **My PRs**: open PRs you authored, with review state, approvals, CI, conflicts, stacks, comment count, age.
- Notifications (from PR Radar itself, click to bring the dashboard forward) for: new review request, request removed (not when you reviewed it yourself), approved, changes requested, CI red/green, new comments, merge conflict, merged/closed.
- The Dock icon shows how many PRs are waiting for your review. Links open in your default browser.
- Nothing leaves your machine except calls to GitHub.

## Requirements

- macOS (developed and tested on Apple silicon) and Python 3 (tested with Homebrew's: `brew install python`).
- `gh` installed and logged in: `brew install gh && gh auth login`. PR Radar uses whatever account `gh` is logged in as and never stores a token itself. For organisation repos that enforce SAML SSO, that login must be authorised for the organisation.

## Install and run

    git clone https://github.com/jakubdolejs/pr-radar.git
    cd pr-radar
    ./pr-radar

The first run installs PR Radar (about a minute): it copies the code and a private Python environment to `~/Library/Application Support/pr-radar/app`, builds `~/Applications/PR Radar.app`, and opens it. You can delete the clone afterwards; the app doesn't depend on it. Open it from Spotlight or the Dock like any app.

On first launch pick the repos to watch in the **Repos** menu: tick or untick repos, or add one by name. The list shows repos where you recently authored or reviewed PRs first, then the rest alphabetically. Newly added repos start with a silent baseline, so you don't get a burst of notifications. Allow notifications when macOS asks.

- Closing the window keeps PR Radar running and polling; **⌘Q** quits it.
- **View → Refresh** (⌘R) fetches now.
- Polling runs every 5 minutes, Mon-Fri 08:00-19:00 in your timezone. macOS may delay polls while the app is idle in the background (App Nap), so notifications can arrive late when the window is hidden. Polls also run when you switch back to the app.
- To start it at login, add `PR Radar` in System Settings → General → Login Items & Extensions (click +, pick `~/Applications/PR Radar.app`). A login launch starts with the window hidden.

## Command line

    ./pr-radar                      # open the app, installing it first if needed
    ./pr-radar install-app          # reinstall; also how you update (see below)
    ./pr-radar uninstall [--purge]  # remove the app and its environment (--purge: also config and data)
    ./pr-radar --once [--open]      # fetch once, write the dashboard and notify (--open shows it in your browser)

Running `./pr-radar` from a clone opens the *installed* app, not the clone's code, and tells you when the installed copy is older.

## Config and data

- Settings: `~/.config/pr-radar/config.json` (repos, timezone, work hours/days, poll interval, required approvals).
- Generated data (dashboard, snapshot, log): `~/Library/Application Support/pr-radar/`. Check `pr-radar.log` if something looks wrong. The installed copy of the app is in its `app/` subfolder.
- First run only records a baseline (no notifications). One notification after 6 consecutive failed polls.

## Updating

    git pull && ./pr-radar install-app

Then quit and reopen the app. If Homebrew upgrades Python and the app stops launching, run `./pr-radar install-app` again to rebuild its environment.

## Uninstalling

    ./pr-radar uninstall            # keeps your config and data
    ./pr-radar uninstall --purge    # removes those too

Remove PR Radar from Login Items too if you added it.

## Licence

[MIT](LICENSE)
