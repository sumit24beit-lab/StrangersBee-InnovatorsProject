// Toggle Chatboxes
document.querySelector('.advisor-btn').onclick = () => {
  document.querySelector('.advisor-box').classList.toggle('active');
  document.querySelector('.advisor-box').style.display =
    document.querySelector('.advisor-box').style.display === 'flex' ? 'none' : 'flex';
};

document.querySelector('.order-btn').onclick = () => {
  document.querySelector('.order-box').classList.toggle('active');
  document.querySelector('.order-box').style.display =
    document.querySelector('.order-box').style.display === 'flex' ? 'none' : 'flex';
};

// Advisor Bot Logic
function sendAdvisorMessage() {
  let input = document.getElementById("advisor-input");
  let msg = input.value.trim();
  if (!msg) return;
  appendChat("advisor-chat", "You: " + msg);
  input.value = "";
  let reply = "I'm your Smart Advisor! Try asking about today's offers or menu.";
  if (msg.toLowerCase().includes("menu")) reply = "Today's popular dishes: Misal Pav, Vada Pav, Pav Bhaji 🍛";
  if (msg.toLowerCase().includes("offer")) reply = "25% off on all Maharashtrian thalis today!";
  appendChat("advisor-chat", "Bot: " + reply);
}

// Order Bot Logic
function sendOrderMessage() {
  let input = document.getElementById("order-input");
  let msg = input.value.trim();
  if (!msg) return;
  appendChat("order-chat", "You: " + msg);
  input.value = "";
  let reply = "You can track your order using your Order ID.";
  if (msg.toLowerCase().includes("track")) reply = "Your order is being prepared 🍳 and will arrive in 25 minutes!";
  appendChat("order-chat", "Bot: " + reply);
}

// Helper to append messages
function appendChat(containerId, text) {
  let container = document.getElementById(containerId);
  let p = document.createElement("p");
  p.textContent = text;
  container.appendChild(p);
  container.scrollTop = container.scrollHeight;
}                                                                                                                                                                                                                     // --- Existing code above remains same --- //


// --- Welcome Popups --- //
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
  setTimeout(() => orderPopup.remove(), 6000);
}