# Mahesa Tech

Mahesa Tech is a SaaS platform for automating and converting invoices to comply with Japanese legal standards (Qualified Invoice System).

## Main Features

- Professional landing page
- Pricing page for paid plans
- Invoice conversion according to Japanese regulations
- Responsive and easy to extend

## Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```
3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Folder Structure

```
/pages         # Main Next.js pages
/components    # Reusable components (Header, etc)
/styles        # CSS modules & global styles
```

## Reference

- [Japanese Qualified Invoice System](https://hls-global.jp/en/2023/05/17/introduction-to-the-new-japanese-invoice-system-implementation-qualified-invoice-issuers-2/)

## License

MIT

## SaaS Paid User Flow

1. **User Registration/Login**
   - User signs up and logs in to their account.

2. **Subscription/Purchase**
   - User selects a pricing tier (e.g. Pro/Enterprise) and completes payment (Stripe, etc).

3. **Access Paid Features**
   - After payment, user status is updated to "paid".
   - User can access unlimited conversions, dashboard, API, and other premium features.

4. **Usage Tracking**
   - User's conversion history, usage limits, and billing info are tracked in their account.

5. **Renewal/Upgrade**
   - User can renew, upgrade, or downgrade their plan from the dashboard.

6. **Logout/Account Management**
   - User can manage profile, billing, and logout securely.

**Technical Implementation:**
- Use authentication (JWT, NextAuth, etc).
- Store user status (free/paid) in backend/database.
- Check user status before allowing access to paid features.
- Integrate payment gateway for subscription management.
