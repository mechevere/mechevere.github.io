import { getCollection, type CollectionEntry } from 'astro:content';
export async function getLearnings() {
  const preview = import.meta.env.DEV || import.meta.env.INCLUDE_DRAFTS === 'true';
  return (await getCollection('writing', ({ data }) => preview || !data.draft))
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}
export function getTags(posts: CollectionEntry<'writing'>[]) {
  return [...new Set(posts.flatMap(post => post.data.tags))].sort();
}
export const tagUrl = (tag: string) => `/learnings/tags/${encodeURIComponent(tag)}/`;
