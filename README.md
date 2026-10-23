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
    python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
    ./pr-radar

The first run builds `~/Applications/PR Radar.app` (an alias bundle that runs this checkout, so keep the folder where it is; if you move it, re-run `./pr-radar install-app`) and opens it. Afterwards open it from Spotlight or the Dock like any app.

On first launch pick the repos to watch in the **Repos** menu: tick or untick repos, or add one by name. The list shows repos where you recently authored or reviewed PRs first, then the rest alphabetically. Newly added repos start with a silent baseline, so you don't get a burst of notifications. Allow notifications when macOS asks.

- Closing the window keeps PR Radar running and polling; **⌘Q** quits it.
- **View → Refresh** (⌘R) fetches now.
- Polling runs every 5 minutes, Mon-Fri 08:00-19:00 in your timezone. macOS may delay polls while the app is idle in the background (App Nap), so notifications can arrive late when the window is hidden. Polls also run when you switch back to the app.
- To start it at login, add `PR Radar` in System Settings → General → Login Items & Extensions (click +, pick `~/Applications/PR Radar.app`). A login launch starts with the window hidden.

## Command line

    ./pr-radar              # open the app, building it first if needed
    ./pr-radar install-app  # rebuild the app bundle
    ./pr-radar --once [--open]   # fetch once, write the dashboard and notify (--open shows it in your browser)

## Config and data

- Settings: `~/.config/pr-radar/config.json` (repos, timezone, work hours/days, poll interval, required approvals).
- Generated data (dashboard, snapshot, log): `~/Library/Application Support/pr-radar/`. Check `pr-radar.log` if something looks wrong.
- First run only records a baseline (no notifications). One notification after 6 consecutive failed polls.

## Updating

    git pull && .venv/bin/pip install -r requirements.txt && ./pr-radar install-app

Then quit and reopen the app.

## Uninstalling

Quit the app, then delete `~/Applications/PR Radar.app`, `~/.config/pr-radar`, `~/Library/Application Support/pr-radar` and the checkout. Remove it from Login Items if you added it.

## Licence

[MIT](LICENSE)
