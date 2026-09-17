import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';
export const collections = {writing: defineCollection({loader:glob({pattern:'**/*.md',base:'./src/content/writing'}),schema:z.object({title:z.string(),description:z.string(),date:z.coerce.date(),tags:z.array(z.string().trim().toLowerCase().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/, "Use lowercase words separated by hyphens")).default([]).transform(tags => [...new Set(tags)]),draft:z.boolean().default(true)})})};
