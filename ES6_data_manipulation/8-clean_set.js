// Create a function named <<cleanSet>> that returns a string of all the set values
//    that start with a specific string
// Accepts two arguments
// When a value starts with <<startString>> you only append the rest of the string
export default function cleanSet(setToCheck, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const setToClean = setToCheck;
  const listResult = [];
  for (const elem of setToClean) {
    if (elem.startsWith(startString)) {
      listResult.push(elem.substr(startString.length));
    }
  }
  return listResult.join('-');
}
