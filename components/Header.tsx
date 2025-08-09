import React from 'react';
import styles from '../styles/Home.module.css';

export default function Header() {
  return (
    <header className={styles.header}>
      <h1>Mahesa Tech</h1>
      <nav>
        <a href="/#features">Features</a>
        <a href="/#contact">Contact</a>
        <a href="/pricing">Pricing</a>
      </nav>
    </header>
  );
}
