const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const chatBox = document.querySelector(".chatbox");
const chatbotToggler = document.querySelector(".chatbot-toggler");
const chatbotCloseBtn = document.querySelector(".close-btn");


/*
let userMessage;
const inputInitHeight = chatInput.scrollHeight;
const createChatLi = (message, className) => {
    // create a chat <li> element with passed message and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi;
}

const handleChat = () => {
    userMessage = chatInput.value.trim();
    if (!userMessage) return;
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;


    //Append the chat message
    chatBox.appendChild(createChatLi(userMessage, "outgoing"));
    chatBox.scrollTo(0, chatBox.scrollHeight);
    setTimeout(() => {
        chatBox.appendChild(createChatLi("Typing...", "incoming"));
        chatBox.scrollTo(0, chatBox.scrollHeight);
    }, 500);
}

chatInput.addEventListener("input", () => {
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

});

//sendChatBtn.addEventListener("click", handleChat);
*/


chatbotCloseBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));

function send_message() {
    console.log(flag,"flag");

    let message = document.getElementById("text_context").value;
    if(flag===1){
        $.ajax({
        type: 'POST',
        url: 'send_message',
        data: {
            message: message,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            console.log("success");
        }
    });
    document.getElementById("text_context").value = "";
    }
    else{
        temp = "<li class='chat outgoing' style='margin-left: 73%'> <p>" + message + "</p> <span class='material-symbols-outlined'>face</span> </li><br>";
        answer.append(message);
        $("#chatbox").append(temp);
        sending();

    }

}