export default function getListStudentIds(arrayIds) {
  if (!Array.isArray(arrayIds)) {
    return [];
  }
  return arrayIds.map((x) => x.id);
}
