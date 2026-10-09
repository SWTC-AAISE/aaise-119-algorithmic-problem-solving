"use strict";
const records = [
  {id:"E01", type:"laptop", available:true, battery:80},
  {id:"E02", type:"tablet", available:true, battery:50},
  {id:"E03", type:"laptop", available:false, battery:90},
  {id:"E04", type:"laptop", available:true, battery:50}
];
function select(rows, predicates) {
  return rows.filter(row => predicates.every(predicate => predicate(row)));
}
function run() {
  const threshold = Number(document.getElementById("minimum").value);
  const laptopsOnly = document.getElementById("laptops").checked;
  if (!Number.isInteger(threshold) || threshold < 0 || threshold > 100) {
    document.getElementById("result").textContent = "Battery must be an integer from 0 through 100.";
    return;
  }
  const rules = [row => row.available, row => row.battery >= threshold];
  if (laptopsOnly) rules.push(row => row.type === "laptop");
  document.getElementById("result").textContent = JSON.stringify({
    selected: select(records, rules).map(row => row.id),
    emptyCriteria: select(records, []).map(row => row.id)
  }, null, 2);
}
document.getElementById("controls").addEventListener("submit", event => {
  event.preventDefault();
  run();
});
run();
