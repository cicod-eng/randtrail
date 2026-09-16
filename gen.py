#!/usr/bin/env python3
"""Generate RandTrail static pages (hubs, exchange landings, legal pages).

Run:  python3 gen.py
Keeps the header/footer consistent across every page. depth = 0 (root),
1 (hub), 2 (exchange landing) controls the relative path prefix.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

FAVICON = ("<link rel=\"icon\" href='data:image/svg+xml,<svg xmlns=\"http://www.w3.org/2000/svg\" "
           "viewBox=\"0 0 100 100\"><circle cx=\"50\" cy=\"50\" r=\"48\" fill=\"%23007A4D\"/>"
           "<text x=\"50\" y=\"68\" font-size=\"54\" font-weight=\"bold\" text-anchor=\"middle\" "
           "fill=\"%23C9A227\" font-family=\"Arial\">R</text></svg>'>")

FONTS = ('  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')

LOGO = ('<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true">'
        '<circle cx="16" cy="16" r="15" fill="#007A4D"/>'
        '<path d="M8 20 L13 15 L17 17 L24 10" fill="none" stroke="#C9A227" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M20.5 10 L24 10 L24 13.5" fill="none" stroke="#C9A227" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

LOGO_FOOT = ('<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true">'
             '<circle cx="16" cy="16" r="15" fill="#C9A227"/>'
             '<path d="M8 20 L13 15 L17 17 L24 10" fill="none" stroke="#00533A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
             '<path d="M20.5 10 L24 10 L24 13.5" fill="none" stroke="#00533A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

NAV = [
    ("Start Here", "start-here/", [
        ("Crypto Basics", "start-here/crypto-basics/"),
        ("Bitcoin", "start-here/bitcoin/"),
        ("Stablecoins", "start-here/stablecoins/"),
        ("Beginner Guides", "start-here/beginner-guides/"),
    ]),
    ("Exchanges", "exchanges/", [
        ("Binance", "exchanges/binance/"),
        ("OKX", "exchanges/okx/"),
        ("Binance vs OKX", "exchanges/binance-vs-okx/"),
    ]),
    ("Buy & Sell", "buy-sell/", [
        ("Buy Crypto", "buy-sell/buy-crypto/"),
        ("Sell Crypto", "buy-sell/sell-crypto/"),
        ("ZAR Deposits", "buy-sell/zar-deposits/"),
        ("Cash Out", "buy-sell/withdrawals/"),
        ("P2P", "buy-sell/p2p/"),
    ]),
    ("Wallets & Safety", "wallets-safety/", [
        ("Crypto Wallets", "wallets-safety/crypto-wallets/"),
        ("Account Security", "wallets-safety/account-security/"),
        ("Transfers & Networks", "wallets-safety/transfers-networks/"),
        ("Scam Prevention", "wallets-safety/scam-prevention/"),
    ]),
    ("Tax & Regulation", "tax-regulation/", [
        ("Crypto Tax", "tax-regulation/crypto-tax/"),
        ("SARS", "tax-regulation/sars/"),
        ("FSCA & CASP", "tax-regulation/fsca-casp/"),
        ("FICA", "tax-regulation/fica/"),
        ("Legal & Compliance", "tax-regulation/legal-compliance/"),
    ]),
]

FOOT_LINKS = [
    ("Start Here", [("Crypto Basics", "start-here/crypto-basics/"),
                    ("Bitcoin", "start-here/bitcoin/"),
                    ("Stablecoins", "start-here/stablecoins/"),
                    ("Beginner Guides", "start-here/beginner-guides/")]),
    ("Exchanges", [("Binance", "exchanges/binance/"),
                   ("OKX", "exchanges/okx/"),
                   ("Binance vs OKX", "exchanges/binance-vs-okx/")]),
    ("Buy & Sell", [("Buy Crypto", "buy-sell/buy-crypto/"),
                    ("Sell Crypto", "buy-sell/sell-crypto/"),
                    ("ZAR Deposits", "buy-sell/zar-deposits/"),
                    ("Cash Out", "buy-sell/withdrawals/"),
                    ("P2P", "buy-sell/p2p/")]),
    ("Wallets & Safety", [("Crypto Wallets", "wallets-safety/crypto-wallets/"),
                          ("Account Security", "wallets-safety/account-security/"),
                          ("Transfers & Networks", "wallets-safety/transfers-networks/"),
                          ("Scam Prevention", "wallets-safety/scam-prevention/")]),
    ("Tax & Regulation", [("Crypto Tax", "tax-regulation/crypto-tax/"),
                          ("SARS", "tax-regulation/sars/"),
                          ("FSCA & CASP", "tax-regulation/fsca-casp/"),
                          ("FICA", "tax-regulation/fica/")]),
]


def nav_html(p, active_label):
    out = []
    for label, href, items in NAV:
        act = ' class="active"' if label == active_label else ''
        out.append(f'<li class="has-dropdown"><a href="{p}{href}"{act}>{label}</a><ul class="dropdown-menu">')
        for ilabel, ihref in items:
            out.append(f'<li><a href="{p}{ihref}">{ilabel}</a></li>')
        out.append('</ul></li>')
    return ''.join(out)


def foot_cols(p):
    out = []
    for title, items in FOOT_LINKS:
        out.append(f'<div class="footer-col"><h4>{title}</h4><ul>')
        for ilabel, ihref in items:
            out.append(f'<li><a href="{p}{ihref}">{ilabel}</a></li>')
        out.append('</ul></div>')
    return ''.join(out)


def header(p, active_label, title, desc, canonical):
    return f'''<!DOCTYPE html>
<html lang="en-ZA">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  {FAVICON}
{FONTS}
  <link rel="stylesheet" href="{p}css/style.css">
  <link rel="canonical" href="{canonical}">
  <meta property="og:site_name" content="RandTrail">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://randtrail.com/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://randtrail.com/assets/og-image.png">
</head>
<body>

  <header class="site-header">
    <div class="container nav">
      <a href="{p}index.html" class="logo" aria-label="RandTrail home">
        {LOGO}
        <span><span class="rand">Rand</span><span class="trail">Trail</span></span>
      </a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links">
{nav_html(p, active_label)}
      </ul>
    </div>
  </header>
'''


def footer(p):
    return f'''
  <footer class="site-footer">
    <svg class="ndebele-strip" viewBox="0 0 1440 26" preserveAspectRatio="none" aria-hidden="true">
      <defs>
        <pattern id="ndebele" width="40" height="26" patternUnits="userSpaceOnUse">
          <rect width="40" height="26" fill="#003E2B"/>
          <path d="M0 26 L10 8 L20 26 Z" fill="#C9A227"/>
          <path d="M20 26 L30 4 L40 26 Z" fill="#0E9D6E"/>
        </pattern>
      </defs>
      <rect width="1440" height="26" fill="url(#ndebele)"/>
    </svg>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col footer-brand">
          <a href="{p}index.html" class="logo">
            {LOGO_FOOT}
            <span><span class="rand" style="color:#fff">Rand</span><span class="trail">Trail</span></span>
          </a>
          <p>Practical guides to buying, selling, storing and using crypto, written for South Africa.</p>
          <p class="contact"><a href="mailto:hello@randtrail.com">hello@randtrail.com</a></p>
        </div>
{foot_cols(p)}
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="{p}about.html">About</a></li>
            <li><a href="{p}editorial-policy.html">Editorial Policy</a></li>
            <li><a href="{p}affiliate-disclosure.html">Affiliate Disclosure</a></li>
            <li><a href="{p}risk-disclosure.html">Risk Disclosure</a></li>
            <li><a href="{p}contact.html">Contact</a></li>
            <li><a href="{p}privacy.html">Privacy Policy</a></li>
            <li><a href="{p}disclaimer.html">Disclaimer</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="risk">Cryptocurrency is highly volatile and involves significant market, custody and counterparty risk. You may lose some or all of the money you invest. In South Africa, crypto assets fall within the financial-services regulatory framework, and certain crypto asset service providers are subject to FSCA licensing requirements. Income or gains from crypto may be subject to tax under SARS rules. RandTrail provides educational information only and does not provide financial, investment, legal or tax advice.</p>
        <div class="legal">
          <span>&copy; 2026 RandTrail. Not financial advice.</span>
          <span>
            <a href="{p}disclaimer.html">Disclaimer</a>
            <a href="{p}privacy.html">Privacy</a>
            <a href="{p}editorial-policy.html">Editorial Policy</a>
          </span>
        </div>
      </div>
    </div>
  </footer>

  <script src="{p}js/main.js"></script>
</body>
</html>
'''


def write_page(relpath, active_label, title, desc, canonical, main_html, extra_head=""):
    depth = relpath.count("/")
    p = "../" * depth if depth else ""
    full = header(p, active_label, title, desc, canonical) + main_html + footer(p)
    path = os.path.join(BASE, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(full)
    print("wrote", relpath)


def card(icon, href, h3, p):
    return (f'<div class="card"><div class="card-icon {icon}"><svg viewBox="0 0 24 24">'
            f'<circle cx="12" cy="12" r="10"/></svg></div>'
            f'<h3><a href="{href}">{h3}</a></h3><p>{p}</p></div>')


# ============ 4 remaining hubs ============

def hub_exchanges():
    body = '''
  <main>
    <section class="section">
      <div class="container">
        <div class="section-head">
          <div>
            <span class="kicker">Exchanges</span>
            <h1>Compare crypto exchanges in South Africa</h1>
            <p>Choosing an exchange is not only about the lowest trading fee. South African users also need to think about ZAR deposits and withdrawals, verification, security, available coins and banking methods.</p>
          </div>
        </div>
        <div class="card-grid">
          <div class="card">
            <div class="card-logo"><img src="../assets/binance.svg" alt="Binance logo" loading="lazy"></div>
            <h3><a href="binance/">Binance</a></h3>
            <p>A large international exchange with spot trading, stablecoins and a wide range of crypto products. Read our South Africa guides on registration, fees, ZAR access, USDT and withdrawals.</p>
          </div>
          <div class="card">
            <div class="card-logo"><img src="../assets/okx-logo.webp" alt="OKX logo" loading="lazy"></div>
            <h3><a href="okx/">OKX</a></h3>
            <p>A global exchange with spot trading, Web3 tools and a broad range of digital assets. See how OKX works for South African users and how it compares with other platforms.</p>
          </div>
          <div class="card">
            <div class="card-icon blue"><svg viewBox="0 0 24 24"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/></svg></div>
            <h3><a href="binance-vs-okx/">Binance vs OKX</a></h3>
            <p>Which platform makes more sense for South African users? ZAR access, fees, features and ease of use side by side.</p>
          </div>
        </div>

        <div class="compare-wrap">
          <h3 class="compare-title">How RandTrail compares exchanges</h3>
          <div class="compare-grid">
            <div class="compare-item"><span class="ci-label">ZAR access</span><span class="ci-desc">How rand enters and leaves the platform</span></div>
            <div class="compare-item"><span class="ci-label">Total cost</span><span class="ci-desc">Fees, spreads and withdrawal charges add up</span></div>
            <div class="compare-item"><span class="ci-label">Crypto withdrawals</span><span class="ci-desc">Whether assets can move to your own wallet</span></div>
            <div class="compare-item"><span class="ci-label">Regulatory status</span><span class="ci-desc">FSCA CASP licence vs. global platform</span></div>
            <div class="compare-item"><span class="ci-label">Custody</span><span class="ci-desc">Who controls the assets</span></div>
            <div class="compare-item"><span class="ci-label">Product access</span><span class="ci-desc">Spot, stablecoins and other services vary</span></div>
          </div>
          <a href="binance-vs-okx/" class="btn btn-primary">Compare Binance vs OKX &rarr;</a>
          <p class="table-note">Platform features, fees and regulatory status can change. Verify current details with the provider before acting. An FSCA CASP licence should not be read as a recommendation or government endorsement.</p>
        </div>

        <div class="cta-box">
          <h2><img src="../assets/binance-logo.png" alt="Binance" width="24" height="24" style="vertical-align:-5px;margin-right:9px">Considering Binance?</h2>
          <p>If, after comparing the available options, you decide Binance fits your needs, you can use the link below to visit its registration page. Check the fees, supported payment methods and crypto withdrawal options shown for your account before depositing funds.</p>
          <a href="https://www.binance.com/join?ref=GPYBA6R3" class="btn btn-primary" rel="nofollow sponsored noopener" target="_blank">Visit Binance &rarr;</a>
          <p class="cta-disclosure"><strong>Affiliate disclosure:</strong> This is an affiliate link. If you sign up through it, RandTrail may earn a commission at no additional cost to you. This does not affect our reviews, comparisons or editorial conclusions. See our <a href="../affiliate-disclosure.html">affiliate disclosure</a>.</p>
        </div>

        <div class="cta-box">
          <h2><img src="../assets/okx-logo.webp" alt="OKX" width="24" height="24" style="vertical-align:-5px;margin-right:9px">Considering OKX?</h2>
          <p>If you decide OKX fits your needs, you can use the link below to visit its registration page. Check the fees, payment methods and withdrawal options shown for your account before depositing funds.</p>
          <a href="https://www.okx.com/join/OK800" class="btn btn-primary" rel="nofollow sponsored noopener" target="_blank">Visit OKX &rarr;</a>
          <p class="cta-disclosure"><strong>Affiliate disclosure:</strong> This is an affiliate link. If you sign up through it, RandTrail may earn a commission at no additional cost to you. This does not affect our reviews or comparisons. See our <a href="../affiliate-disclosure.html">affiliate disclosure</a>.</p>
        </div>
      </div>
    </section>
  </main>
'''
    write_page("exchanges/index.html", "Exchanges",
               "Compare Crypto Exchanges in South Africa | RandTrail",
               "Compare Binance, OKX and other crypto exchanges for South African users — ZAR access, fees, withdrawals, security and regulatory status.",
               "https://randtrail.com/exchanges/", body)


def hub_buy_sell():
    body = '''
  <main>
    <section class="section section-tint-green">
      <div class="container">
        <div class="section-head">
          <div>
            <span class="kicker">Buy &amp; Sell</span>
            <h1>Move rand in and out of crypto</h1>
            <p>For most beginners, the hardest part is not understanding Bitcoin — it is figuring out how money actually moves. How do you deposit rand? Can you buy USDT directly? How long does an EFT take? How do you sell crypto and withdraw ZAR back to your bank account?</p>
          </div>
        </div>
        <div class="card-grid">
          <div class="card"><div class="card-icon green"><svg viewBox="0 0 24 24"><path d="M12 5v14"/><path d="m5 12 7 7 7-7"/></svg></div><h3><a href="buy-crypto/">Buy Crypto</a></h3><p>How to buy USDT, Bitcoin and other assets with rand — step by step.</p></div>
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg></div><h3><a href="sell-crypto/">Sell Crypto</a></h3><p>How to sell USDT and other assets back into rand.</p></div>
          <div class="card"><div class="card-icon green"><svg viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M12 8v8"/><path d="m8 12 4 4 4-4"/></svg></div><h3><a href="zar-deposits/">ZAR Deposits</a></h3><p>Instant EFT, standard EFT and Capitec — how to deposit rand and how long it takes.</p></div>
          <div class="card"><div class="card-icon blue"><svg viewBox="0 0 24 24"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M12 8v8"/><path d="m8 12 4 4 4-4"/></svg></div><h3><a href="withdrawals/">Cash Out</a></h3><p>How to withdraw ZAR to a South African bank account and how long it takes.</p></div>
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div><h3><a href="p2p/">P2P</a></h3><p>Buying and selling directly with other users — and how to stay safe.</p></div>
        </div>
      </div>
    </section>
  </main>
'''
    write_page("buy-sell/index.html", "Buy & Sell",
               "Buy & Sell Crypto with Rand (ZAR) | RandTrail",
               "How to buy USDT and Bitcoin with rand, deposit ZAR, sell crypto back to rand and withdraw to a South African bank account.",
               "https://randtrail.com/buy-sell/", body)


def hub_wallets():
    body = '''
  <main>
    <section class="section section-tint-blue">
      <div class="container">
        <div class="section-head">
          <div>
            <span class="kicker">Wallets &amp; Safety</span>
            <h1>Keep your crypto safer</h1>
            <p>Crypto transactions can be difficult or impossible to reverse, which makes simple security habits important. RandTrail explains how to protect exchange accounts, use wallets safely and avoid common scams — without turning every guide into a technical manual.</p>
          </div>
        </div>
        <div class="card-grid">
          <div class="card"><div class="card-icon green"><svg viewBox="0 0 24 24"><path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"/><path d="M3 5v14a2 2 0 0 0 2 2h16v-5"/><path d="M18 12a2 2 0 0 0 0 4h4v-4Z"/></svg></div><h3><a href="crypto-wallets/">Crypto Wallets</a></h3><p>Hot vs cold wallets, and where your crypto actually lives.</p></div>
          <div class="card"><div class="card-icon blue"><svg viewBox="0 0 24 24"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg></div><h3><a href="account-security/">Account Security</a></h3><p>2FA, seed phrases, phishing and keeping your exchange account locked down.</p></div>
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></div><h3><a href="transfers-networks/">Transfers &amp; Networks</a></h3><p>How to send and receive crypto safely — and what happens if you use the wrong network.</p></div>
          <div class="card"><div class="card-icon blue"><svg viewBox="0 0 24 24"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div><h3><a href="scam-prevention/">Scam Prevention</a></h3><p>The WhatsApp, Telegram and fake-investment scams targeting South African crypto users.</p></div>
        </div>
      </div>
    </section>
  </main>
'''
    write_page("wallets-safety/index.html", "Wallets & Safety",
               "Crypto Wallets & Safety | RandTrail",
               "How to keep crypto safe in South Africa — wallets, seed phrases, 2FA, safe transfers and how to spot common scams.",
               "https://randtrail.com/wallets-safety/", body)


def hub_tax():
    body = '''
  <main>
    <section class="section section-tint-orange">
      <div class="container">
        <div class="section-head">
          <div>
            <span class="kicker">Tax &amp; Regulation</span>
            <h1>Understand the rules</h1>
            <p>Buying crypto is only part of the picture. South African users also need to understand how crypto fits into local tax, identity verification and financial regulation. RandTrail explains these topics in plain English and links to official sources where possible.</p>
          </div>
        </div>
        <div class="card-grid">
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div><h3><a href="crypto-tax/">Crypto Tax</a></h3><p>How SARS treats crypto, capital gains tax and what you need to keep records of.</p></div>
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></div><h3><a href="sars/">SARS</a></h3><p>How the South African Revenue Service taxes and reports crypto transactions.</p></div>
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3><a href="fsca-casp/">FSCA &amp; CASP</a></h3><p>How crypto asset service providers are licensed and regulated in South Africa.</p></div>
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="M16 10h2"/><path d="M16 14h2"/><path d="M6.17 15a3 3 0 0 1 5.66 0"/><circle cx="9" cy="11" r="2"/><rect x="2" y="5" width="20" height="14" rx="2"/></svg></div><h3><a href="fica/">FICA</a></h3><p>Identity verification and anti-money-laundering rules that apply to crypto platforms.</p></div>
          <div class="card"><div class="card-icon orange"><svg viewBox="0 0 24 24"><path d="M12 3 2 7v5c0 5.5 4.3 9 10 9s10-3.5 10-9V7z"/><path d="m9 12 2 2 4-4"/></svg></div><h3><a href="legal-compliance/">Legal &amp; Compliance</a></h3><p>Is crypto legal in South Africa? Is Binance legal? A plain-English look at the rules.</p></div>
        </div>
        <p class="table-note" style="margin-top:22px;">Tax treatment depends on your circumstances. RandTrail provides educational information only and does not provide financial, investment, legal or tax advice.</p>
      </div>
    </section>
  </main>
'''
    write_page("tax-regulation/index.html", "Tax & Regulation",
               "Crypto Tax & Regulation in South Africa | RandTrail",
               "How SARS taxes crypto, capital gains tax, FSCA and CASP licensing, FICA verification and whether crypto is legal in South Africa.",
               "https://randtrail.com/tax-regulation/", body)


# ============ 2 exchange landings ============

def landing(exchange, title_name, canonical_slug, ref):
    lead = {
        "binance": "Binance users in South Africa often need answers to more than one question. Which ZAR routes are currently available? Can you complete verification? Can you withdraw crypto to an external wallet? What fees apply? This hub brings RandTrail&rsquo;s Binance guides together in one place, with a focus on the practical details that matter to South African users.",
        "okx": "OKX users in South Africa often need answers to more than one question. Which ZAR routes are currently available? Can you complete verification? Can you withdraw crypto to an external wallet? What fees apply? This hub brings RandTrail&rsquo;s OKX guides together in one place, with a focus on the practical details that matter to South African users.",
    }[exchange]
    q_is_avail = {
        "binance": "Is Binance available to users in South Africa?",
        "okx": "Is OKX available to users in South Africa?",
    }[exchange]
    body = f'''
  <main class="container page">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../../index.html">Home</a> <span class="sep">&rsaquo;</span> <a href="../">Exchanges</a> <span class="sep">&rsaquo;</span> <span class="current">{title_name}</span></nav>
    <h1>{title_name} for South Africa</h1>
    <p class="updated">Last updated: 12 September 2026</p>

    <p class="lede">{lead}</p>
    <p>Platform features, payment options and product availability can change, so time-sensitive information should always be checked against current {title_name} documentation before you act.</p>

    <div class="summary-box">
      <h2>Start with the {title_name} guide</h2>
      <p>If you are new to {title_name}, begin with our main guide. It covers account and verification requirements, funding and ZAR access, trading and conversion costs, crypto deposits and withdrawals, tax-record considerations, and common limits and account issues.</p>
      <a href="{ref}" class="btn btn-primary" rel="nofollow sponsored noopener" target="_blank">Visit {title_name} &rarr;</a>
    </div>

    <h2>What should South African users check before using {title_name}?</h2>
    <p>Do not treat &ldquo;Can I use {title_name}?&rdquo; as a single yes-or-no question. Check each of these separately:</p>
    <div class="table-wrap">
      <table class="compare">
        <tr><th>Check</th><th>Why it matters</th></tr>
        <tr><td>Account access</td><td>Determines whether you can open and use the account</td></tr>
        <tr><td>Verification (FICA)</td><td>Identity checks are required before many features become available</td></tr>
        <tr><td>ZAR access</td><td>Funding routes can change</td></tr>
        <tr><td>Product availability</td><td>Not every feature is available to every user</td></tr>
        <tr><td>Crypto withdrawals</td><td>Determines whether assets can be moved off-platform</td></tr>
        <tr><td>Fees</td><td>The trading fee is only one part of the total cost</td></tr>
        <tr><td>Tax records</td><td>South African users may need transaction records for SARS</td></tr>
        <tr><td>Security</td><td>Email and account protection are essential</td></tr>
      </table>
    </div>

    <h2>Verification and account setup</h2>
    <p>Identity verification is an important part of using major crypto platforms. South African users may be asked for a South African ID document or passport, proof of residence and other details as part of FICA-related checks.</p>

    <h2>ZAR access and funding</h2>
    <p>Funding is one of the areas that can change most frequently. Check which ZAR-related routes are currently displayed, whether Instant EFT or P2P options are available, whether crypto deposits are supported, and any limits, fees or verification requirements.</p>

    <h2>Trading fees and total cost</h2>
    <p>A low advertised trading fee does not always mean a low total cost. Your real cost can include maker or taker fees, conversion spreads, withdrawal fees, network charges and payment-route costs. Compare the full route, not one fee in isolation.</p>

    <h2>Crypto withdrawals and transfers</h2>
    <p>Before withdrawing crypto, check the asset, the network, the destination address, any memo or tag required, the minimum withdrawal, the platform withdrawal fee, and whether the receiving wallet supports the same network.</p>

    <h2>Tax and record-keeping</h2>
    <p>Crypto tax rules in South Africa are separate from exchange fees. Keep records of purchase date, purchase value, sale or transfer date, sale value, fees and exchange statements. RandTrail provides general educational information only and does not provide personalised tax advice. Related guide: <a href="../../tax-regulation/crypto-tax/">Crypto Tax in South Africa</a>.</p>

    <h2>{title_name} safety checklist</h2>
    <ul class="check-list">
      <li>Enable two-factor authentication.</li>
      <li>Secure the email account connected to your account.</li>
      <li>Verify the website or app source before logging in.</li>
      <li>Never share OTPs or passwords.</li>
      <li>Check withdrawal addresses carefully.</li>
      <li>Be cautious of fake support accounts.</li>
      <li>Keep your own transaction records.</li>
    </ul>

    <div class="cta-box">
      <h2><img src="../../assets/{'binance-logo.png' if exchange == 'binance' else 'okx-logo.webp'}" alt="{title_name}" width="24" height="24" style="vertical-align:-5px;margin-right:9px">Considering {title_name}?</h2>
      <p>If, after comparing the available options, you decide {title_name} fits your needs, you can use the link below to visit its registration page. Check the fees, supported payment methods and withdrawal options shown for your account before depositing funds.</p>
      <a href="{ref}" class="btn btn-primary" rel="nofollow sponsored noopener" target="_blank">Visit {title_name} &rarr;</a>
      <p class="cta-disclosure"><strong>Affiliate disclosure:</strong> This is an affiliate link. If you sign up through it, RandTrail may earn a commission at no additional cost to you. This does not affect our reviews, comparisons or editorial conclusions. See our <a href="../../affiliate-disclosure.html">affiliate disclosure</a>.</p>
    </div>
  </main>
'''
    write_page(f"exchanges/{exchange}/index.html", "Exchanges",
               f"{title_name} South Africa Guide: ZAR, Fees, Withdrawals | RandTrail",
               f"Practical {title_name} guides for South African users — account verification, ZAR access, fees, crypto withdrawals, tax records and safety.",
               f"https://randtrail.com/exchanges/{exchange}/", body)


# ============ legal pages ============

def legal(rel, title, desc, body_inner):
    body = f'  <main class="container page">\n{body_inner}\n  </main>\n'
    write_page(rel, "", title, desc, f"https://randtrail.com/{rel}", body)


def make_legal_pages():
    legal("about.html", "About RandTrail", "What RandTrail is and how we approach crypto education for South Africa.", '''
    <h1>About RandTrail</h1>
    <p class="updated">Last updated: 12 September 2026</p>
    <p>RandTrail is an educational guide to crypto, written for readers in South Africa. We explain how to buy, sell, store and use crypto, with a focus on the details that matter locally: rand (ZAR) payments, South African banking methods, local and international exchanges, and the SARS, FSCA and FICA rules that apply here.</p>
    <p>We do not assume the platform with the most features is automatically the best choice. The right exchange depends on what you want to do, how you fund your account and how you plan to withdraw your money.</p>
    <p>RandTrail provides educational information only. We do not provide financial, investment, legal or tax advice.</p>
''')

    legal("editorial-policy.html", "Editorial Policy | RandTrail", "How RandTrail researches, writes, reviews and updates its crypto guides.", '''
    <h1>Editorial Policy</h1>
    <p class="updated">Last updated: 12 September 2026</p>
    <p>Crypto information goes out of date quickly. Fees change, payment methods change, exchange interfaces change and rules change. We review and update guides regularly and try to separate three things: what a platform says, what official sources say, and what users actually see when using the service.</p>
    <h2>How we write</h2>
    <ul>
      <li>We prioritise practical detail over promotional language.</li>
      <li>We link to official sources where possible.</li>
      <li>We state risks and limitations, not only benefits.</li>
      <li>We label time-sensitive details and flag when they should be re-checked.</li>
    </ul>
    <h2>Affiliate links</h2>
    <p>Where a guide includes an affiliate link, we disclose it clearly. An affiliate relationship does not change how we assess a platform.</p>
''')

    legal("affiliate-disclosure.html", "Affiliate Disclosure | RandTrail", "How RandTrail uses affiliate links and what they mean for you.", '''
    <h1>Affiliate Disclosure</h1>
    <p class="updated">Last updated: 12 September 2026</p>
    <p>Some links on RandTrail are affiliate links. If you sign up or make a purchase through one of these links, RandTrail may earn a commission at no additional cost to you.</p>
    <h2>What this means</h2>
    <ul>
      <li>Affiliate links are marked with rel="sponsored" and are clearly disclosed.</li>
      <li>A commission does not change our reviews, comparisons or editorial conclusions.</li>
      <li>We assess platforms on practical criteria, not on whether they offer a referral program.</li>
    </ul>
    <p>Affiliate links on this site currently relate to Binance and OKX.</p>
''')

    legal("risk-disclosure.html", "Risk Disclosure | RandTrail", "The risks of buying and holding crypto, stated plainly.", '''
    <h1>Risk Disclosure</h1>
    <p class="updated">Last updated: 12 September 2026</p>
    <p>Cryptocurrency is highly volatile and involves significant market, custody, counterparty and operational risk. You may lose some or all of the money you invest.</p>
    <h2>Before you buy crypto</h2>
    <ul>
      <li>Prices can move sharply in either direction.</li>
      <li>Transactions can be difficult or impossible to reverse.</li>
      <li>Exchanges can fail, and assets held on an exchange carry custody risk.</li>
      <li>Scams are common, including on messaging apps.</li>
      <li>Tax may apply to your gains, and record-keeping is your responsibility.</li>
    </ul>
    <p>Do not deposit money simply because a platform is popular, and do not send crypto until you have checked the address and network carefully. RandTrail provides educational information only.</p>
''')

    legal("privacy.html", "Privacy Policy | RandTrail", "How RandTrail handles data and privacy.", '''
    <h1>Privacy Policy</h1>
    <p class="updated">Last updated: 12 September 2026</p>
    <p>RandTrail is a static educational website. We do not require you to create an account and we do not sell personal data.</p>
    <h2>What we collect</h2>
    <ul>
      <li>Standard server logs (IP address, browser, pages visited) for security and analytics.</li>
      <li>Email messages you send to hello@randtrail.com.</li>
    </ul>
    <h2>Third parties</h2>
    <p>Some pages link to third-party services such as exchanges. When you click an affiliate link and leave RandTrail, that site&rsquo;s own privacy policy applies. Some pages may use privacy-respecting analytics. This policy may be updated over time.</p>
''')

    legal("disclaimer.html", "Disclaimer | RandTrail", "RandTrail is educational content, not financial advice.", '''
    <h1>Disclaimer</h1>
    <p class="updated">Last updated: 12 September 2026</p>
    <p>RandTrail provides educational information only and does not provide financial, investment, legal or tax advice. Nothing on this site is a recommendation to buy, sell or hold any asset.</p>
    <h2>Tax and regulation</h2>
    <p>Tax treatment depends on your circumstances. Regulatory status can change. Always verify current details with official sources such as SARS, the FSCA and the platform itself before making decisions.</p>
    <p>If you have significant holdings or a complex situation, consult a qualified South African financial or tax professional.</p>
''')

    legal("contact.html", "Contact | RandTrail", "Get in touch with RandTrail.", '''
    <h1>Contact</h1>
    <p class="updated">Last updated: 12 September 2026</p>
    <p>Have a correction, a question, or a topic you would like us to cover? Email us at <a href="mailto:hello@randtrail.com">hello@randtrail.com</a>.</p>
    <p>We aim to reply within a few business days.</p>
''')

    # redirect the email in page anchors
    print("legal pages written")


if __name__ == "__main__":
    hub_exchanges()
    hub_buy_sell()
    hub_wallets()
    hub_tax()
    landing("binance", "Binance", "exchanges/binance", "https://www.binance.com/join?ref=GPYBA6R3")
    landing("okx", "OKX", "exchanges/okx", "https://www.okx.com/join/OK800")
    make_legal_pages()
    print("done")
