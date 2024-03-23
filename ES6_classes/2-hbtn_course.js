// Implement a class named <HolbertonCourse>
export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // Getter for the name property
  get name() {
    return this._name;
  }

  // Setter for <name>
  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Getter for number
  get length() {
    return this._number;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._number = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (!Array.isArray(value) || value.some((v) => typeof v !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
