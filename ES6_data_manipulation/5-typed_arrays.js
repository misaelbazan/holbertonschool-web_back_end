export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position > 255) {
    throw new Error('Position outside range');
  }
  const arrayBuff = new ArrayBuffer(length);
  const arrayTyped = new Int8Array(arrayBuff);

  arrayTyped[position] = value;

  return arrayBuff;
}
