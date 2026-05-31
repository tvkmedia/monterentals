// Vite config — multi-page static site.
// Each .html file is its own entry point; Vite bundles them all into dist/.
// On Hostinger Build & Deploy this is detected automatically (Vite preset).

import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: '.',
  publicDir: 'public',         // files in public/ are copied verbatim to dist/
  base: './',                  // relative asset URLs (works on any subpath)

  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        index:               resolve(__dirname, 'index.html'),
        search:              resolve(__dirname, 'search.html'),
        travelGuide:         resolve(__dirname, 'travel-guide.html'),
        locations:           resolve(__dirname, 'locations.html'),
        support:             resolve(__dirname, 'support.html'),
        manageBooking:       resolve(__dirname, 'manage-booking.html'),
        monteClub:           resolve(__dirname, 'monte-club.html'),
        legal:               resolve(__dirname, 'legal.html'),
        articleRoadTrip:     resolve(__dirname, 'article-road-trip-tips.html'),
        articlePanoramic:    resolve(__dirname, 'article-panoramic-routes.html'),
        articleDrivingRules: resolve(__dirname, 'article-driving-rules.html'),
        articleProkletije:   resolve(__dirname, 'article-prokletije.html'),
        articleSinjajevina:  resolve(__dirname, 'article-sinjajevina.html'),
        articleKomovi:       resolve(__dirname, 'article-komovi.html'),
      },
    },
  },

  server: {
    port: 5173,
    open: '/index.html',
  },
});
