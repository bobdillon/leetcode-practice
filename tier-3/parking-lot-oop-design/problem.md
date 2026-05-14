# Parking Lot — OOP System Design

**Type:** Original system design prompt (no LeetCode number)  
**Topic:** OOP Design, Class Hierarchy, State Management

## Prompt

Design an object-oriented parking lot system.

Your design should support:

1. **Multiple vehicle types** — e.g. motorcycle, car, truck. Each type occupies a different number/size of spots.
2. **Multiple spot types** — e.g. compact, regular, large. A vehicle can only park in a spot that fits it (or larger, if policy allows).
3. **Spot allocation** — when a vehicle enters, find and assign an available spot. Return a ticket or raise an error if full.
4. **Entry and exit flow** — vehicle checks in, receives a ticket; on exit, ticket is used to locate and free the spot.
5. **Payment** — calculate the fee based on time parked. Support at least one pricing strategy (e.g. flat hourly rate).
6. **Capacity tracking** — at any point, report how many spots of each type remain.

## Discussion Points

- What classes do you define, and what are their responsibilities?
- How do you model the relationship between vehicle types and spot types?
- Where does pricing logic live — on the ticket, a separate `PricingStrategy`, or the lot itself?
- How would you extend this to multiple floors or multiple lots?
- What are the tradeoffs of your allocation algorithm (first available vs. nearest to entrance)?
- How would you handle concurrency if this were a real system?

## Constraints (for the exercise)

- Implement in Python, 30-50 lines of core OOP skeleton
- No execution required — focus on class design and articulating tradeoffs out loud
- Talk through every design decision before coding it
