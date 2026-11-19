# Before switching adidamari.co.il to the new site

1. **Move the images into the site.** Most images still load from the old WordPress site (adidamari.co.il/wp-content/uploads/...). Copy them into `assets/img/` (same year/month folders), then rebuild so the pages use the local copies.
   - When copying, make sharp **and** light WebP versions from the full-resolution originals (e.g. `dddssss.png`, `aaa.png`, `big-screen1.png`, `sssss.png`, not the compressed `-scaled.webp`), and keep the originals for the click-to-enlarge view (`data-full`).
2. Check that every page loads with images, with WordPress not involved.
3. In names.co.il, point the domain to GitHub Pages (website records only; leave any email records alone).
4. Turn on HTTPS in GitHub Pages settings.
5. Only after the new site is live and checked: cancel the WordPress hosting.

# Open questions to confirm
- Medical app: Role / Scope in the info row were guessed.
- NFT: comparison tables were retyped from images. Double-check each ✓ / ✗.
- NFT: Wireframing section removed (copy kept in `_build/removed/nft-wireframing.html`).
