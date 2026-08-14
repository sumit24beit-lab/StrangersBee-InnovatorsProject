function redirectToHome() {
  const animation = document.querySelector(".loader");
  if (!animation) { 
    window.location.href = "/home";
    return;
  }
  animation.style.opacity = "1";
  animation.style.pointerEvents = "auto";

  setTimeout(() => {
    window.location.href = "/home";
  }, 2700);
}

// auth.js - simple client-only signup & login flow (prototype)
document.addEventListener('DOMContentLoaded', () => {
  const toSignup = document.getElementById('toSignup');
  const toLogin = document.getElementById('toLogin');
  const logoutBtn = document.getElementById('logoutBtn');

  if (toSignup) toSignup.addEventListener('click', () => location.href = '/signup');
  if (toLogin) toLogin.addEventListener('click', () => location.href = '/login');
  
  // --- Logout Functionality ---
  if (logoutBtn) {
    logoutBtn.addEventListener('click', (e) => {
      e.preventDefault();
      localStorage.removeItem('oc_logged_in');
      localStorage.removeItem('oc_user');
      alert('You have been logged out successfully!');
      window.location.href="/login";
    });
  }

  // --- Already Logged In Check (for login/signup pages only) ---
  const isLoginPage = window.location.pathname.endsWith('login.html');
  const isSignupPage = window.location.pathname.endsWith('signup.html');
  const loggedIn = localStorage.getItem('oc_logged_in') === '1';

  if (loggedIn && (isLoginPage || isSignupPage)) {
    alert('You are already logged in!');
    window.location.href="/home";
    return;
  }

  /* ----------------- Sign Up ------------------*/
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
      localStorage.setItem('oc_user', JSON.stringify({name,email,pass}));
      // show spoons animation small overlay then redirect to home
      localStorage.setItem('oc_logged_in', '1');
      redirectToHome(); // will trigger spoon overlay handled by main.js
    });
  }

  /* ----------------- Sign Up ------------------*/
  const loginForm = document.getElementById('loginForm');
  if (loginForm){
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim();
      const pass = document.getElementById('loginPass').value;
      // naive check: if oc_user exists, allow; else allow anyway (prototype)
      const usr = JSON.parse(localStorage.getItem('oc_user') || '{}');
      if (usr.email === email) {
      localStorage.setItem('oc_logged_in', '1');
      alert('Login successful!');
      redirectToHome();
      } else {
      alert('User not found. Please sign up first.');
      }
    });
  }
});
