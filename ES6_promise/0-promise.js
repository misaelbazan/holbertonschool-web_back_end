// Return a Promise
export default function getResponseFromAPI() {
	const myPromise = new Promise((resolve, reject) => {
		resolve('Success');
	});
	return myPromise;
}
