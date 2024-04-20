export default function hasValuesFromArray(setToCheck, array) {
  for (const x of array) {
    if (!setToCheck.has(x)) {
      return false;
    }
  }
  return true;
}
