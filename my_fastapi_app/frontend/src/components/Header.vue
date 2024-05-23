<template>
    <header class="header">
      <div class="logo" @click="goToHomePage">
        <img src="https://via.placeholder.com/50" alt="AIS Paper Factory Logo" />
        <span>AIS Paper Factory</span>
      </div>
      <div class="login-form">
        <input type="text" placeholder="ID" :value="loginId" @input="$emit('update:loginId', $event.target.value)" />
        <input type="password" placeholder="PW" :value="loginPw" @input="$emit('update:loginPw', $event.target.value)" />
        <button @click="login">Login</button>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: 'AppHeader',
    props: {
      loginId: String,
      loginPw: String,
    },
    methods: {
      goToHomePage() {
        this.$emit('goToHomePage');
      },
      login() {
        this.$emit('login');
      },
    },
  };
  </script>
  
  <style>
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
  </style>
  