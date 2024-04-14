export default function guardrail(functionName) {
  const guardrailMsg = 'Guardrail was processed';
  const queue = [];

  try {
    queue.push(functionName());
  } catch (e) {
    queue.push(`${e.name}: ${e.message}`);
  }

  queue.push(guardrailMsg);
  return queue;
}
