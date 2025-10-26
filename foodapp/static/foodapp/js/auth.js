// auth.js - simple client-only signup & login flow (prototype)
document.addEventListener('DOMContentLoaded', () => {
  const toSignup = document.getElementById('toSignup');
  const toLogin = document.getElementById('toLogin');

  if (toSignup) toSignup.addEventListener('click', () => location.href = '/signup/');
  if (toLogin) toLogin.addEventListener('click', () => location.href = '/login/');

  const signupForm = document.getElementById('signupForm');
  if (signupForm){
    signupForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('suName').value.trim();
      const email = document.getElementById('suEmail').value.trim();
      const pass = document.getElementById('suPass').value;
      const pass2 = document.getElementById('suPass2').value;
      const tc = document.getElementById('tcCheck').checked;
      if (!tc) return alert('Please accept Terms & Conditions');
      if (pass !== pass2) return alert('Passwords do not match');
      // Save to localStorage (prototype)
      localStorage.setItem('oc_user', JSON.stringify({name,email}));
      // show spoons animation small overlay then redirect to home
      localStorage.setItem('oc_logged_in', '1');
      window.location.href = '/'; // will trigger spoon overlay handled by main.js
    });
  }

  const loginForm = document.getElementById('loginForm');
  if (loginForm){
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim();
      const pass = document.getElementById('loginPass').value;
      // naive check: if oc_user exists, allow; else allow anyway (prototype)
      const usr = localStorage.getItem('oc_user');
      localStorage.setItem('oc_logged_in', '1');
      window.location.href = '/';
    });
  }
});
