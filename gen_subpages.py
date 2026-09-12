#!/usr/bin/env python3
"""Generate the 17 lightweight sub-hub pages (kills the nav/footer 404s).

Reuses gen.py's header/footer/write_page so the chrome stays consistent.
Run:  python3 gen_subpages.py
"""
from gen import write_page

UPDATED = '<p class="updated">Last updated: 12 September 2026</p>'


def crumb(parent, current):
    return (f'<nav class="breadcrumb" aria-label="Breadcrumb">'
            f'<a href="../../index.html">Home</a> <span class="sep">&rsaquo;</span> '
            f'<a href="../">{parent}</a> <span class="sep">&rsaquo;</span> '
            f'<span class="current">{current}</span></nav>')


def page(relpath, active, parent, current, title, desc, inner):
    body = f'  <main class="container page">\n    {crumb(parent, current)}\n    <h1>{title}</h1>\n    {UPDATED}\n{inner}\n  </main>\n'
    canonical = f"https://randtrail.com/{relpath.replace('index.html', '')}"
    write_page(relpath, active, f"{title} | RandTrail", desc, canonical, body)


# ---- Start Here ----

page("start-here/crypto-basics/index.html", "Start Here", "Start Here", "Crypto Basics",
     "Crypto Basics, Explained for South Africa",
     "What crypto actually is, how blockchains and wallets work, and the difference between buying on an exchange and holding in your own wallet.",
     """
    <p class="lede">Crypto is money and value recorded on a shared digital ledger instead of a bank&rsquo;s records. When you buy crypto, you are not usually holding a physical coin — you are holding a record on a network such as Bitcoin or Ethereum, controlled by a key that only you (or your exchange) can use.</p>
    <p>Three ideas matter most at the start. First, a <strong>blockchain</strong> is a public record of transactions that many computers maintain together. Second, a <strong>wallet</strong> holds the keys that control your crypto — and those keys are what actually matter, not the wallet app itself. Third, an <strong>exchange</strong> such as Binance or OKX is where most people first buy crypto with rand, but leaving assets there means the exchange holds the keys on your behalf.</p>
    <p>The practical consequence for South African users: you buy crypto with rand through a platform, then choose whether to leave it there or move it to a wallet you control. Each choice trades convenience against control.</p>
    <h2>Start with these</h2>
    <ul>
      <li><a href="../bitcoin/">What is Bitcoin?</a> — the first and most recognised crypto asset.</li>
      <li><a href="../stablecoins/">What are stablecoins?</a> — USDT, USDC and assets designed to hold a steady value.</li>
      <li><a href="../beginner-guides/">Beginner guides</a> — the practical path from first rand to first purchase.</li>
      <li><a href="../../exchanges/binance/">Binance South Africa review</a> — how a major exchange works for SA users.</li>
    </ul>
""")

page("start-here/bitcoin/index.html", "Start Here", "Start Here", "Bitcoin",
     "Bitcoin in South Africa",
     "What Bitcoin is, how it differs from other crypto, and how South Africans buy it with rand.",
     """
    <p class="lede">Bitcoin is the first and largest cryptocurrency: a digital asset with a fixed supply schedule and no single company or government in charge. For many people it is the entry point into crypto, and in South Africa it is widely available through local and international exchanges.</p>
    <p>Bitcoin&rsquo;s price is famously volatile, which is the single most important thing to understand before buying. People buy it for different reasons — some as a long-term holding, some to trade — but the mechanics of getting rand in and out are the same as for any other crypto asset.</p>
    <p>You can buy Bitcoin with rand by depositing ZAR on an exchange and placing an order, or by buying from another user through P2P. The route that suits you depends on your bank, how fast you want to move and the fees shown.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="../../buy-sell/how-to-deposit-zar-on-binance/">How to deposit ZAR on Binance</a> — fund an account with rand.</li>
      <li><a href="../../buy-sell/how-to-buy-usdt-south-africa/">How to buy USDT with ZAR</a> — the same funding steps apply to Bitcoin.</li>
      <li><a href="../../exchanges/binance/">Binance South Africa review</a> and <a href="../../exchanges/okx/">OKX review</a> — two platforms that support SA users.</li>
    </ul>
""")

page("start-here/stablecoins/index.html", "Start Here", "Start Here", "Stablecoins",
     "Stablecoins in South Africa",
     "What USDT, USDC and other stablecoins are, why they exist, and how South Africans buy them with rand.",
     """
    <p class="lede">A stablecoin is a crypto asset designed to keep a steady value — most commonly by tracking the US dollar. The two you will see most in South Africa are <strong>USDT</strong> (Tether) and <strong>USDC</strong> (USD Coin). They are used as a stable store of value and as a way to move money between exchanges without the price swings of Bitcoin.</p>
    <p>Stablecoins matter to South African users because they sit at the centre of how rand moves in and out of crypto. Many people buy USDT with rand, use it to trade or transfer value, and later sell it back for rand. The price being roughly stable removes one variable from that flow.</p>
    <p>Stablecoins still carry risk — they depend on the issuer holding the backing assets, and a &ldquo;stable&rdquo; price is not a guarantee. But for moving value and parking money between trades, they are the standard tool.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="../../buy-sell/how-to-buy-usdt-south-africa/">How to buy USDT with ZAR</a> — the main route into stablecoins.</li>
      <li><a href="../../buy-sell/how-to-deposit-zar-on-binance/">How to deposit ZAR on Binance</a> — fund an account first.</li>
      <li><a href="../crypto-basics/">Crypto basics</a> — how wallets and keys work before you move funds.</li>
    </ul>
""")

page("start-here/beginner-guides/index.html", "Start Here", "Start Here", "Beginner Guides",
     "Beginner Crypto Guides for South Africa",
     "The step-by-step path for a South African beginner — from opening an account to buying crypto with rand and keeping it safe.",
     """
    <p class="lede">If you are new to crypto in South Africa, the shortest path is: understand the basics, choose an exchange, deposit rand, buy a small amount, and only then worry about wallets and taxes. You do not need to master every topic before you start.</p>
    <p>The order below follows the real journey most South Africans take. Start with how money actually gets in and out, because that is where beginners lose the most time and money — not in understanding the technology.</p>
    <h2>Follow the journey</h2>
    <ul>
      <li><a href="../crypto-basics/">Crypto basics</a> — the few ideas that actually matter.</li>
      <li><a href="../../exchanges/binance/">Binance review</a> or <a href="../../exchanges/okx/">OKX review</a> — pick a platform.</li>
      <li><a href="../../buy-sell/how-to-deposit-zar-on-binance/">Deposit ZAR</a> — get rand into your account.</li>
      <li><a href="../../buy-sell/how-to-buy-usdt-south-africa/">Buy USDT with ZAR</a> — your first purchase.</li>
      <li><a href="../../buy-sell/how-to-withdraw-from-binance/">Withdraw to your bank</a> — how money comes back out.</li>
      <li><a href="../../wallets-safety/account-security/">Account security</a> — lock it down before you hold more.</li>
    </ul>
""")

# ---- Buy & Sell ----

page("buy-sell/buy-crypto/index.html", "Buy & Sell", "Buy &amp; Sell", "Buy Crypto",
     "How to Buy Crypto in South Africa",
     "The practical ways to buy Bitcoin, USDT and other crypto with rand — deposit ZAR, card, or P2P, and what each route costs.",
     """
    <p class="lede">You can buy crypto in South Africa by depositing rand on an exchange and buying there, paying by card, or buying directly from another user through P2P. There is no single cheapest route — the right one depends on your bank, how fast you need it and the fee shown at the time.</p>
    <p>For most people the cleanest route is to deposit ZAR on an exchange such as Binance and then buy the asset you want. The card route is faster but often carries a processing fee, and P2P skips the deposit step but means buying from another user.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="how-to-buy-usdt-south-africa/">How to buy USDT with ZAR</a> — the full routes compared.</li>
      <li><a href="how-to-deposit-zar-on-binance/">How to deposit ZAR on Binance</a> — fund an account first.</li>
      <li><a href="../../exchanges/binance/">Binance review</a> and <a href="../../exchanges/okx/">OKX review</a> — platform choice.</li>
    </ul>
""")

page("buy-sell/sell-crypto/index.html", "Buy & Sell", "Buy &amp; Sell", "Sell Crypto",
     "How to Sell Crypto in South Africa",
     "How to sell Bitcoin, USDT and other crypto back into rand and move it to a South African bank account.",
     """
    <p class="lede">Selling crypto in South Africa usually means converting your asset back to rand — either by selling on an exchange and withdrawing ZAR, or by selling to another user through P2P. The goal is normally the same: get rand into your bank account.</p>
    <p>Before selling, confirm how the money will reach you. A ZAR withdrawal to a South African bank account is one route; P2P is another, where the buyer pays you directly. Each has different timing and fees, so check the amount you will actually receive before you confirm.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="how-to-withdraw-from-binance/">How to withdraw from Binance</a> — the main route back to rand.</li>
      <li><a href="p2p/">P2P trading</a> — sell directly to another user.</li>
      <li><a href="../../tax-regulation/crypto-tax/">Crypto tax in South Africa</a> — selling can trigger a taxable gain.</li>
    </ul>
""")

page("buy-sell/zar-deposits/index.html", "Buy & Sell", "Buy &amp; Sell", "ZAR Deposits",
     "Deposit ZAR on Crypto Exchanges",
     "How to deposit rand into a crypto exchange — Absa Pay, Capitec Pay, card, Apple Pay and bank transfer, and which to pick.",
     """
    <p class="lede">Depositing rand is the step that turns your South African bank balance into crypto you can trade. On Binance the current ZAR routes include Absa Pay, Capitec Pay, card, Apple Pay and bank transfer (EFT) — with Google Pay currently not supported.</p>
    <p>The method that suits you depends mostly on which bank you use: Absa clients can use Absa Pay, Capitec clients can use Capitec Pay, and anyone else can use a card or a linked bank transfer. Always check the fee and the receive amount shown for your own account before you confirm.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="how-to-deposit-zar-on-binance/">How to deposit ZAR on Binance</a> — every method, step by step.</li>
      <li><a href="how-to-buy-usdt-south-africa/">How to buy USDT with ZAR</a> — what to do after the deposit lands.</li>
      <li><a href="../../exchanges/binance/">Binance review</a> — ZAR routes, fees and safety.</li>
    </ul>
""")

page("buy-sell/withdrawals/index.html", "Buy & Sell", "Buy &amp; Sell", "Withdrawals",
     "Withdraw Crypto to a South African Bank",
     "How to withdraw crypto or ZAR from an exchange to a South African bank account, how long it takes, and what it costs.",
     """
    <p class="lede">Withdrawing means moving your crypto or rand off an exchange — usually to your own bank account or a wallet you control. In South Africa the two main paths are a ZAR withdrawal to a local bank, or a crypto withdrawal to an external wallet.</p>
    <p>ZAR withdrawals go through the payment rails the exchange supports, which can change over time. Crypto withdrawals require you to check the network and address carefully, because a mistake there is often unrecoverable.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="how-to-withdraw-from-binance/">How to withdraw from Binance</a> — ZAR and crypto routes compared.</li>
      <li><a href="../../wallets-safety/transfers-networks/">Transfers &amp; networks</a> — avoid the wrong-network mistake.</li>
      <li><a href="../../tax-regulation/crypto-tax/">Crypto tax in South Africa</a> — what a withdrawal means for SARS.</li>
    </ul>
""")

page("buy-sell/p2p/index.html", "Buy & Sell", "Buy &amp; Sell", "P2P",
     "P2P Crypto Trading in South Africa",
     "How peer-to-peer crypto works in South Africa — buying and selling directly with other users, the escrow system, and how to stay safe.",
     """
    <p class="lede">P2P (peer-to-peer) lets you buy or sell crypto directly with another user, paying in rand, without first depositing money into an exchange&rsquo;s fiat balance. The exchange sits in the middle to hold the crypto in escrow until the payment is confirmed, which is what makes the trade safer than dealing with a stranger directly.</p>
    <p>The flow matters more than the theory. When you buy, the seller&rsquo;s crypto is reserved (escrowed) at the moment the order is created; you pay the seller by bank transfer or another offered method; then the seller releases the crypto only after confirming your payment has arrived. That ordering is what protects both sides.</p>
    <p>Two rules keep you out of trouble. Pay only from a payment method in your own name, and mark the order as paid only after the money has actually left your account. Never trade outside the platform&rsquo;s P2P process, and treat a price far better than the market as a warning sign, not an opportunity.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="how-to-deposit-zar-on-binance/">How to deposit ZAR on Binance</a> — see the P2P method alongside the deposit routes.</li>
      <li><a href="how-to-buy-usdt-south-africa/">How to buy USDT with ZAR</a> — P2P as one of four routes.</li>
      <li><a href="../../wallets-safety/scam-prevention/">Scam prevention</a> — the scams to watch for.</li>
    </ul>
""")

# ---- Wallets & Safety ----

page("wallets-safety/crypto-wallets/index.html", "Wallets & Safety", "Wallets &amp; Safety", "Crypto Wallets",
     "Crypto Wallets for South Africans",
     "Hot vs cold wallets, custodial vs self-custody, and where your crypto actually lives.",
     """
    <p class="lede">A crypto wallet stores the keys that control your crypto, not the coins themselves. The key distinction is who controls those keys: a <strong>custodial</strong> wallet on an exchange means the exchange holds them; a <strong>self-custody</strong> wallet means you do, and you are solely responsible for not losing them.</p>
    <p>Wallets also split into <strong>hot</strong> (connected to the internet, such as a phone or browser wallet) and <strong>cold</strong> (kept offline, such as a hardware wallet). Hot wallets are convenient for spending and trading; cold wallets are for larger amounts you plan to hold.</p>
    <p>For most South African beginners, the practical answer is: keep small, actively-traded amounts on the exchange, and move anything you plan to hold long-term into a wallet you control — then protect the recovery phrase as carefully as the money itself.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="../transfers-networks/">Transfers &amp; networks</a> — how to move crypto without losing it.</li>
      <li><a href="../account-security/">Account security</a> — protect the keys and the recovery phrase.</li>
      <li><a href="../../buy-sell/how-to-withdraw-from-binance/">How to withdraw from Binance</a> — moving assets to your own wallet.</li>
    </ul>
""")

page("wallets-safety/account-security/index.html", "Wallets & Safety", "Wallets &amp; Safety", "Account Security",
     "Crypto Account Security",
     "How to protect your exchange account and wallet — 2FA, passwords, phishing, and the recovery phrase.",
     """
    <p class="lede">Most crypto losses in South Africa do not come from a broken blockchain — they come from weak account security: reused passwords, phishing links, and shared one-time codes. The single highest-impact step is enabling <strong>two-factor authentication (2FA)</strong> on both your exchange account and your email.</p>
    <p>Beyond 2FA, use a unique password, secure the email account that resets everything, and never share an OTP with anyone — including someone claiming to be exchange support. No legitimate support agent asks for your password or one-time code.</p>
    <p>If you use a self-custody wallet, the <strong>recovery phrase</strong> is the key to everything. Write it down, store it offline, and never type it into a website or send it to anyone. Anyone who has it has your funds.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="../scam-prevention/">Scam prevention</a> — the common scams and how to spot them.</li>
      <li><a href="../crypto-wallets/">Crypto wallets</a> — where keys and recovery phrases fit in.</li>
      <li><a href="../../exchanges/binance/">Binance review</a> — security features on a major exchange.</li>
    </ul>
""")

page("wallets-safety/transfers-networks/index.html", "Wallets & Safety", "Wallets &amp; Safety", "Transfers &amp; Networks",
     "Crypto Transfers &amp; Networks",
     "How to send and receive crypto safely — choosing the right network, checking addresses, and what happens if you use the wrong one.",
     """
    <p class="lede">The most important rule in crypto transfers: the <strong>network must match on both sides</strong>. The same asset can exist on several networks — for example USDT on TRC-20 (Tron), ERC-20 (Ethereum) or BEP-20 (BNB Smart Chain) — and sending to the wrong one can mean the funds are lost for good.</p>
    <p>Networks differ mainly in speed and cost. TRC-20 transfers are typically cheap, while ERC-20 transfers are often more expensive. But the cheapest option is only correct if the receiving wallet supports that same network, so always check the destination first rather than defaulting to the lowest fee.</p>
    <p>Before you send, check four things: the asset, the network, the full address, and any memo or tag the destination requires. Send a small test amount first for a larger transfer. If the address or network is wrong, the transaction usually cannot be reversed.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="../crypto-wallets/">Crypto wallets</a> — how addresses and networks fit together.</li>
      <li><a href="../../buy-sell/how-to-buy-usdt-south-africa/">How to buy USDT with ZAR</a> — includes what to check when moving USDT.</li>
      <li><a href="../../buy-sell/how-to-withdraw-from-binance/">How to withdraw from Binance</a> — withdrawing to an external wallet.</li>
    </ul>
""")

page("wallets-safety/scam-prevention/index.html", "Wallets & Safety", "Wallets &amp; Safety", "Scam Prevention",
     "Crypto Scam Prevention",
     "The WhatsApp, Telegram and fake-investment scams targeting South African crypto users, and how to spot them.",
     """
    <p class="lede">The most common crypto scams in South Africa are not technical hacks — they are social tricks: a WhatsApp or Telegram group promising guaranteed returns, a &ldquo;support agent&rdquo; who contacts you first, or a fake investment platform that shows profits but never pays out. The pattern is almost always the same: someone you do not know offers you money for sending them money or your keys.</p>
    <p>Guaranteed or fixed returns are the clearest red flag — no legitimate crypto investment guarantees a profit. A second red flag is being contacted first: real exchanges do not message you asking for your password, OTP or recovery phrase.</p>
    <p>The defences are simple. Never share your recovery phrase, passwords or OTPs. Verify any website or app before logging in. Treat unsolicited investment offers as scams by default, and keep trades on the exchange rather than moving to private chat.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="../account-security/">Account security</a> — the habits that stop most scams.</li>
      <li><a href="../../buy-sell/p2p/">P2P trading</a> — safe buying and selling between users.</li>
      <li><a href="../../exchanges/binance/">Binance review</a> — using a major platform safely.</li>
    </ul>
""")

# ---- Tax & Regulation ----

page("tax-regulation/sars/index.html", "Tax & Regulation", "Tax &amp; Regulation", "SARS",
     "SARS and Crypto in South Africa",
     "How the South African Revenue Service treats crypto, what it can see through CARF reporting, and what you need to declare.",
     """
    <p class="lede">SARS treats crypto as an asset, not as a foreign currency, and taxes it through the normal income tax and capital gains tax rules. Buying and holding by itself is generally not taxable; tax can arise when you dispose of crypto, and activities such as mining or staking can create taxable income.</p>
    <p>South Africa&rsquo;s Crypto-Asset Reporting Framework (CARF) took effect on 1 March 2026, which means relevant crypto service providers must collect and report certain transaction data to SARS. That has made undisclosed crypto activity much harder to hide, so past activity is increasingly visible to the tax authority.</p>
    <p>Whether a gain is taxed as income (up to 45%) or as a capital gain (effectively lower for individuals) depends on how you behave, not on a label you choose. Keep records of every purchase and disposal.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="crypto-tax/">Crypto tax in South Africa</a> — the full guide to what is taxed and how.</li>
      <li><a href="fsca-casp/">FSCA &amp; CASP</a> — the separate licensing side of regulation.</li>
      <li><a href="is-binance-legal-south-africa/">Is Binance legal in South Africa?</a> — the legal status of a major exchange.</li>
    </ul>
""")

page("tax-regulation/fsca-casp/index.html", "Tax & Regulation", "Tax &amp; Regulation", "FSCA &amp; CASP",
     "FSCA &amp; CASP Crypto Licensing",
     "How crypto asset service providers are licensed and regulated in South Africa, and what an FSCA licence does and does not mean.",
     """
    <p class="lede">The Financial Sector Conduct Authority (FSCA) declared crypto assets to be financial products in October 2022, which brought crypto asset service providers (CASPs) under South Africa&rsquo;s financial-services framework. Existing providers had to apply for a CASP licence, and local platforms such as Luno and VALR hold local licences.</p>
    <p>Two things are easy to misread. First, an FSCA licence is a regulatory authorisation, not a recommendation or government endorsement of a platform. Second, a licence held in another country is not a South African FSCA CASP licence — so a global exchange with overseas licences is not the same as a locally licensed CASP.</p>
    <p>For users, the practical takeaway is to check a platform&rsquo;s current status rather than assuming &ldquo;licensed&rdquo; means &ldquo;regulated here&rdquo;. Status can change, so verify against the FSCA&rsquo;s published lists.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="is-binance-legal-south-africa/">Is Binance legal in South Africa?</a> — the legal and licensing picture.</li>
      <li><a href="fica/">FICA</a> — the identity verification side of compliance.</li>
      <li><a href="sars/">SARS</a> — the tax authority&rsquo;s separate rules.</li>
    </ul>
""")

page("tax-regulation/fica/index.html", "Tax & Regulation", "Tax &amp; Regulation", "FICA",
     "FICA and Crypto in South Africa",
     "What FICA means for crypto users — identity verification, anti-money-laundering rules, and why exchanges ask for your ID.",
     """
    <p class="lede">FICA — the Financial Intelligence Centre Act — is South Africa&rsquo;s anti-money-laundering law, and it is why exchanges ask for your ID, proof of residence and sometimes more before you can deposit or trade. Verification is not optional friction; it is a legal requirement the platform has to meet.</p>
    <p>For you, FICA mostly shows up as <strong>identity verification</strong> when you open an account or raise your limits. Completing it early unlocks deposit and withdrawal routes, and an account with unverified details is often the reason a feature or payment method does not appear.</p>
    <p>Being &ldquo;FICA-registered&rdquo; or completing verification does not mean a platform is licensed by the FSCA — they are separate requirements. One is about knowing your customer; the other is about being authorised as a financial-services provider.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="fsca-casp/">FSCA &amp; CASP</a> — how FICA fits with licensing.</li>
      <li><a href="is-binance-legal-south-africa/">Is Binance legal in South Africa?</a> — verification and legal status.</li>
      <li><a href="../../buy-sell/how-to-deposit-zar-on-binance/">How to deposit ZAR on Binance</a> — where verification unlocks ZAR routes.</li>
    </ul>
""")

page("tax-regulation/legal-compliance/index.html", "Tax & Regulation", "Tax &amp; Regulation", "Legal &amp; Compliance",
     "Crypto Legal &amp; Compliance in South Africa",
     "Is crypto legal in South Africa? A plain-English look at the rules covering exchanges, tax, and what individuals can do.",
     """
    <p class="lede">Crypto is legal to own and use in South Africa, and it is regulated rather than banned. Crypto assets are treated as financial products under the FSCA framework, and income or gains from them are taxable under SARS rules. The regulation is about how providers must operate, not about stopping individuals from using crypto.</p>
    <p>For an individual, the questions that actually matter are practical: can you use a given exchange, how does verification work, and what do you owe SARS. Whether a specific platform is available can change, so check the current position rather than relying on a single yes-or-no label.</p>
    <h2>Related guides</h2>
    <ul>
      <li><a href="is-binance-legal-south-africa/">Is Binance legal in South Africa?</a> — the legal status of a major exchange.</li>
      <li><a href="crypto-tax/">Crypto tax in South Africa</a> — what you owe SARS.</li>
      <li><a href="fsca-casp/">FSCA &amp; CASP</a> and <a href="fica/">FICA</a> — the two compliance tracks.</li>
    </ul>
""")

print("17 sub-pages written")
