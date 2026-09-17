import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';
const readingList = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/reading-list' }),
  schema: z.object({
    title: z.string().trim().min(1),
    url: z.url().refine(value => ['http:', 'https:'].includes(new URL(value).protocol), 'Use an HTTP or HTTPS link'),
  }),
});
export const collections = {readingList, writing: defineCollection({loader:glob({pattern:'**/*.md',base:'./src/content/writing'}),schema:z.object({title:z.string(),description:z.string(),date:z.coerce.date(),tags:z.array(z.string().trim().toLowerCase().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/, "Use lowercase words separated by hyphens")).default([]).transform(tags => [...new Set(tags)]),draft:z.boolean().default(true)})})};
