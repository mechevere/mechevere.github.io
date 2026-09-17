import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
export default defineConfig({site:'https://mechevere.github.io', trailingSlash:'always', integrations:[sitemap()], markdown:{shikiConfig:{theme:'github-light'}}, devToolbar:{enabled:false}});
