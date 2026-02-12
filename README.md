# CYFSA Parent Platform — Ontario Educational Resource

**Educational information only — NOT LEGAL ADVICE — Ontario jurisdiction only**

This repo is a static website + an optional Python analyzer prototype (not deployed by default). It is built to teach *process + evidence literacy* under Ontario’s CYFSA and help parents find **verified** lawyer resources (LSO directory / LAO / LSRS). It does **not** list individual lawyers unless you add verified listings yourself.

---

## 🚀 QUICK START (Static site in ~10 minutes)

### 1) Upload to GitHub
```bash
git init
git add .
git commit -m "Initial commit - CYFSA Parent Platform"
git branch -M main
git remote add origin https://github.com/<yourusername>/cyfsa-parent-platform.git
git push -u origin main
```

### 2) Deploy to Netlify (free)
1. Netlify → **Add new site** → **Import from Git**
2. Select your repo
3. Build command: `echo "static"`
4. Publish directory: `/`
5. Deploy

---

## ⚠️ What this repo does and does NOT do

### ✅ Included
- Landing page with **verified** directories (LAO, LSO Directory, LSRS)
- Law-firms page (placeholder layout + how to add verified firm listings)
- Subscriber-area page (client-side “gate” for convenience only)
- Payment instructions (Interac e-transfer)
- Analyzer rules JSON + Python engine prototype

### ❌ Not included (by design)
- No fake lawyer names, phone numbers, “success rates”, or invented credentials
- No real security / client portal / encrypted uploads (static sites cannot do that)

If you need real authentication, storage, and uploads, deploy a backend (Netlify Functions, Cloudflare Workers, or a small Flask app) and use proper auth.

---

## Compliance rules (non-negotiable)
- Ontario only. If a document references another jurisdiction, flag **out_of_jurisdiction**.
- Educational flags only. No legal advice. No predicting outcomes.
- Do not infer identity, consent, or authenticity from documents.
- Quotes from user docs limited to **≤25 words**.
- Display the disclaimer on every page/output.

---

## Verified public resources used (you should keep these links)
- Legal Aid Ontario contact + toll-free: https://www.legalaid.on.ca/more/corporate/contact-legal-aid-ontario/
- LAO “How do I apply”: https://www.legalaid.on.ca/services/how-do-i-apply-for-legal-aid/
- Law Society of Ontario Lawyer & Paralegal Directory: https://lso.ca/public-resources/finding-a-lawyer-or-paralegal/lawyer-and-paralegal-directory
- Law Society Referral Service: https://lsrs.lso.ca/lsrs/redefineLocale.action?currentLang=en

---

## Optional: Run the Python analyzer locally (prototype)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install flask
python analyzer/engine.py
```

---

## License / disclaimer
This project is an **educational resource** only. It is **not a law firm**, not a client portal, and provides **no legal advice**.
© 2026
