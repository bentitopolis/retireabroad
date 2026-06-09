function loadComponent(elementId, componentPath) {
  fetch(componentPath)
    .then(response => response.text())
    .then(data => {
      document.getElementById(elementId).innerHTML = data;
    })
    .catch(error => console.error('Error loading component:', error));
}
document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("global-header")) loadComponent("global-header", "components/header.html");
  if (document.getElementById("global-footer")) loadComponent("global-footer", "components/footer.html");
  if (window.M) M.Sidenav.init(document.querySelectorAll('.sidenav'));
});

// 1. Firebase Configuration and Initialization
// API key protection is applied via console-level restrictions rather than configuration file edits.
const firebaseConfig = {
  apiKey: "AIzaSyCUHdjd9J1pa6mEytX_b2yq89TFvFj8k-s",
  authDomain: "turing-mark-445020-k1.firebaseapp.com",
  projectId: "turing-mark-445020-k1",
  storageBucket: "turing-mark-445020-k1.firebasestorage.app",
  messagingSenderId: "551955609502",
  appId: "1:551955609502:web:cc20feee804bb1dae3488f",
};

// Initialize Firebase and Firestore instances
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// 2. DOM Elements and Library Initializations
document.addEventListener('DOMContentLoaded', function () {

  // Initialize Materialize UI components
  if (window.M) {
    M.Sidenav.init(document.querySelectorAll('.sidenav'));
    M.CharacterCounter.init(document.querySelectorAll('#feedback'));
  }

  // Initialize AOS (Animate On Scroll) safely
  if (typeof AOS !== 'undefined') {
    AOS.init({ duration: 1000, once: true });
  }

  // 3. Feedback Form Submission Logic
  const form = document.getElementById('feedback-form');
  const btn = document.getElementById('submit-btn');
  const bar = document.getElementById('submit-progress');

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      // Validate form inputs
      if (!form.checkValidity()) {
        M.toast({ html: 'Please fill in the required fields.' });
        return;
      }

      // Honeypot field to prevent automated spam bots
      if (document.getElementById('company').value) return;

      // Disable button and show loading state
      btn.disabled = true;
      bar.style.display = 'block';

      const email = document.getElementById('email').value.trim();
      const feedback = document.getElementById('feedback').value.trim();

      // Prepare payload for Firestore
      const payload = {
        email: email,
        feedback: feedback,
        source: 'web-feedback',
        createdAt: firebase.firestore.FieldValue.serverTimestamp(),
      };

      try {
        // Submit data to Firestore collection
        await db.collection('retireabroad_web_feedback').add(payload);

        M.toast({ html: 'Thanks for your feedback! 🙏' });
        form.reset();

        // Redirect user to the Thank You page
        setTimeout(() => {
          window.location.href = 'thank_you.html';
        }, 700);
      } catch (err) {
        console.error('Firestore error:', err);
        M.toast({ html: 'Something went wrong. Please try again.' });
      } finally {
        // Restore button state and hide loading bar
        btn.disabled = false;
        bar.style.display = 'none';
      }
    });
  }
});

// 4. App Screenshots Slider Logic
let currentSlide = 0;
const totalSlides = 6;
const screenshots = [
  'assets/images/screenshots/events.png',
  'assets/images/screenshots/visa-tracker-1.png',
  'assets/images/screenshots/planner.png',
  'assets/images/screenshots/provinces.png',
  'assets/images/screenshots/itinerary.png',
  'assets/images/screenshots/living.png'
];

// Attach function to the global window object to allow inline HTML onclick triggers
window.changeSlide = function (direction) {
  // Hide current text description
  const currentTextSlide = document.getElementById(`slide-${currentSlide}`);
  if (currentTextSlide) {
    currentTextSlide.classList.remove('active');
  }

  // Calculate the next index, handling negative values for previous slide
  currentSlide = (currentSlide + direction + totalSlides) % totalSlides;

  // Show the next text description
  const nextTextSlide = document.getElementById(`slide-${currentSlide}`);
  if (nextTextSlide) {
    nextTextSlide.classList.add('active');
  }

  // Update image source with a smooth fade effect
  const imgElement = document.getElementById('current-img');
  if (imgElement) {
    imgElement.style.opacity = 0; // Trigger fade out

    setTimeout(() => {
      imgElement.src = screenshots[currentSlide]; // Swap image
      imgElement.style.opacity = 1; // Trigger fade in
    }, 200);
  }
};