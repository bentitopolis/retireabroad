function loadComponent(elementId, componentPath) {
  fetch(componentPath)
    .then(response => response.text())
    .then(data => {
      document.getElementById(elementId).innerHTML = data;
    })
    .catch(error => console.error('Error loading component:', error));
}
document.addEventListener("DOMContentLoaded", () => {
  if(document.getElementById("global-header")) loadComponent("global-header", "components/header.html");
  if(document.getElementById("global-footer")) loadComponent("global-footer", "components/footer.html");
});
