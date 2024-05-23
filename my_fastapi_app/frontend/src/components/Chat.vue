<template>
    <div class="chat-container">
      <div class="chat-header">
        <div class="avatar">
          <img src="https://via.placeholder.com/50" alt="Avatar" />
        </div>
        <div class="title">Based on Llama3-8B</div>
      </div>
      <div class="chat-body" ref="chatBody">
        <div
          v-for="(message, index) in currentChat.messages"
          :key="index"
          :class="['message', message.type]"
        >
          <div class="message-content">{{ message.content }}</div>
        </div>
      </div>
      <div class="chat-footer">
        <input
          :value="newMessage"
          @input="$emit('update:newMessage', $event.target.value)"
          @keyup.enter="sendMessage"
          type="text"
          :disabled="isBotReplying"
          placeholder="Type your message..."
        />
        <button @click="sendMessage" :disabled="isBotReplying">Send</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ChatPage',
    props: {
      currentChat: Object,
      newMessage: String,
      isBotReplying: Boolean,
    },
    methods: {
      sendMessage() {
        this.$emit('sendMessage');
      },
      scrollToBottom() {
        this.$emit('scrollToBottom');
      },
    },
  };
  </script>
  
  <style>
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
  