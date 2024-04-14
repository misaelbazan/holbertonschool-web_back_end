export default function guardrail(functionName) {
  const guardrailMsg = 'Guardrail was processed';
  const queue = [];

  try {
    queue.push(functionName());
  } catch (e) {
    queue.push(e);
  }

  queue.push(guardrailMsg);
  return queue;
}
