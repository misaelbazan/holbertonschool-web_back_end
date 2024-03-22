import ClassRooms from "./0-classroom.js";

function initializeRooms() {
  const class_room1 = new ClassRooms(19);
  const class_room2 = new ClassRooms(20);
  const class_room3 = new ClassRooms(34);

  const array_class = [class_room1, class_room2, class_room3];

  return array_class;
}

export default initializeRooms;
