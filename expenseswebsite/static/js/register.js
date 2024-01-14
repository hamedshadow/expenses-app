// console.log("working fine")


const usernameField = document.querySelector("#usernameField");
const feedbackArea = document.querySelector(".invalid-feedback");

usernameField.addEventListener("keyup", (e) => {
  console.log("7777777", 7777777);
  
  const usernameVal = e.target.value;
  console.log(`${usernameVal}`);

  usernameField.classList.remove('is-invalid');
  feedbackArea.style.display="none";
 

  if (`${usernameVal.length}` > 0) {
    fetch("/authentication/validate-username", {
      body: JSON.stringify({ username: `${usernameVal}` }), 
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if(data.username_error){
            usernameField.classList.add('is-invalid');
            feedbackArea.style.display="block";
            feedbackArea.innerHTML=`<p>${data.username_error}</p>`;
        }
         
      });
    // console.log(`${usernameVal.length}`);
  }
  
});