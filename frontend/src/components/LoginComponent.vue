<template>
    <div class="login-container">
      <h1>登入</h1>
      <form @submit.prevent="handleLogin">
        <div>
          <label for="username">帳戶：</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div>
          <label for="password">密碼：</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">登入</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    setup() {
      const username = ref('');
      const password = ref('');
  
      const handleLogin = () => {
        // 這裡應該添加登入邏輯，例如向後端API發送請求
        console.log('帳戶:', username.value);
        console.log('密碼:', password.value);
      };
  
      return { username, password, handleLogin };
    }
  };
  </script>
  
  <style>
  /* 添加一些基本樣式 */
  .login-container {
    max-width: 300px;
    margin: auto;
    padding: 20px;
    text-align: center;
  }
  </style>
  