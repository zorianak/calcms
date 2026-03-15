import { defineConfig } from '@pandacss/dev';

export default defineConfig({
  // Whether to use CSS reset
  preflight: true,

  // Where to look for your css declarations
  include: ['./src/**/*.{js,jsx,ts,tsx}'],

  // Files to exclude
  exclude: [],

  // Theme customisation
  theme: {
    extend: {
      tokens: {
        colors: {
          // Add your brand colors here
          // brand: { value: '#your-color' }
        },
      },
    },
  },

  // Output directory for generated CSS utilities
  outdir: 'styled-system',

  // JSX framework
  jsxFramework: 'react',
});
