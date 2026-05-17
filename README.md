# Building with the Claude API

This is a follow-along of the [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) course by Anthropic.

My main takeaways from this course are:
- the importance of having a prompt evaluation strategy to systematically improve prompts
- the use of start and stop sequences to guide the model to produce a specific format
- the use of XML tags to delimit sections

## Lessons Learned

- [API](/01-api/LESSONS.md)
- [Prompt Evaluation](/02-prompt-evaluation/LESSONS.md)
- [Prompt Engineering](/03-prompt-engineering/LESSONS.md)
- [RAG](/05-rag/LESSONS.md)
- [Features](/06-features/LESSONS.md)
- [Claude Code](/08-claude-code/LESSONS.md)
- [Agents and Workflows](/09-agents-and-workflows/LESSONS.md)

## Cost

The course itself is free, but accessing the API is not. Completing the course with little deviation from the content cost $1.15. The highest contribution to this came from the use of the code execution feature, costing $0.72.

![Claude API Course Cost](/assets/claude-api-course-cost.png)

Apparently there is a free tier, but it has lower limits. I haven't seen it advertised anywhere; that's why I went with the $5 plan. The credits expire after one year.

A positive impression from the Claude Console is that the spend limit is honored. The request that exceeds the limit still finishes without getting interrupted, but subsequent requests receive a rate limit response.

![Claude API Limits](/assets/claude-api-limits.png)