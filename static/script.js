document.getElementById('churnForm').onsubmit = async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const res = await fetch('/predict_churn', {method: 'POST', body: formData});
  const data = await res.json();
  document.getElementById('result').innerText = data.result || data.error;
};
