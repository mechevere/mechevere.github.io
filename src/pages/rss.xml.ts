import rss from '@astrojs/rss';
import {getCollection} from 'astro:content';
export async function GET(context:any){const posts=await getCollection('writing',({data})=>!data.draft);return rss({title:'Mateo Echeverri',description:'Learnings by Mateo Echeverri.',site:context.site,items:posts.map(p=>({title:p.data.title,description:p.data.description,pubDate:p.data.date,link:`/learnings/${p.id}/`}))});}
