<template>
  <div id="app">
    <Header
      :loginId="loginId"
      :loginPw="loginPw"
      @update:loginId="updateLoginId"
      @update:loginPw="updateLoginPw"
      @login="login"
      @goToHomePage="goToHomePage"
    />
    <div class="main-container">
      <Sidebar
        :chats="chats"
        :currentChatIndex="currentChatIndex"
        @newChat="newChat"
        @selectChat="selectChat"
      />
      <div class="content">
        <HomePage v-if="currentPage === 'home'" @submitForm="submitForm" :form="form" @update:form="updateForm" />
        <ChatPage v-else :currentChat="currentChat" :newMessage="newMessage" :isBotReplying="isBotReplying" @sendMessage="sendMessage" @update:newMessage="updateNewMessage" />
      </div>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Sidebar from './components/Sidebar.vue';
import HomePage from './components/Home.vue';
import ChatPage from './components/Chat.vue';

export default {
  name: 'App',
  components: {
    Header,
    Sidebar,
    HomePage,
    ChatPage,
  },
  data() {
    return {
      chats: [{ messages: [] }],
      currentChatIndex: 0,
      newMessage: '',
      isBotReplying: false,
      currentPage: 'home',
      loginId: '',
      loginPw: '',
      form: {
        name: '',
        email: '',
        message: '',
      },
    };
  },
  computed: {
    currentChat() {
      return this.chats[this.currentChatIndex];
    },
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
      if (this.newMessage.trim() !== '') {
        this.currentChat.messages.push({ content: this.newMessage, type: 'user' });
        this.newMessage = '';
        this.isBotReplying = true;
        this.reply();
      }
    },
    reply() {
      setTimeout(() => {
        this.currentChat.messages.push({ content: 'This is a reply from AIS Paper Factory.', type: 'bot' });
        this.isBotReplying = false;
      }, 1000);
    },
    goToHomePage() {
      this.currentPage = 'home';
    },
    login() {
      alert(`Logged in with ID: ${this.loginId}`);
    },
    submitForm(form) {
      alert(`Form submitted: ${JSON.stringify(form)}`);
    },
    updateNewMessage(message) {
      this.newMessage = message;
    },
    updateLoginId(id) {
      this.loginId = id;
    },
    updateLoginPw(pw) {
      this.loginPw = pw;
    },
    updateForm(updatedForm) {
      this.form = updatedForm;
    },
  },
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

.main-container {
  display: flex;
  flex: 1;
  height: calc(100vh - 60px);
}

.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>
