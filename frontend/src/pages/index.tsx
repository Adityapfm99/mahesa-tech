import React from 'react';
import Head from 'next/head';
import styles from '../../styles/Home.module.css';

export default function Home() {
  return (
    <>
      <Head>
        <title>Mahesa Tech</title>
        <meta name="description" content="Mahesa Tech - Innovative SaaS Solutions" />
      </Head>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1>Mahesa Tech</h1>
          <nav>
            <a href="/features">Features</a>
            <a href="/contact">Contact</a>
          </nav>
        </header>
        <main>
          <section className={styles.hero}>
            <h2>Empowering Your Business with Technology</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nunc ut laoreet cursus, enim erat dictum urna, nec gravida sem erat ac erat.</p>
            <button className={styles.cta}>Get Started</button>
          </section>
          <section id="features" className={styles.features}>
            <h3>Our Features</h3>
            <ul>
              <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
              <li>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</li>
              <li>Donec ullamcorper nulla non metus auctor fringilla.</li>
              <li>Vestibulum id ligula porta felis euismod semper.</li>
              <li><strong>Convert Invoice Legal Japan:</strong> Automate and convert invoices to comply with Japanese legal standards for business documentation.</li>
            </ul>
          </section>
        \
        </main>
        <section className={styles.testimonials}>
          <h3>Testimonials</h3>
          <div>
            <blockquote>
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante."
            </blockquote>
            <p>- John Doe, CEO ExampleCorp</p>
          </div>
          <div>
            <blockquote>
              "Sed posuere consectetur est at lobortis. Aenean eu leo quam. Pellentesque ornare sem."
            </blockquote>
            <p>- Jane Smith, CTO SampleInc</p>
          </div>
        </section>
        <footer className={styles.footer}>
          &copy; 2025 Mahesa Tech
        </footer>
      </div>
    </>
  );
}