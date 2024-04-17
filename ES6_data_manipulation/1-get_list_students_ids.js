export default function getListStudentsIds(arrayIds) {
  if (!Array.isArray(arrayIds)) {
    return [];
  }
  return arrayIds.map((x) => x.id);
}
