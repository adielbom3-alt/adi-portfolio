from flows import nft_flow, beneficiary_flow, pending_flow

_Y = '<td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td>'
_N = '<td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td>'


def cmp_table(cols, rows):
    head = '<thead><tr><th></th>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr></thead>'
    body = ''.join('<tr><th scope="row">' + name + '</th>' + ''.join(_Y if v == 'y' else _N for v in vals) + '</tr>' for name, vals in rows)
    return '<div class="cmp-card"><table class="cmp">' + head + '<tbody>' + body + '</tbody></table></div>'


def marquee(names):
    label = ", ".join(names)
    return ('<div class="marquee" aria-label="Platforms we studied: ' + label + '"><div class="marquee-track" aria-hidden="true">'
            + ''.join('<span>' + n + '</span>' for _ in range(4) for n in names) + '</div></div>')


def feat(n, title, imgs, phones=False, trim_mobile=False):
    shots = ''.join(f'<img src="{src}"' + (f' data-full="{full}"' if full else '') + f' alt="{alt}" loading="lazy">' for src, full, alt in imgs)
    cls = ("feature-shots phones-shots" + (" trim-mobile" if trim_mobile else "")) if phones else ("feature-shots two" if len(imgs) == 2 else "feature-shots")
    style = f' style="--n:{len(imgs)}"' if phones else ""
    return (f'        <article class="feature">\n          <div class="feature-text"><h3><span class="fn">{n:02d}</span>{title}</h3></div>\n'
            f'          <div class="{cls}"{style}>{shots}</div>\n        </article>')


# Page sources. {IMG} = image folder, {UP} = path to site root, {ARROW} = arrow icon.

HOME = """
<div class="home-frame">
  <section class="hero">
    <div class="hero-text">
      <div class="spark" aria-hidden="true"><svg viewBox="0 0 64 64" width="44" height="44">
        <defs><linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset=".55" stop-color="#F8C23A"/><stop offset="1" stop-color="#E9A21F"/></linearGradient></defs>
        <path class="s s1" d="M38 8c1.4 10.6 5.4 14.6 16 16-10.6 1.4-14.6 5.4-16 16-1.4-10.6-5.4-14.6-16-16 10.6-1.4 14.6-5.4 16-16Z"/>
        <path class="s s2" d="M14 6c.7 5.3 2.7 7.3 8 8-5.3.7-7.3 2.7-8 8-.7-5.3-2.7-7.3-8-8 5.3-.7 7.3-2.7 8-8Z"/>
        <path class="s s3" d="M18 38c.6 4.6 2.4 6.4 7 7-4.6.6-6.4 2.4-7 7-.6-4.6-2.4-6.4-7-7 4.6-.6 6.4-2.4 7-7Z"/>
      </svg></div>
      <h1>Product designer at <b class="nb">WSC-Sports</b>, turning complex workflows into intuitive, <span class="nb">user-centered</span> experiences through thoughtful design, attention to detail, and a focus on business goals.</h1>
    </div>
    <div class="hero-photo">
      <img src="{IMG}2025/09/profile-pic.png" alt="Adi Elbom" width="483" height="483">
    </div>
    <a class="scroll-btn" href="#work" id="scrollBtn">Scroll to explore <span aria-hidden="true">↓</span></a>
  </section>

  <section class="projects" id="work" aria-label="Case studies">

    <div class="card reveal" aria-disabled="true">
      <div class="card-media"><img src="{IMG}2026/10/SK-05-%E2%80%93-Apply-caption-preset_default-hover.png" alt="Caption presets panel on the Video Studio timeline" loading="lazy" width="3840" height="2160"></div>
      <div class="card-body">
        <span class="tag">SaaS • Video • Creator tools</span>
        <h2>Animated captions that keep creators in one place</h2>
        <p>A caption-styling feature in the Video Studio platform that lets users pick, edit, and save animated caption presets directly on the editing timeline, keeping the entire video workflow in a single tool.</p>
        <span class="btn soon">Coming soon</span>
      </div>
    </div>

    <a class="card reveal" href="{UP}nft-admin/">
      <div class="card-media"><img src="{IMG}2025/10/Sarari-Dark-8889-scaled.png" alt="Blockchain admin platform dashboard" loading="lazy"></div>
      <div class="card-body">
        <span class="tag">SaaS • Admin • Blockchain</span>
        <h2>An admin marketplace platform from scratch</h2>
        <p>An admin SaaS platform that lets companies manage items, donor details, financial reports, and donation approvals, all controlled by an internal employee.</p>
        <span class="btn">View case study {ARROW}</span>
      </div>
    </a>

    <a class="card reveal" href="{UP}money-transfer-platform/">
      <div class="card-media"><img src="{IMG}2025/10/Open-1-2-scaled.png" alt="Money transfer platform dashboard" loading="lazy"></div>
      <div class="card-body">
        <span class="tag">SaaS • Mobile • Finance</span>
        <h2>How companies boost their profits</h2>
        <p>A platform for business users to manage their funds through transfers and currency conversions, monitor operations from a central dashboard, execute transfers, and export reports.</p>
        <span class="btn">View case study {ARROW}</span>
      </div>
    </a>

    <a class="card reveal" href="{UP}medical-students-app/">
      <div class="card-media plain"><img src="{IMG}2025/10/Sarari-12-scaled.png" alt="Medical students app screens" loading="lazy"></div>
      <div class="card-body">
        <span class="tag">Mobile • Medical • Academy</span>
        <h2>Medical student app for hospital setting</h2>
        <p>An intuitive app for medical interns with daily updates and exam and assignment tracking. A library of educational videos supports their professional development.</p>
        <span class="btn">View case study {ARROW}</span>
      </div>
    </a>
  </section>
</div>
<aside class="hello-pop" id="hello-pop" role="dialog" aria-labelledby="hello-title" aria-describedby="hello-text" hidden>
  <button class="hello-close" type="button" aria-label="Close">
    <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
  </button>
  <div class="hello-art" aria-hidden="true">
    <svg class="hello-hi" viewBox="-6 -2 100 80" width="104" height="83">
      <path class="hi-line" pathLength="1" d="M14 58C22 50 31 34 34 20C36 12 34 8 31 9C27 10 26 18 26 28L25 62C28 50 34 42 40 42C46 42 46 48 45 54C44 60 46 63 50 62C55 60 59 52 61 44C60 52 59 58 61 62C63 64 68 62 74 55"/>
      <circle class="hi-dot" cx="62.5" cy="33" r="1.9"/>
    </svg>
  </div>
  <h2 id="hello-title">Thanks for stopping by</h2>
  <p id="hello-text">My newest projects aren’t on the site yet. If my work caught your eye, let’s talk and I’ll walk you through&nbsp;them.</p>
  <a class="hello-cta" href="https://api.whatsapp.com/send?phone=972507307688" target="_blank" rel="noopener">Let’s connect</a>
</aside>
"""

NFT = """
<main class="wrap">
  <header class="cs-head">
    <h1><span class="lt">Heritage meets blockchain,</span> <b>an admin built from scratch</b></h1>
    <p class="lede">Israel’s largest heritage organization wanted to reach younger donors with <span class="nb">limited-edition</span> digital collectibles. I&nbsp;designed the admin platform that gives their team full control, from the first collection to the final donation.</p>
    <dl class="meta">
      <div><dt>Role</dt><dd>Product Designer</dd></div>
      <div><dt>Team</dt><dd>PM, designer, project &amp; dev teams</dd></div>
      <div><dt>Scope</dt><dd>Research, UX, wireframes, UI</dd></div>
      <div><dt>Platform</dt><dd>Desktop web (B2B)</dd></div>
    </dl>
  </header>

  <figure class="hero-shot own-frame"><img src="{UP}assets/media/nft-hero.webp" alt="Blockchain admin platform, dashboard overview" width="2400" height="1355"></figure>

  <section class="tldr">
    <article><p class="eyebrow">The challenge</p><p>Launch a blockchain donation experience with no existing reference, without losing the spirit of giving.</p></article>
    <article><p class="eyebrow">The company</p><p>Israel’s largest heritage organization, funded by donations and now reaching younger donors with digital collectibles.</p></article>
    <article><p class="eyebrow">The project</p><p>An admin system for item management, donor details, financial reports and donation approval, all run by an internal employee.</p></article>
  </section>

  <div class="story">
    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Exploring the problem</p>
      <p class="statement">We had to create a product from scratch, with <em>no references</em> for admin systems in the blockchain world, especially for donations.</p>
      <div class="duo"><img src="{IMG}2025/10/Frame-12436-scaled.webp" alt="Brainstorm board" loading="lazy"><img src="{IMG}2025/10/Frame-12435678-scaled.webp" alt="Research mapping" loading="lazy"></div>
    </section>

    <section class="chapter sub reveal">
      <p class="pill">Market research</p>
      <p class="support">We studied the admin systems of large online-marketplace platforms such as Shopify, Wix, Magento and BigCommerce to learn how they are built and which features work. Since we were starting from zero, this told us where to begin.</p>
      <div class="marquee" aria-label="Platforms we studied: Shopify, Wix, BigCommerce, Magento"><div class="marquee-track" aria-hidden="true"><span>Shopify</span><span>Wix</span><span>BigCommerce</span><span>Magento</span><span>Shopify</span><span>Wix</span><span>BigCommerce</span><span>Magento</span><span>Shopify</span><span>Wix</span><span>BigCommerce</span><span>Magento</span><span>Shopify</span><span>Wix</span><span>BigCommerce</span><span>Magento</span></div></div>
      <div class="cmp-grid"><div class="cmp-card"><table class="cmp"><thead><tr><th></th><th>Wix</th><th>BigCommerce</th><th>Shopify</th><th>Magento</th></tr></thead><tbody><tr><th scope="row">System &amp; settings</th><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr><tr><th scope="row">Low-stock notifications</th><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr><tr><th scope="row">Activity logs</th><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr><tr><th scope="row">Scheduled drops</th><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td></tr><tr><th scope="row">Editing items</th><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr></tbody></table></div><div class="cmp-card"><table class="cmp"><thead><tr><th></th><th>Wix</th><th>BigCommerce</th><th>Shopify</th><th>Magento</th></tr></thead><tbody><tr><th scope="row">Real-time data dashboard</th><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr><tr><th scope="row">Collection, category, item</th><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td></tr><tr><th scope="row">Real-time orders &amp; reports</th><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr><tr><th scope="row">User information</th><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr><tr><th scope="row">Marketing &amp; analytics</th><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td><td class="n" aria-label="No"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M7.2 7.2l5.6 5.6M12.8 7.2l-5.6 5.6"/></svg></td><td class="y" aria-label="Yes"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8.5"/><path d="M6.5 10.2l2.3 2.3 4.7-4.8"/></svg></td></tr></tbody></table></div></div>
    </section>

    <section class="chapter band reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Key insights</p>
      <p class="statement big">What the team needed most was to run it all <em>on their own.</em></p>
      <p class="support">The research pointed to one need above all: independence from developers. Full control over uploads and visibility, <span class="nb">real-time</span> reports, and drops timed to key dates, on a foundation <span class="nb">built to scale.</span></p>
    </section>

    <section class="chapter hide-mobile reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>User journey</p>
      <p class="statement">One flow in detail: building <em>collections and items</em> in a clear hierarchy, from draft to published.</p>
      <figure class="flow"><div class="flow-scroll">{FLOW_NFT}</div><span class="flow-hint" aria-hidden="true"><span class="hint-mouse">Move across to explore</span><span class="hint-touch">Swipe to explore</span> →</span></figure>
      <p class="note">This is one use case of the full system. Feel free to contact me to learn more.</p>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Visual design</p>
      <p class="statement">A calm, minimal admin for the team, <em>a vivid marketplace</em> for donors.</p>
      <div class="features">
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">01</span>Home dashboard</h3></div>
          <div class="feature-shots"><img src="{UP}assets/img/nft/home-dashboard-sm.webp" data-full="{UP}assets/img/nft/home-dashboard.webp" alt="Home dashboard" loading="lazy"></div>
        </article>
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">02</span>Add &amp; view collections</h3></div>
          <div class="feature-shots two"><img src="{UP}assets/img/nft/collections-sm.webp" data-full="{UP}assets/img/nft/collections.webp" alt="Collections table" loading="lazy"><img src="{UP}assets/img/nft/collection-details-sm.webp" data-full="{UP}assets/img/nft/collection-details.webp" alt="Collection details with associated items" loading="lazy"></div>
        </article>
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">03</span>Add &amp; view items</h3></div>
          <div class="feature-shots two"><img src="{UP}assets/img/nft/items-sm.webp" data-full="{UP}assets/img/nft/items.webp" alt="Items table" loading="lazy"><img src="{UP}assets/img/nft/new-item-sm.webp" data-full="{UP}assets/img/nft/new-item.webp" alt="Adding a new item" loading="lazy"></div>
        </article>
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">04</span>Donor lead · Associate Items</h3></div>
          <div class="feature-shots two"><img src="{UP}assets/img/nft/donors-sm.webp" data-full="{UP}assets/img/nft/donors.webp" alt="Donors table" loading="lazy"><img src="{UP}assets/img/nft/associate-items-sm.webp" data-full="{UP}assets/img/nft/associate-items.webp" alt="Associating items to a collection" loading="lazy"></div>
        </article>
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Impact</p>
      <p class="statement">Non-technical teams now create and manage NFTs <em>at scale</em>, on their own.</p>
      <ul class="results">
        <li><span class="big-num">27%</span><p class="eyebrow">Faster creation</p><h3>Time to complete the creation flow</h3><p>A step-by-step flow with live previews cut the average completion time (estimated).</p></li>
        <li><span class="big-num">30%</span><p class="eyebrow">More consistent</p><h3>Consistency through templates</h3><p>Predefined templates simplified creation and reduced errors (estimated).</p></li>
        <li><span class="big-num">~3</span><p class="eyebrow">Fewer errors per session</p><h3>Fewer data-entry mistakes</h3><p>Validations, field restrictions and in-context guidance reduced manual corrections.</p></li>
      </ul>
    </section>
  </div>

  <a class="next reveal" href="{UP}money-transfer-platform/">
    <span class="eyebrow">Next case study</span>
    <span class="title">Boosting companies’ profits</span>
    <span class="go">View case study {ARROW}</span>
  </a>
</main>
"""

MONEY = """
<main class="wrap">
  <header class="cs-head">
    <h1><span class="lt">Money transfers for business,</span> <b>without the friction</b></h1>
    <p class="lede">A B2B platform for one of Israel’s leading financial groups, where business clients transfer funds, convert currencies and track every operation from one dashboard.</p>
    <dl class="meta">
      <div><dt>Role</dt><dd>Product Designer</dd></div>
      <div><dt>Team</dt><dd>PM, 2 product designers, dev team</dd></div>
      <div><dt>Scope</dt><dd>Research, UX, UI, mobile</dd></div>
      <div><dt>Platform</dt><dd>Desktop web + mobile</dd></div>
    </dl>
  </header>

  <figure class="hero-shot"><img src="{UP}assets/media/money-hero.webp" alt="Money transfer platform dashboard" width="2400" height="1406"></figure>

  <section class="tldr">
    <article><p class="eyebrow">The challenge</p><p>Give business clients a transparent way to move large sums, competing with global giants on both fees and ease of use.</p></article>
    <article><p class="eyebrow">The company</p><p>One of Israel’s leading financial groups, active in insurance, investments, credit and distribution.</p></article>
    <article><p class="eyebrow">Impact</p><p>~25% more engagement, ~30% faster transactions, and 23% of new users paying in their first session.</p></article>
  </section>

  <div class="story">
    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Exploring the problem</p>
      <p class="statement">Building from scratch meant learning what business clients <em>expect from the best</em> in the market.</p>
    </section>

    <section class="chapter sub reveal">
      <p class="pill">Market research</p>
      <p class="support">We studied B2B transfer and currency platforms such as Currencycloud, OFX, Tipalti and Payoneer to see how they’re built and which features business clients expect.</p>
      {MARQUEE}
      <div class="cmp-grid">{T1}{T2}</div>
    </section>

    <section class="chapter band reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Key insights</p>
      <p class="statement big">Low fees aren’t enough. It has to be <em>easy to use.</em></p>
      <p class="support">Clients needed a real alternative to global fintechs: low fees with high usability, <span class="nb">real-time</span> monitoring, clear tracking of every transaction, and a smooth fit with their existing <span class="nb">financial systems.</span></p>
    </section>

    <section class="chapter hide-mobile reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>User journey</p>
      <p class="statement">Adding a beneficiary, with <em>back-office approval</em> before the first payment.</p>
      <figure class="flow"><div class="flow-scroll">{FLOW_BEN}</div><span class="flow-hint" aria-hidden="true"><span class="hint-mouse">Move across to explore</span><span class="hint-touch">Swipe to explore</span> →</span></figure>
    </section>

    <section class="chapter sub hide-mobile reveal">
      <p class="statement">Pending requests: <em>approve, edit or reject</em> payments in one place.</p>
      <figure class="flow"><div class="flow-scroll">{FLOW_PEND}</div><span class="flow-hint" aria-hidden="true"><span class="hint-mouse">Move across to explore</span><span class="hint-touch">Swipe to explore</span> →</span></figure>
      <p class="note">These are selected use cases of the full system. Feel free to contact me to learn more.</p>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Visual design</p>
      <p class="statement">The company’s brand, <em>tuned for a financial tool</em>.</p>
      <div class="features">
{FEATURES}
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Key outcomes</p>
      <p class="statement">Complex fund transfers became a <em>secure, self-service</em> platform.</p>
      <ul class="results">
        <li><span class="big-num">25%</span><p class="eyebrow">Estimated growth</p><h3>Higher engagement</h3><p>Business clients significantly increased their usage since launch.</p></li>
        <li><span class="big-num">30%</span><p class="eyebrow">Approximately</p><h3>Shorter transaction times</h3><p>Faster transfers, better efficiency and higher satisfaction.</p></li>
        <li><span class="big-num">23%</span><p class="eyebrow">Paid in first session</p><h3>Onboarding to paid</h3><p>Users who started sign-up chose a payment plan in their first session or soon after.</p></li>
      </ul>
    </section>
  </div>

  <a class="next reveal" href="{UP}medical-students-app/">
    <span class="eyebrow">Next case study</span>
    <span class="title">Medical students app</span>
    <span class="go">View case study {ARROW}</span>
  </a>
</main>
"""
_cols = ["Currencycloud", "OFX", "Tipalti", "Payoneer"]
MONEY = (MONEY
  .replace("{MARQUEE}", marquee(_cols))
  .replace("{T1}", cmp_table(_cols, [("International transfers", "yyyy"), ("Payment management", "yyyy"), ("Exchange rates", "yyyy"), ("ERP integration", "ynyn"), ("Payment method support", "yyyy")]))
  .replace("{T2}", cmp_table(_cols, [("Tax &amp; compliance", "nnyy"), ("Self-service portal", "nnyy"), ("Multi-currency support", "yyyy"), ("Invoice automation", "nnyn"), ("Cryptocurrency support", "nnnn")]))
  .replace("{FLOW_BEN}", beneficiary_flow()).replace("{FLOW_PEND}", pending_flow())
  .replace("{FEATURES}", "\n".join([
      feat(1, "Home dashboard", [("{IMG}2025/05/open-2-2-2-scaled.png", "{IMG}2025/05/open-2-2-2.png", "Home dashboard")]),
      feat(2, "Beneficiaries · add &amp; pay", [("{IMG}2025/06/big-1-1-scaled.png", "{IMG}2025/06/big-1-1.png", "Beneficiaries list"), ("{IMG}2025/06/big-2-1.png", "", "Paying a beneficiary")]),
      feat(3, "Pending requests", [("{IMG}2025/06/big-3-scaled.png", "{IMG}2025/06/big-3.png", "Pending requests"), ("{IMG}2025/06/big-4-scaled.png", "{IMG}2025/06/big-4.png", "Pending request details")]),
      feat(4, "Activity", [("{IMG}2025/06/big-5-scaled.png", "{IMG}2025/06/big-5.png", "Activity"), ("{IMG}2025/06/big-6-scaled.png", "{IMG}2025/06/big-6.png", "Activity filters")]),
      feat(5, "Mobile app", [("{IMG}2025/06/screen-m2.png", "", "Mobile screen"), ("{IMG}2025/06/screen-m4.png", "", "Mobile screen"), ("{IMG}2025/06/screen-m8.png", "", "Mobile screen"), ("{IMG}2025/06/screen-m6.png", "", "Mobile screen"), ("{IMG}2025/06/screen-m44.png", "", "Mobile screen")], phones=True, trim_mobile=True),
  ])))


MEDICAL = """
<main class="wrap">
  <header class="cs-head">
    <h1><span class="lt">Learning that fits</span> <b>between hospital shifts</b></h1>
    <p class="lede">A mobile-first app for Sheba Medical Center’s interns: daily updates, exams and assignments, and a library of educational videos, all in one place.</p>
    <dl class="meta">
      <div><dt>Role</dt><dd>Product Designer</dd></div>
      <div><dt>Client</dt><dd>Sheba Medical Center</dd></div>
      <div><dt>Scope</dt><dd>Research, UX, UI</dd></div>
      <div><dt>Platform</dt><dd>Mobile app (B2C)</dd></div>
    </dl>
  </header>

  <figure class="hero-shot phones-hero"><img src="{IMG}2025/10/Sarari-12-scaled.png" alt="Medical students app, three key screens" width="2560" height="1746"></figure>

  <section class="tldr">
    <article><p class="eyebrow">The challenge</p><p>Give interns the learning content they need, fast, on a phone, in the few minutes they have between shifts.</p></article>
    <article><p class="eyebrow">The client</p><p>Sheba’s department for interns, which pairs academic learning with practical training in the hospital.</p></article>
    <article><p class="eyebrow">Impact</p><p>21% more mobile sessions, rollouts cut from two weeks to 6 days, and 42% faster content discovery.</p></article>
  </section>

  <div class="story">
    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Exploring the problem</p>
      <p class="statement">Interns need the <em>right content</em>, on their phone, in the few minutes they have.</p>
      <div class="duo">
        <img src="{IMG}2025/10/Frame-1243666-scaled.webp" alt="Research board: questions, UX and edge cases" loading="lazy">
        <div class="mini-phones"><img src="{IMG}2025/05/IMG_8739.png" alt="Reference app screen" loading="lazy"><img src="{IMG}2025/05/IMG_8737.png" alt="Reference app screen" loading="lazy"><img src="{IMG}2025/05/IMG_8742.png" alt="Reference app screen" loading="lazy"><img src="{IMG}2025/05/IMG_8738.png" alt="Reference app screen" loading="lazy"></div>
      </div>
    </section>

    <section class="chapter sub reveal">
      <p class="pill">Market research</p>
      <p class="support">I studied leading learning platforms such as Coursera, Udemy, Domestika and Skillshare to see how the market leaders solve the challenges we faced.</p>
      {MARQUEE}
      <div class="cmp-grid">{T1}{T2}</div>
    </section>

    <section class="chapter band reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Key insights</p>
      <p class="statement big">Every action had to fit <em>in a few taps.</em></p>
      <ul class="trio" style="--cols:4">
        <li><h3>Updates come first</h3><p>Real-time notifications from lecturers sit at the top of the home page, so nothing is missed between shifts.</p></li>
        <li><h3>Find it fast</h3><p>Quick filters by class or lecturer, plus a search with autocomplete, cut the time to the right lesson.</p></li>
        <li><h3>One lesson, one place</h3><p>Media, reference files and assessments live together on each lesson page, with favorites for quick return.</p></li>
        <li><h3>Synced with lecturers</h3><p>Assignments and results are saved straight to the lecturers’ admin platform, with no extra steps.</p></li>
      </ul>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Visual design</p>
      <p class="statement">A calm, focused app that <em>surfaces what’s next</em> for every intern.</p>
      <div class="features">
{FEATURES}
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n" aria-hidden="true"></span>Key outcomes</p>
      <p class="statement">Better mobile access, easier navigation, <em>less admin work</em>.</p>
      <ul class="results">
        <li><span class="big-num">21%</span><p class="eyebrow">More mobile sessions</p><h3>Mobile sessions surge</h3><p>Students access study materials even during hospital shifts.</p></li>
        <li><span class="big-num">6d</span><p class="eyebrow">Down from two weeks</p><h3>Faster feature rollouts</h3><p>Fast feedback workshops with developers shortened critical rollouts.</p></li>
        <li><span class="big-num">42%</span><p class="eyebrow">Faster</p><h3>Content discovery</h3><p>Task-focused navigation cut the average time to find relevant content.</p></li>
      </ul>
    </section>
  </div>

  <a class="next reveal" href="{UP}nft-admin/">
    <span class="eyebrow">Next case study</span>
    <span class="title">Blockchain admin platform</span>
    <span class="go">View case study {ARROW}</span>
  </a>
</main>
"""
_mcols = ["Coursera", "Udemy", "Domestika", "Skillshare"]
MEDICAL = (MEDICAL
  .replace("{MARQUEE}", marquee(_mcols))
  .replace("{T1}", cmp_table(_mcols, [("Activity dashboard", "yyny"), ("Filters by topic / lecturer", "yyyn"), ("Lesson media player", "yyyy"), ("Reference materials", "yyyn"), ("Assessments &amp; quizzes", "yynn")]))
  .replace("{T2}", cmp_table(_mcols, [("Real-time notifications", "yynn"), ("Admin sync", "yynn"), ("Favorites &amp; personalization", "yyyy"), ("Offline access", "yynn"), ("Collaboration &amp; peer learning", "yyyy")]))
  .replace("{FEATURES}", "\n".join([
      feat(1, "Home page", [("{IMG}2025/06/2.png", "", "Home page"), ("{IMG}2025/06/Homepage-All1.png", "", "Home page, all activities"), ("{IMG}2025/06/Homepage-All1-1.png", "", "Home page, filtered"), ("{IMG}2025/05/Homepage-All1-1.png", "", "Home page, details")], phones=True),
      feat(2, "Lesson page", [("{IMG}2025/06/1.png", "", "Lesson page"), ("{IMG}2025/06/dd.png", "", "Lesson video"), ("{IMG}2025/05/Lesson-page-Media-details.png", "", "Lesson media details"), ("{IMG}2025/06/Lesson-page-Reference.png", "", "Reference files"), ("{IMG}2025/06/Lesson-page-Exam-details-chose-answer.png", "", "Lesson assessment")], phones=True),
  ])))


NFT = NFT.replace("{FLOW_NFT}", nft_flow())

PAGES = {
    "index.html": ("Adi Elbom · Product Designer", "Product designer at WSC-Sports, turning complex workflows into intuitive, user-centered experiences.", 0, "work", HOME),
    "nft-admin/index.html": ("Blockchain Admin Platform · Adi Elbom", "Case study: a B2B admin platform for a blockchain donation marketplace, designed from scratch.", 1, "nft-admin", NFT),
    "money-transfer-platform/index.html": ("Money Transfer Platform · Adi Elbom", "Case study: a B2B money transfer and currency conversion platform for business clients.", 1, "money-transfer-platform", MONEY),
    "medical-students-app/index.html": ("Medical Students App · Adi Elbom", "Case study: a mobile-first learning app for medical interns at Sheba Medical Center.", 1, "medical-students-app", MEDICAL),
}
