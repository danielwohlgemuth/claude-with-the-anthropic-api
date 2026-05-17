# Agent and Workflows

## Evaluator-Optimizer Workflow Pattern

- A producer creates an output
- A grader evaluates the output against the criteria and either accepts it or rejects it with feedback

```mermaid
flowchart TD
    start((Start))
    produce[Produce]
    grade{Grade}
    stop((Stop))

    start -->|Input| produce
    produce -->|Output| grade
    grade -->|Accepted| stop
    grade -->|Rejected with feedback| produce
```

## Parallelization

Instead of having a single large prompt that contains multiple criteria, it can be split into multiple smaller prompts that can be processed in parallel and aggregated at the end.

```mermaid
flowchart TD
    start((Start))
    process_a[Process A]
    process_b[Process B]
    aggregate[Aggregate]
    stop((Stop))

    start -->|Input| process_a
    start -->|Input| process_b
    process_a -->|Output A| aggregate
    process_b -->|Output B| aggregate
    aggregate -->|Final Output| stop
```

## Chaining

Similar to parallelization, this approach breaks large tasks into smaller steps, but processes them sequentially instead of in parallel.

```mermaid
flowchart TD
    start((Start))
    process_a[Process A]
    process_b[Process B]
    stop((Stop))

    start -->|Input| process_a
    process_a -->|Output A| process_b
    process_b -->|Output B| stop
```

## Routing

The input is first classified into a category and then forwarded to a pipeline with category-specific prompts and tools.

```mermaid
flowchart TD
    start((Start))
    classify{Classify}
    process_a[Process A]
    process_b[Process B]
    stop((Stop))

    start -->|Input| classify
    classify -->|Route A| process_a
    classify -->|Route B| process_b
    process_a -->|Output A| stop
    process_b -->|Output B| stop
```