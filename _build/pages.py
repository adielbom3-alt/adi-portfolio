from flows import nft_flow

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
      <div class="card-media"><img src="{IMG}2025/10/Sarari-Dark-8889-scaled.png" alt="NFT admin platform dashboard" loading="lazy"></div>
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

  <figure class="hero-shot own-frame"><img src="{UP}assets/media/nft-hero.webp" alt="NFT admin platform, dashboard overview" width="2400" height="1355"></figure>

  <section class="tldr">
    <article><p class="eyebrow">The challenge</p><p>Launch a blockchain donation experience with no existing reference, without losing the spirit of giving.</p></article>
    <article><p class="eyebrow">The company</p><p>Israel’s largest heritage organization, funded by donations and now reaching younger donors with digital collectibles.</p></article>
    <article><p class="eyebrow">The project</p><p>An admin system for item management, donor details, financial reports and donation approval, all run by an internal employee.</p></article>
  </section>

  <div class="story">
    <section class="chapter reveal">
      <p class="pill"><span class="n">01</span>Exploring the problem</p>
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
      <p class="pill"><span class="n">02</span>Key insights</p>
      <p class="statement big">What the team needed most was to run it all <em>on their own.</em></p>
      <p class="support">The research pointed to one need above all: independence from developers. Full control over uploads and visibility, <span class="nb">real-time</span> reports, and drops timed to key dates, on a foundation <span class="nb">built to scale.</span></p>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">03</span>User journey</p>
      <p class="statement">One flow in detail: building <em>collections and items</em> in a clear hierarchy, from draft to published.</p>
      <figure class="flow"><div class="flow-scroll">{FLOW_NFT}</div><span class="flow-hint" aria-hidden="true"><span class="hint-mouse">Move across to explore</span><span class="hint-touch">Swipe to explore</span> →</span></figure>
      <p class="note">This is one use case of the full system. Feel free to contact me to learn more.</p>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">04</span>Visual design</p>
      <p class="statement">A calm, minimal admin for the team, <em>a vivid marketplace</em> for donors.</p>
      <div class="features">
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">01</span>Home dashboard</h3></div>
          <div class="feature-shots"><img src="{IMG}2024/12/Sarari-Dark-4.png" alt="Home dashboard" loading="lazy"></div>
        </article>
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">02</span>Add &amp; view collections</h3></div>
          <div class="feature-shots two"><img src="{IMG}2025/10/dddssss-scaled.png" data-full="{IMG}2025/10/dddssss.png" alt="Collections table" loading="lazy"><img src="{IMG}2025/10/aaa-scaled.png" data-full="{IMG}2025/10/aaa.png" alt="Collection detail" loading="lazy"></div>
        </article>
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">03</span>Add &amp; view items</h3></div>
          <div class="feature-shots two"><img src="{IMG}2025/10/big-screen1-scaled.png" data-full="{IMG}2025/10/big-screen1.png" alt="Items table" loading="lazy"><img src="{IMG}2025/04/flow-nft.png" alt="Item creation flow" loading="lazy"></div>
        </article>
        <article class="feature">
          <div class="feature-text"><h3><span class="fn">04</span>Donor lead · item purchase</h3></div>
          <div class="feature-shots two"><img src="{IMG}2025/10/sssss-scaled.png" data-full="{IMG}2025/10/sssss.png" alt="Donor purchase completion" loading="lazy"><img src="{IMG}2024/12/sc5-2.png" alt="Purchase completion detail" loading="lazy"></div>
        </article>
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">05</span>Impact</p>
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
    <p class="lede">A B2B platform where business users manage funds through transfers and currency conversions, track operations from one dashboard, and export reports.</p>
    <dl class="meta">
      <div><dt>Role</dt><dd>Product Designer</dd></div>
      <div><dt>Team</dt><dd>PM, 2 product designers, dev team</dd></div>
      <div><dt>Scope</dt><dd>Research, UX, UI, mobile</dd></div>
      <div><dt>Platform</dt><dd>Desktop web + mobile</dd></div>
    </dl>
  </header>

  <figure class="hero-shot"><img src="{IMG}2025/10/Open-1-2-scaled.png" alt="Money transfer platform dashboard"></figure>

  <section class="tldr">
    <article><p class="eyebrow">The challenge</p><p>How do you give business clients a seamless, transparent way to transfer large sums, competing with global giants while keeping fees low and frustration out?</p></article>
    <article><p class="eyebrow">The company</p><p>One of Israel’s leading financial groups, active in insurance, asset and investment management, credit and distribution.</p></article>
    <article><p class="eyebrow">Impact</p><p>~25% growth in engagement, ~30% shorter transaction times, and 23% of new users paying in their first session.</p></article>
  </section>

  <div class="story">
    <section class="chapter reveal">
      <p class="pill"><span class="n">01</span>Exploring the problem</p>
      <p class="statement">A great experience for <em>specific customer needs</em>, under real delivery pressure.</p>
      <p class="support">The research was done by another product designer and me, with daily feedback from our product manager, alongside an ongoing development process that demanded a lot of the team’s time.</p>
      <div class="logos">
        <img src="{IMG}2025/04/pngwing.com-2-scaled.png" alt="" loading="lazy">
        <img src="{IMG}2025/05/Group-scaled.png" alt="" loading="lazy">
        <img src="{IMG}2024/12/Group-1.svg" alt="" loading="lazy">
        <img src="{IMG}2025/04/Tipalti_logo-1.png" alt="Tipalti" loading="lazy">
        <img src="{IMG}2025/05/Oradian-Brand-Mark@2x-1-scaled.png" alt="Oradian" loading="lazy">
      </div>
    </section>

    <section class="chapter sub reveal">
      <p class="pill">Market research</p>
      <p class="support">We examined B2B money-transfer and currency-exchange platforms such as Currencycloud, OFX and Payoneer to understand how their systems are built and what makes them effective. Building from scratch, we needed to know which features our customers would expect.</p>
      <div class="duo framed"><div><img src="{IMG}2025/10/pro-1.png" alt="Competitor analysis" loading="lazy"></div><div><img src="{IMG}2025/10/pro-2.png" alt="Competitor feature comparison" loading="lazy"></div></div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">02</span>Key insights</p>
      <p class="statement big">Low fees are not enough. It has to be <em>easy to use</em>.</p>
      <ul class="trio" style="--cols:4">
        <li><h3>Robust admin</h3><p>Support operational efficiency and real-time transaction monitoring.</p></li>
        <li><h3>Beat the giants</h3><p>Combine low fees with high usability as a real alternative to global fintechs.</p></li>
        <li><h3>Track everything</h3><p>Manage and follow past and pending transactions efficiently.</p></li>
        <li><h3>Fit the ecosystem</h3><p>Integrate with existing financial systems and compliance requirements.</p></li>
      </ul>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">03</span>User journey</p>
      <p class="statement">Adding a beneficiary, with <em>validation at every step</em>.</p>
      <p class="support">Each step of adding a new beneficiary for future transfers is validated and approved by the back office, to make sure the beneficiary is legitimate.</p>
      <figure class="shot framed"><img src="{IMG}2025/04/ftt-scaled.png" alt="Add beneficiary flow" loading="lazy"></figure>
    </section>

    <section class="chapter sub reveal">
      <p class="pill">Open pending requests</p>
      <p class="support">Pending requests let the user decide what happens next: requests awaiting authorization can be handed to an admin for final processing, while requests that need no action are view-only.</p>
      <figure class="shot framed"><img src="{IMG}2025/03/11-1.png" alt="Pending requests flow" loading="lazy"></figure>
      <p class="note">These are selected use cases of the full system. Feel free to contact me to learn more.</p>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">04</span>Wireframing</p>
      <p class="statement">Hand sketches first, then <em>high-fidelity</em> wireframes.</p>
      <div class="screens">
        <figure><img src="{IMG}2024/09/11-1.png" alt="Dashboard wireframe" loading="lazy"><figcaption><b>Home dashboard</b>Recent and pending actions, the user’s financial data graph, and live currency exchange rates.</figcaption></figure>
        <figure><img src="{IMG}2024/09/66.png" alt="Dashboard wireframe variation" loading="lazy"><figcaption><b>Home dashboard · details</b>Exploring how balance and actions sit together.</figcaption></figure>
        <figure><img src="{IMG}2024/12/2.6-Beneficiaries-profile.png" alt="Beneficiary transfers wireframe" loading="lazy"><figcaption><b>Beneficiary transfers</b>Monthly transfer history summary and a connection-note feature.</figcaption></figure>
        <figure><img src="{IMG}2024/09/33.png" alt="Reports wireframe" loading="lazy"><figcaption><b>Reports</b>User-specific filters, customizable views, downloading and sharing.</figcaption></figure>
        <figure><img src="{IMG}2024/10/Sarari-Dark.png" alt="Report view wireframe" loading="lazy"><figcaption><b>Reports · view</b>List and preview modes; pick and check reports before opening them.</figcaption></figure>
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">05</span>Visual design</p>
      <p class="statement">The company’s brand, <em>tuned for a financial tool</em>.</p>
      <p class="support">A minimalistic approach using the company’s UI brand in various shades plus one accent color. We built on the existing colors and fonts, with targeted adjustments for the system’s needs, strengthening the brand’s presence.</p>
      <figure class="shot"><img src="{IMG}2025/04/%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%9E%D7%A1%D7%9A-2025-04-02-%D7%91-18.16.01.png" alt="Design system" loading="lazy"></figure>
    </section>

    <section class="chapter reveal">
      <p class="pill">The final screens · Desktop</p>
      <figure class="scene">
        <img src="{IMG}2025/05/open-2-2-2-scaled.png" alt="Home dashboard" loading="lazy">
        <figcaption class="scene-band"><h3>Home dashboard</h3><p>The system works on the user’s balance, so actions depend on available funds. The dashboard shows the live balance and its value against other currencies; hovering reveals recent actions and the option to add funds.</p></figcaption>
      </figure>
      <figure class="scene">
        <img src="{IMG}2025/06/big-1-1-scaled.png" alt="Beneficiaries" loading="lazy">
        <figcaption class="scene-band"><h3>Beneficiaries · add &amp; pay</h3><p>Beneficiaries handle transactions like payments and conversions. They are created and approved through the admin system first, then they are ready to go.</p></figcaption>
        <div class="extra"><img src="{IMG}2025/06/big-2-1.png" alt="Beneficiary payment" loading="lazy"></div>
      </figure>
      <figure class="scene">
        <img src="{IMG}2025/06/big-3-scaled.png" alt="Pending requests" loading="lazy">
        <figcaption class="scene-band"><h3>Pending requests</h3><p>All open requests and those that hit an issue with the admin-side controller. Requests waiting on the user are separated from those still open, so the next step is always clear.</p></figcaption>
        <div class="extra"><img src="{IMG}2025/06/big-4-scaled.png" alt="Pending request detail" loading="lazy"></div>
      </figure>
      <figure class="scene">
        <img src="{IMG}2025/06/big-5-scaled.png" alt="Activity" loading="lazy">
        <figcaption class="scene-band"><h3>Activity</h3><p>Every operation, past and present, in one place, with filters to focus on exactly what the user wants to check and track.</p></figcaption>
        <div class="extra"><img src="{IMG}2025/06/big-6-scaled.png" alt="Activity filters" loading="lazy"></div>
      </figure>
    </section>

    <section class="chapter reveal">
      <p class="pill">The final screens · Mobile</p>
      <p class="statement">Translating dense tables and <em>complex flows</em> to a phone.</p>
      <p class="support">The mobile app carries over the comprehensive tables and the money-transfer process, the hardest parts of the system to fit on a small screen.</p>
      <div class="phones" style="--n:5">
        <img src="{IMG}2025/06/screen-m2.png" alt="Mobile screen" loading="lazy">
        <img src="{IMG}2025/06/screen-m4.png" alt="Mobile screen" loading="lazy">
        <img src="{IMG}2025/06/screen-m8.png" alt="Mobile screen" loading="lazy">
        <img src="{IMG}2025/06/screen-m6.png" alt="Mobile screen" loading="lazy">
        <img src="{IMG}2025/06/screen-m44.png" alt="Mobile screen" loading="lazy">
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">06</span>Key outcomes</p>
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

MEDICAL = """
<main class="wrap">
  <header class="cs-head">
    <h1><span class="lt">Learning that fits</span> <b>between hospital shifts</b></h1>
    <p class="lede">A mobile-first app for Sheba Medical Center’s interns: daily updates, exams and assignments, and a library of educational videos in one place.</p>
    <dl class="meta">
      <div><dt>Role</dt><dd>Product Designer</dd></div>
      <div><dt>Client</dt><dd>Sheba Medical Center</dd></div>
      <div><dt>Scope</dt><dd>Research, UX, wireframes, UI</dd></div>
      <div><dt>Platform</dt><dd>Mobile app (B2C)</dd></div>
    </dl>
  </header>

  <figure class="hero-shot bg" style="background-image:url('{IMG}2025/10/Rectangle-312.webp')"><img src="{IMG}2025/10/Sarari-12-scaled.png" alt="Medical students app, three key screens"></figure>

  <section class="tldr">
    <article><p class="eyebrow">The challenge</p><p>Design an intuitive app for people who need important learning content fast. A mobile-first approach makes it even harder.</p></article>
    <article><p class="eyebrow">The client</p><p>Sheba’s department for interns builds a framework that pairs academic learning with practical training.</p></article>
    <article><p class="eyebrow">Impact</p><p>21% more mobile sessions, rollouts cut from two weeks to 6 days, and 42% faster content discovery.</p></article>
  </section>

  <div class="story">
    <section class="chapter reveal">
      <p class="pill"><span class="n">01</span>Exploring the problem</p>
      <p class="statement">Interns need the <em>right content</em>, on their phone, in the few minutes they have.</p>
      <p class="support">We started from a product brief describing the users and potential use cases, and researched similar apps to analyze their structure and audiences.</p>
      <figure class="shot"><img src="{IMG}2025/10/Frame-1243666-scaled.webp" alt="Research board" loading="lazy"></figure>
      <div class="phones" style="--n:4">
        <img src="{IMG}2025/05/IMG_8739.png" alt="Reference app screen" loading="lazy">
        <img src="{IMG}2025/05/IMG_8737.png" alt="Reference app screen" loading="lazy">
        <img src="{IMG}2025/05/IMG_8742.png" alt="Reference app screen" loading="lazy">
        <img src="{IMG}2025/05/IMG_8738.png" alt="Reference app screen" loading="lazy">
      </div>
    </section>

    <section class="chapter sub reveal">
      <p class="pill">Market research</p>
      <p class="support">I researched leading learning platforms such as Coursera, Udemy and Domestika, and brought a range of their proven features into our app, to see how the market leaders solve the challenges we faced.</p>
      <div class="duo framed"><div><img src="{IMG}2025/10/Frame-%D7%A9%D7%93%D7%A9.png" alt="Competitor analysis" loading="lazy"></div><div><img src="{IMG}2025/10/Frame-%D7%A9%D7%93.png" alt="Competitor feature comparison" loading="lazy"></div></div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">02</span>Wireframing</p>
      <p class="statement">Home, lessons, assignments: the <em>key use cases</em> in high fidelity.</p>
      <p class="support">After exploring directions in hand sketches, I detailed the main flows as high-fidelity wireframes.</p>
      <div class="screens phones-row" style="--n:3">
        <figure><img src="{IMG}2025/02/Homepage-All-5.png" alt="Home page wireframe" loading="lazy"><figcaption><b>Home page</b>The most important actions up front, like real-time notifications.</figcaption></figure>
        <figure><img src="{IMG}2025/02/Homepage-Filter-category-2.png" alt="Filters wireframe" loading="lazy"><figcaption><b>My activities · filters</b>Quick searches for activities.</figcaption></figure>
        <figure><img src="{IMG}2025/02/Homepage-Apply-filter-homepage-wire.png" alt="Filtered results wireframe" loading="lazy"><figcaption><b>After filtering</b>Selected actions and switching between features.</figcaption></figure>
        <figure><img src="{IMG}2025/02/Lesson-page-Media.png" alt="Lesson page wireframe" loading="lazy"><figcaption><b>Lesson page</b>Lessons, related files, and tasks to complete.</figcaption></figure>
        <figure><img src="{IMG}2025/02/Lesson-page-Media-details.png" alt="Lesson media wireframe" loading="lazy"><figcaption><b>Lesson media</b>Video and lesson details.</figcaption></figure>
        <figure><img src="{IMG}2025/02/Lesson-page-Media-2.png" alt="Reference files wireframe" loading="lazy"><figcaption><b>Reference files</b>Save favorite files.</figcaption></figure>
        <figure><img src="{IMG}2025/02/Lesson-page-Exam-details-chose-answer.png" alt="Lesson assessment wireframe" loading="lazy"><figcaption><b>Lesson assessment</b>A lesson-specific assignment, saved to the lecturers’ admin platform.</figcaption></figure>
        <figure><img src="{IMG}2025/02/Lesson-page-Exam-result-details.png" alt="Assessment results wireframe" loading="lazy"><figcaption><b>Assessment results</b>Results and answer details.</figcaption></figure>
        <figure><img src="{IMG}2024/12/Notifications.png" alt="Notifications wireframe" loading="lazy"><figcaption><b>Notifications</b>Real-time updates and additional resources.</figcaption></figure>
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">03</span>The final screens</p>
      <p class="statement">Home page</p>
      <p class="support">The student’s home page shows the latest and most important notifications, plus processes and actions for their enrolled classes. A filter at the top narrows everything by class or lecturer.</p>
      <div class="phones" style="--n:4">
        <img src="{IMG}2025/06/2.png" alt="Home page" loading="lazy">
        <img src="{IMG}2025/06/Homepage-All1.png" alt="Home page, all activities" loading="lazy">
        <img src="{IMG}2025/06/Homepage-All1-1.png" alt="Home page, filtered" loading="lazy">
        <img src="{IMG}2025/05/Homepage-All1-1.png" alt="Home page, detail" loading="lazy">
      </div>
    </section>

    <section class="chapter sub reveal">
      <p class="statement">Lesson page</p>
      <p class="support">Each lesson is organized into information, videos and uploaded files, plus a section for tests and online assignments that are part of the physical course.</p>
      <div class="phones" style="--n:5">
        <img src="{IMG}2025/06/1.png" alt="Lesson page" loading="lazy">
        <img src="{IMG}2025/06/dd.png" alt="Lesson video" loading="lazy">
        <img src="{IMG}2025/05/Lesson-page-Media-details.png" alt="Lesson media details" loading="lazy">
        <img src="{IMG}2025/06/Lesson-page-Reference.png" alt="Lesson reference files" loading="lazy">
        <img src="{IMG}2025/06/Lesson-page-Exam-details-chose-answer.png" alt="Lesson assessment" loading="lazy">
      </div>
    </section>

    <section class="chapter reveal">
      <p class="pill"><span class="n">04</span>Key outcomes</p>
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
    <span class="title">NFT admin platform</span>
    <span class="go">View case study {ARROW}</span>
  </a>
</main>
"""

NFT = NFT.replace("{FLOW_NFT}", nft_flow())

PAGES = {
    "index.html": ("Adi Elbom · Product Designer", "Product designer at WSC-Sports, turning complex workflows into intuitive, user-centered experiences.", 0, "work", HOME),
    "nft-admin/index.html": ("NFT Admin Platform · Adi Elbom", "Case study: a B2B admin platform for an NFT donation marketplace, designed from scratch.", 1, "nft-admin", NFT),
    "money-transfer-platform/index.html": ("Money Transfer Platform · Adi Elbom", "Case study: a B2B money transfer and currency conversion platform for business clients.", 1, "money-transfer-platform", MONEY),
    "medical-students-app/index.html": ("Medical Students App · Adi Elbom", "Case study: a mobile-first learning app for medical interns at Sheba Medical Center.", 1, "medical-students-app", MEDICAL),
}
