// console.log("working fine")
const usernameField = document.querySelector("#usernameField");


usernameField.addEventListener("keyup", (e) => {
  console.log("7777777", 7777777);

  const usernameVal = e.target.value;

  if (usernameVal.len > 0) {
    fetch("/authentication/validate-username", {
        body: JSON.stringify({ username: usernameVal }), 
        method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data",595959);
         
      });
    
  }
  
});