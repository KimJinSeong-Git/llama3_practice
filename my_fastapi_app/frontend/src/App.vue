<template>
  <div id="app">
    <header class="header">
      <div class="logo" @click="goToHomePage">
        <img src="https://via.placeholder.com/50" alt="AIS Paper Factory Logo">
        <span>AIS Paper Factory</span>
      </div>
      <div class="login-form">
        <input type="text" placeholder="ID" v-model="loginId">
        <input type="password" placeholder="PW" v-model="loginPw">
        <button @click="login">Login</button>
      </div>
    </header>
    <div class="main-container">
      <div class="sidebar">
        <button @click="newChat">New Chat</button>
        <ul>
          <li v-for="(chat, index) in chats" :key="index" @click="selectChat(index)" :class="{ active: currentChatIndex === index }">
            Chat {{ index + 1 }}
          </li>
        </ul>
      </div>
      <div class="content">
        <div v-if="currentPage === 'home'">
          <h1>Home Page</h1>
          <form @submit.prevent="submitForm">
            <div>
              <label for="name">Name:</label>
              <input type="text" id="name" v-model="form.name">
            </div>
            <div>
              <label for="email">Email:</label>
              <input type="email" id="email" v-model="form.email">
            </div>
            <div>
              <label for="message">Message:</label>
              <textarea id="message" v-model="form.message"></textarea>
            </div>
            <button type="submit">Submit</button>
          </form>
        </div>
        <div v-else-if="currentPage === 'chat'">
          <div class="chat-container">
            <div class="chat-header">
              <div class="avatar"><img src="https://via.placeholder.com/50" alt="Avatar"></div>
              <div class="title">Based on Llama3-8B</div>
            </div>
            <div class="chat-body" ref="chatBody">
              <div v-for="(message, index) in currentChat.messages" :key="index" :class="['message', message.type]">
                <div class="message-content">{{ message.content }}</div>
              </div>
            </div>
            <div class="chat-footer">
              <input v-model="newMessage" @keyup.enter="sendMessage" type="text" :disabled="isBotReplying" placeholder="Type your message...">
              <button @click="sendMessage" :disabled="isBotReplying">Send</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      chats: [
        { messages: [] }
      ],
      currentChatIndex: 0,
      newMessage: "",
      isBotReplying: false,
      currentPage: 'home',
      loginId: '',
      loginPw: '',
      form: {
        name: '',
        email: '',
        message: ''
      }
    };
  },
  computed: {
    currentChat() {
      return this.chats[this.currentChatIndex];
    }
  },
  methods: {
    newChat() {
      this.chats.push({ messages: [] });
      this.currentChatIndex = this.chats.length - 1;
      this.currentPage = 'chat';
    },
    selectChat(index) {
      this.currentChatIndex = index;
      this.currentPage = 'chat';
    },
    sendMessage() {
      if (this.newMessage.trim() !== "") {
        this.currentChat.messages.push({ content: this.newMessage, type: 'user' });
        this.newMessage = "";
        this.isBotReplying = true;
        this.reply();
        this.scrollToBottom();
      }
    },
    reply() {
      // Mock reply from ChatGPT
      setTimeout(() => {
        this.currentChat.messages.push({ content: "This is a reply from AIS Paper Factory.", type: 'bot' });
        this.isBotReplying = false;
        this.scrollToBottom();
      }, 1000);
    },
    scrollToBottom() {
      this.$nextTick(() => {
        const chatBody = this.$refs.chatBody;
        chatBody.scrollTop = chatBody.scrollHeight;
      });
    },
    goToHomePage() {
      this.currentPage = 'home';
    },
    login() {
      // Implement login functionality here
      alert(`Logged in with ID: ${this.loginId}`);
    },
    submitForm() {
      alert(`Form submitted: ${JSON.stringify(this.form)}`);
      // Implement form submission logic here
    }
  }
};
</script>

<style>
body {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #e6e6e6;
  display: flex;
  flex-direction: column;
}

.header {
  width: 100%;
  background-color: #004b8d;
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
}

.header .logo {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.header .logo img {
  border-radius: 50%;
  margin-right: 10px;
}

.header .logo span {
  font-size: 1.5em;
  font-weight: bold;
}

.header .login-form {
  display: flex;
  align-items: center;
}

.header .login-form input {
  margin-right: 10px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.header .login-form button {
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}

.main-container {
  display: flex;
  flex: 1;
  height: calc(100vh - 60px);
}

.sidebar {
  width: 200px;
  background-color: #004b8d;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.sidebar button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  margin-bottom: 20px;
}

.sidebar ul {
  list-style: none;
  padding: 0;
  width: 100%;
  flex-grow: 1;
  overflow-y: auto;
}

.sidebar li {
  padding: 10px;
  cursor: pointer;
  text-align: center;
  border-radius: 5px;
  margin-bottom: 5px;
  transition: background-color 0.3s;
}

.sidebar li:hover,
.sidebar li.active {
  background-color: #003766;
}

.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.chat-header {
  background-color: #004b8d;
  color: #fff;
  padding: 20px;
  display: flex;
  align-items: center;
}

.chat-header .avatar img {
  border-radius: 50%;
  margin-right: 15px;
}

.chat-header .title {
  font-size: 1.5em;
  font-weight: bold;
}

.chat-body {
  padding: 20px;
  flex-grow: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.chat-body .message {
  margin-bottom: 15px;
  padding: 15px;
  border-radius: 10px;
  max-width: 70%;
}

.chat-body .user {
  background-color: #004b8d;
  color: #fff;
  align-self: flex-end;
}

.chat-body .bot {
  background-color: #f1f1f1;
  color: #333;
  align-self: flex-start;
}

.chat-footer {
  background-color: #f7f7f7;
  padding: 20px;
  display: flex;
  border-top: 1px solid #e6e6e6;
}

.chat-footer input {
  flex: 1;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 10px;
  margin-right: 10px;
}

.chat-footer input:disabled {
  background-color: #e6e6e6;
  cursor: not-allowed;
}

.chat-footer button {
  padding: 15px 20px;
  border: none;
  border-radius: 10px;
  background-color: #004b8d;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s;
}

.chat-footer button:disabled {
  background-color: #999;
  cursor: not-allowed;
}

.chat-footer button:hover {
  background-color: #003766;
}
</style>
