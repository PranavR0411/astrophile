# Pranav R. Iyengar — personal website

Static site (plain HTML/CSS, no build step) for GitHub Pages.

```
index.html              About, research-across-the-spectrum figure, contact
projects.html           All projects
projects/*.html         One page per project
assets/css/style.css    All styling
assets/js/site.js       Email link
assets/favicon.svg
tools/localize_images.py  Copies images from Wix into assets/img
```

## Publish on GitHub Pages

1. Create a repository named **`<your-github-username>.github.io`** (this gives you the root URL `https://<username>.github.io`). Any other repo name also works; the site will live at `https://<username>.github.io/<repo>/`.
2. Upload the contents of this folder to the repository root (drag-and-drop on github.com, or `git push`).
3. In the repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch → `main` / `(root)`** → Save.
4. The site goes live within a minute or two.

## Before you delete the Wix site

Images and the CV PDF are currently loaded from Wix's servers. To make the site self-contained:

```bash
python3 tools/localize_images.py     # downloads images to assets/img and rewrites the pages
```

Then save your CV as `assets/cv.pdf` and replace the Wix CV URL (search for `filesusr.com`) in the HTML files with `assets/cv.pdf` (or `../assets/cv.pdf` inside `projects/`).

## Editing

- Text lives directly in the HTML files.
- Colours and fonts are the variables at the top of `assets/css/style.css`.
- The email address used by the contact buttons is in the `data-u` / `data-d` attributes (search for `js-email`).
