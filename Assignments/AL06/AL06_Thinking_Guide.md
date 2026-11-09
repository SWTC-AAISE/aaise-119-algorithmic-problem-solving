# AL06 Thinking Guide: Why Recursion Fits

Optional support. Read only your chosen scenario if it helps. No written response
is required. These examples explain the reasoning; your implementation and tests
remain your work.

## Fundraiser Tracker

“I want to know how much money we have actually received. A campaign can contain
individual donations, teams, and smaller groups within those teams. Counting only
the first level would miss donations. Adding every recorded amount would count
pledges as money already available. An individual received donation contributes
its amount; a pledge is still a valid record, but contributes nothing to this total.”

“I can ask each team the same question: how much have you received? A team can
ask its smaller groups that question and combine their answers with its own
individual donations. Eventually each question reaches a donation or an empty
group, where the answer is straightforward. Recursion fits because every nested
group presents the same kind of problem, however many levels there are.”

## Project Effort Estimator

“I need the hours of work still remaining, rather than every hour ever estimated.
A project contains tasks and groups of tasks, and some groups contain smaller
groups. An unfinished task contributes its estimated hours. A finished task adds
nothing to remaining work. The grouping itself does not represent extra hours:
counting a group's combined answer again as separate work would double-count it.”

“I can ask each group how much unfinished work it contains. Its answer combines
individual unfinished tasks with the answers from its smaller groups. The same
question works for the whole project and for a deeply nested subgroup. Eventually
there is only an individual task to consider, or an empty group with no remaining
hours. Recursion lets the structure of the reasoning follow the project structure.”

## Inventory Counter

“I need a usable-stock count. A storage location can contain individual stock
records and smaller locations or containers. Damaged stock remains in the records
because it matters to the business, but it is not available for use. A usable entry
contributes its quantity; a damaged entry contributes nothing to this particular
answer. An empty location has no stock to contribute.”

“I can ask each location how many usable items it holds, including its smaller
locations. Each smaller location answers the same question until the reasoning
reaches individual stock records. Combining those answers produces the whole
location's usable count without assuming a fixed number of nesting levels. That
repeated question is why recursion is useful here; an explicit stack is another
way to keep track of the locations still waiting to be examined.”
