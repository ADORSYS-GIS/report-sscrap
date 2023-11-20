document.addEventListener("DOMContentLoaded", function() {
  const analyzeButton = document.getElementById("mybutton");

  analyzeButton.addEventListener("click", analysisbuttton);

  function analysisbuttton() {
    fetch("/api/start-analysis", {
      method: "POST",
    })
      .then(response => {
        if (response.ok) {
          window.location.href="/api/start-analysis"
          console.log("Data analysis initiated.");
        } else {
          console.error("Failed to initiate data analysis.");
        }
      })
      .catch(error => {
        console.error("An error occurred during data analysis initiation:", error);
      });
    return null;
  }
});