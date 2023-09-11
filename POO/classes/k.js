function test(...args) {
  return a(...args);
}

function a(...args) {
  for (const arg of args) {
    console.log(arg);
  }
}
