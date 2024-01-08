<template>
  <div class="LoginView-container">
    <h1>Log in</h1>
    <form @submit.prevent="LoginView">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />

      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />

      <button type="submit">Log in</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    LoginView() {
      // You can implement your LoginView logic here
      // For a simple example, we'll just log the entered username and password
      console.log("Username:", this.username);
      console.log("Password:", this.password);

      // You may want to redirect the user to another page after successful LoginView
      // For example: this.$router.push('/dashboard');
    },
  },
};
</script>

<style scoped>
.LoginView-container {
  max-width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-top: 50px;
}

h1 {
  text-align: center;
  color: #a1d573;
}

label {
  display: block;
  margin-bottom: 8px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 16px;
  box-sizing: border-box;
}

button {
  background-color: #a1d573;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
