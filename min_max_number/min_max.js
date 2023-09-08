function min(tableau) {
  if (
    Array.isArray(tableau) &&
    tableau.every(function (element) {
      return typeof element === 'number';
    }) &&
    tableau.length > 0
  ) {
    let min = tableau[0];
    for (const nombre of tableau) {
      if (nombre < min) {
        min = nombre;
      }
    }
    return min;
  }

  return -1;
}

function max(tableau) {
  if (
    Array.isArray(tableau) &&
    tableau.every(function (element) {
      return typeof element === 'number';
    }) &&
    tableau.length > 0
  ) {
    let max = tableau[0];
    for (const nombre of tableau) {
      if (nombre > min) {
        max = nombre;
      }
    }
    return max;
  }

  return -1;
}

function min_max(tableau) {
  return [min(tableau), max(tableau)];
}

const arr1 = ['kjfjkdkjs', -1000, 2, -100];

console.log(min(arr1), max(arr1));
console.log(min_max(arr1));
