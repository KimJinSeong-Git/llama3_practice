<template>
  <div id="app">
    <div class="chat-container">
      <div class="chat-header">
        <div class="avatar"><img src="https://via.placeholder.com/50" alt="Avatar"></div>
        <div class="title">ChatGPT</div>
      </div>
      <div class="chat-body">
        <div v-for="(message, index) in messages" :key="index" :class="message.type">
          <div class="message-content">{{ message.content }}</div>
        </div>
      </div>
      <div class="chat-footer">
        <input v-model="newMessage" @keyup.enter="sendMessage" type="text" placeholder="Type your message...">
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      messages: [],
      newMessage: ""
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== "") {
        this.messages.push({ content: this.newMessage, type: 'user' });
        this.newMessage = "";
        this.reply();
      }
    },
    reply() {
      // Mock reply from ChatGPT
      setTimeout(() => {
        this.messages.push({ content: "This is a reply from ChatGPT.", type: 'bot' });
      }, 500);
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.chat-container {
  max-width: 400px;
  margin: 50px auto;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.chat-header {
  background-color: #007bff;
  color: #fff;
  padding: 15px;
  display: flex;
  align-items: center;
}

.chat-header .avatar img {
  border-radius: 50%;
  margin-right: 10px;
}

.chat-body {
  padding: 15px;
  max-height: 300px;
  overflow-y: auto;
}

.chat-body .message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}

.chat-body .user {
  background-color: #007bff;
  color: #fff;
  align-self: flex-end;
}

.chat-body .bot {
  background-color: #f4f4f4;
  color: #333;
}

.chat-footer {
  background-color: #f9f9f9;
  padding: 15px;
  display: flex;
}

.chat-footer input {
  flex: 1;
  padding: 10px;
  border: none;
  border-radius: 5px;
  margin-right: 10px;
}

.chat-footer button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}
</style>
