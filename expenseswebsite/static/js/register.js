// console.log("working fine")


const usernameField = document.querySelector("#usernameField");
const feedbackArea = document.querySelector(".invalid-feedback");
const emailField = document.querySelector("#emailField");
const passwordField = document.querySelector("#passwordField");
const emailFeedbackArea = document.querySelector(".emailFeedbackArea");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitBtn = document.querySelector(".submit-btn")




const handleToggleInput = (e) => {
    // console.log(e);
    if (showPasswordToggle.textContent === "SHOW") {
        showPasswordToggle.textContent = "HIDE";
        passwordField.setAttribute("type", "text");
    } else {
        showPasswordToggle.textContent = "SHOW";
        passwordField.setAttribute("type", "password");
    }
};

showPasswordToggle.addEventListener("click", handleToggleInput);


emailField.addEventListener("keyup", (e) => {
    console.log("email", 12345);
    const emailVal = e.target.value;

    emailField.classList.remove('is-invalid');
    emailFeedbackArea.style.display = "none";


    if (`${emailVal.length}` > 0) {
        fetch("/authentication/validate-email", {
                body: JSON.stringify({ email: `${emailVal}` }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                if (data.email_error) {
                    submitBtn.disabled = true;
                    emailField.classList.add('is-invalid');
                    emailFeedbackArea.style.display = "block";
                    emailFeedbackArea.innerHTML = `<p>${ data.email_error }</p>`;
                } else {

                    submitBtn.removeAttribute("disabled");
                }

            });
        // console.log(`${usernameVal.length}`);
    } 

});





usernameField.addEventListener("keyup", (e) => {
    console.log("7777777", 7777777);

    const usernameVal = e.target.value;
    console.log(`${usernameVal}`);
    usernameSuccessOutput.style.display = "block";
    usernameSuccessOutput.textContent = `Checking  ${usernameVal}`;
    usernameField.classList.remove('is-invalid');
    feedbackArea.style.display = "none";


    if (`${usernameVal.length}` > 0) {
        fetch("/authentication/validate-username", {
                body: JSON.stringify({ username: `${usernameVal}` }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                // console.log("data", data);
                usernameSuccessOutput.style.display = "none";
                if (data.username_error) {
                    usernameField.classList.add('is-invalid');
                    feedbackArea.style.display = "block";
                    feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
                    submitBtn.disabled = true;
                } else {
                    submitBtn.removeAttribute("disabled");
                }

            });
        // console.log(`${usernameVal.length}`);
    } 

});