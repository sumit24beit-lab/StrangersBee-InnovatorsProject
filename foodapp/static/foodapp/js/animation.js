// animation.js - plays cook -> rider -> message animation, then redirects home
document.addEventListener('DOMContentLoaded', ()=>{
  const chef = document.getElementById('chef');
  const rider = document.getElementById('rider');
  const msg = document.getElementById('msg');

  // start sequence
  setTimeout(()=> {
    // chef slides in from left a bit
    chef.style.left = '40px';
    setTimeout(()=> {
      // pretend to cook (small bob)
      chef.style.transform = 'translateY(-6px)';
      setTimeout(()=> {
        chef.style.transform = 'translateY(0)';
        // rider enters fast
        rider.style.left = '-100px';
        rider.style.transition = 'all 1s linear';
        setTimeout(()=> {
          rider.style.left = '110%';
          // show message after rider crosses
          setTimeout(()=> {
            msg.classList.add('show');
            // after 2s redirect to home
            setTimeout(()=> {
              window.location.href = '/';
            },2000);
          },900);
        },300);
      },900);
    },800);
  },300);
});
