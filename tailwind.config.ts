import containerQueries from '@tailwindcss/container-queries';
import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';
import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {
      colors: {
        'custom-green': '#E9EED9',
        'custom-blue' : '#213555', 
        'custom-brown' : '#493628',
        'custom-dark-brown': '#3B2A21',
        'custom-teal': '#637E76',
        'dark-teal': '#006A67',
        'custom-orange': '#FFAD60',
        'custom-light-orange': '#FBD288',
        'iris': '#F3CCFF'
      },
    }
  },

  plugins: [typography, forms, containerQueries]
} satisfies Config;
