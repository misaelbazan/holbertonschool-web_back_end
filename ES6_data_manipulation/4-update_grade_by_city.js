export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  const filteredLoc = studentsList.filter((x) => x.location === city);

  newGrades.forEach(({ studentId, grade }) => {
    filteredLoc.forEach((student) => {
      if (student.id === studentId) {
        student.grade = grade;
      }
      if (student.grade === undefined) {
        student.grade = 'N/A';
      }
    });
  });

  return filteredLoc;
}
