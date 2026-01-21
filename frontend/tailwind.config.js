/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'pastel-bg': '#e6e0d4',     // Even Darker Cream/Beige for contrast
                'pastel-card': '#ffffff',   // White
                'pastel-accent': '#D81B60', // High-Visibility Pink
                'pastel-text': '#333333',   // Dark Charcoal
                'pastel-muted': '#64748b',  // Slate Gray
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },
            animation: {
                'scan': 'scan 4s linear infinite',
            },
            keyframes: {
                scan: {
                    '0%': { top: '0%' },
                    '100%': { top: '100%' },
                }
            }
        },
    },
    plugins: [],
}
