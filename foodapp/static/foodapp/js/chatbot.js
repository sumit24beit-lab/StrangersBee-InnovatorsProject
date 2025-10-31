// Toggle open/close
function toggleChat(id) {
  document.querySelectorAll('.chat-window').forEach(win => {
    if (win.id !== id) win.classList.add('hidden');
  });
  document.getElementById(id).classList.toggle('hidden');
}

// Send user message + simple bot reply
function sendMsg(botType) {
  const input = document.getElementById(`${botType}-input`);
  const body = document.getElementById(`${botType}-body`);
  const text = input.value.trim();
  if (!text) return;

  const userMsg = document.createElement('div');
  userMsg.className = 'user-msg';
  userMsg.textContent = text;
  body.appendChild(userMsg);
  input.value = '';

  // Simple responses
  let reply = '';
  if (botType === 'advisor') {
    if (text.toLowerCase().includes('menu')) reply = 'We have 50+ delicious items 🍽️';
    else if (text.toLowerCase().includes('offer')) reply = 'Today: Flat 20% off on orders above ₹299 🎉';
    else if (text.toLowerCase().includes('thanks')) reply = 'You’re welcome! 😊';
    else reply = 'Let me check that for you!';
  } else {
    if (text.toLowerCase().includes('track')) reply = 'Your order is out for delivery 🚚';
    else if (text.toLowerCase().includes('cancel')) reply = 'Order canceled successfully ✅';
    else if (text.toLowerCase().includes('modify')) reply = 'Please specify your changes.';
    else reply = 'I can assist with tracking or modifying orders!';
  }

  const botMsg = document.createElement('div');
  botMsg.className = 'bot-msg';
  botMsg.textContent = reply;
  setTimeout(() => body.appendChild(botMsg), 500);

  body.scrollTop = body.scrollHeight;
}

window.addEventListener("load", () => {
  setTimeout(showAdvisorWelcome, 5000); // after 5 sec
  setTimeout(showOrderWelcome, 8000);   // after 8 sec
});

function showAdvisorWelcome() {
  const advisorPopup = document.createElement("div");
  advisorPopup.className = "chat-popup red";
  advisorPopup.innerHTML = "👋 Hi there! Want to explore today's food offers?";
  document.body.appendChild(advisorPopup);
  setTimeout(() => advisorPopup.remove(), 6000);
}

function showOrderWelcome() {
  const orderPopup = document.createElement("div");
  orderPopup.className = "chat-popup black";
  orderPopup.innerHTML = "🚴 Need help tracking your order?";
  document.body.appendChild(orderPopup);
  setTimeout(() => orderPopup.remove(), 6000);
}