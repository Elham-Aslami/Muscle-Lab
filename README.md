# Anatomy Practical 2 — GitHub Pages

This folder is ready to upload. The current app includes the fuller, non-clickable anatomical context and the camera-selection fix, plus phone home-screen icons, offline caching, and a mobile grid-width fix. No installation, API key, backend, or build command is needed to publish the prepared files.

## Publish with GitHub's website

1. Extract `Anatomy_Practical_2_GitHub_Pages.zip` on your computer.
2. Create a GitHub repository, for example `anatomy-practical-2`. GitHub Free supports Pages from public repositories; eligible paid plans also support private repositories. Read the publishing note below before choosing public visibility.
3. Choose **Add file → Upload files**. Upload the extracted folder's **contents**, including `index.html` and the `icons`, `app`, and `scripts` folders. Do not upload the ZIP itself. `index.html` must appear at the top level of the repository.
4. Commit the files to the `main` branch.
5. Open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then **main** and **/(root)**. Click **Save**.
6. Wait for deployment, then use the **Visit site** link in Pages settings. Your project URL will normally be `https://YOUR-USERNAME.github.io/anatomy-practical-2/`, using your actual GitHub username and repository name. Publishing can take up to ten minutes.

Official instructions: [GitHub Pages publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [creating a Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Open it on your phone

Open the published HTTPS website link in your phone's browser. You do not need to download the HTML onto the phone.

- **iPhone:** in Safari, open the Share menu, choose **Add to Home Screen**, enable **Open as Web App** if shown, and tap **Add**. [Apple instructions](https://support.apple.com/en-ca/guide/iphone/iphea86e5236/27/ios/27).
- **Android:** in Chrome, open the menu and choose **Install and create shortcut → Install**, or the equivalent **Install app / Add to Home screen** option offered by your browser. [Google instructions](https://support.google.com/chrome/answer/9658361?hl=en&co=GENIE.Platform%3DAndroid).

Open it online once and allow the app and 3D model to finish loading. The site caches its core files for later offline visits. Offline access depends on the browser retaining that cache; clearing site data or browser storage eviction can remove it. External source links still require internet access. Current browsers with WebGL show the interactive 3D model; the embedded image reference is available if 3D is unsupported.

## Keep your progress

Scores, settings, and uploaded lab photos remain in the browser on each device. They are not automatically uploaded to GitHub and do not sync between your computer and phone.

To transfer progress from the downloaded app or another device, use **Settings & backup → Export backup**, then **Import backup** on the published site. Keep backups private; they may include your photographs. Regular exports also protect progress if browser data is cleared.

## Files

| File or folder | Purpose |
| --- | --- |
| `index.html` | Ready-to-run app, with the study content, visuals and 3D model embedded |
| `manifest.webmanifest` | Phone installation details and relative URLs |
| `sw.js` | Offline cache and scoped update handling |
| `icons/` | Browser and home-screen icons |
| `.nojekyll` | Publishes the prepared static files without a Jekyll build |
| `app/` | Editable application source and prepared content/model assets |
| `scripts/build-pages.mjs` | Rebuilds the app and cache revision after source edits |
| `package.json`, `package-lock.json` | Reproducible build dependencies |
| `NOTICE.md`, `VALIDATION.md` | Attribution, asset licenses and validation notes |

All web asset paths are relative, so the app works at a GitHub project URL such as `/anatomy-practical-2/` as well as a site's root. The ready-to-upload folder does not contain student backups, lab-photo uploads, or the original workbook PDFs.

## Edit and rebuild later

Publishing the prepared files does not require Node.js. For source edits, install Node.js 20 or later, then run these commands in this folder:

```sh
npm ci
npm run build
```

Upload or commit the changed source files together with the generated `index.html`, `manifest.webmanifest`, and `sw.js`. Rebuilding automatically changes the offline cache revision. When online, reopening or refreshing the app retrieves the latest page without resetting saved progress. Do not edit only the generated HTML and leave the source behind.

For a local web preview, run `python -m http.server 8000` from this folder and open `http://localhost:8000/`. Opening `index.html` directly also runs the study app, but installation and service-worker caching require HTTPS or localhost.

Optional anatomy preparation scripts in `app/` retain the original asset-processing workflow. They require the original source assets and Python dependencies and are not needed to build or publish this prepared app.

## Publishing note

GitHub Pages sites are normally public even when their source repository is private. Workbook figures in this app were provided for personal study; public redistribution permissions have not been verified. Obtain permission or replace those figures with appropriately licensed alternatives before public distribution. Keep the model/software attributions in `NOTICE.md`. No site has been published on your behalf by preparing this package.
