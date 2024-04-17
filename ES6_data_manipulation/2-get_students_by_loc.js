export default function getStudentsByLocation(arrayLoc, city) {
  if (!Array.isArray(arrayLoc)) {
    return [];
  }
  return arrayLoc.filter((x) => (x.location === city));
}
