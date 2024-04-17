export default function getStudentIdsSum(listStudents) {
  const arrayIndexes = listStudents.map((x) => x.id);
  const sumOfIdx = arrayIndexes.reduce((accumulator, currentValue) => accumulator + currentValue);

  return sumOfIdx;
}
