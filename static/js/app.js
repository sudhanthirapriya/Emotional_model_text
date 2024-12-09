document.addEventListener("DOMContentLoaded", () => {
    const chatbox = document.getElementById("chatbox");
    const userInput = document.getElementById("userInput");
    const sendBtn = document.getElementById("sendBtn");

    sendBtn.addEventListener("click", async () => {
        const message = userInput.value.trim();
        if (!message) return;

        // Display user message
        addMessage("You", message, "chat-user");

        // Clear input
        userInput.value = "";

        // Call the API
        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: message }),
            });
            const data = await response.json();

            // Display bot response
            addMessage("Bot", data.response, "chat-bot");
        } catch (error) {
            addMessage("Bot", "Sorry, something went wrong.", "chat-bot");
        }
    });

    function addMessage(sender, message, className) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("chat-message", className);
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatbox.appendChild(messageElement);
        chatbox.scrollTop = chatbox.scrollHeight;
    }
});
