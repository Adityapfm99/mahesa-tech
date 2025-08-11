import React from 'react';
import styles from '../styles/Home.module.css';

export default function Header() {
  return (
    <header className={styles.headerModern}>
      <div className={styles.logoArea}>
        {/* Replace with your SVG logo if available */}
        <span className={styles.logoIcon}> 
          {/* Example SVG logo */}
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
            <circle cx="16" cy="16" r="16" fill="#0070f3"/>
            <text x="16" y="21" textAnchor="middle" fontSize="16" fill="#fff" fontFamily="Arial" fontWeight="bold">M</text>
          </svg>
        </span>
        <span className={styles.logoText}>Mahesa Tech</span>
        <span className={styles.tagline}>Japanese Invoice Automation SaaS</span>
      </div>
      <nav className={styles.navModern}>
        <a href="/">Home</a>
        <a href="/features">Our Services</a>
        <a href="/pricing">Pricing</a>
        <a href="/contact">Contact</a>
        <a href="/login" className={styles.loginNav}>Login</a>
      </nav>
    </header>
  );
}
