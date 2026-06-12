# SEU Brand Brochure Demo

A single-page digital brand brochure for **Southeast University (SEU)**.

## Why the QR code shows 404

The QR code points to:

```
https://dzha0118-ai.github.io/seu-brochure-demo
```

If scanning it shows a GitHub **404**, the page has **not been deployed to GitHub Pages yet**. The QR itself is correct — it will work as soon as the repository is published.

## How to deploy (so the QR works)

1. Create a new public GitHub repository named `seu-brochure-demo` under the account `dzha0118-ai`.
2. Upload all files from this folder to the repository (or push with Git):
   - `index.html`
   - `seu_logo.png`
   - `cover_optimized.jpg`
   - `intro_optimized.jpg`
   - `seu_brochure_qr.png`
   - any other image/assets used by the page
3. Go to **Settings → Pages** in the repository.
4. Under **Source**, select **Deploy from a branch**, choose `main`, and folder `/ (root)`.
5. Save. After ~1 minute, the site will be live at `https://dzha0118-ai.github.io/seu-brochure-demo`.
6. Scan the QR code again — it will now open the brochure.

## Local preview

Run a local server in this folder:

```bash
python -m http.server 8765
```

Then open `http://localhost:8765` in your browser.

## Latest updates

- Cover badge centered and animated.
- Interactive globe network in the **Global Collaboration Network** section (hover points for partner info).
- Smooth hover/scroll animations across cards, campuses, disciplines, and stats.

