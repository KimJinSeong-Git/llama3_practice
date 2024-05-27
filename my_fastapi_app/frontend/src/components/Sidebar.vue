<template>
    <div class="sidebar">
      <button @click="newChat">New Chat</button>
      <ul>
        <li
          v-for="(chat, index) in chats"
          :key="index"
          @click="selectChat(index)"
          :class="{ active: currentChatIndex === index }"
        >
          Chat {{ index + 1 }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ChatSidebar',
    props: {
      chats: Array,
      currentChatIndex: Number,
    },
    methods: {
      newChat() {
        this.$emit('newChat');
      },
      selectChat(index) {
        this.$emit('selectChat', index);
      },
    },
  };
  </script>
  
  <style>
  .sidebar {
    width: 200px;
    background-color: #004b8d;
    color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    box-shadow: 5px 0px 5px -2px gray;
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
  </style>
  