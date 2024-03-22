import ClassRooms from "./0-classroom.js";

function initializeRooms() {
  const classRoom1 = new ClassRooms(19);
  const classRoom2 = new ClassRooms(20);
  const classRoom3 = new ClassRooms(34);

  const arrayClass = [classRoom1, classRoom2, classRoom3];

  return arrayClass;
}

export default initializeRooms;
