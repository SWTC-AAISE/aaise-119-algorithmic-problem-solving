"use strict";
const records = [
  {id:"A", battery:70}, {id:"B", battery:50},
  {id:"C", battery:70}, {id:"D", battery:30}
];
function insertionSort(rows, key) {
  const ordered = [...rows];
  let comparisons = 0, moves = 0;
  for (let position = 1; position < ordered.length; position++) {
    const item = ordered[position];
    let previous = position - 1;
    while (previous >= 0) {
      comparisons++;
      if (key(ordered[previous]) <= key(item)) break;
      ordered[previous + 1] = ordered[previous];
      previous--;
      moves++;
    }
    ordered[previous + 1] = item;
  }
  return {ordered, comparisons, moves};
}
function run() {
  const traced = insertionSort(records, row => row.battery);
  const libraryCopy = [...records].sort((a, b) => a.battery - b.battery);
  const mutatingExample = [...records];
  const returned = mutatingExample.sort((a, b) => a.battery - b.battery);
  document.getElementById("result").textContent = JSON.stringify({
    original: records.map(row => row.id),
    insertion: traced.ordered.map(row => row.id),
    comparisons: traced.comparisons, shifts: traced.moves,
    libraryCopy: libraryCopy.map(row => row.id),
    sortReturnsSameArray: returned === mutatingExample,
    sortedWorkingArray: mutatingExample.map(row => row.id)
  }, null, 2);
}
document.getElementById("run").addEventListener("click", run);
run();
