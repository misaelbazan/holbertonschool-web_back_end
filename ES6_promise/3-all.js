import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promise1 = uploadPhoto();
  const promise2 = createUser();

  Promise.all([promise1, promise2])
    .then((values) => {
      const photoBody = values[0].body;
      const firstNameUser = values[1].firstName;
      const lastNameUser = values[1].lastName;
      console.log(`${photoBody}, ${firstNameUser}, ${lastNameUser}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
